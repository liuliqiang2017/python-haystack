# -*- coding: utf-8 -*-
#
# TARGET arch is: ['-target', 'i386-win']
# WORD_SIZE is: 4
# POINTER_SIZE is: 4
# LONGDOUBLE_SIZE is: 12
#
import ctypes


c_int128 = ctypes.c_ubyte*16
c_uint128 = c_int128
void = None
if ctypes.sizeof(ctypes.c_longdouble) == 12:
    c_long_double_t = ctypes.c_longdouble
else:
    c_long_double_t = ctypes.c_ubyte*12

# if local wordsize is same as target, keep ctypes pointer function.
if ctypes.sizeof(ctypes.c_void_p) == 4:
    POINTER_T = ctypes.POINTER
else:
    # required to access _ctypes
    import _ctypes
    # Emulate a pointer class using the approriate c_int32/c_int64 type
    # The new class should have :
    # ['__module__', 'from_param', '_type_', '__dict__', '__weakref__', '__doc__']
    # but the class should be submitted to a unique instance for each base type
    # to that if A == B, POINTER_T(A) == POINTER_T(B)
    ctypes._pointer_t_type_cache = {}
    def POINTER_T(pointee):
        # a pointer should have the same length as LONG
        fake_ptr_base_type = ctypes.c_uint32 
        # specific case for c_void_p
        if pointee is None: # VOID pointer type. c_void_p.
            pointee = type(None) # ctypes.c_void_p # ctypes.c_ulong
            clsname = 'c_void'
        else:
            clsname = pointee.__name__
        if clsname in ctypes._pointer_t_type_cache:
            return ctypes._pointer_t_type_cache[clsname]
        # make template
        class _T(_ctypes._SimpleCData,):
            _type_ = 'I'
            _subtype_ = pointee
            def _sub_addr_(self):
                return self.value
            def __repr__(self):
                return '%s(%d)'%(clsname, self.value)
            def contents(self):
                raise TypeError('This is not a ctypes pointer.')
            def __init__(self, **args):
                raise TypeError('This is not a ctypes pointer. It is not instanciable.')
        _class = type('LP_%d_%s'%(4, clsname), (_T,),{}) 
        ctypes._pointer_t_type_cache[clsname] = _class
        return _class



UINT8 = ctypes.c_ubyte
UCHAR = ctypes.c_ubyte
BOOL = ctypes.c_ubyte
CHAR = ctypes.c_byte
INT8 = ctypes.c_byte
WCHAR = ctypes.c_uint16
UINT16 = ctypes.c_uint16
USHORT = ctypes.c_uint16
SHORT = ctypes.c_int16
UINT32 = ctypes.c_uint32
ULONG = ctypes.c_uint32
LONG = ctypes.c_int32
UINT64 = ctypes.c_uint64
ULONGLONG = ctypes.c_uint64
LONGLONG = ctypes.c_int64
PVOID64 = ctypes.c_uint64
PPVOID64 = ctypes.c_uint64
PVOID32 = ctypes.c_uint32
PPVOID32 = ctypes.c_uint32
VOID = None
DOUBLE = ctypes.c_double
PUINT8 = POINTER_T(ctypes.c_ubyte)
PUCHAR = POINTER_T(ctypes.c_ubyte)
PBOOL = POINTER_T(ctypes.c_ubyte)
PCHAR = POINTER_T(ctypes.c_byte)
PINT8 = POINTER_T(ctypes.c_byte)
PUINT16 = POINTER_T(ctypes.c_uint16)
PUSHORT = POINTER_T(ctypes.c_uint16)
PSHORT = POINTER_T(ctypes.c_int16)
PUINT32 = POINTER_T(ctypes.c_uint32)
PULONG = POINTER_T(ctypes.c_uint32)
PLONG = POINTER_T(ctypes.c_int32)
PUINT64 = POINTER_T(ctypes.c_uint64)
PULONGLONG = POINTER_T(ctypes.c_uint64)
PLONGLONG = POINTER_T(ctypes.c_int64)
PVOID = POINTER_T(None)
PPVOID = POINTER_T(POINTER_T(None))
class struct__HEAP(ctypes.Structure):
    pass

class struct__HEAP_LOCK(ctypes.Structure):
    pass

class union_c__S__HEAP_LOCK_U_Win7SP1X86DOT_00003BADOT32DOTh_16330(ctypes.Union):
    pass

class struct__RTL_CRITICAL_SECTION(ctypes.Structure):
    pass

class struct__RTL_CRITICAL_SECTION_DEBUG(ctypes.Structure):
    pass

class struct__LIST_ENTRY(ctypes.Structure):
    pass

struct__LIST_ENTRY._pack_ = True # source:True
struct__LIST_ENTRY._fields_ = [
    ('Flink', POINTER_T(struct__LIST_ENTRY)),
    ('Blink', POINTER_T(struct__LIST_ENTRY)),
]

LIST_ENTRY = struct__LIST_ENTRY
struct__RTL_CRITICAL_SECTION_DEBUG._pack_ = True # source:True
struct__RTL_CRITICAL_SECTION_DEBUG._fields_ = [
    ('Type', ctypes.c_uint16),
    ('CreatorBackTraceIndex', ctypes.c_uint16),
    ('CriticalSection', POINTER_T(struct__RTL_CRITICAL_SECTION)),
    ('ProcessLocksList', LIST_ENTRY),
    ('EntryCount', ctypes.c_uint32),
    ('ContentionCount', ctypes.c_uint32),
    ('Flags', ctypes.c_uint32),
    ('CreatorBackTraceIndexHigh', ctypes.c_uint16),
    ('SpareUSHORT', ctypes.c_uint16),
]

struct__RTL_CRITICAL_SECTION._pack_ = True # source:True
struct__RTL_CRITICAL_SECTION._fields_ = [
    ('DebugInfo', POINTER_T(struct__RTL_CRITICAL_SECTION_DEBUG)),
    ('LockCount', ctypes.c_int32),
    ('RecursionCount', ctypes.c_int32),
    ('OwningThread', POINTER_T(None)),
    ('LockSemaphore', POINTER_T(None)),
    ('SpinCount', ctypes.c_uint32),
]

RTL_CRITICAL_SECTION = struct__RTL_CRITICAL_SECTION
union_c__S__HEAP_LOCK_U_Win7SP1X86DOT_00003BADOT32DOTh_16330._pack_ = True # source:False
union_c__S__HEAP_LOCK_U_Win7SP1X86DOT_00003BADOT32DOTh_16330._fields_ = [
    ('CriticalSection', RTL_CRITICAL_SECTION),
]

struct__HEAP_LOCK._pack_ = True # source:True
struct__HEAP_LOCK._fields_ = [
    ('Lock', union_c__S__HEAP_LOCK_U_Win7SP1X86DOT_00003BADOT32DOTh_16330),
]

class struct__HEAP_PSEUDO_TAG_ENTRY(ctypes.Structure):
    _pack_ = True # source:True
    _fields_ = [
    ('Allocs', ctypes.c_uint32),
    ('Frees', ctypes.c_uint32),
    ('Size', ctypes.c_uint32),
     ]

class struct__HEAP_ENTRY(ctypes.Structure):
    pass

