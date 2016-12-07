# 
# Copyright (c) 2014 Sebastian Muniz
# 
# This code is part of point source decompiler
#

from traceback import print_stack

from middleend.mir_exception import MiddleIrException
from middleend.mir.mir_llvm_instance import MiddleIrLLVMInstance
from area import Area

from llvmlite import *


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

    def __init__(self, ty, name):
        """Initialize the instance."""
        super(MiddleIrGlobalVariable, self).__init__()
        Area.__init__(self)

        self.type = ty
        #self.value = None
        self.name = name
        self.module = None

    @property
    def type(self):
        """Return the type of the variable."""
        return self._type

    @type.setter
    def type(self, type):
        """Store the type of the variable."""
        self._type = type

    #@property
    #def value(self):
    #    """Return the value of the variable."""
    #    return self._value

    #@value.setter
    #def value(self, value):
    #    """Store the value of the variable."""
    #    self._value = value

    @property
    def name(self):
        """Return the name of the variable."""
        return self._name

    @name.setter
    def name(self, name):
        """Store the name of the variable."""
        self._name = name

    @staticmethod
    def create_if_needed(module, _type, name):
        """Create a new global variable if it doesn't exists yet. Otherwise
        return the existing one.
        
        """
        try:
            gvar = MiddleIrGlobalVariable.get(module, name)
        except MiddleIrGlobalVariableException, err:
            gvar = MiddleIrGlobalVariable.new(module, _type, name)
        return gvar

    @staticmethod
    def new(module, _type, name):
        """Create a new global vairable."""
        new_gvar = MiddleIrGlobalVariable(_type, name)
        module.add_global_variable(new_gvar)
        return new_gvar

    @property
    def module(self):
        """Return the module of the variable."""
        return self._module

    @module.setter
    def module(self, module):
        """Store the module of the variable."""
        self._module = module

    # TODO Confirm it does not exists in LVMLite
    #@property
    #def is_declaration(self):
    #    return self._ptr.is_declaration

    @property
    def alignment(self):
        """Return the alignment property of a global variable."""
        return self._ptr.alignment

    @alignment.setter
    def alignment(self, value):
        """Store the alignment property of a global variable."""
        self._ptr.alignment = value

    @staticmethod
    def get(module, name):
        """Return an existing global variable based on its name."""
        #gv = module._ptr.globals.get(name, None)
        gv = module.get_global_variable_by_name(name)
        if not gv:
            raise MiddleIrGlobalVariableException("No global named '%s'" % name)
        return gv

    def delete(self):
        """Remove an existing global variable based on its name."""
        if self in self.module.global_variables:
            self.module.global_variables.discard(self)

        if self._ptr:
            self._ptr.delete()

    @property
    def initializer(self):
        """Return the global variable initializer."""
        return self._initializer

    @initializer.setter
    def initializer(self, initializer):
        """Store the global variable initializer."""
        self._initializer = initializer
        self._ptr.initializer = initializer._ptr

    def get_readable_inners(self):
        """..."""
        return self.initializer.get_readable_inners()
