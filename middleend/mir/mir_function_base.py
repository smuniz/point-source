# 
# Copyright (c) 2013 Sebastian Muniz
# 
# This code is part of point source decompiler
#

from middleend.mir_exception import MiddleIrException
from middleend.mir.mir_llvm_instance import MiddleIrLLVMInstance
from area import Area

__all__ = ["MiddleIrFunctionBase", "MiddleIrFunctionBaseException"]


class MiddleIrFunctionBaseException(MiddleIrException):
    """Middle IR function base exception."""
    pass


class MiddleIrFunctionBase(MiddleIrLLVMInstance, Area):
    """Middle level intermediate representation class of functions being
    decompiled.

    """

    def __init__(self):
        """Initialize the intermediate level IR module class."""
        super(MiddleIrFunctionBase, self).__init__()

