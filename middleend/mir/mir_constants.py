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


class MiddleIrConstantString(MiddleIrBaseConstant):
    """Middle level intermediate representation class of non-null-terminated
    string constant.
    
    """

    def __init__(self, value):
        """Initialize the instance."""
        super(MiddleIrConstantString, self).__init__(Constant.string(value))


class MiddleIrConstantStringZ(MiddleIrBaseConstant):
    """Middle level intermediate representation class of null-terminated string
    constant.
    
    """

    def __init__(self, value):
        """Initialize the instance."""
        super(MiddleIrConstantStringZ, self).__init__(Constant.stringz(value))


class MiddleIrConstantNull(MiddleIrBaseConstant):
    """Middle level intermediate representation class of NULL constant."""

    def __init__(self, _type):
        """Initialize the instance."""
        super(MiddleIrConstantNull, self).__init__(Constant.null(_type._ptr))


class MiddleIrConstantAllOnes(MiddleIrBaseConstant):
    """Middle level intermediate representation class of all-ones constant."""

    def __init__(self, _type):
        """Initialize the instance."""
        super(MiddleIrConstantAllOnes, self).__init__(
            Constant.all_ones(_type._ptr))


class MiddleIrConstantUndef(MiddleIrBaseConstant):
    """Middle level intermediate representation class of undefined constant."""

    def __init__(self, _type):
        """Initialize the instance."""
        super(MiddleIrConstantUndef, self).__init__(Constant.undef(_type._ptr))


class MiddleIrConstantIntSignExtend(MiddleIrBaseConstant):
    """Middle level intermediate representation class of an integer
    sig0extended value constant.

    """

    def __init__(self, _type, value):
        """Initialize the instance."""
        super(MiddleIrConstantIntSignExtend, self).__init__(
            Constant.int_signextend(_type._ptr, value))


class MiddleIrConstantReal(MiddleIrBaseConstant):
    """Middle level intermediate representation class of real value
    constant.

    """

    def __init__(self, _type, value):
        """Initialize the instance."""
        super(MiddleIrConstantReal, self).__init__(
            Constant.real(_type._ptr, value))


class MiddleIrConstantArray(MiddleIrBaseConstant):
    """Middle level intermediate representation class of array constant."""

    def __init__(self, _type, elements):
        """Initialize the instance."""
        super(MiddleIrConstantArray, self).__init__(
            Constant.array(
                _type._ptr,
                [element._ptr for element in elements]))

class MiddleIrConstantStruct(MiddleIrBaseConstant):
    """Middle level intermediate representation class of a structure of
    constants.

    """

    def __init__(self, elements):
        """Initialize the instance."""
        super(MiddleIrConstantStruct, self).__init__(Constant.struct(
            [element._ptr for element in elements]))


class MiddleIrConstantPackedStruct(MiddleIrBaseConstant):
    """Middle level intermediate representation class of a packed-structure of
    constants.

    """

    def __init__(self, elements):
        """Initialize the instance."""
        super(MiddleIrConstantPackedStruct,
        self).__init__(Constant.packed_struct(
            [element._ptr for element in elements]))


class MiddleIrConstantVector(MiddleIrBaseConstant):
    """Middle level intermediate representation class of a vector of constants.

    """

    def __init__(self, elements):
        """Initialize the instance."""
        super(MiddleIrConstantVector, self).__init__(Constant.vector(
            [element._ptr for element in elements]))


class MiddleIrConstantSizeof(MiddleIrBaseConstant):
    """Middle level intermediate representation class of a sizeof() constant.
    
    """

    def __init__(self, _type):
        """Initialize the instance."""
        super(MiddleIrConstantSizeof, self).__init__(Constant.sizeof(
            _type._ptr))
