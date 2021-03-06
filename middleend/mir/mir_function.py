# 
# Copyright (c) 2017 Sebastian Muniz
# 
# This code is part of point source decompiler
#
from traceback import print_stack

from llvmlite.ir import *

#from middleend.mir_exception import MiddleIrException
from mir_function_base import MiddleIrFunctionBase, \
                                MiddleIrFunctionBaseException
from mir_type import *

from middleend.mir.mir_llvm_instance import MiddleIrLLVMInstance
from middleend.mir.mir_module import MiddleIrModule

#
# LLVM calling conventions converted to our equivalents.
#
#from idaapi import *
#CALL_CONV_C             = CM_CC_C
#CALL_CONV_FASTCALL      = CM_CC_FASTCALL
#CALL_CONV_COLDCALL      = CM_CC_COLDCALL
#CALL_CONV_X86_STDCALL   = CM_CC_X86_STDCALL
#CALL_CONV_X86_FASTCALL  = CM_CC_X86_FASTCALL
#CALL_CONV_GHC           = CM_CC_GHC
#CALL_CONV_ARM_APCS      = CM_CC_ARM_APCS
#CALL_CONV_ARM_AAPCS     = CM_CC_ARM_AAPCS
#CALL_CONV_ARM_AAPCS_VFP = CM_CC_ARM_AAPCS_VFP
#CALL_CONV_MSP430_INTR   = CM_CC_MSP430_INTR
#CALL_CONV_X86_THISCALL  = CM_CC_X86_THISCALL
#CALL_CONV_PTX_KERNEL    = CM_CC_PTX_KERNEL
#CALL_CONV_PTX_DEVICE    = CM_CC_PTX_DEVICE
#CALL_CONV_MBLAZE_INTR   = CM_CC_MBLAZE_INTR
#CALL_CONV_MBLAZE_SVOL   = CM_CC_MBLAZE_SVOL

#CALLING_CONVENTIONS = {
#     #CALL_CONV_C             : "C",
#     CALL_CONV_FASTCALL      : "Fastcall",
#     #CALL_CONV_COLDCALL      : "Coldcall",
#     #CALL_CONV_X86_STDCALL   : "x86 stdcall",
#     #CALL_CONV_X86_FASTCALL  : "x86 fastcall",
#     #CALL_CONV_GHC           : "GHC",
#     #CALL_CONV_ARM_APCS      : "ARM Procedure Calling Standard",
#     #CALL_CONV_ARM_AAPCS     : "ARM Architecture Procedure Calling Standard",
#     #CALL_CONV_ARM_AAPCS_VFP : "ARM Architecture Procedure Calling Standard - hard floating point ABI",
#     #CALL_CONV_MSP430_INTR   : "MSP430 interrupt routines",
#     #CALL_CONV_X86_THISCALL  : "x86 thiscall",
#     #CALL_CONV_PTX_KERNEL    : "PTX kernel",
#     #CALL_CONV_PTX_DEVICE    : "PTX device",
#     #CALL_CONV_MBLAZE_INTR   : "MBlaze ???",
#     #CALL_CONV_MBLAZE_SVOL   : "MBlaze ???",
#    }
#

class MiddleIrFunctionException(MiddleIrFunctionBaseException):
    """Middle IR function exception."""
    pass


#class MiddleIrIntrinsicFunction(MiddleIrFunction):
#    def __init__(self, name, mir_module):
#        MiddleIrFunction.__init__(name, mir_module)
class MiddleIrValue(MiddleIrLLVMInstance):

    def __init__(self, _type):
        super(MiddleIrValue, self).__init__(_type)
        self.type = _type
        self.name = ""

    @property
    def name(self):
        """Return the name of the value."""
        return self._ptr.name

    @name.setter
    def name(self, name):
        """Store the name of the value."""
        self._ptr.name = name

    @property
    def type(self):
        """Return the Type object representing the type of the value."""
        return self._type

    @type.setter
    def type(self, _type):
        """Store the Type object representing the type of the value."""
        self._type = _type


class MiddleIrArgument(MiddleIrValue):

    def __init__(self, _type):
        super(MiddleIrArgument, self).__init__(_type)

    def get_readable_inners(self):
        """..."""
        return self.name

