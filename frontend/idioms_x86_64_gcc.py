# 
# Copyright (c) 2017 Sebastian Muniz
#
# This code is part of point source decompiler
#

from traceback import format_exc

from idioms import IdiomAnalyzer, IdiomAnalyzerException

from middleend.mir import *


class X86_64GccIdiomAnalyzerException(IdiomAnalyzerException):
    """Generic exception for idioms analyzer on x86_64 architecture."""
    pass


class X86_64GccIdiomAnalyzer(IdiomAnalyzer):
    """Support for x86_64 GCC specific idioms analyzer."""

    def __init__(self, debugger, lir_function, mir_module, mir_function):
        """Initialize idiom analyzer for the x86_64 architecture."""
        IdiomAnalyzer.__init__(
            self, debugger, lir_function, mir_module, mir_function)

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
