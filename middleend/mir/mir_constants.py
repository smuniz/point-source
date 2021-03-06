# 
# Copyright (c) 2016 Sebastian Muniz
# 
# This code is part of point source decompiler
#
from middleend.mir_exception import MiddleIrException
from middleend.mir.mir_type import *
from middleend.mir.mir_llvm_instance import MiddleIrLLVMInstance

from llvmlite import ir

#__all__ = ["MiddleIrConstantBool",
#            "MiddleIrConstantInt",
#            "MiddleIrConstantArray",
#    ]


class MiddleIrBaseConstantException(MiddleIrException):
    """Middle IR constant exception class."""
    pass


class MiddleIrBaseConstant(MiddleIrLLVMInstance):
    """Middle IR constant expressions and values base class."""

    def __init__(self, _type):
        super(MiddleIrBaseConstant, self).__init__(_type)

        self.type = None
        self.name = None
        self.value = None

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

    def get_readable_inners(self):
        """Return internal object representation in a readable fashion."""
        return self.value

class MiddleIrConstantInt(MiddleIrBaseConstant):
    """Middle level intermediate representation class of integer constant."""

    def __init__(self, const_type, value):
        """Initialize the instance."""
        super(MiddleIrConstantInt, self).__init__(
            ir.Constant(const_type._ptr, value)
            )

        self.value = value
        self.type = const_type

    def get_readable_inners(self):
        return self.value

# XXX Only StringZ exists.
#class MiddleIrConstantString(MiddleIrBaseConstant):
#    """Middle level intermediate representation class of non-null-terminated
#    string constant.
#    
#    """
#
#    def __init__(self, value):
#        """Initialize the instance."""
#        super(MiddleIrConstantString, self).__init__(ir.Constant(value))
#
#        self.value = repr(value).replace("'", "\"")

class MiddleIrConstantStringZ(MiddleIrBaseConstant):
    """Middle level intermediate representation class of null-terminated string
    constant.
    
    """

    def __init__(self, value):
        """Initialize the instance."""
        n = (len(value) + 2)
        buf = bytearray((' ' * n).encode('ascii'))
        buf[-1] = 0
        buf[:-1] = value.encode('utf-8')
        super(MiddleIrConstantStringZ, self).__init__(
            ir.Constant(ir.ArrayType(ir.IntType(8), n), value))

        self.value = repr(value).replace("'", "\"")


class MiddleIrConstantNull(MiddleIrBaseConstant):
    """Middle level intermediate representation class of NULL constant."""

    def __init__(self, _type):
        """Initialize the instance."""
        super(MiddleIrConstantNull, self).__init__(ir.Constant(_type._ptr, None))


class MiddleIrConstantAllOnes(MiddleIrBaseConstant):
    """Middle level intermediate representation class of all-ones constant."""

    def __init__(self, _type):
        """Initialize the instance."""
        if isinstance(_type._ptr, ir.IntType):
            super(MiddleIrConstantAllOnes, self).__init__(
                ir.Constant(_type._ptr, int('1' * _type._ptr.width, 2)))
                #ir.Constant.all_ones(_type._ptr, None))
        else:
            raise MiddleIrException(
                "Cannot create 'all ones' type from non-integer")


class MiddleIrConstantUndef(MiddleIrBaseConstant):
    """Middle level intermediate representation class of undefined constant."""

    def __init__(self, _type):
        """Initialize the instance."""
        super(MiddleIrConstantUndef, self).__init__(ir.Constant(_type._ptr, ir.Undefined))


class MiddleIrConstantIntSignExtend(MiddleIrBaseConstant):
    """Middle level intermediate representation class of an integer
    sig0extended value constant.

    """

    def __init__(self, _type, value):
        """Initialize the instance."""
        super(MiddleIrConstantIntSignExtend, self).__init__(
            ir.Constant(_type._ptr, value))


class MiddleIrConstantReal(MiddleIrBaseConstant):
    """Middle level intermediate representation class of real value
    constant.

    """

    def __init__(self, _type, value):
        """Initialize the instance."""
        super(MiddleIrConstantReal, self).__init__(
            ir.Constant(_type._ptr, value))


class MiddleIrConstantArray(MiddleIrBaseConstant):
    """Middle level intermediate representation class of array constant."""

    def __init__(self, _type, elements):
        """Initialize the instance."""
        super(MiddleIrConstantArray, self).__init__(
            ir.Constant(
                ir.ArrayType(_type._ptr, len(elements)), 
                [element._ptr for element in elements]))

class MiddleIrConstantStruct(MiddleIrBaseConstant):
    """Middle level intermediate representation class of a structure of
    constants.

    """

    def __init__(self, elements):
        """Initialize the instance."""
        super(MiddleIrConstantStruct, self).__init__(
            ir.Constant.literal_struct(
                [element._ptr for element in elements]))


#class MiddleIrConstantPackedStruct(MiddleIrBaseConstant):
#    """Middle level intermediate representation class of a packed-structure of
#    constants.
#
#    """
#
#    def __init__(self, elements):
#        """Initialize the instance."""
#        super(MiddleIrConstantPackedStruct,
#        self).__init__(ir.Constant.packed_struct(
#            [element._ptr for element in elements]))
#

#class MiddleIrConstantVector(MiddleIrBaseConstant):
#    """Middle level intermediate representation class of a vector of constants.
#
#    """
#
#    def __init__(self, elements):
#        """Initialize the instance."""
#        super(MiddleIrConstantVector, self).__init__(ir.Constant.vector(
#            [element._ptr for element in elements]))
#

#class MiddleIrConstantSizeof(MiddleIrBaseConstant):
#    """Middle level intermediate representation class of a sizeof() constant.
#    
#    """
#
#    def __init__(self, _type):
#        """Initialize the instance."""
#        super(MiddleIrConstantSizeof, self).__init__(ir.Constant.sizeof(
#            _type._ptr))