class union_c__S__HEAP_ENTRY_Ua_0(ctypes.Union):
    pass

class struct_c__S__HEAP_ENTRY_Ua_Sa_3(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('InterceptorValue', ctypes.c_uint32),
    ('UnusedBytesLength', ctypes.c_uint16),
    ('EntryOffset', ctypes.c_ubyte),
    ('ExtendedBlockSignature', ctypes.c_ubyte),
     ]

class struct_c__S__HEAP_ENTRY_Ua_Sa_1(ctypes.Structure):
    pass

class union_c__S__HEAP_ENTRY_Ua_Sa_Ua_2(ctypes.Union):
    _pack_ = True # source:False
    _fields_ = [
    ('SegmentOffset', ctypes.c_ubyte),
    ('LFHFlags', ctypes.c_ubyte),
     ]

struct_c__S__HEAP_ENTRY_Ua_Sa_1._pack_ = True # source:False
struct_c__S__HEAP_ENTRY_Ua_Sa_1._fields_ = [
    ('SubSegmentCode', POINTER_T(None)),
    ('PreviousSize', ctypes.c_uint16),
    ('_2', union_c__S__HEAP_ENTRY_Ua_Sa_Ua_2),
    ('UnusedBytes', ctypes.c_ubyte),
]

class struct_c__S__HEAP_ENTRY_Ua_Sa_0(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('Size', ctypes.c_uint16),
    ('Flags', ctypes.c_ubyte),
    ('SmallTagIndex', ctypes.c_ubyte),
     ]

class struct_c__S__HEAP_ENTRY_Ua_Sa_5(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('AgregateCode', ctypes.c_uint64),
     ]

class struct_c__S__HEAP_ENTRY_Ua_Sa_2(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('FunctionIndex', ctypes.c_uint16),
    ('ContextValue', ctypes.c_uint16),
     ]

class struct_c__S__HEAP_ENTRY_Ua_Sa_4(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('Code1', ctypes.c_uint32),
    ('Code2', ctypes.c_uint16),
    ('Code3', ctypes.c_ubyte),
    ('Code4', ctypes.c_ubyte),
     ]

union_c__S__HEAP_ENTRY_Ua_0._pack_ = True # source:False
union_c__S__HEAP_ENTRY_Ua_0._fields_ = [
    ('_0', struct_c__S__HEAP_ENTRY_Ua_Sa_0),
    ('_1', struct_c__S__HEAP_ENTRY_Ua_Sa_1),
    ('_2', struct_c__S__HEAP_ENTRY_Ua_Sa_2),
    ('_3', struct_c__S__HEAP_ENTRY_Ua_Sa_3),
    ('_4', struct_c__S__HEAP_ENTRY_Ua_Sa_4),
    ('_5', struct_c__S__HEAP_ENTRY_Ua_Sa_5),
]

struct__HEAP_ENTRY._pack_ = True # source:True
struct__HEAP_ENTRY._fields_ = [
    ('_0', union_c__S__HEAP_ENTRY_Ua_0),
]

HEAP_ENTRY = struct__HEAP_ENTRY
class struct__HEAP_TAG_ENTRY(ctypes.Structure):
    _pack_ = True # source:True
    _fields_ = [
    ('Allocs', ctypes.c_uint32),
    ('Frees', ctypes.c_uint32),
    ('Size', ctypes.c_uint32),
    ('TagIndex', ctypes.c_uint16),
    ('CreatorBackTraceIndex', ctypes.c_uint16),
    ('TagName', ctypes.c_uint16 * 24),
     ]

class struct__HEAP_COUNTERS(ctypes.Structure):
    _pack_ = True # source:True
    _fields_ = [
    ('TotalMemoryReserved', ctypes.c_uint32),
    ('TotalMemoryCommitted', ctypes.c_uint32),
    ('TotalMemoryLargeUCR', ctypes.c_uint32),
    ('TotalSizeInVirtualBlocks', ctypes.c_uint32),
    ('TotalSegments', ctypes.c_uint32),
    ('TotalUCRs', ctypes.c_uint32),
    ('CommittOps', ctypes.c_uint32),
    ('DeCommitOps', ctypes.c_uint32),
    ('LockAcquires', ctypes.c_uint32),
    ('LockCollisions', ctypes.c_uint32),
    ('CommitRate', ctypes.c_uint32),
    ('DecommittRate', ctypes.c_uint32),
    ('CommitFailures', ctypes.c_uint32),
    ('InBlockCommitFailures', ctypes.c_uint32),
    ('CompactHeapCalls', ctypes.c_uint32),
    ('CompactedUCRs', ctypes.c_uint32),
    ('AllocAndFreeOps', ctypes.c_uint32),
    ('InBlockDeccommits', ctypes.c_uint32),
    ('InBlockDeccomitSize', ctypes.c_uint32),
    ('HighWatermarkSize', ctypes.c_uint32),
    ('LastPolledSize', ctypes.c_uint32),
     ]

HEAP_COUNTERS = struct__HEAP_COUNTERS
class struct__HEAP_TUNING_PARAMETERS(ctypes.Structure):
    _pack_ = True # source:True
    _fields_ = [
    ('CommittThresholdShift', ctypes.c_uint32),
    ('MaxPreCommittThreshold', ctypes.c_uint32),
     ]

HEAP_TUNING_PARAMETERS = struct__HEAP_TUNING_PARAMETERS
struct__HEAP._pack_ = True # source:True
struct__HEAP._fields_ = [
    ('Entry', HEAP_ENTRY),
    ('SegmentSignature', ctypes.c_uint32),
    ('SegmentFlags', ctypes.c_uint32),
    ('SegmentListEntry', LIST_ENTRY),
    ('Heap', POINTER_T(struct__HEAP)),
    ('BaseAddress', POINTER_T(None)),
    ('NumberOfPages', ctypes.c_uint32),
    ('FirstEntry', POINTER_T(struct__HEAP_ENTRY)),
    ('LastValidEntry', POINTER_T(struct__HEAP_ENTRY)),
    ('NumberOfUnCommittedPages', ctypes.c_uint32),
    ('NumberOfUnCommittedRanges', ctypes.c_uint32),
    ('SegmentAllocatorBackTraceIndex', ctypes.c_uint16),
    ('Reserved', ctypes.c_uint16),
    ('UCRSegmentList', LIST_ENTRY),
    ('Flags', ctypes.c_uint32),
    ('ForceFlags', ctypes.c_uint32),
    ('CompatibilityFlags', ctypes.c_uint32),
    ('EncodeFlagMask', ctypes.c_uint32),
    ('Encoding', HEAP_ENTRY),
    ('PointerKey', ctypes.c_uint32),
    ('Interceptor', ctypes.c_uint32),
    ('VirtualMemoryThreshold', ctypes.c_uint32),
    ('Signature', ctypes.c_uint32),
    ('SegmentReserve', ctypes.c_uint32),
    ('SegmentCommit', ctypes.c_uint32),
    ('DeCommitFreeBlockThreshold', ctypes.c_uint32),
    ('DeCommitTotalFreeThreshold', ctypes.c_uint32),
    ('TotalFreeSize', ctypes.c_uint32),
    ('MaximumAllocationSize', ctypes.c_uint32),
    ('ProcessHeapsListIndex', ctypes.c_uint16),
    ('HeaderValidateLength', ctypes.c_uint16),
    ('HeaderValidateCopy', POINTER_T(None)),
    ('NextAvailableTagIndex', ctypes.c_uint16),
    ('MaximumTagIndex', ctypes.c_uint16),
    ('TagEntries', POINTER_T(struct__HEAP_TAG_ENTRY)),
    ('UCRList', LIST_ENTRY),
    ('AlignRound', ctypes.c_uint32),
    ('AlignMask', ctypes.c_uint32),
    ('VirtualAllocdBlocks', LIST_ENTRY),
    ('SegmentList', LIST_ENTRY),
    ('AllocatorBackTraceIndex', ctypes.c_uint16),
    ('gap_in_pdb_ofs_B2', ctypes.c_ubyte * 2),
    ('NonDedicatedListLength', ctypes.c_uint32),
    ('BlocksIndex', POINTER_T(None)),
    ('UCRIndex', POINTER_T(None)),
    ('PseudoTagEntries', POINTER_T(struct__HEAP_PSEUDO_TAG_ENTRY)),
    ('FreeLists', LIST_ENTRY),
    ('LockVariable', POINTER_T(struct__HEAP_LOCK)),
    ('CommitRoutine', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(None), POINTER_T(POINTER_T(None)), POINTER_T(ctypes.c_uint32)))),
    ('FrontEndHeap', POINTER_T(None)),
    ('FrontHeapLockCount', ctypes.c_uint16),
    ('FrontEndHeapType', ctypes.c_ubyte),
    ('gap_in_pdb_ofs_DB', ctypes.c_ubyte * 1),
    ('Counters', HEAP_COUNTERS),
    ('TuningParameters', HEAP_TUNING_PARAMETERS),
]

