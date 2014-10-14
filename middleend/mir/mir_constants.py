# 
# Copyright (c) 2013 Sebastian Muniz
# 
# This code is part of point source decompiler
#

from middleend.mir_exception import MiddleIrException
from middleend.mir.mir_type import *
from middleend.mir.mir_llvm_instance import MiddleIrLLVMInstance

from llvm.core import *

#__all__ = ["MiddleIrConstantBool", "MiddleIrConstantInt",
#    "MiddleIrConstantArray"]


class MiddleIrBaseConstantException(MiddleIrException):
    """Middle IR constant exception class."""
    pass


class MiddleIrBaseConstant(MiddleIrLLVMInstance):
    """Middle IR constant expressions and values base class."""

    def __init__(self, _type):
        super(MiddleIrBaseConstant, self).__init__(_type)

        self.type = None
        self.name = None

    @property
    def type(self):
        """Return the type of the constant."""
        return self._type

    @type.setter
    def type(self, type):
        """Store the type of the constant."""
        self._type = type

    @property
    def name(self):
        """Return the name of the constant."""
        return self._name

    @name.setter
    def name(self, name):
        """Store the name of the constant."""
        self._name = name


class MiddleIrConstantInt(MiddleIrBaseConstant):
    """Middle level intermediate representation class of integer constant."""

    def __init__(self, const_type, value):
        """Initialize the instance."""
        super(MiddleIrConstantInt, self).__init__(
            Constant.int(const_type._ptr, value)
            )

        self.type = const_type


class MiddleIrConstantStringZ(MiddleIrBaseConstant):
    """Middle level intermediate representation class of null-terminated string
    constant.
    
    """

    def __init__(self, value):
        """Initialize the instance."""
        super(MiddleIrConstantStringZ, self).__init__(Constant.stringz(value))


class MiddleIrConstantNull(MiddleIrBaseConstant):
    """
    Middle level intermediate representation class of NULL constant.

    """

    def __init__(self, _type):
        """Initialize the instance."""
        super(MiddleIrConstantArray, self).__init__(Constant.null(_type._ptr))


class MiddleIrConstantArray(MiddleIrBaseConstant):
    """
    Middle level intermediate representation class of array constant.

    """

    def __init__(self, _type, size):
        """Initialize the instance."""
        super(MiddleIrConstantArray, self).__init__(Constant.array(_type._llvm_get_type(), size))

#class MiddleIrConstantFP(MiddleIrBaseConstant):
#    """
#    Middle level intermediate representation class of floating-point constant.
#
#    """
#
#    def __init__(self):
#        """Initialize the instance."""
#        super(MiddleIrConstantFP, self).__init__(Constant.FP())


