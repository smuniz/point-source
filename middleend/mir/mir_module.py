#
# Copyright (c) 2013 Sebastian Muniz
#
# This code is part of point source decompiler
#

import middleend.mir.mir_llvm_instance
reload(middleend.mir.mir_llvm_instance)
from middleend.mir.mir_llvm_instance import MiddleIrLLVMInstance

from middleend.mir.area import Area

from middleend.mir_exception import MiddleIrException
from middleend.mir.mir_function import MiddleIrFunction

from llvm import *
from llvm.core import *


class MiddleIrModuleException(MiddleIrException):
    """Middle IR module exception."""
    pass


class MiddleIrModule(MiddleIrLLVMInstance, Area):
    """Middle level intermediate representation class of application being
    decompiled.

    This class main purpose is to provide a simple abstraction layer over the
    LLVM IR module object.

    """

    ALLOW_MIR_VERIFY = False

    def __init__(self, module_name):
        """Initialize the intermediate level IR module class."""
        super(MiddleIrModule, self).__init__()

        # Display debugging information during development phase.
        self.debug = True

        # Store the list of all the MIR functions in this module.
        self.functions = set()

        # Create an empty LLVM IR module.
        self._ptr = Module.new(module_name)

        self.target = None

        self.global_variables = set()

    def create_intrinsic_function(self, name):
        """Add the specified intrinsic function to the current module."""
        return MiddleIrIntrinsicFunction(name, self)

    def create_function(self, name):
        """Add the specified function to the current module."""
        mir_function = MiddleIrFunction(name, self)

        self.functions.add(mir_function)

        return mir_function

    def add_global_variable(self, global_variable): #, name):
        """Add the specified global variable to the current module."""
        ty = global_variable.type._ptr
        name = global_variable.name
        address_space = 0

        global_variable._ptr = self._ptr.add_global_variable(
            ty,
            name,
            address_space)

        global_variable.module = self

        self.global_variables.add(global_variable)

    def get_global_variable_named(self, name):
        """Iterate through every global variable and return the one matching
        the specified name.
        
        """
        for gvar in self.global_variables:
            if gvar.name is name:
                return gvar
        return None

    def get_function_named(self, name):
        """Iterate through every function and return the one matching the
        specified name.
        
        """
        for mir_function in self.functions:
            if mir_function.name is name:
                return mir_function
        return None

    def add_function(self, mir_function):
        """Add the specified function to the current module."""
        # Add only if it doesn't exist yet.
        if mir_function not in self.functions:
            self.functions.add(mir_function)

        mir_function.module = self

        fty = mir_function._llvm_type._ptr
        name = mir_function.name

        llvm_func_def = self._ptr.add_function(fty, name)

        mir_function._llvm_definition = llvm_func_def

    def __repr__(self):
        """Return a string object with the module representation."""
        return repr(self._ptr)

    def __str__(self):
        """Return a string object with the module text representation."""
        return str(self._ptr)

    @property
    def global_variables(self):
        """Return the global variables architecture."""
        return self._global_variables

    @global_variables.setter
    def global_variables(self, global_variables):
        """Store the global variables architecture."""
        self._global_variables = global_variables

    @property
    def target(self):
        """Return the target architecture."""
        return self._target

    @target.setter
    def target(self, target):
        """Store the target architecture."""
        self._target = target

    def verify(self):
        """Verify the module checking for errors."""
        try:
            if self.ALLOW_MIR_VERIFY:
                self._ptr.verify()
        except LLVMException, err:
            raise MiddleIrModuleException(err)

    def get_function_by_address(self, address):
        """Return the function at the specified address."""
        for mir_function in self.functions:
            if mir_function.get_start_address() == address:
                return mir_function

        raise MiddleIrModuleException(
            "No function with start address 0x%X" % address)

    def get_indexed_function(self, index):
        """Return the function at the specified position in the functions list.
        
        """
        if index < len(self.functions):
            return list(self.functions)[index]

        raise MiddleIrModuleException(
            "Function index %d is out of scope." % index)

    def __getitem__(self, key):
        """..."""
        if isinstance(key, slice):
            indices = key.indices(len(self))
            return [self[i] for i in xrange(*indices)]

        elif isinstance(key, int) or isinstance(key, long):
            try:
                return self.get_indexed_functions(key)
            except MiddleIrModuleException, err:
                raise IndexError

        else:
            raise TypeError

    #def to_bitcode(self, ss):
    #    """Write LLVM bitcode representing the specified object."""
    #    self._ptr.to_bitcode(ss)

    #def from_bitcode(self, ss):
    #    """Write LLVM bitcode representing the specified object."""
    #    self._ptr.from_bitcode(ss)

    @staticmethod
    def new(module_name):
        """Create a new module."""
        return MiddleIrModule(module_name)
