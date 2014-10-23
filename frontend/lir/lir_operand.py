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

SPR_TYPES = [
    O_SPEC0,
    O_SPEC1,
    O_SPEC2,
    O_SPEC3,
    O_SPEC4,
    O_SPEC5,
    ]

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
    O_SPEC0     : "Special operand 0",
    O_SPEC1     : "Special operand 1",
    O_SPEC2     : "Special operand 2",
    O_SPEC3     : "Special operand 3",
    O_SPEC4     : "Special operand 4",
    O_SPEC5     : "Special operand 5"
    }


class LowLevelOperandException(Exception):
    """Generic exceptino for the low-level operand IR."""
    pass


class LowLevelOperand(object):
    """Operand item optionally used by an instruction."""

    def __init__(self, gpr_names=None, spr_names=None):
        """Initialize instance."""
        self.number = 0
        self.value = None
        self.type = O_VOID
        self.analyzed = False
        self.gpr_names = gpr_names
        self.spr_names = spr_names

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
        return self.type in SPR_TYPES

    @property
    def analyzed(self):
        return self._analyzed

    @analyzed.setter
    def analyzed(self, state):
        self._analyzed = bool(state)

    @property
    def reg_name(self):
        """Retur nthe name of the register represented by the operand (if
        any).

        """
        if self.is_reg:
            return self.gpr_names.get(self.value, None)
        elif self.is_displ:
            return self.gpr_names.get(self.value[1], None)
        elif self.is_special:
            return self.spr_names.get(self.type, None)
        else:
            return None

    def __str__(self):
        if self.is_void: # or self.value is None:
            return ""

        elif self.is_displ or self.is_phrase:
            return "0x%X(%s)" % (self.value[1], self.reg_name)

        elif self.is_reg:
            return "%s" % self.reg_name

        elif self.is_near or self.is_far:
            return "0x%08X" % self.value

        elif self.is_mem:
            return "0x%08X" % self.value

        elif self.is_imm:
            return "0x%08X" % self.value

        elif self.is_special:
            return "%s" % self.reg_name

        raise LowLevelOperandException("Unknown operand type : %r" % self.type)
