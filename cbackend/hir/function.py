# 
# Copyright (c) 2014 Sebastian Muniz
# 
# This code is part of point source decompiler
#

from statements import Statement, CompoundStatement

from middleend.mir.mir_function import *

#
# MIR calling conventions to C equivalents.
#
CALLING_CONVENTIONS = {
     CALL_CONV_C             : "ccall",
     CALL_CONV_FASTCALL      : "fastcall",
     CALL_CONV_COLDCALL      : "coldcall",
     CALL_CONV_X86_STDCALL   : "x86call",
     CALL_CONV_X86_FASTCALL  : "x86fastcall",
     CALL_CONV_GHC           : "unk",
     CALL_CONV_ARM_APCS      : "unk",
     CALL_CONV_ARM_AAPCS     : "unk",
     CALL_CONV_ARM_AAPCS_VFP : "unk",
     CALL_CONV_MSP430_INTR   : "unk",
     CALL_CONV_X86_THISCALL  : "unk",
     CALL_CONV_PTX_KERNEL    : "unk",
     CALL_CONV_PTX_DEVICE    : "unk",
     CALL_CONV_MBLAZE_INTR   : "unk",
     CALL_CONV_MBLAZE_SVOL   : "unk",
    }


class FunctionException(Exception):
    """Base exception for HIR function exceptions."""
    pass


