# 
# Copyright (c) 2014 Sebastian Muniz
# 
# This code is part of point source decompiler
#

from traceback import print_stack

from middleend.mir_exception import MiddleIrException
from middleend.mir.mir_llvm_instance import MiddleIrLLVMInstance

from area import Area

from llvm import *
from llvm.core import *

#__all__ = [ "MiddleIrInstructionBuilder",
#            "MiddleIrInstructionBuilderException",
#            "MiddleIrInstruction",
#            "MiddleIrInstructionException",
#            "MiddleIrVolatileInstruction"]


class MiddleIrInstructionBuilderException(MiddleIrException):
    """MIR instruction builder exception."""
    pass


class MiddleIrInstructionBuilder(object):
    """Instruction builder class for middle-end IR warpper arround LLVM IR.
    
    """

    def __init__(self, mir_basic_block):
        """Instruction builder instance initialization."""

        self.mir_basic_block = mir_basic_block

        #
        # Instantiate a LLVM instruction builder to create each instruction
        # specified by the user.
        #
        self._ptr = Builder.new(mir_basic_block._ptr)

    @property
    def _ptr(self):
        """Return builder type."""
        return self._llvm_ptr

    @_ptr.setter
    def _ptr(self, ptr):
        """Store builder type."""
        self._llvm_ptr = ptr

    def position_at_address(self, address):
        """Position the builder at the specified address."""
        if len(self.mir_basic_block) == 0:
            llvm_basic_block = self.mir_basic_block._ptr

            self._ptr.position_at_beginning(llvm_basic_block)
            return

        for mir_inst in self.mir_basic_block:
            # If current instruction address is lower that the one specified by
            # the user, continue the search with the next available
            # instruction.
            if mir_inst.get_start_address() <= address:
                llvm_inst = mir_inst._ptr
                #print "---> LLVM inst 0x%X %s" % \
                #    (mir_inst.get_start_address(), mir_inst)
                continue

            llvm_inst = mir_inst._ptr

            if llvm_inst is None:
                raise MiddleIrInstructionBuilderException(
                    "Warning: _ptr returned None at 0x%X" % \
                    address)

            self._ptr.position_before(llvm_inst)
            return

        raise MiddleIrInstructionBuilderException(
            "Unable to find suitable position for address 0x%X" % address)

    #
    # Arithmethic, bitwise and logical
    #
    def add(self, lhs, rhs, name=""):
        """Generate a LLVM IR add instruction."""
        #_type = LLVM_add
        return MiddleIrInstruction(self._ptr.add(
            lhs._ptr, rhs._ptr, name))

    #
    # Misc.
    #
    def call(self, callee, arguments, name=""):
        """Generate a LLVM IR call instruction."""
        return MiddleIrCallInstruction(self, callee, arguments, name)

    #
    # Memory
    #
    def alloca(self, _type, size=None, name=""):
        """Generate a LLVM IR alloca instruction."""
        return MiddleIrAllocaInstruction(self, _type, size, name)

    def alloca_array(self, ty, size, name=""):
        """Generate a LLVM IR alloca_array instruction."""
        #_type = OPCODE_ALLOCA
        return MiddleIrInstruction(
            self._ptr.alloca_array(ty._ptr, size, name))

    def free(self, ptr):
        """Generate a LLVM IR free instruction."""
        #return MiddleIrInstruction(self._ptr.alloca_array(ptr))
        raise Exception("Builder.free not implemented.")

    def gep(self, pointer, indices, name="", inbounds=False):
        """Generate a LLVM IR getelementptr instruction."""
        return MiddleIrGepInstruction(self, pointer, indices, name, inbounds)

    def load(self, ptr, name=""):
        """Generate a LLVM IR load instruction."""
        return MiddleIrLoadInstruction(self, ptr, name)

    def malloc(self, ty, name=""):
        """Generate a LLVM IR malloc instruction."""
        #_type = OPCODE_ALLOCA
        _type = None
        return MiddleIrInstruction(
            self._ptr.malloc(ty._ptr, name), _type)

    def malloc_array(self, ty, size, name=""):
        """Generate a LLVM IR malloc_array instruction."""
        return MiddleIrInstruction(self._ptr.malloc_array(
                ty._ptr, size, name))

    def store(self, value, pointer, align=0, volatile=False):
        """Generate a LLVM IR store instruction."""
        return MiddleIrStoreInstruction(self, value, pointer, align, volatile)

    def inttoptr(self, value, dest_type, name=""):
        """Generate a LLVM IR inttoptr instruction."""
        return MiddleIrIntToPtrInstruction(self, value, dest_type, name)

    #
    # Terminator instructions
    #
    def branch(self, bblk):
        """Generate a LLVM IR branch instruction."""
        _type = OPCODE_UNREACHABLE #LLVM_unreachable
        llvm_type = self._ptr.branch(bblk._ptr)
        return MiddleIrInstruction(llvm_inst, _type)

    def ret(self, ret_val=None):
        """Generate a LLVM IR 'ret' instruction of the right type."""
        return MiddleIrRetInstruction(self, ret_val)

    #
    # Others
    #
    def pointer(self, pointee, addr_space=0):
        """Generate a LLVM IR pointer instruction."""
        llvm_pointee = pointee._ptr
        return MiddleIrInstruction(
            self._ptr.pointer(llvm_pointee, addr_space))


    @staticmethod
    def new(basic_block):
        """Create a instruction builder for the current basic block."""
        try:
            new_builder = basic_block.instruction_builder
        except MiddleIrException, err:
            new_builder = MiddleIrInstructionBuilder(basic_block)
        return new_builder

    #def delete(self):
    #    """Delete ourselves."""
    #    if self in self.module.functions:
    #        self.module.functions.remove(self)

    #    if self._ptr:
    #        self._ptr.delete()
