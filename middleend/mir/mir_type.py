# 
# Copyright (c) 2014 Sebastian Muniz
# 
# This code is part of point source decompiler
#
from middleend.mir.mir_llvm_instance import MiddleIrLLVMInstance

from llvm.core import Type

__all__ = [ "MiddleIrTypeChar",
            "MiddleIrTypeInt",
            "MiddleIrTypeFloat",
            "MiddleIrTypeDouble",
            "MiddleIrTypeX86Fp80",
            "MiddleIrTypePpcFp128",
            "MiddleIrTypeFp128",
            "MiddleIrTypeFunction",
            "MiddleIrTypeOpaque",
            "MiddleIrTypeStruct",
            "MiddleIrTypePackedStruct",
            "MiddleIrTypeArray",
            "MiddleIrTypePointer",
            "MiddleIrTypeVector",
            "MiddleIrTypeLabel",
            "MiddleIrTypeVoid",
            ]


class MiddleIrBaseType(MiddleIrLLVMInstance):
    """Middle IR basic operations on data types."""
    
    def __init__(self, llvm_type):
        """Initialize the instance."""
        super(MiddleIrBaseType, self).__init__(llvm_type)
        self.type = None

    @property
    def type(self):
        """Return the internal type."""
        return self._type

    @type.setter
    def type(self, _type):
        """Store the internal type."""
        self._type = _type


class MiddleIrTypeChar(MiddleIrBaseType):
    """Middle level intermediate representation class of char type."""

    def __init__(self):
        """Initialize the instance."""
        super(MiddleIrTypeChar, self).__init__(Type.int(8))


class MiddleIrTypeInt(MiddleIrBaseType):
    """Middle level intermediate representation class of integer type."""

    def __init__(self, bits=32):
        """Initialize the instance."""
        super(MiddleIrTypeInt, self).__init__(Type.int(bits))

    @property
    def width(self):
        return self._ptr.width


class MiddleIrTypeFloat(MiddleIrBaseType):
    """Middle level intermediate representation class of 32-bit floating point
    type.

    """

    def __init__(self):
        """Initialize the instance."""
        super(MiddleIrTypeFloat, self).__init__(Type.float())


class MiddleIrTypeDouble(MiddleIrBaseType):
    """Middle level intermediate representation class of 64-bit double type."""

    def __init__(self):
        """Initialize the instance."""
        super(MiddleIrTypeDouble, self).__init__(Type.double())


class MiddleIrTypeX86Fp80(MiddleIrBaseType):
    """Middle level intermediate representation class of 80-bit x86 floating
    point type.
    
    """

    def __init__(self):
        """Initialize the instance."""
        super(MiddleIrTypeX86Fp80, self).__init__(Type.x86_fp80())


class MiddleIrTypeFp128(MiddleIrBaseType):
    """Middle level intermediate representation class of 128-bit floating
    point type (112-bit mantissa).
    
    """

    def __init__(self):
        """Initialize the instance."""
        super(MiddleIrTypeFp128, self).__init__(Type.fp128())


class MiddleIrTypePpcFp128(MiddleIrBaseType):
    """Middle level intermediate representation class of 128-bit floating
    point type (two 64-bits).
    
    """

    def __init__(self):
        """Initialize the instance."""
        super(MiddleIrTypePpcFp128, self).__init__(Type.ppc_fp128())


class MiddleIrTypeFunction(MiddleIrBaseType):
    """Middle level intermediate representation class of function type."""

    def __init__(self, return_type, parameters, variadic_arguments=False):
        """Initialize the instance."""
        self.return_type = return_type
        self.parameters = parameters

        super(MiddleIrTypeFunction, self).__init__(
            Type.function(
                return_type._ptr,
                [param._ptr for param in parameters],
                variadic_arguments
                )
            )


class MiddleIrTypeOpaque(MiddleIrBaseType):
    """Middle level intermediate representation class of opaque struct type."""

    def __init__(self, name):
        """Initialize the instance."""
        super(MiddleIrTypeOpaque, self).__init__(Type.opaque(name))

    def set_body(self, body):
        """Store opaque type body definition."""
        self._ptr.set_body([body_element._ptr for body_element in body])

        self.type = list(body)

class MiddleIrTypeStruct(MiddleIrBaseType):
    """Middle level intermediate representation class of unpacked struct type.
    
    """

    def __init__(self, elements, name=''):
        """Initialize the instance."""
        element_types = [element._ptr for element in elements]
        super(MiddleIrTypeStruct, self).__init__(
            Type.struct(element_types, name))

        self.type = list(elements)


class MiddleIrTypePackedStruct(MiddleIrBaseType):
    """Middle level intermediate representation class of packed struct type."""

    def __init__(self, elements, name=''):
        """Initialize the instance."""
        super(MiddleIrTypePackedStruct, self).__init__(
            Type.packed_struct(
                [element._ptr for element in elements],
                name
                )
            )
        self.type = list(elements)


class MiddleIrTypeArray(MiddleIrBaseType):
    """Middle level intermediate representation class of array type."""

    def __init__(self, _type, size):
        """Initialize the instance."""
        super(MiddleIrTypeArray, self).__init__(
            Type.array(_type._ptr, size))

        self.type = _type


class MiddleIrTypePointer(MiddleIrBaseType):
    """Middle level intermediate representation class of pointer type."""

    def __init__(self, pointee_type, addr_space=0):
        """Initialize the instance."""
        # TODO : Validate parameter and raise exception.
        #if self.pointee is None:
            #raise MiddleIr
        self.type = pointee_type
        super(MiddleIrTypePointer, self).__init__(
            Type.pointer(pointee._ptr, addr_space))


class MiddleIrTypeVector(MiddleIrBaseType):
    """Middle level intermediate representation class of vector type."""

    def __init__(self, element_ty, count):
        """Initialize the instance."""
        element_type = element_ty._ptr
        super(MiddleIrTypeVector, self).__init__(Type.vector(element_type, count))


class MiddleIrTypeLabel(MiddleIrBaseType):
    """Middle level intermediate representation class of label type."""

    def __init__(self):
        """Initialize the instance."""
        super(MiddleIrTypeLabel, self).__init__(Type.label())


class MiddleIrTypeVoid(MiddleIrBaseType):
    """Middle level intermediate representation class of void type."""

    def __init__(self):
        """Initialize the instance."""
        super(MiddleIrTypeVoid, self).__init__(Type.void())
