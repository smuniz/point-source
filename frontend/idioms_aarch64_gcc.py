# 
# Copyright (c) 2017 Sebastian Muniz
#
# This code is part of point source decompiler
#

from traceback import format_exc

from idioms import IdiomAnalyzer, IdiomAnalyzerException

from middleend.mir import *


class AArh64GccIdiomAnalyzerException(IdiomAnalyzerException):
    """Generic exception for idioms analyzer on AArh64 architecture."""
    pass


class AArh64GccIdiomAnalyzer(IdiomAnalyzer):
    """Support for AArch64 (ARM 64-bits) GCC specific idioms analyzer."""

    def __init__(self, debugger):
        """Initialize idiom analyzer for the AArch64 architecture."""
        super(AArh64GccIdiomAnalyzer, self).__init__(debugger)

    def init(self, lir_function, mir_function, symbol_tables):
        """Clean any internal state and setup everything for new analysis."""
        super(AArh64GccIdiomAnalyzer, self).init(
            lir_function, mir_function, symbol_tables)

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
