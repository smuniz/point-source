# 
# Copyright (c) 2014 Sebastian Muniz
# 
# This code is part of point source decompiler
#

__all__ = ["OPERAND_TYPES", "OPERAND_DESCRIPTION", 
    "LowLevelOperandException", "LowLevelOperand"
    ]

#
# Operand types
#                  Description                          Data field
O_VOID      = 0 #  No Operand                           ----------
O_REG       = 1 #  General Register (al,ax,es,ds...)    reg
O_MEM       = 2 #  Direct Memory Reference  (DATA)      addr
O_PHRASE    = 3 #  Memory Ref [Base Reg + Index Reg]    phrase
O_DISPL     = 4 #  Memory Reg [Base Reg + Index Reg + Displacement] phrase+addr
O_IMM       = 5 #  Immediate Value                      value
O_FAR       = 6 #  Immediate Far Address  (CODE)        addr
O_NEAR      = 7 #  Immediate Near Address (CODE)        addr
O_SPEC0     = 8 #  Special register 1 (arch. specific)
O_SPEC1     = 9 #  Special register 2 (arch. specific)
O_SPEC2     = 10 #  Special register 3 (arch. specific)
O_SPEC3     = 11 #  Special register 4 (arch. specific)
O_SPEC4     = 12 #  Special register 5 (arch. specific)
O_SPEC5     = 13 #  Special register 6 (arch. specific)

OPERAND_TYPES = [
    O_VOID,
    O_REG,
    O_MEM,
    O_PHRASE,
    O_DISPL,
    O_IMM,
    O_FAR,
    O_NEAR,
    O_SPEC0,
    O_SPEC1,
    O_SPEC2,
    O_SPEC3,
    O_SPEC4,
    O_SPEC5,
    ]

OPERAND_DESCRIPTION = {
    O_VOID      : "No Operand", 
    O_REG       : "General Register",
    O_MEM       : "Direct Memory Reference  (DATA)",
    O_PHRASE    : "Memory Ref [Base Reg + Index Reg]",
    O_DISPL     : "Memory Reg [Base Reg + Index Reg + Displacement]",
    O_IMM       : "Immediate Value",
    O_FAR       : "Immediate Far Address  (CODE)",
    O_NEAR      : "Immediate Near Address (CODE)",
    O_SPEC0     : "Special register 0",
    O_SPEC1     : "Special register 1",
    O_SPEC2     : "Special register 2",
    O_SPEC3     : "Special register 3",
    O_SPEC4     : "Special register 4",
    O_SPEC5     : "Special register 5"
    }


class LowLevelOperandException(Exception):
    """Generic exceptino for the low-level operand IR."""
    pass


class LowLevelOperand(object):
    """Operand item optionally used by an instruction."""

    def __init__(self):
        """Initialize instance."""
        self.number = 0
        self.value = None
        self.type = O_VOID
        self.analyzed = False

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, _type):
        self._type = _type

    @property
    def number(self):
        """Return the operand number in the instruction."""
        return self._number

    @number.setter
    def number(self, number):
        """Store the operand number in the instruction."""
        self._number = number

    @property
    def is_void(self):
        return self.type is O_VOID

    @property
    def is_reg(self):
        return self.type is O_REG

    def is_reg_n(self, n=None):
        if self.type is O_REG:

            if n is not None:
                if self.value != n:
                    return False

            return True

        return False

    #@property
    #def is_reg(self):
    #    return self.type is O_REG

    @property
    def is_mem(self):
        return self.type is O_MEM

    @property
    def is_phrase(self):
        return self.type is O_PHRASE  

    @property
    def is_displ(self):
        return self.type is O_DISPL

    @property
    def is_imm(self):
        return self.type is O_IMM

    @property
    def is_far(self):
        return self.type is O_FAR

    @property
    def is_near(self):
        return self.type is O_NEAR

    @property
    def is_special(self):
        return self.type >= O_SPEC0

    @property
    def analyzed(self):
        return self._analyzed

    @analyzed.setter
    def analyzed(self, state):
        self._analyzed = bool(state)

    def __str__(self):
        if self.is_void: # or self.value is None:
            return ""

        elif self.is_displ or self.is_phrase:
            # TODO : Obtain correct or well-known operand representation.
            return "0x%X(r%d)" % (self.value[1], self.value[0])

        elif self.is_reg:
            # TODO : Obtain correct or well-known operand representation.
            return "r%d" % self.value

        elif self.is_near or self.is_far:
            # TODO : Determine address pointer size for the format.
            return "0x%08X" % self.value

        elif self.is_mem:
            # TODO: Use a name as reference instead of the address.
            return "0x%08X" % self.value

        elif self.is_imm:
            return "0x%08X" % self.value

        elif self.is_special:
            # TODO / FIXME : Determine the right representation.
            # Ask the debugger ?!?!?!
            return "SPRx"

        raise LowLevelOperandException("Unknown operand type : %r" % self.type)