HEAP = struct__HEAP
PHEAP = POINTER_T(struct__HEAP)
PPHEAP = POINTER_T(POINTER_T(struct__HEAP))
class struct__HEAP_LOCAL_DATA(ctypes.Structure):
    pass

class struct__HEAP_LOCAL_SEGMENT_INFO(ctypes.Structure):
    pass

class union__HEAP_BUCKET_COUNTERS(ctypes.Union):
    pass

class struct_c__U__HEAP_BUCKET_COUNTERS_Sa_0(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('TotalBlocks', ctypes.c_uint32),
    ('SubSegmentCounts', ctypes.c_uint32),
     ]

class struct_c__U__HEAP_BUCKET_COUNTERS_Sa_1(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('Aggregate64', ctypes.c_int64),
     ]

union__HEAP_BUCKET_COUNTERS._pack_ = True # source:True
union__HEAP_BUCKET_COUNTERS._fields_ = [
    ('_0', struct_c__U__HEAP_BUCKET_COUNTERS_Sa_0),
    ('_1', struct_c__U__HEAP_BUCKET_COUNTERS_Sa_1),
]

HEAP_BUCKET_COUNTERS = union__HEAP_BUCKET_COUNTERS
class struct__HEAP_SUBSEGMENT(ctypes.Structure):
    pass

class struct__SINGLE_LIST_ENTRY(ctypes.Structure):
    pass

struct__SINGLE_LIST_ENTRY._pack_ = True # source:True
struct__SINGLE_LIST_ENTRY._fields_ = [
    ('Next', POINTER_T(struct__SINGLE_LIST_ENTRY)),
]

SINGLE_LIST_ENTRY = struct__SINGLE_LIST_ENTRY
class union_c__S__HEAP_SUBSEGMENT_Ua_3(ctypes.Union):
    pass

class struct_c__S__HEAP_SUBSEGMENT_Ua_Sa_0(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('BlockSize', ctypes.c_uint16),
    ('Flags', ctypes.c_uint16),
    ('BlockCount', ctypes.c_uint16),
    ('SizeIndex', ctypes.c_ubyte),
    ('AffinityIndex', ctypes.c_ubyte),
     ]

union_c__S__HEAP_SUBSEGMENT_Ua_3._pack_ = True # source:False
union_c__S__HEAP_SUBSEGMENT_Ua_3._fields_ = [
    ('_0', struct_c__S__HEAP_SUBSEGMENT_Ua_Sa_0),
    ('Alignment', ctypes.c_uint32 * 2),
]

class struct__HEAP_USERDATA_HEADER(ctypes.Structure):
    pass

class union_c__S__HEAP_USERDATA_HEADER_Ua_0(ctypes.Union):
    pass

class struct_c__S__HEAP_USERDATA_HEADER_Ua_Sa_1(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('SubSegment', POINTER_T(struct__HEAP_SUBSEGMENT)),
    ('Reserved', POINTER_T(None)),
    ('SizeIndex', ctypes.c_uint32),
    ('Signature', ctypes.c_uint32),
     ]

union_c__S__HEAP_USERDATA_HEADER_Ua_0._pack_ = True # source:False
union_c__S__HEAP_USERDATA_HEADER_Ua_0._fields_ = [
    ('SFreeListEntry', SINGLE_LIST_ENTRY),
    ('_1', struct_c__S__HEAP_USERDATA_HEADER_Ua_Sa_1),
]

struct__HEAP_USERDATA_HEADER._pack_ = True # source:True
struct__HEAP_USERDATA_HEADER._fields_ = [
    ('_0', union_c__S__HEAP_USERDATA_HEADER_Ua_0),
]

class struct__INTERLOCK_SEQ(ctypes.Structure):
    pass

class union_c__S__INTERLOCK_SEQ_Ua_0(ctypes.Union):
    pass

class struct_c__S__INTERLOCK_SEQ_Ua_Sa_0(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('Depth', ctypes.c_uint16),
    ('FreeEntryOffset', ctypes.c_uint16),
     ]

class struct_c__S__INTERLOCK_SEQ_Ua_Sa_1(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('OffsetAndDepth', ctypes.c_uint32),
    ('Sequence', ctypes.c_uint32),
     ]

class struct_c__S__INTERLOCK_SEQ_Ua_Sa_2(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('Exchg', ctypes.c_int64),
     ]

union_c__S__INTERLOCK_SEQ_Ua_0._pack_ = True # source:False
union_c__S__INTERLOCK_SEQ_Ua_0._fields_ = [
    ('_0', struct_c__S__INTERLOCK_SEQ_Ua_Sa_0),
    ('_1', struct_c__S__INTERLOCK_SEQ_Ua_Sa_1),
    ('_2', struct_c__S__INTERLOCK_SEQ_Ua_Sa_2),
]

struct__INTERLOCK_SEQ._pack_ = True # source:True
struct__INTERLOCK_SEQ._fields_ = [
    ('_0', union_c__S__INTERLOCK_SEQ_Ua_0),
]

INTERLOCK_SEQ = struct__INTERLOCK_SEQ
struct__HEAP_SUBSEGMENT._pack_ = True # source:True
struct__HEAP_SUBSEGMENT._fields_ = [
    ('LocalInfo', POINTER_T(struct__HEAP_LOCAL_SEGMENT_INFO)),
    ('UserBlocks', POINTER_T(struct__HEAP_USERDATA_HEADER)),
    ('AggregateExchg', INTERLOCK_SEQ),
    ('_3', union_c__S__HEAP_SUBSEGMENT_Ua_3),
    ('SFreeListEntry', SINGLE_LIST_ENTRY),
    ('Lock', ctypes.c_uint32),
]

