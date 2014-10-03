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
    pass
    #def __init__(self, mir_type, value):
    #    super(MiddleIrBaseConstant, self).__init__(self, mir_type, value)


#class MiddleIrConstantFP(MiddleIrBaseConstant):
#    """
#    Middle level intermediate representation class of floating-point constant.
#
#    """
#
#    def __init__(self):
#        """Initialize the instance."""
#        super(MiddleIrConstantFP, self).__init__(Constant.FP())


class MiddleIrConstantInt32(MiddleIrBaseConstant):
    """Middle level intermediate representation class of integer constant."""

    def __init__(self, value):
        """Initialize the instance."""
        # TODO / FIXME : check this.
        int_type = MiddleIrTypeInt(32)._ptr

        super(MiddleIrConstantInt32, self).__init__(
            Constant.int(int_type, value))
            #Constant.int(Type.int(32), value))


class MiddleIrConstantStringZ(MiddleIrBaseConstant):
    """Middle level intermediate representation class of null-terminated string
    constant.
    
    """

    def __init__(self, value):
        """Initialize the instance."""
        super(MiddleIrConstantStringZ, self).__init__(Constant.stringz(value))


#class MiddleIrConstantArray(MiddleIrBaseConstant):
#    """
#    Middle level intermediate representation class of array constant.
#
#    """
#
#    def __init__(self, _type, size):
#        """Initialize the instance."""
#        super(MiddleIrConstantArray, self).__init__(Constant.array(_type._llvm_get_type(), size))

