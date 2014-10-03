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
            "MiddleIrInstructionException"]


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

            if not llvm_inst:
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
        """Generate an LLVM IR xxx instruction."""
        return MiddleIrInstruction(self.llvm_builder.add(
            lhs._ptr, rhs._ptr, name))

    #
    # Misc.
    #
    def call(self, fn, args, name=""):
        """Generate an LLVM IR xxx instruction."""
        llvm_func = fn._llvm_get_definition()
        arguments = [arg._ptr for arg in args]

        return MiddleIrInstruction(
            self.llvm_builder.call(llvm_func, arguments, name))

    #
    # Memory
    #
    def alloca(self, ty, name=""):
        """Generate an LLVM IR xxx instruction."""
        return MiddleIrInstruction(
            self.llvm_builder.alloca(ty._ptr, name))

    def alloca_array(self, ty, size, name=""):
        """Generate an LLVM IR xxx instruction."""
        return MiddleIrInstruction(
            self.llvm_builder.alloca_array(ty._ptr, size, name))

    def free(self, ptr):
        """Generate an LLVM IR xxx instruction."""
        #return MiddleIrInstruction(self.llvm_builder.alloca_array(ptr))
        raise Exception("Builder.free not implemented.")

    def gep(self, ptr, mir_indices, name=""):
        """Generate an LLVM IR getelementptr instruction."""
        pointer = ptr._ptr
        #indices = mir_indices#._ptr
        indices = [idx._ptr for idx in mir_indices]

        return MiddleIrInstruction(
            self.llvm_builder.gep(pointer, indices, name))

    def load(self, ptr, name=""):
        """Generate an LLVM IR xxx instruction."""
        return MiddleIrInstruction(self.llvm_builder.load(ptr, name))

    def malloc(self, ty, name=""):
        """Generate an LLVM IR xxx instruction."""
        return MiddleIrInstruction(self.llvm_builder.malloc(ty._ptr, name))

    def malloc_array(self, ty, size, name=""):
        """Generate an LLVM IR xxx instruction."""
        return MiddleIrInstruction(self.llvm_builder.malloc_array(
                ty._ptr, size, name))

    def store(self, mir_value, mir_ptr):
        """Generate an LLVM IR xxx instruction."""
        return MiddleIrInstruction(self.llvm_builder.store(
                mir_value, mir_ptr._ptr))

    #
    # Terminator instructions
    #
    def branch(self, bblk):
        """Generate an LLVM IR xxx instruction."""
        return MiddleIrInstruction(
            self.llvm_builder.branch(
                bblk._ptr))

    def ret(self, ret_val=None):
        """Generate an LLVM IR 'ret' instruction of the right type."""
        _type = LLVM_ret
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
        """Generate an LLVM IR xxx instruction."""
        llvm_pointee = pointee._ptr
        return MiddleIrInstruction(
            self.llvm_builder.pointer(llvm_pointee, addr_space))

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
        MiddleIrLLVMInstance.__init__(self)
        Area.__init__(self)

        self.print_address = True
        
        # LLVM specific objects initialization.
        self._ptr = llvm_instruction

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
        if self.is_terminator:
            self.group = TERMINATOR_GROUP
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


TERMINATOR_GROUP = 0
UNKNOWN_GROUP = 3

GROUP_NAMES = {
    TERMINATOR_GROUP : "terminator",
    UNKNOWN_GROUP : "unknown",
    }

LLVM_ret = 0
LLVM_br = 1
LLVM_switch = 2
LLVM_indirectbr = 3
LLVM_invoke = 4
LLVM_resume = 5
LLVM_unreachable = 6

"""
TERMINATOR_INSTRUCTIONS = [
    LLVM_ret,
    LLVM_br,
    LLVM_switch,
    LLVM_indirectbr,
    LLVM_invoke,
    LLVM_resume,
    LLVM_unreachable,
    ]
"""
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
