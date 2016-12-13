#
# Copyright (c) 2017 Sebastian Muniz
#
# This code is part of point source decompiler
#


from middleend.mir.area import Area

from middleend.mir_exception import MiddleIrException

import middleend.mir.mir_llvm_instance
reload(middleend.mir.mir_llvm_instance)
from middleend.mir.mir_llvm_instance import MiddleIrLLVMInstance

from llvmlite import ir

#
# Keep track of modules created during a session so if the user specifies a new
# module based on a previously analyzed filename then we'll return the existing
# one and avoid recreation of a new module and possible collisions.
#
modules_cache = dict()


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

    def __init__(self, name):
        """Initialize the intermediate level IR module class."""
        # Create an empty LLVM IR module.
        super(MiddleIrModule, self).__init__(ir.Module(name))

        # Display debugging information during development phase.
        self.debug = True

        # Store the list of all the MIR functions in this module.
        self.functions = set()

        self.target = None

        self.global_variables = dict()

        # Update the modules cache to keep it updated.
        global modules_cache
        if name in modules_cache:
            raise MiddleIrModuleException(
                "Error creating new module instance named '%s' because it "
                "already exists." % name)

    @property
    def name(self):
        """Return the current module name."""
        return self._ptr.id

    @name.setter
    def name(self, name):
        """Store the current module name."""
        old_name = self.name
        self._ptr.id = name

        # Update the modules cache to keep it updated.
        global modules_cache
        if name in modules_cache:
            del modules_cache[name]
        modules_cache.set(name, self)

    def create_intrinsic_function(self, name):
        """Add the specified intrinsic function to the current module."""
        #return MiddleIrIntrinsicFunction(name, self)
        raise MiddleIrModuleException("Should validate this is working")

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

        global_variable._ptr = ir.GlobalVariable(
            self._ptr,
            ty,
            name,
            address_space)
        #global_variable._ptr = self._ptr.add_global_variable(
        #    ty,
        #    name,
        #    address_space)

        global_variable.module = self

        # Add the newly created global variable to the list of existing ones.
        self.global_variables[global_variable.name] = global_variable

    def get_global_variable_by_name(self, name):
        """Iterate through every global variable and return the one matching
        the specified name.
        
        """
        return self.global_variables.get(name, None)

    def get_function_by_name(self, name):
        """Iterate through every function and return the one matching the
        specified name.
        
        """
        for mir_function in self.functions:
            if mir_function.name == name:
                return mir_function
        return None

    def add_function(self, mir_function):
        """Add the specified function to the current module."""
        # Add only if it doesn't exist yet.
        try:
            if mir_function not in self.functions:
                self.functions.add(mir_function)

            mir_function.module = self

            fty = mir_function._llvm_type._ptr
            name = mir_function.name

            #llvm_func_def = self._ptr.add_function(fty, name)
            llvm_func_def = ir.Function(self._ptr, fty, name)

            mir_function._llvm_definition = llvm_func_def
        except Exception, err:
            raise MiddleIrModuleException(err)

    def remove_function(self, mir_function):
        """Remove the specified middle end function."""
        if mir_function in self.functions:
            self.functions.remove(mir_function)

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
        except Exception, err:
            raise MiddleIrModuleException(err)

    #def get_function_by_address(self, address):
    #    """Iterate through every function and return the one matching the
    #    specified address.
    #    
    #    """
    #    for mir_function in self.functions:
    #        if address in mir_function.prologue_addresses:
    #            return mir_function
    #    return None

    def get_function_by_address(self, address):
        """Return the function at the specified address."""
        for mir_function in self.functions:
            if mir_function.start_address == address:
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
                return self.get_indexed_function(key)
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
    def new(name):
        """Create a new module."""
        global modules_cache
        res = modules_cache.get(name, None)
        if res is None:
            return MiddleIrModule(name)
        else:
            return res
