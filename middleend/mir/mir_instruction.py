# 
# Copyright (c) 2013 Sebastian Muniz
# 
# This code is part of point source decompiler
#

from traceback import print_stack

from middleend.mir_exception import MiddleIrException
from middleend.mir.mir_llvm_instance import MiddleIrLLVMInstance

from area import Area

from llvm import *
from llvm.core import *

__all__ = [ "MiddleIrInstructionBuilder",
            "MiddleIrInstructionBuilderException",
            "MiddleIrInstruction",
            "MiddleIrInstructionException",
            "MiddleIrVolatileInstruction"]


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
        # Instantiate an LLVM instruction builder for further usage.
        #
        self.llvm_builder = Builder.new(mir_basic_block._ptr)

    def position_at_address(self, address):
        """Position the builder at the specified address."""
        if len(self.mir_basic_block) == 0:
            llvm_basic_block = self.mir_basic_block._ptr

            self.llvm_builder.position_at_beginning(llvm_basic_block)
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

            self.llvm_builder.position_before(llvm_inst)
            return

        raise MiddleIrInstructionBuilderException(
            "Unable to find suitable position for address 0x%X" % address)

    #
    # Arithmethic, bitwise and logical
    #
    def add(self, lhs, rhs, name=""):
        """Generate an LLVM IR add instruction."""
        #_type = LLVM_add
        return MiddleIrInstruction(self.llvm_builder.add(
            lhs._ptr, rhs._ptr, name))

    #
    # Misc.
    #
    def call(self, fn, args, name=""):
        """Generate an LLVM IR call instruction."""
        llvm_func = fn._llvm_definition

        if isinstance(args, list):
            arguments = [arg._ptr for arg in args]
        else:
            arguments = [args._ptr, ]

        try:
            llvm_inst = self.llvm_builder.call(llvm_func, arguments, name)
            _type = OPCODE_CALL #LLVM_call
            return MiddleIrInstruction(
                llvm_inst, _type)
        except TypeError, err:
            raise MiddleIrInstructionException(err)

    #
    # Memory
    #
    def alloca(self, ty, size=None, name=""):
        """Generate an LLVM IR alloca instruction."""
        sizeptr = size._ptr if size else None
        _type = OPCODE_ALLOCA #LLVM_alloca
        return MiddleIrInstruction(
            self.llvm_builder.alloca(ty._ptr, sizeptr, name), _type)

    def alloca_array(self, ty, size, name=""):
        """Generate an LLVM IR alloca_array instruction."""
        return MiddleIrInstruction(
            self.llvm_builder.alloca_array(ty._ptr, size, name))

    def free(self, ptr):
        """Generate an LLVM IR free instruction."""
        #return MiddleIrInstruction(self.llvm_builder.alloca_array(ptr))
        raise Exception("Builder.free not implemented.")

    def gep(self, pointer, mir_indices, name="", inbounds=False):
        """Generate an LLVM IR getelementptr instruction."""
        indices = [idx._ptr for idx in mir_indices]
        llvm_inst = self.llvm_builder.gep(pointer._ptr, indices, name, inbounds)
        _type = OPCODE_GETELEMENTPTR # LLVM_getelementptr

        return MiddleIrInstruction(llvm_inst, _type)

    def load(self, ptr, name=""):
        """Generate an LLVM IR load instruction."""
        _type = OPCODE_LOAD
        return MiddleIrInstruction(self.llvm_builder.load(ptr, name), _type)

    def malloc(self, ty, name=""):
        """Generate an LLVM IR malloc instruction."""
        #_type = OPCODE_ALLOCA
        _type = None
        return MiddleIrInstruction(
            self.llvm_builder.malloc(ty._ptr, name), _type)

    def malloc_array(self, ty, size, name=""):
        """Generate an LLVM IR malloc_array instruction."""
        return MiddleIrInstruction(self.llvm_builder.malloc_array(
                ty._ptr, size, name))

    def store(self, mir_value, mir_ptr):
        """Generate an LLVM IR store instruction."""
        return MiddleIrInstruction(self.llvm_builder.store(
                mir_value, mir_ptr._ptr))

    #
    # Terminator instructions
    #
    def branch(self, bblk):
        """Generate an LLVM IR branch instruction."""
        _type = OPCODE_UNREACHABLE #LLVM_unreachable
        llvm_type = self.llvm_builder.branch(bblk._ptr)
        return MiddleIrInstruction(llvm_inst, _type)

    def ret(self, ret_val=None):
        """Generate an LLVM IR 'ret' instruction of the right type."""
        _type = OPCODE_RET #LLVM_ret
        llvm_inst = None
        operands = None

        if ret_val is None:
            #Generate an LLVM IR 'ret_void' instruction.
            llvm_inst = self.llvm_builder.ret_void()

        elif type(ret_val) in (tuple, list):
            # Generate an LLVM IR 'ret_many' instruction.
            raise Exception("TODO / FIXME: ret_many native llvmpy objs")
            llvm_inst = self.llvm_builder.ret_many(ret_val)

        else:
            # We're returning just one value.
            llvm_inst = self.llvm_builder.ret(ret_val._ptr)
            operands = [ret_val, ]

        return MiddleIrInstruction(llvm_inst, _type, operands=operands)

    #
    # Others
    #
    def pointer(self, pointee, addr_space=""):
        """Generate an LLVM IR pointer instruction."""
        llvm_pointee = pointee._ptr
        return MiddleIrInstruction(
            self.llvm_builder.pointer(llvm_pointee, addr_space))


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

    @property
    def type(self):
        """Return the type this instruction belongs to."""
        return self._type

    @type.setter
    def type(self, _type):
        """Store the type this instruction belongs to."""
        self._type = _type

        # Automatically set group 
        # TODO / FIXME : wtf
        #print "type : %d" % _type
        #print "[[[[[]]]]]]]]]]]]>>> %s" % self._ptr
        #print str(self._ptr.name)
        if self._ptr is None:
            self.group = UNKNOWN_GROUP

        if _type in TERMINATOR_INSTRUCTIONS:
            self.group = TERMINATOR_GROUP

        elif _type in MEMORY_ACCESS_OPERATIONS:
            self.group = MEMORY_ACCESS_GROUP

        elif _type in OTHER_INSTRUCTIONS:
            self.group = OTHER_GROUP

        #if self.is_terminator:
        #    self.group = TERMINATOR_GROUP

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
            raise FrontEndException(
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

TERMINATOR_GROUP = 0
BINARY_OP_GROUP = 1
SHIFT_GROUP = 2
LOGICAL_SHIFT_GROUP = 3
ARITHMETIC_SHIFT_GROUP = 4
ASSOCIATIVE_GROUP = 5
COMMUTATIVE_GROUP = 6

MEMORY_ACCESS_GROUP = 9

OTHER_GROUP = 10
UNKNOWN_GROUP = 11

GROUP_NAMES = {
    TERMINATOR_GROUP : "terminator",

    BINARY_OP_GROUP : "binary",
    SHIFT_GROUP : "shift",
    LOGICAL_SHIFT_GROUP : "logical",
    ARITHMETIC_SHIFT_GROUP : "arithmetic",
    ASSOCIATIVE_GROUP : "associative",
    COMMUTATIVE_GROUP : "commutative",

    MEMORY_ACCESS_GROUP : "memory_access",

    OTHER_GROUP : "other",
    UNKNOWN_GROUP : "unknown",
    }

"""
LLVM_ret = 0
LLVM_br = 1
LLVM_switch = 2
LLVM_indirectbr = 3
LLVM_invoke = 4
LLVM_resume = 5
LLVM_unreachable = 6

LLVM_icmp = 0x10
LLVM_fcmp = 0x11
LLVM_phi = 0x12
LLVM_select = 0x13
LLVM_call = 0x14
LLVM_va_arg = 0x15
LLVM_landingpad = 0x16


LLVM_alloca = 0x20
LLVM_load = 0x21
LLVM_store = 0x22
LLVM_fence = 0x23
LLVM_cmpxchg = 0x24
LLVM_atomicrmw = 0x25
LLVM_getelementptr = 0x26
"""


TERMINATOR_INSTRUCTIONS = [
    OPCODE_RET,
    OPCODE_BR,
    OPCODE_SWITCH,
    OPCODE_INDIRECT_BR,
    OPCODE_INVOKE,
    OPCODE_RESUME,
    OPCODE_UNREACHABLE,
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

"""

Binary Operations
'add' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'fadd' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'sub' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'fsub' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'mul' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'fmul' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'udiv' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'sdiv' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'fdiv' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'urem' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'srem' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'frem' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:

Bitwise Binary Operations
'shl' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'lshr' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'ashr' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'and' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'or' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'xor' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:

Vector Operations
'extractelement' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'insertelement' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'shufflevector' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:

Aggregate Operations
'extractvalue' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'insertvalue' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:

Memory Access and Addressing Operations
'alloca' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'load' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Examples:
'store' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'fence' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'cmpxchg' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'atomicrmw' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'getelementptr' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:

Conversion Operations
'trunc .. to' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'zext .. to' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'sext .. to' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'fptrunc .. to' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'fpext .. to' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'fptoui .. to' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'fptosi .. to' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'uitofp .. to' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'sitofp .. to' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'ptrtoint .. to' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'inttoptr .. to' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'bitcast .. to' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'addrspacecast .. to' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:

Other Operations
'icmp' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'fcmp' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'phi' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'select' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'call' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'va_arg' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:
'landingpad' Instruction
Syntax:
Overview:
Arguments:
Semantics:
Example:

Intrinsic Functions

Variable Argument Handling Intrinsics
'llvm.va_start' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.va_end' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.va_copy' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:

Accurate Garbage Collection Intrinsics
'llvm.gcroot' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.gcread' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.gcwrite' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:

Code Generator Intrinsics
'llvm.returnaddress' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.frameaddress' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.read_register' and 'llvm.write_register' Intrinsics
Syntax:
Overview:
Semantics:
'llvm.stacksave' Intrinsic
Syntax:
Overview:
Semantics:
'llvm.stackrestore' Intrinsic
Syntax:
Overview:
Semantics:
'llvm.prefetch' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.pcmarker' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.readcyclecounter' Intrinsic
Syntax:
Overview:
Semantics:
'llvm.clear_cache' Intrinsic
Syntax:
Overview:
Semantics:

Standard C Library Intrinsics
'llvm.memcpy' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.memmove' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.memset.*' Intrinsics
Syntax:
Overview:
Arguments:
Semantics:
'llvm.sqrt.*' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.powi.*' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.sin.*' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.cos.*' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.pow.*' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.exp.*' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.exp2.*' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.log.*' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.log10.*' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.log2.*' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.fma.*' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.fabs.*' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.copysign.*' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.floor.*' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.ceil.*' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.trunc.*' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.rint.*' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.nearbyint.*' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.round.*' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:

Bit Manipulation Intrinsics
'llvm.bswap.*' Intrinsics
Syntax:
Overview:
Semantics:
'llvm.ctpop.*' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.ctlz.*' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.cttz.*' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:

Arithmetic with Overflow Intrinsics
'llvm.sadd.with.overflow.*' Intrinsics
Syntax:
Overview:
Arguments:
Semantics:
Examples:
'llvm.uadd.with.overflow.*' Intrinsics
Syntax:
Overview:
Arguments:
Semantics:
Examples:
'llvm.ssub.with.overflow.*' Intrinsics
Syntax:
Overview:
Arguments:
Semantics:
Examples:
'llvm.usub.with.overflow.*' Intrinsics
Syntax:
Overview:
Arguments:
Semantics:
Examples:
'llvm.smul.with.overflow.*' Intrinsics
Syntax:
Overview:
Arguments:
Semantics:
Examples:
'llvm.umul.with.overflow.*' Intrinsics
Syntax:
Overview:
Arguments:
Semantics:
Examples:

Specialised Arithmetic Intrinsics
'llvm.fmuladd.*' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
Examples:

Half Precision Floating Point Intrinsics
'llvm.convert.to.fp16' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
Examples:
'llvm.convert.from.fp16' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
Examples:

Debugger Intrinsics

Exception Handling Intrinsics

Trampoline Intrinsics
'llvm.init.trampoline' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.adjust.trampoline' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:

Memory Use Markers
'llvm.lifetime.start' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.lifetime.end' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.invariant.start' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.invariant.end' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:

General Intrinsics
'llvm.var.annotation' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.ptr.annotation.*' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.annotation.*' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.trap' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.debugtrap' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.stackprotector' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.stackprotectorcheck' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.objectsize' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.expect' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.assume' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:
'llvm.donothing' Intrinsic
Syntax:
Overview:
Arguments:
Semantics:

Stack Map Intrinsics
"""
