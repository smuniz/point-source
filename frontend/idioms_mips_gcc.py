# 
# Copyright (c) 2017 Sebastian Muniz
#
# This code is part of point source decompiler
#

from traceback import format_exc

from idioms import IdiomAnalyzer, IdiomAnalyzerException

from middleend.mir import *


class MipsGccIdiomAnalyzerException(IdiomAnalyzerException):
    """Generic exception for idioms analyzer on Mips architecture."""
    pass


class MipsGccIdiomAnalyzer(IdiomAnalyzer):
    """Support for arm specific idioms analyzer."""

    def __init__(self, debugger):
        """Initialize idiom analyzer for the ARM architecture."""
        super(MipsGccIdiomAnalyzer, self).__init__(debugger)

    def init(self, lir_function, mir_function, symbol_tables):
        """Clean any internal state and setup everything for new analysis."""
        super(MipsGccIdiomAnalyzer, self).init(
            lir_function, mir_function, symbol_tables)

    def perform_phase0_analysis(self):
        """Execute the most basic idiom analysis on current function previous
        to every other major analysis.

        """
        print "[-] Warning: perform_phase0_analysis() is empty"

    def perform_phase1_analysis(self):
        """
        Execute the basic idiom analysis on current function previous to MIR
        generation.

        """
        print "[-] Warning: perform_phase1_analysis() is empty"

    def perform_phase2_analysis(self):
        """
        Execute the basic idiom analysis on current function after to MIR
        generation.

        """
        print "[-] Warning: perform_phase2_analysis() is empty"

    def detect_epilogue(self):
        """Check wheater the function epilogue is present or not."""
        # FIXME
        pass

    def detect_prologue(self):
        # FIXME
        pass

    def detect_unoptimized_code_sequences(self):
        # FIXME
        pass

    def guess_compiler_type(self):
        # FIXME
        return False

    def is_call_instruction(self, lir_inst):
        # FIXME
        return False

    def detect_calling_convention(self):
        """Obtain the calling convention detected by the compiler."""
        # FIXME: Detect calling convention.
        print "    Calling convention: %s" % \
            self.mir_function.calling_convention_name

        return True

