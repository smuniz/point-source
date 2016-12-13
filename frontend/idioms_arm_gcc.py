# 
# Copyright (c) 2017 Sebastian Muniz
#
# This code is part of point source decompiler
#

from traceback import format_exc

from idioms import IdiomAnalyzer, IdiomAnalyzerException

from middleend.mir import *


class ArmGccIdiomAnalyzerException(IdiomAnalyzerException):
    """Generic exception for idioms analyzer on Arm architecture."""
    pass


class ArmGccIdiomAnalyzer(IdiomAnalyzer):
    """Support for arm specific idioms analyzer."""

    def __init__(self, debugger):
        """Initialize idiom analyzer for the ARM architecture."""
        super(ArmGccIdiomAnalyzer, self).__init__(debugger)

    def init(self, lir_function, mir_function, symbol_tables):
        """Clean any internal state and setup everything for new analysis."""
        super(ArmGccIdiomAnalyzer, self).init(
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