# ---------------------------------------------------------------------------------


class MiddleIrInstructionException(Exception):
    """MIR instruction generic exception."""
    pass


class MiddleIrInstruction(MiddleIrLLVMInstance, Area):
    """
    Middle level intermediate representation class of an instruction inside a
    basic block.

    This class main objetive is to provide a simple abstration layer over the
    LLVM IR instruction obeject.

    """

    def __init__(self, llvm_instruction=None, _type=None, operands=None):
        """Initialize the intermediate level IR module class."""
        #super(MiddleIrInstruction, self).__init__()
        # LLVM specific objects initialization.
        MiddleIrLLVMInstance.__init__(self, llvm_instruction)
        Area.__init__(self)

        self.print_address = True
        
        self.type = _type

        if operands is None:
            self.operands = list()
        else:
            self.operands = operands

        self.is_used = False

    @property
    def type(self):
        """Return the type this instruction belongs to."""
        return self._type

    @type.setter
    def type(self, _type):
        """Store the type this instruction belongs to."""
        self._type = _type

        #
        # Automatically set group 
        #
        #print "type : %d" % _type
        #print "[[[[[]]]]]]]]]]]]>>> %s" % self._ptr

        if _type in TERMINATOR_INSTRUCTIONS:
            self.group = TERMINATOR_GROUP

        elif _type in MEMORY_ACCESS_OPERATIONS:
            self.group = MEMORY_ACCESS_GROUP

        elif _type in OTHER_INSTRUCTIONS:
            self.group = OTHER_GROUP

        #elif self.is_binary_op:
        #    self.group = BINARY_OP_GROUP

        #elif self.is_shift:
        #    self.group = SHIFT_GROUP

        #elif self.is_logical_shift:
        #    self.group = LOGICAL_SHIFT_GROUP

        #elif self.is_arithmetic_shift:
        #    self.group = ARITHMETIC_SHIFT_GROUP

        #elif self.is_associative:
        #    self.group = ASSOCIATIVE_GROUP

        #elif self.is_commutative:
        #    self.group = COMMUTATIVE_GROUP

        else:
            self.group = UNKNOWN_GROUP

    @property
    def print_address(self):
        """Display the instruction address as a side comment when obtaining its
        string representation.

        """
        return self._print_address

    @print_address.setter
    def print_address(self, do_print):
        """Display the instruction address as a side comment when obtaining its
        string representation.

        """
        self._print_address = bool(do_print)

    def __str__(self):
        """Return string representation of the current instruction."""
        inst_str = "%s" % self._ptr

        if self.print_address:
            inst_str += "  ; %s" % \
                ", ".join(["0x%X" % address for address in self.addresses])

        #print "__str__ = %s" % inst_str
        return inst_str

    @property
    def group_name(self):
        """Return the group name where this instruction belongs to."""
        try:
            return GROUP_NAMES[self.group]
        except IndexError, err:
            raise MiddleIrInstructionException(
                "Unable to get type name for type (%d) specified." % \
                self.group)

    @property
    def group(self):
        """Return an integer representing the instruction group."""
        return self._group

    @group.setter
    def group(self, group):
        """Store an integer representing the instruction group."""
        self._group = group

    @property
    def is_terminator(self):
        """Indicate if the current instruction is a terminator."""
        return self._ptr.is_terminator

    @property
    def is_binary_op(self):
        return self._ptr.is_binary_op

    @property
    def is_shift(self):
        return self._ptr.is_shift

    @property
    def is_cast(self):
        return self._ptr.is_cast

    @property
    def is_logical_shift(self):
        return self._ptr.is_logical_shift

    @property
    def is_arithmetic_shift(self):
        return self._ptr.is_arithmetic_shift

    @property
    def is_associative(self):
        return self._ptr.is_associative

    @property
    def is_commutative(self):
        return self._ptr.is_commutative

    @property
    def is_binary_op(self):
        """Indicate if the current instruction is a binary operator."""
        return self._ptr.is_binary_op

    @property
    def is_shift(self):
        """Indicate if the current instruction is a shift."""
        return self._ptr.is_shift

    @property
    def is_cast(self):
        """Indicate if the current instruction is a cast."""
        return self._ptr.is_cast

    @property
    def is_logical_shift(self):
        """Indicate if the current instruction is a logical shift."""
        return self._ptr.is_logical_shift

    @property
    def is_arithmetic_shift(self):
        """Indicate if the current instruction is an arithmethic shift."""
        return self._ptr.is_arithmetic_shift

    @property
    def is_associative(self):
        """Indicate if the current instruction is associative."""
        return self._ptr.is_associative

    @property
    def is_commutative(self):
        """Indicate if the current instruction is a commutative."""
        return self._ptr.is_commutative


