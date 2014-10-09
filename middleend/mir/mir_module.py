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
        self.mir_functions = list()

        # Create an empty LLVM IR module.
        self._ptr = Module.new(module_name)

    def create_intrinsic_function(self, name):
        """Add the specified intrinsic function to the current module."""
        return MiddleIrIntrinsicFunction(name, self)

    def create_function(self, name):
        """Add the specified function to the current module."""
        mir_function = MiddleIrFunction(name, self)

        self.mir_functions.append(mir_function)

        return mir_function

    def add_global_variable(self, global_variable, name):
        """Add the specified global variable to the current module."""
        #ty = global_variable._ptr.type
        ty = global_variable.type._ptr
        #name = global_variable.name
        address_space = 0

        global_variable._ptr = self._ptr.add_global_variable(
            ty,
            name,
            address_space)

        #global_variable._ptr.initializer = global_variable.value._ptr

    def add_function(self, mir_function):
        """Add the specified function to the current module."""
        mir_function.module = self._ptr

        # Add only if it doesn't exist yet.
        if mir_function not in self.mir_functions:
            self.mir_functions.append(mir_function)

        fty = mir_function._llvm_get_type()._ptr
        name = mir_function.name

        llvm_func_def = self._ptr.add_function(fty, name)

        mir_function._llvm_set_definition(llvm_func_def)

    def __repr__(self):
        """Return a string object with the module representation."""
        return repr(self._ptr)

    def __str__(self):
        """Return a string object with the module text representation."""
        return str(self._ptr)

    def set_target(self, target):
        """Store the target architecture."""
        self.target = target

    def get_target(self):
        """Return the target architecture."""
        return self.target

    def verify(self):
        """Verify the module checking for errors."""
        try:
            if self.ALLOW_MIR_VERIFY:
                self._ptr.verify()
        except LLVMException, err:
            raise MiddleIrModuleException(err)

    def get_function_by_address(self, address):
        """Return the function at the specified address."""
        for mir_function in self.mir_functions:
            if mir_function.get_start_address() == address:
                return mir_function

        raise MiddleIrModuleException(
            "No function with start address 0x%X" % address)

    def get_function(self, index):
        """Return the function at the specified position in the functions list.
        
        """
        if index <= len(self.mir_functions):
            return self.mir_functions[index]

        raise MiddleIrModuleException(
            "Function index %d is out of scope." % index)

    def __getitem__(self, key):
        """..."""
        if isinstance(key, slice):
            indices = key.indices(len(self))
            return [self[i] for i in xrange(*indices)]

        elif isinstance(key, int) or isinstance(key, long):
            try:
                return self.get_function(key)
            except MiddleIrModuleException, err:
                raise IndexError

        else:
            raise TypeError

