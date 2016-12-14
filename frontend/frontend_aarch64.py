# 
# Copyright (c) 2017 Sebastian Muniz
# 
# This code is part of point source decompiler
#

from frontend import FrontEnd

import idioms_aarch64_gcc
reload(idioms_aarch64_gcc)
from idioms_aarch64_gcc import AArch64GccIdiomAnalyzer

# Import MIR related modules
from middleend.mir import *


class FrontEndAArch64Exception(Exception):
    """Generic ARM front-end exception."""
    pass


class FrontEndAArch64(FrontEnd):
    """Front-end support for the AArch (ARM 64-bits) architecture."""

    TARGET_ARCH = "aarch64"

    def __init__(self, debugger):
        """Perform ARM front-end instance initialization."""
        FrontEnd.__init__(self, AArch64GccIdiomAnalyzer, debugger)

    def on_assignment(self, lir_inst):
        """Handle Low level IR assignment instructions."""
        return None

    def on_unconditional_branch(self, lir_inst):
        """Handle Low level IR unconditional branch instructions."""
        return None

    def on_conditional_branch(self, lir_inst):
        """Handle Low level IR conditional branch instructions."""
        return None

    def on_unknown(self, lir_inst):
        """Handle unknown Low level IR instructions."""
        return None

    def _extract_callee_address(self, lir_inst):
        """Return the callee address from a call instruction, if any."""
        if not self.idiom_analyzer.is_call_instruction(lir_inst):
            return None

        # FIXME This was copied from PPC without any testing... check it
        #if len(lir_inst) == 1:
        #    return lir_inst[0].value

        return None

    #def analyze_callee(self, callee_address):
    #    """Analyze the callee function by performing a live analysis on it."""
    #    lir_function = self.debugger.generate_lir(callee_address)
    #    #print lir_function
    #    return lir_function

    def _is_stack_destination(self, lir_inst):
        """Check that destination of the operation is the stack."""
        # TODO
        return False
