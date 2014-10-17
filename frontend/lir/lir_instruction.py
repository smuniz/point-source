# 
# Copyright (c) 2014 Sebastian Muniz
# 
# This code is part of point source decompiler
#


class LowLevelInstructionException(Exception):
    """Low-end instruction exception class."""
    pass


class LowLevelInstruction(object):
    """Hold instruction information obtained along with it's attributes from
    the function being analyzed.

    """

    # FIXME : These hardcoded values are duplicated in generic_disasm/base.py
    TYPE_NAMES = {
        0 : "assignment",
        1 : "cond. branch",
        2 : "uncond. branch",
        3 : "unknown",
        }

    def __init__(self):
        """Instance initialization."""
        self.address = None
        self.macro = False
        self.operands = list()
        self.name = ""
        self.type = None
        self.group = None
        self.mnemonic = None
        self.analyzed = False
        self.basic_block = None

    @property
    def basic_block(self):
        """Indicate the current instructions it belongs to."""
        return self._basic_block

    @basic_block.setter
    def basic_block(self, basic_block):
        """Store the current instructions it belongs to."""
        self._basic_block = basic_block

    @property
    def macro(self):
        """Indicate if the current instruction is a macro instruction
        (simplified instruction output wrapping two or more native
        instructions).

        """
        return self._macro

    @macro.setter
    def macro(self, macro):
        """Store if the current instruction is a macro instruction."""
        self._macro = bool(macro)

    @property
    def mnemonic(self):
        """Return the instructions mnemonic."""
        return self._mnemonic

    @mnemonic.setter
    def mnemonic(self, mnemonic):
        """Return the instructions mnemonic."""
        self._mnemonic = mnemonic

    def __str__(self):
        """Return the instructions string representation."""
        inst_repr = "%s" % self.mnemonic

        #
        # Get all (if any) the operands involved in this instruction.
        #
        if len(self):
            inst_repr += " " * (10 - len(inst_repr))

        inst_repr += ", ".join([str(op) for op in self])
        #for index, op in enumerate(self):
        #    if index > 0:
        #        inst_repr += ", "
        #    inst_repr += str(op)

        #inst_repr += ";"

        return inst_repr

    @property
    def group_name(self):
        """Return the group name where this instruction belongs to."""
        try:
            return self.TYPE_NAMES[self.group]
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
    def type(self):
        """Return an integer representing the instruction type."""
        return self._type

    @type.setter
    def type(self, _type):
        """Store an integer representing the instruction type."""
        self._type = _type

    def is_type(self, _type):
        """Return a boolean indicating if the specified type matches the
        current instruction type.

        """
        return self.type == _type

    #def __eq__(self, other):
    #    """Compare two instruction by its type and return if they are the same
    #    or not.

    #    """
    #    return self.is_type(other)

    def get_operand(self, n):
        """Return an instance of LowLevelOperand with the operand number
        specified.

        """
        if n < len(self):
            return self.operands[n]
        else:
            raise IndexError(
                "Invalid operand index (%d) on instruction \"%s\"" % (
                n, '-'))

    def get_operands_count(self):
        """Return the total number of operands."""
        return len(self.operands)

    def __len__(self):
        """Return the bytes length of the current instruction."""
        # FIXME: return inst length instead of operans qty.
        return self.get_operands_count()

    def __getitem__(self, key):
        if isinstance(key, slice):
            indices = key.indices(len(self))
            return [self[i] for i in xrange(*indices)]
        elif isinstance(key, int) or isinstance(key, long):
            return self.get_operand(key)
        else:
            raise TypeError

    @property
    def address(self):
        """Return the effective address of the instruction."""
        return self._address

    @address.setter
    def address(self, address):
        """Store the effective address of the instruction."""
        self._address = address

    @property
    def analyzed(self):
        """Return true in case that the instruction has been successfuly
        analized. Otherwise return false.

        """
        return self._analyzed

    @analyzed.setter
    def analyzed(self, state):
        """Store the analysis state of the instruction."""
        self._analyzed = bool(state)
