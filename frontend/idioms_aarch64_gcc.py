# 
# Copyright (c) 2017 Sebastian Muniz
#
# This code is part of point source decompiler
#

from traceback import format_exc

from idioms import IdiomAnalyzer, IdiomAnalyzerException

from middleend.mir import *


class AArch64GccIdiomAnalyzerException(IdiomAnalyzerException):
    """Generic exception for idioms analyzer on AArch64 architecture."""
    pass


class AArch64GccIdiomAnalyzer(IdiomAnalyzer):
    """Support for AArch64 (ARM 64-bits) GCC specific idioms analyzer."""

    def __init__(self, debugger):
        """Initialize idiom analyzer for the AArch64 architecture."""
        super(AArch64GccIdiomAnalyzer, self).__init__(debugger)

    def init(self, lir_function, mir_function, symbol_tables):
        """Clean any internal state and setup everything for new analysis."""
        super(AArch64GccIdiomAnalyzer, self).init(
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
        # FIXME TODO
        pass

    def detect_prologue(self):
        # FIXME TODO
        pass

    def detect_unoptimized_code_sequences(self):
        # FIXME TODO
        pass

    def guess_compiler_type(self):
        # FIXME TODO
        return False

    def is_call_instruction(self, lir_inst):
        # FIXME TODO
        return False

    def detect_calling_convention(self):
        """Obtain the calling convention detected by the compiler."""
        # FIXME TODO: Detect calling convention.
        print "    Calling convention: %s" % \
            self.mir_function.calling_convention_name

        return True