class union__SLIST_HEADER(ctypes.Union):
    pass

class struct_c__U__SLIST_HEADER_Sa_1(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('Next', SINGLE_LIST_ENTRY),
    ('Depth', ctypes.c_uint16),
    ('Sequence', ctypes.c_uint16),
     ]

union__SLIST_HEADER._pack_ = True # source:True
union__SLIST_HEADER._fields_ = [
    ('Alignment', ctypes.c_uint64),
    ('_1', struct_c__U__SLIST_HEADER_Sa_1),
]

SLIST_HEADER = union__SLIST_HEADER
struct__HEAP_LOCAL_SEGMENT_INFO._pack_ = True # source:True
struct__HEAP_LOCAL_SEGMENT_INFO._fields_ = [
    ('Hint', POINTER_T(struct__HEAP_SUBSEGMENT)),
    ('ActiveSubsegment', POINTER_T(struct__HEAP_SUBSEGMENT)),
    ('CachedItems', POINTER_T(struct__HEAP_SUBSEGMENT) * 16),
    ('SListHeader', SLIST_HEADER),
    ('Counters', HEAP_BUCKET_COUNTERS),
    ('LocalData', POINTER_T(struct__HEAP_LOCAL_DATA)),
    ('LastOpSequence', ctypes.c_uint32),
    ('BucketIndex', ctypes.c_uint16),
    ('LastUsed', ctypes.c_uint16),
    ('gap_in_pdb_ofs_64', ctypes.c_ubyte * 4),
]

class struct__LFH_BLOCK_ZONE(ctypes.Structure):
    _pack_ = True # source:True
    _fields_ = [
    ('ListEntry', LIST_ENTRY),
    ('FreePointer', POINTER_T(None)),
    ('Limit', POINTER_T(None)),
     ]

class struct__LFH_HEAP(ctypes.Structure):
    pass

class struct__HEAP_BUCKET(ctypes.Structure):
    pass

class struct_c__S__HEAP_BUCKET_Sa_2(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('UseAffinity', ctypes.c_uint8, 1),
    ('DebugFlags', ctypes.c_uint8, 2),
    ('PADDING_0', ctypes.c_uint8, 5),
     ]

struct__HEAP_BUCKET._pack_ = True # source:True
struct__HEAP_BUCKET._fields_ = [
    ('BlockUnits', ctypes.c_uint16),
    ('SizeIndex', ctypes.c_ubyte),
    ('_2', struct_c__S__HEAP_BUCKET_Sa_2),
]

class struct__USER_MEMORY_CACHE_ENTRY(ctypes.Structure):
    _pack_ = True # source:True
    _fields_ = [
    ('UserBlocks', SLIST_HEADER),
    ('AvailableBlocks', ctypes.c_uint32),
    ('gap_in_pdb_ofs_C', ctypes.c_ubyte * 4),
     ]

class union__HEAP_BUCKET_RUN_INFO(ctypes.Union):
    pass

class struct_c__U__HEAP_BUCKET_RUN_INFO_Sa_0(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('Bucket', ctypes.c_uint32),
    ('RunLength', ctypes.c_uint32),
     ]

class struct_c__U__HEAP_BUCKET_RUN_INFO_Sa_1(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('Aggregate64', ctypes.c_int64),
     ]

union__HEAP_BUCKET_RUN_INFO._pack_ = True # source:True
union__HEAP_BUCKET_RUN_INFO._fields_ = [
    ('_0', struct_c__U__HEAP_BUCKET_RUN_INFO_Sa_0),
    ('_1', struct_c__U__HEAP_BUCKET_RUN_INFO_Sa_1),
]

HEAP_BUCKET_RUN_INFO = union__HEAP_BUCKET_RUN_INFO
struct__LFH_HEAP._pack_ = True # source:True
struct__LFH_HEAP._fields_ = [
    ('Lock', RTL_CRITICAL_SECTION),
    ('SubSegmentZones', LIST_ENTRY),
    ('ZoneBlockSize', ctypes.c_uint32),
    ('Heap', POINTER_T(None)),
    ('SegmentChange', ctypes.c_uint32),
    ('SegmentCreate', ctypes.c_uint32),
    ('SegmentInsertInFree', ctypes.c_uint32),
    ('SegmentDelete', ctypes.c_uint32),
    ('CacheAllocs', ctypes.c_uint32),
    ('CacheFrees', ctypes.c_uint32),
    ('SizeInCache', ctypes.c_uint32),
    ('gap_in_pdb_ofs_44', ctypes.c_ubyte * 4),
    ('RunInfo', HEAP_BUCKET_RUN_INFO),
    ('UserBlockCache', struct__USER_MEMORY_CACHE_ENTRY * 12),
    ('Buckets', struct__HEAP_BUCKET * 128),
    ('LocalData', struct__HEAP_LOCAL_DATA * 1),
]

struct__HEAP_LOCAL_DATA._pack_ = True # source:True
struct__HEAP_LOCAL_DATA._fields_ = [
    ('DeletedSubSegments', SLIST_HEADER),
    ('CrtZone', POINTER_T(struct__LFH_BLOCK_ZONE)),
    ('LowFragHeap', POINTER_T(struct__LFH_HEAP)),
    ('Sequence', ctypes.c_uint32),
    ('gap_in_pdb_ofs_14', ctypes.c_ubyte * 4),
    ('SegmentInfo', struct__HEAP_LOCAL_SEGMENT_INFO * 128),
]