class Function(object):
    """Function class representing a HIR function."""

    def __init__(self):
        self._prologue_addresses = set()
        self._epilogue_addresses = set()
        self.parameters = list()
        self.blocks = list()

        self.start_address = 0
        self.end_address = 0

        self.return_type = None

        self.calling_convention = CALL_CONV_C
        self.name = ""
        #self.current = 0

    @property
    def has_parameters(self):
        """Indicate if the current function parameters or not."""
        return len(self.parameters) > 0

    @property
    def parameters(self):
        """Return the parameters list for the current function."""
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Return the parameters list for the current function."""
        self._parameters = parameters

    def get_parameter_n(self, n):
        """Return the parameter for the current function at the specified
        index.
        
        """
        try:
            return self.parameters[n]
        except IndexError, err:
            return None

    #def parameter(self, _type, name="", position=None):
    #    """Store the parameter for the current function at the specified
    #    index.
    #    
    #    """
    #    if position is None:
    #        self._parameters.append((_type, name))
    #    else:
    #        # TODO: should we check invalid index?
    #        try:
    #            self._parameters[position] = (_type, name)
    #        except IndexError, err:
    #            raise FunctionException(
    #                "Invalid index (%d) setting parameter." % position)

    @property
    def return_type(self):
        """Return the 'return type' for the current function.""" 
        return self._return_type

    @return_type.setter
    def return_type(self, return_type):
        """Return the 'return type' for the current function.""" 
        self._return_type = return_type

    @property
    def calling_convention(self):
        """Return the calling convention for the current function."""
        return self._calling_convention

    @calling_convention.setter
    def calling_convention(self, calling_convention):
        """Store the calling convention for the current function."""
        if calling_convention not in CALLING_CONVENTIONS:
            raise FunctionException(
                "Invalid calling convention specified (%s)" % \
                calling_convention)

        self._calling_convention = calling_convention

    @property
    def calling_convention_name(self):
        """Return the name of the calling convention for the current
        function.
        
        """
        return CALLING_CONVENTIONS[self.calling_convention]

    @property
    def name(self):
        """Return the name of the function."""
        return self._name

    @name.setter
    def name(self, name):
        """Store the name of the function."""
        self._name = name

    @property
    def start_address(self):
        """Return the start address of the function."""
        return self._start_address

    @start_address.setter
    def start_address(self, address):
        """Store the start address of the function."""
        self._start_address = address

    @property
    def end_address(self):
        """Return the end address of the function."""
        return self._end_address

    @end_address.setter
    def end_address(self, address):
        """Store the end address of the function."""
        self._end_address = address

    @property
    def prologue_addresses(self):
        """Return the list of prologue addresses."""
        return self._prologue_addresses

    @property
    def epilogue_addresses(self):
        """Return the list of epilogue addresses."""
        return self._epilogue_addresses

    def add_prologue_address(self, address):
        """Mark the specified address as part of the function prologue and
        remove it from the list of statements to analyze.

        """
        self._prologue_addresses.add(address)
        #self.remove_statement_by_address(address)

    def add_epilogue_address(self, address):
        """Mark the specified address as part of the function epilogue and
        remove it from the list of statements to analyze.

        """
        self._epilogue_addresses.add(address)
        #self.remove_statement_by_address(address)

    #def get_statement_by_address(self, address):
    #    for block in self:
    #        st = block.get_statement_by_address(address)
    #        if st is not None:
    #            return st
    #    return None

    #def get_statement_by_index(self, index):
    #    """Given the index referencing a statement among ALL the statements in
    #    every block, find it and return it.

    #    """
    #    i = 0
    #    for block in self:
    #        for stmt in block:
    #            if i == index:
    #                return stmt
    #            i += 1
    #    return None

    #def mark_statement_removed_by_index(self, index):
    #    """Given the index referencing a statement among ALL the statements in
    #    every block, find it and remove it from the list of it's block.

    #    """
    #    i = 0
    #    for block in self:
    #        for stmt in block:
    #            if i == index:
    #                stmt.remove()
    #                return True
    #            i += 1
    #    return False

    #def remove_statement_by_address(self, address):
    #    """Given a specific virtual memory address, remove the statement whose
    #    assembly instruction is located at that address.

    #    """
    #    for block in self:
    #        if block.remove_statement_by_address(address):
    #            return True
    #    return False

    #def remove_statement_by_index(self, index):
    #    """Given the index referencing a statement among ALL the statements in
    #    every block, find it and remove it from the list of it's block.

    #    """
    #    i = 0
    #    for block in self:
    #        for stmt in block:
    #            if i == index:
    #                return block.remove_statement(stmt)
    #            i += 1
    #    return False

    #def has_address(self, address):
    #    for block in self.blocks:
    #        #if block.get_statement_by_address(address) is not None:
    #            #return True
    #        print "checking block %s" % block
    #        for st in block:
    #            print "checking address 0x%X" % address
    #            if st.has_address(address):
    #                return True
    #    return False

    @property
    def blocks(self):
        return self._blocks

    @blocks.setter
    def blocks(self, blocks):
        self._blocks = blocks

    def add_block(self, block):
        """Add the new block to the inner blocks of this object after it is
        validated.
        
        """
        if not isinstance(block, CompoundStatement):
            raise FunctionException(
                "Invalid function block statement : %s" % block)

        self._blocks.append(block)

    #def get_block_index(self, block):
    #    """Return the inner block index based on the block specified."""
    #    return self._blocks.index(block)

    #def get_block_by_address(self, ea):
    #    raise FunctionException("Function.get_block_by_address()")

    #def get_blocks_count(self):
    #    """Return the total number of blocks currently stored."""
    #    return len(self._blocks)

    #def __getitem__(self, key):
    #    """..."""
    #    if isinstance(key, slice):
    #        indices = key.indices(len(self))
    #        return [self[i] for i in xrange(*indices)]

    #    elif isinstance(key, (int, long)):
    #        try:
    #            return self.block[key]
    #        except KeyError:
    #            raise IndexError
    #    else:
    #        raise TypeError

    def __len__(self):
        """Return the total number of statements in the current function."""
        return sum([len(b) for b in self.blocks])

    #def __delitem__(self, item):
    #    raise FunctionException("TODO: Function.__delitem__()")

    @property
    def is_calling_convention_c(self):
        return self.calling_convention == CALL_CONV_C

    @property
    def is_calling_convention_fastcall(self):
        return self.calling_convention == CALL_CONV_FASTCALL

    @property
    def is_calling_convention_coldcall(self):
        return self.calling_convention == CALL_CONV_COLDCALL

    @property
    def is_calling_convention_x86_stdcall(self):
        return self.calling_convention == CALL_CONV_X86_STDCALL

    @property
    def is_calling_convention_x86_fastcall(self):
        return self.calling_convention == CALL_CONV_X86_FASTCALL

    @property
    def is_calling_convention_ghc(self):
        return self.calling_convention == CALL_CONV_GHC

    @property
    def is_calling_convention_arm_apcs(self):
        return self.calling_convention == CALL_CONV_ARM_APCS

    @property
    def is_calling_convention_arm_aapcs(self):
        return self.calling_convention == CALL_CONV_ARM_AAPCS

    @property
    def is_calling_convention_arm_aapcs_vfp(self):
        return self.calling_convention == CALL_CONV_ARM_AAPCS_VFP

    @property
    def is_calling_convention_msp430_intr(self):
        return self.calling_convention == CALL_CONV_MSP430_INTR

    @property
    def is_calling_convention_x86_thiscall(self):
        return self.calling_convention == CALL_CONV_X86_THISCALL

    @property
    def is_calling_convention_ptx_kernel(self):
        return self.calling_convention == CALL_CONV_PTX_KERNEL

    @property
    def is_calling_convention_ptx_device(self):
        return self.calling_convention == CALL_CONV_PTX_DEVICE

    @property
    def is_calling_convention_mblaze_intr(self):
        return self.calling_convention == CALL_CONV_MBLAZE_INTR

    @property
    def is_calling_convention_mblaze_svol(self):
        return self.calling_convention == CALL_CONV_MBLAZE_SVOL

    def __str__(self):
        _str = ""

        indent_level = 1
        indent_spaces = 4
        indent = " " * (indent_level * indent_spaces)

        ret_type = self.return_type
        name = self.name
        params = "()"#self.parameter

        _str += "%(ret_type)s %(name)s %(params)s\n" % vars()
        _str += "{\n"

        #from textwrap import TextWrapper
        if len(self) == 0:
            _str += "%(indent)s// Empty function.\n" % vars()
        else:
            for idx, block in enumerate(self.blocks):
                _str += "%(indent)s// Block %(idx)d\n" % vars()

                # Set the label name in case it was specified and only when
                # there is more than one block statement present.
                if len(self.blocks) > 1 and block.label is not None:
                    label = block.label
                    _str += "%(indent)s%(label)s:\n" % vars()

                #w = TextWrapper()
                #w.initial_indent = indent_level * indent_spaces
                #w.subsequent_indent = w.initial_indent
                block_str = ""
                for line in str(block).splitlines():
                    block_str += "%(indent)s%(line)s\n" % vars()
                _str += "%(block_str)s\n" % vars()

        _str += "}"

        return _str