class MiddleIrVolatileInstruction(object):

    def __init__(self, llvm_instruction=None):
        self.llvm_instruction = llvm_instruction

#
# Instructions groups identifiers and names.
#
TERMINATOR_GROUP = 0

BINARY_OP_GROUP = 1
SHIFT_GROUP = 2
LOGICAL_SHIFT_GROUP = 3
ARITHMETIC_SHIFT_GROUP = 4
ASSOCIATIVE_GROUP = 5
COMMUTATIVE_GROUP = 6

MEMORY_ACCESS_GROUP = 9

BITWISE_BINARY_GROUP = 10
VECTOR_GROUP = 11
AGGREGATE_GROUP = 12
CONVERSION_GROUP = 13

OTHER_GROUP = 14
UNKNOWN_GROUP = 15

GROUP_NAMES = {
    TERMINATOR_GROUP        : "terminator",

    BINARY_OP_GROUP         : "binary",
    SHIFT_GROUP             : "shift",
    LOGICAL_SHIFT_GROUP     : "logical",
    ARITHMETIC_SHIFT_GROUP  : "arithmetic",
    ASSOCIATIVE_GROUP       : "associative",
    COMMUTATIVE_GROUP       : "commutative",

    MEMORY_ACCESS_GROUP     : "memory_access",

    BITWISE_BINARY_GROUP    : "bitwise_binary",
    VECTOR_GROUP            : "vector",
    AGGREGATE_GROUP         : "aggregate",
    CONVERSION_GROUP        : "conversion",

    OTHER_GROUP             : "other",
    UNKNOWN_GROUP           : "unknown",
    }