HEAP_LOCAL_DATA = struct__HEAP_LOCAL_DATA
PHEAP_LOCAL_DATA = POINTER_T(struct__HEAP_LOCAL_DATA)
PPHEAP_LOCAL_DATA = POINTER_T(POINTER_T(struct__HEAP_LOCAL_DATA))
HEAP_LOCAL_SEGMENT_INFO = struct__HEAP_LOCAL_SEGMENT_INFO
PHEAP_LOCAL_SEGMENT_INFO = POINTER_T(struct__HEAP_LOCAL_SEGMENT_INFO)
PPHEAP_LOCAL_SEGMENT_INFO = POINTER_T(POINTER_T(struct__HEAP_LOCAL_SEGMENT_INFO))
HEAP_LOCK = struct__HEAP_LOCK
PHEAP_LOCK = POINTER_T(struct__HEAP_LOCK)
PPHEAP_LOCK = POINTER_T(POINTER_T(struct__HEAP_LOCK))
HEAP_SUBSEGMENT = struct__HEAP_SUBSEGMENT
PHEAP_SUBSEGMENT = POINTER_T(struct__HEAP_SUBSEGMENT)
PPHEAP_SUBSEGMENT = POINTER_T(POINTER_T(struct__HEAP_SUBSEGMENT))
HEAP_USERDATA_HEADER = struct__HEAP_USERDATA_HEADER
PHEAP_USERDATA_HEADER = POINTER_T(struct__HEAP_USERDATA_HEADER)
PPHEAP_USERDATA_HEADER = POINTER_T(POINTER_T(struct__HEAP_USERDATA_HEADER))
LFH_HEAP = struct__LFH_HEAP
PLFH_HEAP = POINTER_T(struct__LFH_HEAP)
PPLFH_HEAP = POINTER_T(POINTER_T(struct__LFH_HEAP))
PRTL_CRITICAL_SECTION = POINTER_T(struct__RTL_CRITICAL_SECTION)
PPRTL_CRITICAL_SECTION = POINTER_T(POINTER_T(struct__RTL_CRITICAL_SECTION))
RTL_CRITICAL_SECTION_DEBUG = struct__RTL_CRITICAL_SECTION_DEBUG
PRTL_CRITICAL_SECTION_DEBUG = POINTER_T(struct__RTL_CRITICAL_SECTION_DEBUG)
PPRTL_CRITICAL_SECTION_DEBUG = POINTER_T(POINTER_T(struct__RTL_CRITICAL_SECTION_DEBUG))
PPLIST_ENTRY = POINTER_T(POINTER_T(struct__LIST_ENTRY))
PLIST_ENTRY = POINTER_T(struct__LIST_ENTRY)
PSINGLE_LIST_ENTRY = POINTER_T(struct__SINGLE_LIST_ENTRY)
PPSINGLE_LIST_ENTRY = POINTER_T(POINTER_T(struct__SINGLE_LIST_ENTRY))
PHEAP_TAG_ENTRY = POINTER_T(struct__HEAP_TAG_ENTRY)
HEAP_TAG_ENTRY = struct__HEAP_TAG_ENTRY
PPHEAP_TAG_ENTRY = POINTER_T(POINTER_T(struct__HEAP_TAG_ENTRY))
PHEAP_BUCKET_COUNTERS = POINTER_T(union__HEAP_BUCKET_COUNTERS)
PPHEAP_BUCKET_COUNTERS = POINTER_T(POINTER_T(union__HEAP_BUCKET_COUNTERS))
PHEAP_BUCKET_RUN_INFO = POINTER_T(union__HEAP_BUCKET_RUN_INFO)
PPHEAP_BUCKET_RUN_INFO = POINTER_T(POINTER_T(union__HEAP_BUCKET_RUN_INFO))
PINTERLOCK_SEQ = POINTER_T(struct__INTERLOCK_SEQ)
PPINTERLOCK_SEQ = POINTER_T(POINTER_T(struct__INTERLOCK_SEQ))
HEAP_BUCKET = struct__HEAP_BUCKET
PHEAP_BUCKET = POINTER_T(struct__HEAP_BUCKET)
PPHEAP_BUCKET = POINTER_T(POINTER_T(struct__HEAP_BUCKET))
PHEAP_COUNTERS = POINTER_T(struct__HEAP_COUNTERS)
PPHEAP_COUNTERS = POINTER_T(POINTER_T(struct__HEAP_COUNTERS))
HEAP_PSEUDO_TAG_ENTRY = struct__HEAP_PSEUDO_TAG_ENTRY
PHEAP_PSEUDO_TAG_ENTRY = POINTER_T(struct__HEAP_PSEUDO_TAG_ENTRY)
PPHEAP_PSEUDO_TAG_ENTRY = POINTER_T(POINTER_T(struct__HEAP_PSEUDO_TAG_ENTRY))
PHEAP_ENTRY = POINTER_T(struct__HEAP_ENTRY)
PPHEAP_ENTRY = POINTER_T(POINTER_T(struct__HEAP_ENTRY))
PHEAP_TUNING_PARAMETERS = POINTER_T(struct__HEAP_TUNING_PARAMETERS)
PPHEAP_TUNING_PARAMETERS = POINTER_T(POINTER_T(struct__HEAP_TUNING_PARAMETERS))
LFH_BLOCK_ZONE = struct__LFH_BLOCK_ZONE
PLFH_BLOCK_ZONE = POINTER_T(struct__LFH_BLOCK_ZONE)
PPLFH_BLOCK_ZONE = POINTER_T(POINTER_T(struct__LFH_BLOCK_ZONE))
PPSLIST_HEADER = POINTER_T(POINTER_T(union__SLIST_HEADER))
PSLIST_HEADER = POINTER_T(union__SLIST_HEADER)
USER_MEMORY_CACHE_ENTRY = struct__USER_MEMORY_CACHE_ENTRY
PUSER_MEMORY_CACHE_ENTRY = POINTER_T(struct__USER_MEMORY_CACHE_ENTRY)
PPUSER_MEMORY_CACHE_ENTRY = POINTER_T(POINTER_T(struct__USER_MEMORY_CACHE_ENTRY))
class struct__HEAP_SEGMENT(ctypes.Structure):
    pass

class struct__HEAP(ctypes.Structure):
    pass

class struct__HEAP_LOCK(ctypes.Structure):
    pass

class union_c__S__HEAP_LOCK_U_Win7SP1X86DOT_000160EDOT32DOTh_19641(ctypes.Union):
    _pack_ = True # source:False
    _fields_ = [
    ('CriticalSection', RTL_CRITICAL_SECTION),
     ]

struct__HEAP_LOCK._pack_ = True # source:True
struct__HEAP_LOCK._fields_ = [
    ('Lock', union_c__S__HEAP_LOCK_U_Win7SP1X86DOT_000160EDOT32DOTh_19641),
]

struct__HEAP._pack_ = True # source:True
struct__HEAP._fields_ = [
    ('Entry', HEAP_ENTRY),
    ('SegmentSignature', ctypes.c_uint32),
    ('SegmentFlags', ctypes.c_uint32),
    ('SegmentListEntry', LIST_ENTRY),
    ('Heap', POINTER_T(struct__HEAP)),
    ('BaseAddress', POINTER_T(None)),
    ('NumberOfPages', ctypes.c_uint32),
    ('FirstEntry', POINTER_T(struct__HEAP_ENTRY)),
    ('LastValidEntry', POINTER_T(struct__HEAP_ENTRY)),
    ('NumberOfUnCommittedPages', ctypes.c_uint32),
    ('NumberOfUnCommittedRanges', ctypes.c_uint32),
    ('SegmentAllocatorBackTraceIndex', ctypes.c_uint16),
    ('Reserved', ctypes.c_uint16),
    ('UCRSegmentList', LIST_ENTRY),
    ('Flags', ctypes.c_uint32),
    ('ForceFlags', ctypes.c_uint32),
    ('CompatibilityFlags', ctypes.c_uint32),
    ('EncodeFlagMask', ctypes.c_uint32),
    ('Encoding', HEAP_ENTRY),
    ('PointerKey', ctypes.c_uint32),
    ('Interceptor', ctypes.c_uint32),
    ('VirtualMemoryThreshold', ctypes.c_uint32),
    ('Signature', ctypes.c_uint32),
    ('SegmentReserve', ctypes.c_uint32),
    ('SegmentCommit', ctypes.c_uint32),
    ('DeCommitFreeBlockThreshold', ctypes.c_uint32),
    ('DeCommitTotalFreeThreshold', ctypes.c_uint32),
    ('TotalFreeSize', ctypes.c_uint32),
    ('MaximumAllocationSize', ctypes.c_uint32),
    ('ProcessHeapsListIndex', ctypes.c_uint16),
    ('HeaderValidateLength', ctypes.c_uint16),
    ('HeaderValidateCopy', POINTER_T(None)),
    ('NextAvailableTagIndex', ctypes.c_uint16),
    ('MaximumTagIndex', ctypes.c_uint16),
    ('TagEntries', POINTER_T(struct__HEAP_TAG_ENTRY)),
    ('UCRList', LIST_ENTRY),
    ('AlignRound', ctypes.c_uint32),
    ('AlignMask', ctypes.c_uint32),
    ('VirtualAllocdBlocks', LIST_ENTRY),
    ('SegmentList', LIST_ENTRY),
    ('AllocatorBackTraceIndex', ctypes.c_uint16),
    ('gap_in_pdb_ofs_B2', ctypes.c_ubyte * 2),
    ('NonDedicatedListLength', ctypes.c_uint32),
    ('BlocksIndex', POINTER_T(None)),
    ('UCRIndex', POINTER_T(None)),
    ('PseudoTagEntries', POINTER_T(struct__HEAP_PSEUDO_TAG_ENTRY)),
    ('FreeLists', LIST_ENTRY),
    ('LockVariable', POINTER_T(struct__HEAP_LOCK)),
    ('CommitRoutine', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(None), POINTER_T(POINTER_T(None)), POINTER_T(ctypes.c_uint32)))),
    ('FrontEndHeap', POINTER_T(None)),
    ('FrontHeapLockCount', ctypes.c_uint16),
    ('FrontEndHeapType', ctypes.c_ubyte),
    ('gap_in_pdb_ofs_DB', ctypes.c_ubyte * 1),
    ('Counters', HEAP_COUNTERS),
    ('TuningParameters', HEAP_TUNING_PARAMETERS),
]

