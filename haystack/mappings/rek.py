# -*- coding: utf-8 -*-

"""
rekall backed memory_handler.

- rekallProcessMapping: a wrapper around rekall addresspace
- rekallProcessMapper: the memory_handler builder.

"""


import sys
import logging
import struct
from functools import partial

from haystack.mappings import base
from haystack.abc import interfaces
from haystack import target

from rekall import session
from rekall import plugins

log = logging.getLogger('rekall')


class RekallProcessMappingA(base.AMemoryMapping):

    """Process memory mapping using rekall.
    """

    def __init__(self, address_space, start, end, permissions='r--',
                 offset=0, major_device=0, minor_device=0, inode=0, pathname=''):
        base.AMemoryMapping.__init__(
            self,
            start,
            end,
            permissions,
            offset,
            major_device,
            minor_device,
            inode,
            pathname)
        self._backend = address_space

    def read_word(self, addr):
        ws = self._target_platform.get_word_size()
        data = self._backend.read(addr, ws)
        if ws == 4:
            return struct.unpack('I', data)[0]
        elif ws == 8:
            return struct.unpack('Q', data)[0]

    def read_bytes(self, addr, size):
        return self._backend.read(addr, size)

    def read_struct(self, addr, struct):
        size = self._target_platform.get_target_ctypes().sizeof(struct)
        instance = struct.from_buffer_copy(self._backend.read(addr, size))
        instance._orig_address_ = addr
        return instance

    def read_array(self, addr, basetype, count):
        size = self._target_platform.get_target_ctypes().sizeof(basetype * count)
        array = (basetype *count).from_buffer_copy(self._backend.read(addr, size))
        return array

    def reset(self):
        pass


class RekallProcessMapper(interfaces.IMemoryLoader):

    def __init__(self, imgname, pid):
        log.debug("RekallProcessMapper %s %p",imgname, pid)
        self.pid = pid
        self.imgname = imgname
        self._memory_handler = None
        self._init_rekall()

    def _init_rekall(self):
        s = session.Session(
                filename = self.imgname,
                autodetect=["rsds"],
                logger=logging.getLogger(),
                profile_path=[
                    "http://profiles.rekall-forensic.com"
                ])

        self.session = s

        task_plugin = s.plugins.pslist(pid=self.pid)
        maps = []
        # print type(task)
        for task in task_plugin.filter_processes():
            # we need the file address space reader
            address_space = task.get_process_address_space()
            # then we look at vad
            for vad in task.VadRoot.traverse():
                # print type(vad)
                if vad is None:
                    continue
                offset = vad.obj_offset
                start = vad.Start
                end = vad.End
                tag = vad.Tag
                flags = str(vad.u.VadFlags)
                perms = PERMS_PROTECTION[vad.u.VadFlags.Protection.v() & 7]
                pathname = ''
                if vad.u.VadFlags.PrivateMemory == 1 or not vad.ControlArea:
                    pathname = ''
                else:
                    # FIXME, push that to volatility plugin too.
                    try:
                        file_obj = vad.ControlArea.FilePointer
                        if file_obj:
                            pathname = file_obj.FileName or "Pagefile-backed section"
                    except AttributeError:
                        pass

                pmap = RekallProcessMappingA(
                    address_space,
                    start,
                    end,
                    permissions=perms,
                    pathname=pathname)

                maps.append(pmap)

        # get the platform
        meta = s.profile._metadata
        if meta['os'] == "windows":
            os = ''
            if meta['major'] == 5.0:
                os = 'winxp'
            elif meta['major'] == 7.0:
                os = 'win7'
            #
            if meta['arch'] == u'I386':
                self._target = target.TargetPlatform.make_target_win_32(os)
            else:
                self._target = target.TargetPlatform.make_target_win_64(os)
        else:
            if meta['arch'] == u'I386':
                self._target = target.TargetPlatform.make_target_linux_32()
            else:
                self._target = target.TargetPlatform.make_target_linux_64()

        memory_handler = base.MemoryHandler(maps, self._target, self.imgname)
        self._memory_handler = memory_handler

    def make_memory_handler(self):
        return self._memory_handler


PERMS_PROTECTION = dict(enumerate([
    '---',  # 'PAGE_NOACCESS',
    'r--',  # 'PAGE_READONLY',
    '--x',  # 'PAGE_EXECUTE',
    'r-x',  # 'PAGE_EXECUTE_READ',
    'rw-',  # 'PAGE_READWRITE',
    'rc-',  # 'PAGE_WRITECOPY',
    'rwx',  # 'PAGE_EXECUTE_READWRITE',
    'rcx',  # 'PAGE_EXECUTE_WRITECOPY',
]))


# RekallProcessMapper('/home/other/outputs/vol/zeus.vmem', 856)
# RekallProcessMapper('~/outputs/vol/victoria-v8.kcore.img', 1)
