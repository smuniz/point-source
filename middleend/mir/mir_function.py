# 
# Copyright (c) 2013 Sebastian Muniz
# 
# This code is part of point source decompiler
#

from llvm import *
from llvm.core import *

from mir_function_base import MiddleIrFunctionBase, \
                                MiddleIrFunctionBaseException
from mir_type import *

#
# LLVM calling conventions converted to our equivalents.
#
CALL_CONV_C             = CC_C
CALL_CONV_FASTCALL      = CC_FASTCALL
CALL_CONV_COLDCALL      = CC_COLDCALL
CALL_CONV_X86_STDCALL   = CC_X86_STDCALL
CALL_CONV_X86_FASTCALL  = CC_X86_FASTCALL
CALL_CONV_GHC           = CC_GHC
CALL_CONV_ARM_APCS      = CC_ARM_APCS
CALL_CONV_ARM_AAPCS     = CC_ARM_AAPCS
CALL_CONV_ARM_AAPCS_VFP = CC_ARM_AAPCS_VFP
CALL_CONV_MSP430_INTR   = CC_MSP430_INTR
CALL_CONV_X86_THISCALL  = CC_X86_THISCALL
CALL_CONV_PTX_KERNEL    = CC_PTX_KERNEL
CALL_CONV_PTX_DEVICE    = CC_PTX_DEVICE
CALL_CONV_MBLAZE_INTR   = CC_MBLAZE_INTR
CALL_CONV_MBLAZE_SVOL   = CC_MBLAZE_SVOL

CALLING_CONVENTIONS = {
     CALL_CONV_C             : "C",
     CALL_CONV_FASTCALL      : "Fastcall",
     CALL_CONV_COLDCALL      : "Coldcall",
     CALL_CONV_X86_STDCALL   : "x86 stdcall",
     CALL_CONV_X86_FASTCALL  : "x86 fastcall",
     CALL_CONV_GHC           : "GHC",
     CALL_CONV_ARM_APCS      : "ARM Procedure Calling Standard",
     CALL_CONV_ARM_AAPCS     : "ARM Architecture Procedure Calling Standard",
     CALL_CONV_ARM_AAPCS_VFP : "ARM Architecture Procedure Calling Standard - hard floating point ABI",
     CALL_CONV_MSP430_INTR   : "MSP430 interrupt routines",
     CALL_CONV_X86_THISCALL  : "x86 thiscall",
     CALL_CONV_PTX_KERNEL    : "PTX kernel",
     CALL_CONV_PTX_DEVICE    : "PTX device",
     CALL_CONV_MBLAZE_INTR   : "MBlaze ???",
     CALL_CONV_MBLAZE_SVOL   : "MBlaze ???",
    }


class MiddleIrFunctionException(MiddleIrFunctionBaseException):
    """Middle IR function exception."""
    pass


#class MiddleIrIntrinsicFunction(MiddleIrFunction):
#    def __init__(self, name, mir_module):
#        MiddleIrFunction.__init__(name, mir_module)


class MiddleIrFunction(MiddleIrFunctionBase):
    """Middle level intermediate representation class of functions being
    decompiled.

    This class main objetive is to provide a simple abstration layer over the
    LLVM IR function object.

    """

    def __init__(self, name, return_type=MiddleIrTypeVoid(), parameters=None,
        variadic_arguments=False):
        """Initialize the intermediate level IR module class."""
        super(MiddleIrFunction, self).__init__()

        # Initialize the function name.
        self.name = name

        # Epilogue and prologue instruction addresses inside the current
        # function.
        self.prologue_addresses = list()
        self.epilogue_addresses = list()

        #
        # Initialize the LLVM function declaration object and initially set the
        # function parameters and return declaration to void. 
        #
        self.return_type = return_type
        self.parameters = parameters
        self.variadic_arguments = variadic_arguments    # No variadic args by
                                                        # default. Let the user
                                                        # set them. 
        self._llvm_type = None

        # Keep track of every basic block contained in this function.
        self._basic_blocks = list()

        # Store the Middle-end module instance.
        self.module = None

        # Set the default calling convention.
        self.calling_convention = CALL_CONV_C

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
        self._basic_blocks.append(mir_basic_block)

        mir_basic_block._llvm_function = self._llvm_definition

    def get_basic_block(self, index):
        """Return the basic block at the specified position in the basic blocks
        list.

        """
        return self._basic_blocks[index]

    def __getitem__(self, key):
        if isinstance(key, slice):
            indices = key.indices(len(self))
            return [self[i] for i in xrange(*indices)]
        elif isinstance(key, int) or isinstance(key, long):
            try:
                return self.get_basic_block(key)
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
    def parameters(self):
        """Return the list of parameters recevied by the function when it's
        called.
        
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters=None):
        """Set the list of parameters recevied by the function when it's
        called.

        """
        self._parameters = [] if parameters is None else parameters

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
        self.prologue_addresses.append(address)
        #self.removeStatementByAddress(address)

    def add_epilogue_address(self, address):
        """Mark the specified address as part of the function epilogue and
        remove it from the list of statements to analyze.

        """
        self.epilogue_addresses.append(address)
        #self.removeStatementByAddress(address)

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
                                self.parameters,
                                self.variadic_arguments)

        return self.__llvm_type

    @_llvm_type.setter
    def _llvm_type(self, llvm_type):
        """Store the LLVM function declaration object."""
        self.__llvm_type = llvm_type

    def set_argument_name(self, index, name):
        """Set the name for the argument at the specified index."""
        try:
            self._llvm_definition.args[index] = name
        except IndexError, err:
            raise MiddleIrFunctionException(
                "Function \'%s\' has no argument at index %d." % \
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
        self.__llvm_func_def = llvm_func_def

    def _llvm_add_function_to_module(self):
        """Add the LLVM function definition object to the module."""
        # Obtain the necessary information to add the specified function to the
        # current LLVM module.
        #self.llvm_func_def = self.module.add_function(
        #    self._llvm_get_type(), self.get_name())
        pass

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
        if call_conv not in CALLING_CONVENTIONS:
            raise MiddleIrFunctionException(
                "Invalid calling convention specified (%d)." % call_conv)

        self._calling_convention = call_conv

        # TODO : FIXME
        #self._llvm_definition.setCallingConv(call_conv)

    @property
    def calling_convention_name(self):
        """Return the name of the calling convention for the current
        function.
        
        """
        return CALLING_CONVENTIONS[self.calling_convention]

    def __repr__(self):
        """Return a string object with the function representation."""
        return repr(self.llvm_func_def)

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