#
# Instructions groups selection.
#
TERMINATOR_INSTRUCTIONS = [
    OPCODE_RET,
    OPCODE_BR,
    OPCODE_SWITCH,
    OPCODE_INDIRECT_BR,
    OPCODE_INVOKE,
    OPCODE_RESUME,
    OPCODE_UNREACHABLE,
    ]

BINARY_OP_GROUP = [
    OPCODE_ADD,
    OPCODE_FADD,
    OPCODE_SUB,
    OPCODE_FSUB,
    OPCODE_MUL,
    OPCODE_FMUL,
    OPCODE_UDIV,
    OPCODE_SDIV,
    OPCODE_FDIV,
    OPCODE_UREM,
    OPCODE_SREM,
    OPCODE_FREM,
    ]

OTHER_INSTRUCTIONS = [
    OPCODE_ICMP,
    OPCODE_FCMP,
    OPCODE_PHI,
    OPCODE_SELECT,
    OPCODE_CALL,
    OPCODE_VAARG,
    OPCODE_LANDINGPAD,
    ]

MEMORY_ACCESS_OPERATIONS = [
    OPCODE_ALLOCA,
    OPCODE_LOAD,
    OPCODE_STORE,
    OPCODE_FENCE,
    OPCODE_ATOMICCMPXCHG,
    OPCODE_ATOMICRMW,
    OPCODE_GETELEMENTPTR,
    ]

BITWISE_BINARY_OPERATIONS = [
    OPCODE_SHL,
    OPCODE_LSHR,
    OPCODE_ASHR,
    OPCODE_AND,
    OPCODE_OR,
    OPCODE_XOR,
    ]

VECTOR_OPERATIONS = [
    OPCODE_EXTRACTELEMENT,
    OPCODE_INSERTELEMENT,
    OPCODE_SHUFFLEVECTOR,
    ]

AGGREGATE_OPERATIONS = [
    OPCODE_EXTRACTVALUE,
    OPCODE_INSERTVALUE,
    ]

CONVERSION_OPERATIONS = [
    OPCODE_TRUNC,
    OPCODE_ZEXT,
    OPCODE_SEXT,
    OPCODE_FPTRUNC,
    OPCODE_FPEXT,
    OPCODE_FPTOUI,
    OPCODE_FPTOSI,
    OPCODE_UITOFP,
    OPCODE_SITOFP,
    OPCODE_PTRTOINT,
    OPCODE_INTTOPTR,
    OPCODE_BITCAST,
    OPCODE_ADDRSPACECAST,
    ]

