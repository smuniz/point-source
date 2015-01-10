# 
# Copyright (c) 2014 Sebastian Muniz
# 
# This code is part of point source decompiler
#
import abc


class IdiomAnalyzerException(Exception):
    pass


class IdiomAnalyzer(object):
    """Base class to facilitate idioms analysis."""
    __metaclass__ = abc.ABCMeta

    def __init__(self, debugger):
        """Initialize idiom analyzer base class."""
        self.debugger = debugger

    def init(self, lir_function, mir_function, symbols_table):
        """Clean any internal state and setup everything for new analysis."""
        self.lir_function = lir_function  # Function low-level representation

        self.mir_function = mir_function

        # Current module's IR
        if self.mir_function is not None:
            self.mir_module = mir_function.module
        else:
            self.mir_module = None

        # Current architectures instruction set to work with.
        self.iset = self.debugger.instruction_set

        # Store the current MIR function in the symbol tables dict and keep a
        # reference as the current one being used for further analysis.
        symbols_manager = symbols_table
        self.current_symbols_table = \
            symbols_manager.symbols(lir_function.start_address)

    @property
    def mir_function(self):
        """Get a reference to all the symbol tables analyzed."""
        return self._mir_function

    @mir_function.setter
    def mir_function(self, _mir_function):
        """Store a reference to all the symbols tables analyzed."""
        self._mir_function = _mir_function

    @property
    def symbols_table(self):
        """Get a reference to all the symbol tables analyzed."""
        return self._symbols_table

    @symbols_table.setter
    def symbols_table(self, _symbols_table):
        """Store a reference to all the symbols tables analyzed."""
        self._symbols_table = _symbols_table

    @property
    def current_symbols_table(self):
        """Get a reference to the current the symbols tables being analyzed."""
        return self._current_symbols_table

    @current_symbols_table.setter
    def current_symbols_table(self, _symbol_table):
        """Store a reference to all the symbol tables analyzed."""
        self._current_symbols_table = _symbol_table

    def get_signed_value(self, value):
        """..."""
        return (value + 2**31) % 2**32 - 2**31 # WTF?

    def perform_phase0_analysis(self):
        """Execute the basic idiom analysis on current function previous to MIR
        generation.

        """
        # Add any prior action.
        self._perform_phase0_analysis()
        # Add any post action.

    def perform_phase1_analysis(self):
        """Execute the basic idiom analysis on current function previous to MIR
        generation.

        """
        # This is used when a function is being analyzed to determine minimal
        # information about it but no detailed information or analysis are
        # necessary.

        # Add any prior action.
        self.mir_module = self.mir_function.module    # Current module's IR

        self._perform_phase1_analysis()
        # Add any post action.

    def perform_phase2_analysis(self):
        """Execute the basic idiom analysis on current function after to MIR
        generation procedure.

        """
        # Add any prior action.
        self._perform_phase2_analysis()
        # Add any post action.

    @abc.abstractmethod
    def detect_prologue(self):
        """Check wheater the function prologue is present or not."""
        return

    @abc.abstractmethod
    def detect_epilogue(self):
        """Check wheater the function epilogue is present or not."""
        return

    @abc.abstractmethod
    def detect_calling_convention(self):
        """Obtain the calling convention detected by the compiler."""
        return

    @abc.abstractmethod
    def detect_unoptimized_code_sequences(self):
        """When the source code is compiled without any optimization flag
        enabled, the code generated by the compiler might contain redundant
        instructions which were not changed/removed by the optimizer.

        The porpuse of this method is to locate such instructions sequence and
        handle them appropriately.

        """
        return

    def get_string_by_address(self, address, is_unicode_string=False):
        """Return the string pointer by the specified address."""

        if is_unicode_string:
            string = self.debugger.get_string(
                address, None, self.debugger.STRING_TYPE_UNICODE)
        else:
            string = self.debugger.get_string(address)

        # Don't return an empty string, instead return None.
        if string is not None:
            return string
        else:
            return None

    def is_compiler_unknown(self):
        """Return a boolean indicating if the compiler used to generate the
        current binary code is unknown or not.

        """
        return self.lir_function.compiler_type == self.debugger.COMPILER_UNK

    def detect_compiler(self):
        """Obtain the name and type of the compiler used to generate the code
        being analyzed.

        In case the compiler is unknown to the debugger, try to guess it.

        """
        # Let the debugger try first and check if the compiler was successfully
        # detected.
        self.lir_function.compiler_type = self.debugger.get_default_compiler()

        if self.is_compiler_unknown():
            # Try to guess the compiler
            if not self.guess_compiler_type():
                print "Unsupported %s compiler" % \
                    self.debugger.get_compiler_name(self.lir_function.compiler_type)
                return False

        print "    Compiler detected: %s" % \
            self.debugger.get_compiler_name(self.lir_function.compiler_type)

        return True

    @property
    def compiler_type(self):
        """Return the compiler type."""
        return self.compiler

    @compiler_type.setter
    def compiler_type(self, comp):
        """Store the compiler type."""
        self.compiler = comp

    @abc.abstractmethod
    def guess_compiler_type(self):
        """Determine the compiler for the current binary."""
        return

    @abc.abstractmethod
    def is_call_instruction(self, lir_inst):
        """Determine if the specified instruction is a call instruction or
        not.

        """
        return