struct__HEAP_SEGMENT._pack_ = True # source:True
struct__HEAP_SEGMENT._fields_ = [
    ('Entry', HEAP_ENTRY),
    ('SegmentSignature', ctypes.c_uint32),
    ('SegmentFlags', ctypes.c_uint32),
    ('SegmentListEntry', LIST_ENTRY),
    ('Heap', POINTER_T(struct__HEAP)),
    ('BaseAddress', POINTER_T(None)),
    ('NumberOfPages', ctypes.c_uint32),
    ('FirstEntry', POINTER_T(struct__HEAP_ENTRY)),
    ('LastValidEntry', POINTER_T(struct__HEAP_ENTRY)),
    ('NumberOfUnCommittedPages', ctypes.c_uint32),
    ('NumberOfUnCommittedRanges', ctypes.c_uint32),
    ('SegmentAllocatorBackTraceIndex', ctypes.c_uint16),
    ('Reserved', ctypes.c_uint16),
    ('UCRSegmentList', LIST_ENTRY),
]

HEAP_SEGMENT = struct__HEAP_SEGMENT
PPHEAP_SEGMENT = POINTER_T(POINTER_T(struct__HEAP_SEGMENT))
PHEAP_SEGMENT = POINTER_T(struct__HEAP_SEGMENT)
class struct__HEAP_ENTRY_EXTRA(ctypes.Structure):
    pass

class union_c__S__HEAP_ENTRY_EXTRA_Ua_0(ctypes.Union):
    pass

class struct_c__S__HEAP_ENTRY_EXTRA_Ua_Sa_0(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('AllocatorBackTraceIndex', ctypes.c_uint16),
    ('TagIndex', ctypes.c_uint16),
    ('Settable', ctypes.c_uint32),
     ]

class struct_c__S__HEAP_ENTRY_EXTRA_Ua_Sa_1(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('ZeroInit', ctypes.c_uint64),
     ]

union_c__S__HEAP_ENTRY_EXTRA_Ua_0._pack_ = True # source:False
union_c__S__HEAP_ENTRY_EXTRA_Ua_0._fields_ = [
    ('_0', struct_c__S__HEAP_ENTRY_EXTRA_Ua_Sa_0),
    ('_1', struct_c__S__HEAP_ENTRY_EXTRA_Ua_Sa_1),
]

struct__HEAP_ENTRY_EXTRA._pack_ = True # source:True
struct__HEAP_ENTRY_EXTRA._fields_ = [
    ('_0', union_c__S__HEAP_ENTRY_EXTRA_Ua_0),
]

HEAP_ENTRY_EXTRA = struct__HEAP_ENTRY_EXTRA
PHEAP_ENTRY_EXTRA = POINTER_T(struct__HEAP_ENTRY_EXTRA)
PPHEAP_ENTRY_EXTRA = POINTER_T(POINTER_T(struct__HEAP_ENTRY_EXTRA))
class struct__HEAP_LIST_LOOKUP(ctypes.Structure):
    pass

struct__HEAP_LIST_LOOKUP._pack_ = True # source:True
struct__HEAP_LIST_LOOKUP._fields_ = [
    ('ExtendedLookup', POINTER_T(struct__HEAP_LIST_LOOKUP)),
    ('ArraySize', ctypes.c_uint32),
    ('ExtraItem', ctypes.c_uint32),
    ('ItemCount', ctypes.c_uint32),
    ('OutOfRangeItems', ctypes.c_uint32),
    ('BaseIndex', ctypes.c_uint32),
    ('ListHead', POINTER_T(struct__LIST_ENTRY)),
    ('ListsInUseUlong', POINTER_T(ctypes.c_uint32)),
    ('ListHints', POINTER_T(POINTER_T(struct__LIST_ENTRY))),
]

PHEAP_LIST_LOOKUP = POINTER_T(struct__HEAP_LIST_LOOKUP)
PPHEAP_LIST_LOOKUP = POINTER_T(POINTER_T(struct__HEAP_LIST_LOOKUP))
HEAP_LIST_LOOKUP = struct__HEAP_LIST_LOOKUP
class struct__HEAP_UCR_DESCRIPTOR(ctypes.Structure):
    _pack_ = True # source:True
    _fields_ = [
    ('ListEntry', LIST_ENTRY),
    ('SegmentEntry', LIST_ENTRY),
    ('Address', POINTER_T(None)),
    ('Size', ctypes.c_uint32),
     ]

HEAP_UCR_DESCRIPTOR = struct__HEAP_UCR_DESCRIPTOR
PHEAP_UCR_DESCRIPTOR = POINTER_T(struct__HEAP_UCR_DESCRIPTOR)
PPHEAP_UCR_DESCRIPTOR = POINTER_T(POINTER_T(struct__HEAP_UCR_DESCRIPTOR))
class struct__HEAP_LOOKASIDE(ctypes.Structure):
    _pack_ = True # source:True
    _fields_ = [
    ('ListHead', SLIST_HEADER),
    ('Depth', ctypes.c_uint16),
    ('MaximumDepth', ctypes.c_uint16),
    ('TotalAllocates', ctypes.c_uint32),
    ('AllocateMisses', ctypes.c_uint32),
    ('TotalFrees', ctypes.c_uint32),
    ('FreeMisses', ctypes.c_uint32),
    ('LastTotalAllocates', ctypes.c_uint32),
    ('LastAllocateMisses', ctypes.c_uint32),
    ('Counters', ctypes.c_uint32 * 2),
    ('gap_in_pdb_ofs_2C', ctypes.c_ubyte * 4),
     ]