"""
Intrinsic Functions

Variable Argument Handling Intrinsics
'llvm.va_start' Intrinsic
'llvm.va_end' Intrinsic
'llvm.va_copy' Intrinsic

Accurate Garbage Collection Intrinsics
'llvm.gcroot' Intrinsic
'llvm.gcread' Intrinsic
'llvm.gcwrite' Intrinsic

Code Generator Intrinsics
'llvm.returnaddress' Intrinsic
'llvm.frameaddress' Intrinsic
'llvm.read_register' and 'llvm.write_register' Intrinsics
'llvm.stacksave' Intrinsic
'llvm.stackrestore' Intrinsic
'llvm.prefetch' Intrinsic
'llvm.pcmarker' Intrinsic
'llvm.readcyclecounter' Intrinsic
'llvm.clear_cache' Intrinsic

Standard C Library Intrinsics
'llvm.memcpy' Intrinsic
'llvm.memmove' Intrinsic
'llvm.memset.*' Intrinsics
'llvm.sqrt.*' Intrinsic
'llvm.powi.*' Intrinsic
'llvm.sin.*' Intrinsic
'llvm.cos.*' Intrinsic
'llvm.pow.*' Intrinsic
'llvm.exp.*' Intrinsic
'llvm.exp2.*' Intrinsic
'llvm.log.*' Intrinsic
'llvm.log10.*' Intrinsic
'llvm.log2.*' Intrinsic
'llvm.fma.*' Intrinsic
'llvm.fabs.*' Intrinsic
'llvm.copysign.*' Intrinsic
'llvm.floor.*' Intrinsic
'llvm.ceil.*' Intrinsic
'llvm.trunc.*' Intrinsic
'llvm.rint.*' Intrinsic
'llvm.nearbyint.*' Intrinsic
'llvm.round.*' Intrinsic

Bit Manipulation Intrinsics
'llvm.bswap.*' Intrinsics
'llvm.ctpop.*' Intrinsic
'llvm.ctlz.*' Intrinsic
'llvm.cttz.*' Intrinsic

Arithmetic with Overflow Intrinsics
'llvm.sadd.with.overflow.*' Intrinsics
'llvm.uadd.with.overflow.*' Intrinsics
'llvm.ssub.with.overflow.*' Intrinsics
'llvm.usub.with.overflow.*' Intrinsics
'llvm.smul.with.overflow.*' Intrinsics
'llvm.umul.with.overflow.*' Intrinsics

Specialised Arithmetic Intrinsics
'llvm.fmuladd.*' Intrinsic

Half Precision Floating Point Intrinsics
'llvm.convert.to.fp16' Intrinsic
'llvm.convert.from.fp16' Intrinsic

Debugger Intrinsics

Exception Handling Intrinsics

Trampoline Intrinsics
'llvm.init.trampoline' Intrinsic
'llvm.adjust.trampoline' Intrinsic

Memory Use Markers
'llvm.lifetime.start' Intrinsic
'llvm.lifetime.end' Intrinsic
'llvm.invariant.start' Intrinsic
'llvm.invariant.end' Intrinsic

General Intrinsics
'llvm.var.annotation' Intrinsic
'llvm.ptr.annotation.*' Intrinsic
'llvm.annotation.*' Intrinsic
'llvm.trap' Intrinsic
'llvm.debugtrap' Intrinsic
'llvm.stackprotector' Intrinsic
'llvm.stackprotectorcheck' Intrinsic
'llvm.objectsize' Intrinsic
'llvm.expect' Intrinsic
'llvm.assume' Intrinsic
'llvm.donothing' Intrinsic

Stack Map Intrinsics
"""

class MiddleIrRetInstruction(MiddleIrInstruction):
    """Generate a MIR IR 'ret' instruction of the right type."""

    def __init__(self, builder, ret_val):
        super(MiddleIrRetInstruction, self).__init__(_type=OPCODE_RET)
        self.operands = None

        if ret_val is None:
            # Generate a LLVM IR 'ret_void' instruction.
            self._ptr = builder._ptr.ret_void()

        elif type(ret_val) in (tuple, list):
            # Generate a LLVM IR 'ret_many' instruction.
            raise MiddleIrInstructionException("TODO / FIXME: ret_many native llvmpy objs")
            self._ptr = builder._ptr.ret_many(ret_val)
            # Process each return value.
            #self.operands = None

        else:
            # We're returning just one value.
            self._ptr = builder._ptr.ret(ret_val._ptr)
            self.operands = [ret_val, ]


class MiddleIrCallInstruction(MiddleIrInstruction):
    """Generate a MIR IR 'call' instruction."""

    def __init__(self, builder, callee, arguments, name=""):
        super(MiddleIrCallInstruction, self).__init__(_type=OPCODE_CALL)

        self.name = name
        self.callee = callee
        self.arguments = arguments

        #
        # LLVM specifics.
        #
        llvm_func = callee._llvm_definition

        if isinstance(arguments, list):
            arguments_ptr = [arg._ptr for arg in arguments]
        else:
            arguments_ptr = [arguments._ptr, ]

        try:
            self._ptr = builder._ptr.call(llvm_func, arguments_ptr, name)
        except TypeError, err:
            raise MiddleIrInstructionException(
                "Unable to create MIR \'call\' instruction (%s)" % err)

    def get_readable_inners(self):
        """Return the arguments list in a readable fashion."""
        arguments = list()

        for idx, argument in enumerate(self.arguments):
            #print "arg idx:%d -> %s" % (idx, argument)
            arguments.append(argument.get_readable_inners())
        return arguments