class MiddleIrFunction(MiddleIrFunctionBase):
    """Middle level intermediate representation class of functions being
    decompiled.

    This class main objetive is to provide a simple abstration layer over the
    LLVM IR function object.

    """

    def __init__(self, name, return_type=MiddleIrTypeVoid(),
        arguments_types=[], variadic_arguments=False):
        """Initialize the intermediate level IR module class."""
        super(MiddleIrFunction, self).__init__()

        # Initialize the function name.
        self.name = name

        # Epilogue and prologue instruction addresses inside the current
        # function.
        self.prologue_addresses = set()
        self.epilogue_addresses = set()

        #
        # Initialize the LLVM function declaration object and initially set the
        # function arguments and return declaration to void. 
        #
        self.return_type = return_type
        self.arguments_types = arguments_types
        self.arguments = [] # These will be set when the function is
                            # committed.
        self.variadic_arguments = variadic_arguments    # No variadic args by
                                                        # default. Let the user
                                                        # set them. 
        self._llvm_type = None

        # Keep track of every basic block contained in this function.
        self._basic_blocks = set()

        # Store the Middle-end module instance.
        self.module = None

        # Set the default calling convention.
        # FIXME 
        self.calling_convention = "fastcc"#CALL_CONV_FASTCALL

        self._llvm_definition = None

    @property
    def variadic_arguments(self):
        """Indicate if the current function has variadic arguments or not."""
        return self._variadic_arguments

    @variadic_arguments.setter
    def variadic_arguments(self, variadic_arguments):
        """Indicate if the current function has variadic arguments or not."""
        self._variadic_arguments = bool(variadic_arguments)

    def add_basic_block(self, mir_basic_block):
        """Add a new basic block to the function."""
        # Keep updated our internal list
        self._basic_blocks.add(mir_basic_block)

        mir_basic_block._llvm_function = self._llvm_definition

    def get_indexed_basic_block(self, index):
        """Return the basic block at the specified position in the basic blocks
        list.

        """
        if index < len(self.basic_blocks):
            return list(self.basic_blocks)[index]

        raise MiddleIrFunctionException(
            "Basic block index %d is out of scope." % index)

    @property
    def basic_block_count(self):
        """Return the count of basic blocks present in the current function."""
        return len(self._basic_blocks)

    @property
    def basic_blocks(self):
        """Return the list of basic blocks present in the current function."""
        return self._basic_blocks

    @basic_blocks.setter
    def basic_blocks(self, basic_blocks):
        """Store the list of basic blocks present in the current function."""
        self._basic_blocks = basic_blocks

    def __getitem__(self, key):
        if isinstance(key, slice):
            indices = key.indices(len(self))
            return [self[i] for i in xrange(*indices)]
        elif isinstance(key, int) or isinstance(key, long):
            try:
                # TODO / FIXME
                return list(self.basic_blocks)[key]
            except KeyError:
                raise IndexError
        else:
            raise TypeError

    def __len__(self):
        return len(self._basic_blocks)

    @property
    def return_type(self):
        """Return the value type returned by the function to it's caller when
        itfinishes executing it's instructions.

        """
        return self._return_type

    @return_type.setter
    def return_type(self, return_type):
        """Set the declaration of value returned by the function to it's caller
        when it finishes execution.

        """
        self._return_type = return_type

    @property
    def arguments(self):
        """Return the list of arguments recevied by the function when it's
        called.
        
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments=[]):
        """Set the list of arguments recevied by the function when it's
        called.

        """
        self._arguments = arguments

    @property
    def name(self):
        """Return the current function name."""
        return self._name

    @name.setter
    def name(self, name):
        """Store the specified name as the function name."""
        self._name = name

    def add_prologue_address(self, address):
        """Mark the specified address as part of the function prologue and
        remove it from the list of statements to analyze.

        """
        self.prologue_addresses.add(address)

    def add_epilogue_address(self, address):
        """Mark the specified address as part of the function epilogue and
        remove it from the list of statements to analyze.

        """
        self.epilogue_addresses.add(address)

    @property
    def _llvm_type(self):
        """Return the LLVM function declaration object."""
        # We need to represent the class of functions that accept and
        # return the specified types.
        # This is represented by an object of the function declaration
        # (api.llvm.FunctionType):

        # Create the LLVM function declaration object to define current
        # function.
        if self.__llvm_type is None:
            self._llvm_type = MiddleIrTypeFunction(
                                self.return_type,
                                self.arguments_types,
                                self.variadic_arguments)

        return self.__llvm_type

    @_llvm_type.setter
    def _llvm_type(self, llvm_type):
        """Store the LLVM function declaration object."""
        self.__llvm_type = llvm_type

    @property
    def prologue_addresses(self):
        """Return the prologue addresses list."""
        return self._prologue_addresses

    @prologue_addresses.setter
    def prologue_addresses(self, prologue_addresses):
        """Store the prologue addresses list."""
        self._prologue_addresses = prologue_addresses

    def set_argument_name(self, index, name):
        """Set the name for the argument at the specified index."""
        try:
            self.arguments[index] = name
        except IndexError, err:
            raise MiddleIrFunctionException(
                "Function '%s' has no argument at index %d." % \
                    (self.name, index))

    @property
    def _llvm_definition(self):
        """Return the LLVM function object returned after being added to a LLVM
        Module object.

        """
        return self.__llvm_func_def

    @_llvm_definition.setter
    def _llvm_definition(self, llvm_func_def):
        """Store the LLVM function object returned after being added to a LLVM
        Module object.

        """
        if llvm_func_def is not None:
            # Set the argument now that the function has been created and
            # associated to a module. This gives us the arguments to be used
            # inside the function and not just the arguments types (which are
            # the types contained in the arguments but are useless by
            # itselves).
            self.arguments = list()
            for i in range(len(llvm_func_def.args)):
                arg = MiddleIrArgument(llvm_func_def.args[i])
                arg.type = self.arguments_types[i]
                self.arguments.append(arg)

        self.__llvm_func_def = llvm_func_def
        #print self.__llvm_func_def

    @property
    def module(self):
        """Return the LLVM module object owning this function."""
        return self.mir_module

    @module.setter
    def module(self, mir_module):
        """Store the LLVM module object owning this function."""
        self.mir_module = mir_module

    @property
    def calling_convention(self):
        """Return the calling convention of the current function."""
        return self._calling_convention

    @calling_convention.setter
    def calling_convention(self, call_conv):
        """Store the calling convention of the current function."""
        #FIXME Add calling conventions again
        #if call_conv not in CALLING_CONVENTIONS:
        #    raise MiddleIrFunctionException(
        #        "Invalid calling convention specified (%d)." % call_conv)

        self._calling_convention = call_conv

        # TODO : FIXME
        #self._llvm_definition.setCallingConv(call_conv)

    @property
    def calling_convention_name(self):
        """Return the name of the calling convention for the current
        function.
        
        """
        return "fastcall"# CALLING_CONVENTIONS[self.calling_convention]

    def __repr__(self):
        """Return a string object with the function representation."""
        return repr(self._llvm_definition)

    def __str__(self):
        """Return a string object with the function text representation."""
        return str(self._llvm_definition)

    def get_basic_block_by_address(self, address):
        """Return the instruction builder for the corresponding basic block
        that own the specified address.

        """
        for index, basic_block in enumerate(self):
            if basic_block.has_address(address):
                return basic_block

        return None

    def get_instruction_builder_by_address(self, address, update_position=False):
        """Return the instruction builder for the corresponding basic block
        that owns the specified address.

        """
        for index, basic_block in enumerate(self):
            if basic_block.has_address(address):
                builder = basic_block.instruction_builder

                if update_position:
                    builder.position_at_address(address)

                return builder

        raise MiddleIrFunctionException(
            "No MIR builder available for address 0x%X" % address)

    @staticmethod
    def new(module, name, return_type=MiddleIrTypeVoid(), arguments=None,
        variadic_arguments=False):
        """Create a new function."""
        # Make sure that the module exists and it's of the right type.
        # TODO / FIXME : Remove comments below and fix import problem.
        #if not isinstance(module, MiddleIrModule):
        #    raise MiddleIrFunctionException(
        #        "No module specified to add function '%s'." % name)

        # Check if the function already exists inside the module. In case it
        # doesn't exists then we create a new one.
        # Otherwise we'll raise an exception.
        if module.get_function_by_name(name) is not None:
            raise MiddleIrFunctionException(
                "Function '%s' already exists in module '%s'" % (
                name, module.name))

        new_func = MiddleIrFunction(name, return_type, arguments, variadic_arguments)
        module.add_function(new_func)
        return new_func

    @staticmethod
    def get(module, name):
        """Return an existing function matching the specified name."""
        # Make sure that the module exists and it's of the right type.
        if not isinstance(module, MiddleIrModule):
            raise MiddleIrFunctionException(
                "No module specified to return function '%s'." % name)

        # Return the result whether it's an existing function or not.
        return module.get_function_by_name(name)

    def delete(self):
        """Delete ourselves."""
        self.module.remove_function(self)

        # FIXME / TODO : Is this right? Check with new testcases
        #if self._llvm_definition:
        #    self._llvm_definition.delete()

        del self