HEAP_LOOKASIDE = struct__HEAP_LOOKASIDE
PPHEAP_LOOKASIDE = POINTER_T(POINTER_T(struct__HEAP_LOOKASIDE))
PHEAP_LOOKASIDE = POINTER_T(struct__HEAP_LOOKASIDE)
class struct__HEAP_FREE_ENTRY(ctypes.Structure):
    pass

class union_c__S__HEAP_FREE_ENTRY_Ua_0(ctypes.Union):
    pass

class struct_c__S__HEAP_FREE_ENTRY_Ua_Sa_2(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('FunctionIndex', ctypes.c_uint16),
    ('ContextValue', ctypes.c_uint16),
     ]

class struct_c__S__HEAP_FREE_ENTRY_Ua_Sa_0(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('Size', ctypes.c_uint16),
    ('Flags', ctypes.c_ubyte),
    ('SmallTagIndex', ctypes.c_ubyte),
     ]

class struct_c__S__HEAP_FREE_ENTRY_Ua_Sa_3(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('InterceptorValue', ctypes.c_uint32),
    ('UnusedBytesLength', ctypes.c_uint16),
    ('EntryOffset', ctypes.c_ubyte),
    ('ExtendedBlockSignature', ctypes.c_ubyte),
     ]

class struct_c__S__HEAP_FREE_ENTRY_Ua_Sa_4(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('Code1', ctypes.c_uint32),
    ('Code2', ctypes.c_uint16),
    ('Code3', ctypes.c_ubyte),
    ('Code4', ctypes.c_ubyte),
     ]

class struct_c__S__HEAP_FREE_ENTRY_Ua_Sa_1(ctypes.Structure):
    pass

class union_c__S__HEAP_FREE_ENTRY_Ua_Sa_Ua_2(ctypes.Union):
    _pack_ = True # source:False
    _fields_ = [
    ('SegmentOffset', ctypes.c_ubyte),
    ('LFHFlags', ctypes.c_ubyte),
     ]

struct_c__S__HEAP_FREE_ENTRY_Ua_Sa_1._pack_ = True # source:False
struct_c__S__HEAP_FREE_ENTRY_Ua_Sa_1._fields_ = [
    ('SubSegmentCode', POINTER_T(None)),
    ('PreviousSize', ctypes.c_uint16),
    ('_2', union_c__S__HEAP_FREE_ENTRY_Ua_Sa_Ua_2),
    ('UnusedBytes', ctypes.c_ubyte),
]

class struct_c__S__HEAP_FREE_ENTRY_Ua_Sa_5(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('AgregateCode', ctypes.c_uint64),
    ('FreeList', LIST_ENTRY),
     ]

union_c__S__HEAP_FREE_ENTRY_Ua_0._pack_ = True # source:False
union_c__S__HEAP_FREE_ENTRY_Ua_0._fields_ = [
    ('_0', struct_c__S__HEAP_FREE_ENTRY_Ua_Sa_0),
    ('_1', struct_c__S__HEAP_FREE_ENTRY_Ua_Sa_1),
    ('_2', struct_c__S__HEAP_FREE_ENTRY_Ua_Sa_2),
    ('_3', struct_c__S__HEAP_FREE_ENTRY_Ua_Sa_3),
    ('_4', struct_c__S__HEAP_FREE_ENTRY_Ua_Sa_4),
    ('_5', struct_c__S__HEAP_FREE_ENTRY_Ua_Sa_5),
]

struct__HEAP_FREE_ENTRY._pack_ = True # source:True
struct__HEAP_FREE_ENTRY._fields_ = [
    ('_0', union_c__S__HEAP_FREE_ENTRY_Ua_0),
]

HEAP_FREE_ENTRY = struct__HEAP_FREE_ENTRY
PHEAP_FREE_ENTRY = POINTER_T(struct__HEAP_FREE_ENTRY)
PPHEAP_FREE_ENTRY = POINTER_T(POINTER_T(struct__HEAP_FREE_ENTRY))
class struct__HEAP_VIRTUAL_ALLOC_ENTRY(ctypes.Structure):
    _pack_ = True # source:True
    _fields_ = [
    ('Entry', LIST_ENTRY),
    ('ExtraStuff', HEAP_ENTRY_EXTRA),
    ('CommitSize', ctypes.c_uint32),
    ('ReserveSize', ctypes.c_uint32),
    ('BusyBlock', HEAP_ENTRY),
     ]

