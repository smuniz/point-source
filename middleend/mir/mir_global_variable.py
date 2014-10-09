# 
# Copyright (c) 2013 Sebastian Muniz
# 
# This code is part of point source decompiler
#

from traceback import print_stack

from middleend.mir_exception import MiddleIrException
from middleend.mir.mir_llvm_instance import MiddleIrLLVMInstance
from area import Area

from llvm.core import *


class MiddleIrGlobalValueException(MiddleIrException):
    """Middle IR global value exception."""
    pass


class MiddleIrGlobalValue(MiddleIrLLVMInstance, Area):
    """Middle IR representation of a module-scope alias, variables and
    functions. Global variables are represented by the sub-class
    MiddleIrGlobalValue and functions by MiddleIrFunction.
    
    """
    pass


class MiddleIrGlobalVariableException(MiddleIrGlobalValueException):
    """Middle IR global variable exception."""
    pass


class MiddleIrGlobalVariable(MiddleIrGlobalValue):
    """Middle IR representation of a global variable (scope is module width).
    
    """

    def __init__(self, ty, value, name):
        """Initialize the instance."""
        MiddleIrLLVMInstance.__init__(self)#, ty._ptr)
        Area.__init__(self)


        self.type = ty
        self.value = value
        self.name = name

    @property
    def type(self):
        """Return the type of the variable."""
        return self._type

    @type.setter
    def type(self, type):
        """Store the type of the variable."""
        self._type = type

    @property
    def value(self):
        """Return the value of the variable."""
        return self._value

    @value.setter
    def value(self, value):
        """Store the value of the variable."""
        self._value = value

    @property
    def name(self):
        """Return the name of the variable."""
        return self._name

    @name.setter
    def name(self, name):
        """Store the name of the variable."""
        self._name = name
