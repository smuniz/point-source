# 
# Copyright (c) 2013 Sebastian Muniz
# 
# This code is part of point source decompiler
#

from middleend.mir_exception import MiddleIrException

from middleend.mir.mir_llvm_instance import MiddleIrLLVMInstance
from middleend.mir.mir_instruction import MiddleIrInstructionBuilder

__all__ = ["MiddleIrBasicBlockException", "MiddleIrBasicBlock"]


class MiddleIrBasicBlockException(MiddleIrException):
    """Middle IR basic block exception."""
    pass


class MiddleIrBasicBlock(MiddleIrLLVMInstance):
    """Middle level intermediate representation class of an basic block inside
    the function being deocmpiled.

    This class main objetive is to provide a simple abstration layer over the
    LLVM IR basic block obeject.

    """

    def __init__(self, label=""):
        """Initialize the intermediate level IR module class."""
        super(MiddleIrBasicBlock, self).__init__()

        self.label = label

        self.instructions = dict()

        self.mir_inst_builder = None

    def add_instruction(self, mir_instruction):
        """Add a new MIR instruction to the current basic block."""
        # FIXME:
        # MIR instructions might occupy more than 1 address meaning that it'll
        # be equivalent to more than 1 LIR instruction.
        self.instructions[mir_instruction.start_address] = mir_instruction

        self.instructions.keys().sort()

    def get_instruction(self, n):
        """..."""
        k = self.instructions.keys()
        k.sort()  # TODO: do we even need this?

        if n >= len(k):
            raise MiddleIrBasicBlockException(
                "Instruction index %d is out of scope." % n)

        return self.instructions[k[n]]

    def __getitem__(self, key):
        """..."""
        if isinstance(key, slice):
            indices = key.indices(len(self))
            return [self[i] for i in xrange(*indices)]

        elif isinstance(key, int) or isinstance(key, long):
            try:
                return self.get_instruction(key)

            except MiddleIrBasicBlockException:
                raise IndexError

        else:
            raise TypeError

    def __len__(self):
        return len(self.instructions)

    @property
    def end_address(self):
        """Return the last address of the basic block."""
        #try:
        #    max_addr = self[-1].get_end_address()

        #    for inst in self:
        #        if inst.get_end_address > max_addr:
        #            max_addr = inst.get_end_address()

        #    return max_addr
        #except IndexError, err:
        #    return None
        return self._end_address

    @end_address.setter
    def end_address(self, end_address):
        self._end_address = end_address

    @property
    def start_address(self):
        """Return the initial address of the basic block."""
        #try:
        #    min_addr = self[0].get_start_address()

        #    for inst in self:
        #        if inst.get_start_address < min_addr:
        #            min_addr = inst.get_start_address()

        #    return min_addr
        #except IndexError, err:
        #    return None
        return self._start_address

    @start_address.setter
    def start_address(self, start_address):
        self._start_address = start_address

    def has_address(self, address):
        return self.start_address <= address <= self._end_address

    @property
    def label(self):
        """Return the label text of the basic block."""
        return self._label

    @label.setter
    def label(self, label=""):
        """Store the label text of the basic block."""
        self._label = label

    @property
    def instruction_builder(self):
        """Return the Middle-end IR instruction builder instance to be able to
        create and add instructions to the current basic block.

        """
        if self.mir_inst_builder:
            return self.mir_inst_builder

        # Unable to obtain instruction builder for current
        # address. Move on to the next address in the list to
        # analyze.
        raise MiddleIrBasicBlockException("No instruction builder available")

    @instruction_builder.setter
    def instruction_builder(self, mir_inst_builder):
        """Store the Middle-end IR instruction builder instance to be able to
        create and add instructions to the current basic block.

        """
        self.mir_inst_builder = mir_inst_builder

    def _llvm_set_function(self, llvm_function):
        """Store the LLVM function object owning this basic block."""
        self.llvm_function = llvm_function

        # Add the LLVM basic block object to the current function.
        self._ptr = self.llvm_function.append_basic_block(self.label)
        
        #self.instruction_builder = MiddleIrInstructionBuilder(self)

    def __str__(self):
        return str(self._ptr)