class MiddleIrGepInstruction(MiddleIrInstruction):
    """Generate a MIR IR 'gep' instruction."""

    def __init__(self, builder, pointer, indices, name, inbounds):
        super(MiddleIrGepInstruction, self).__init__(
            _type=OPCODE_GETELEMENTPTR)

        self.pointer = pointer
        self.indices = indices
        self.name = name

        #
        # LLVM specifics.
        #
        indices_ptr = [idx._ptr for idx in indices]
        self._ptr = builder._ptr.gep(pointer._ptr, indices_ptr, name, inbounds)

    def get_readable_inners(self):
        """..."""
        return self.pointer.get_readable_inners()


class MiddleIrLoadInstruction(MiddleIrInstruction):
    """Generate a MIR IR 'load' instruction."""

    def __init__(self, builder, pointer, name):#, align=0, volatile=False):
        super(MiddleIrLoadInstruction, self).__init__(
            _type=OPCODE_LOAD)

        self.pointer = pointer
        self.name = name
        #self.align = align
        #self.volatile = volatile

        self._ptr = builder._ptr.load(
                pointer._ptr, name)#align, volatile)

    def get_readable_inners(self):
        """..."""
        return self.pointer.get_readable_inners()


class MiddleIrStoreInstruction(MiddleIrInstruction):
    """Generate a MIR IR 'store' instruction."""

    def __init__(self, builder, value, pointer, align=0, volatile=False):
        super(MiddleIrStoreInstruction, self).__init__(
            _type=OPCODE_STORE)

        self.value = value
        self.pointer = pointer
        self.align = align
        self.volatile = volatile

        self._ptr = builder._ptr.store(
                value._ptr, pointer._ptr, align, volatile)

    def get_readable_inners(self):
        """..."""
        return self.pointer.get_readable_inners()


class MiddleIrAllocaInstruction(MiddleIrInstruction):
    """Generate a MIR IR 'alloca' instruction."""

    def __init__(self, builder, alloca_type, size=None, name=""):
        super(MiddleIrAllocaInstruction, self).__init__(
            _type=OPCODE_ALLOCA)

        self.size_ptr = size._ptr if size else None
        self.alloca_type = alloca_type
        self.name = name

        self._ptr = builder._ptr.alloca(alloca_type._ptr)#, self.size_ptr, name)

    def get_readable_inners(self):
        """..."""
        return self.name


class MiddleIrPtrToIntInstruction(MiddleIrInstruction):
    """Generate a MIR IR 'ptrtoint' instruction."""

    def __init__(self, builder, value, dest_type, name=""):
        super(MiddleIrPtrToIntInstruction, self).__init__(
            _type=OPCODE_PTRTOINT)

        self.value = value
        self.dest_type = dest_type
        self.name = name

        self._ptr = builder._ptr.inttoptr(value._ptr, dest_type._ptr, name)

    def get_readable_inners(self):
        """..."""
        return self.name


class MiddleIrIntToPtrInstruction(MiddleIrInstruction):
    """Generate a MIR IR 'inttoptr' instruction."""

    def __init__(self, builder, value, dest_type, name=""):
        super(MiddleIrIntToPtrInstruction, self).__init__(
            _type=OPCODE_INTTOPTR)

        self.value = value
        self.dest_type = dest_type
        self.name = name

        self._ptr = builder._ptr.inttoptr(value._ptr, dest_type._ptr, name)

    def get_readable_inners(self):
        """..."""
        return self.name