PHEAP_VIRTUAL_ALLOC_ENTRY = POINTER_T(struct__HEAP_VIRTUAL_ALLOC_ENTRY)
PPHEAP_VIRTUAL_ALLOC_ENTRY = POINTER_T(POINTER_T(struct__HEAP_VIRTUAL_ALLOC_ENTRY))
HEAP_VIRTUAL_ALLOC_ENTRY = struct__HEAP_VIRTUAL_ALLOC_ENTRY
__all__ = \
    ['PPHEAP_VIRTUAL_ALLOC_ENTRY', 'HEAP_VIRTUAL_ALLOC_ENTRY', 'VOID',
    'HEAP_FREE_ENTRY', 'PUINT32', 'struct__HEAP_USERDATA_HEADER',
    'INTERLOCK_SEQ', 'PPSLIST_HEADER', 'PHEAP_PSEUDO_TAG_ENTRY',
    'PHEAP_LOCK', 'PPVOID', 'LFH_BLOCK_ZONE', 'PVOID32',
    'struct__HEAP_LIST_LOOKUP', 'PSINGLE_LIST_ENTRY',
    'struct__HEAP_ENTRY_EXTRA', 'UINT16', 'PPHEAP_LOOKASIDE',
    'PHEAP_BUCKET_RUN_INFO', 'union_c__S__HEAP_USERDATA_HEADER_Ua_0',
    'PUSHORT', 'PUCHAR', 'union_c__S__HEAP_ENTRY_Ua_0',
    'HEAP_BUCKET_RUN_INFO',
    'struct_c__S__HEAP_USERDATA_HEADER_Ua_Sa_1',
    'PHEAP_BUCKET_COUNTERS', 'HEAP_ENTRY', 'PPHEAP_USERDATA_HEADER',
    'RTL_CRITICAL_SECTION', 'union__SLIST_HEADER',
    'union__HEAP_BUCKET_COUNTERS', 'PPHEAP_TAG_ENTRY',
    'struct_c__S__HEAP_BUCKET_Sa_2', 'struct__HEAP_SUBSEGMENT',
    'DOUBLE', 'struct_c__S__INTERLOCK_SEQ_Ua_Sa_0',
    'struct_c__S__INTERLOCK_SEQ_Ua_Sa_1',
    'struct_c__S__INTERLOCK_SEQ_Ua_Sa_2', 'PHEAP_ENTRY_EXTRA',
    'HEAP_BUCKET', 'PPHEAP_TUNING_PARAMETERS',
    'struct__LFH_BLOCK_ZONE', 'struct__HEAP_ENTRY', 'PINTERLOCK_SEQ',
    'SLIST_HEADER', 'PLONG', 'LONGLONG', 'PHEAP_SEGMENT', 'SHORT',
    'union_c__S__HEAP_SUBSEGMENT_Ua_3', 'PINT8', 'PPHEAP_ENTRY_EXTRA',
    'PPHEAP_SEGMENT', 'PPRTL_CRITICAL_SECTION_DEBUG',
    'PPHEAP_LIST_LOOKUP', 'HEAP_SUBSEGMENT', 'HEAP_TAG_ENTRY',
    'struct_c__U__HEAP_BUCKET_RUN_INFO_Sa_0',
    'struct_c__U__HEAP_BUCKET_RUN_INFO_Sa_1', 'ULONG', 'struct__HEAP',
    'struct__LFH_HEAP', 'HEAP_USERDATA_HEADER', 'HEAP_LOOKASIDE',
    'struct__INTERLOCK_SEQ', 'struct_c__S__HEAP_FREE_ENTRY_Ua_Sa_4',
    'struct__HEAP_LOCK', 'struct__SINGLE_LIST_ENTRY', 'BOOL',
    'PPHEAP_LOCAL_DATA', 'UINT32',
    'union_c__S__HEAP_ENTRY_EXTRA_Ua_0', 'HEAP_LOCAL_DATA', 'PBOOL',
    'UCHAR', 'union_c__S__INTERLOCK_SEQ_Ua_0',
    'PHEAP_TUNING_PARAMETERS', 'PPVOID32', 'PVOID64',
    'struct__LIST_ENTRY', 'struct_c__U__HEAP_BUCKET_COUNTERS_Sa_1',
    'struct_c__U__HEAP_BUCKET_COUNTERS_Sa_0',
    'PUSER_MEMORY_CACHE_ENTRY', 'PHEAP_TAG_ENTRY',
    'HEAP_LOCAL_SEGMENT_INFO', 'struct__HEAP_LOCAL_SEGMENT_INFO',
    'HEAP_SEGMENT', 'union__HEAP_BUCKET_RUN_INFO', 'HEAP_COUNTERS',
    'PULONG', 'struct__HEAP_LOCAL_DATA', 'WCHAR', 'PHEAP_ENTRY',
    'HEAP_LIST_LOOKUP', 'struct__RTL_CRITICAL_SECTION',
    'PPHEAP_BUCKET', 'struct_c__S__HEAP_FREE_ENTRY_Ua_Sa_2', 'CHAR',
    'LONG', 'PULONGLONG', 'PLFH_BLOCK_ZONE', 'PPSINGLE_LIST_ENTRY',
    'PPHEAP_BUCKET_COUNTERS', 'struct__HEAP_BUCKET', 'PSLIST_HEADER',
    'struct_c__S__HEAP_FREE_ENTRY_Ua_Sa_5',
    'struct__HEAP_UCR_DESCRIPTOR',
    'struct_c__S__HEAP_FREE_ENTRY_Ua_Sa_3', 'PHEAP_LOCAL_DATA',
    'struct_c__S__HEAP_FREE_ENTRY_Ua_Sa_1',
    'struct_c__S__HEAP_FREE_ENTRY_Ua_Sa_0', 'PUINT64',
    'struct__HEAP_LOOKASIDE', 'PRTL_CRITICAL_SECTION_DEBUG',
    'struct__HEAP_SEGMENT', 'struct_c__S__HEAP_ENTRY_EXTRA_Ua_Sa_1',
    'struct__HEAP_VIRTUAL_ALLOC_ENTRY',
    'struct_c__S__HEAP_SUBSEGMENT_Ua_Sa_0', 'PRTL_CRITICAL_SECTION',
    'PPHEAP_LOCAL_SEGMENT_INFO', 'PPHEAP_FREE_ENTRY',
    'RTL_CRITICAL_SECTION_DEBUG', 'PLFH_HEAP',
    'PHEAP_LOCAL_SEGMENT_INFO', 'UINT8', 'struct__HEAP_FREE_ENTRY',
    'PPHEAP_PSEUDO_TAG_ENTRY', 'PLONGLONG',
    'PPUSER_MEMORY_CACHE_ENTRY', 'PPLFH_BLOCK_ZONE',
    'PHEAP_FREE_ENTRY', 'PPHEAP_LOCK',
    'struct__HEAP_TUNING_PARAMETERS', 'HEAP_TUNING_PARAMETERS',
    'UINT64', 'PPHEAP_SUBSEGMENT', 'LFH_HEAP',
    'struct_c__U__SLIST_HEADER_Sa_1', 'PHEAP_BUCKET',
    'union_c__S__HEAP_LOCK_U_Win7SP1X86DOT_000160EDOT32DOTh_19641',
    'USHORT', 'HEAP_ENTRY_EXTRA', 'union_c__S__HEAP_ENTRY_Ua_Sa_Ua_2',
    'HEAP_PSEUDO_TAG_ENTRY', 'PPHEAP', 'HEAP_LOCK', 'PPINTERLOCK_SEQ',
    'LIST_ENTRY', 'USER_MEMORY_CACHE_ENTRY', 'PUINT16',
    'PHEAP_UCR_DESCRIPTOR', 'PHEAP', 'PPVOID64', 'PLIST_ENTRY',
    'struct__HEAP_COUNTERS', 'PHEAP_LIST_LOOKUP', 'PHEAP_SUBSEGMENT',
    'HEAP_UCR_DESCRIPTOR', 'PHEAP_USERDATA_HEADER', 'PHEAP_LOOKASIDE',
    'union_c__S__HEAP_LOCK_U_Win7SP1X86DOT_00003BADOT32DOTh_16330',
    'struct__USER_MEMORY_CACHE_ENTRY',
    'struct_c__S__HEAP_ENTRY_Ua_Sa_1',
    'struct_c__S__HEAP_ENTRY_Ua_Sa_0',
    'struct_c__S__HEAP_ENTRY_Ua_Sa_3',
    'struct_c__S__HEAP_ENTRY_Ua_Sa_2',
    'struct_c__S__HEAP_ENTRY_Ua_Sa_5',
    'struct_c__S__HEAP_ENTRY_Ua_Sa_4', 'PPLIST_ENTRY',
    'struct__RTL_CRITICAL_SECTION_DEBUG', 'INT8', 'PCHAR',
    'ULONGLONG', 'union_c__S__HEAP_FREE_ENTRY_Ua_Sa_Ua_2',
    'struct__HEAP_TAG_ENTRY', 'PSHORT', 'HEAP',
    'PHEAP_VIRTUAL_ALLOC_ENTRY', 'PPLFH_HEAP', 'PUINT8',
    'PHEAP_COUNTERS', 'SINGLE_LIST_ENTRY',
    'struct_c__S__HEAP_ENTRY_EXTRA_Ua_Sa_0',
    'struct__HEAP_PSEUDO_TAG_ENTRY', 'PPHEAP_BUCKET_RUN_INFO',
    'PPHEAP_COUNTERS', 'PPHEAP_ENTRY', 'PPRTL_CRITICAL_SECTION',
    'union_c__S__HEAP_FREE_ENTRY_Ua_0', 'PPHEAP_UCR_DESCRIPTOR',
    'PVOID', 'HEAP_BUCKET_COUNTERS']
