# 
# Copyright (c) 2014 Sebastian Muniz
# 
# This code is part of point source decompiler
#

from frontend import FrontEnd

import idioms_mips_gcc
reload(idioms_mips_gcc)
from idioms_mips_gcc import MipsGccIdiomAnalyzer

# Import MIR related modules
from middleend.mir import *


class FrontEndMipsException(Exception):
    """Generic MIPS front-end exception."""
    pass


class FrontEndMips(FrontEnd):
    """Front-end support for the MIPS architecture."""

    TARGET_ARCH = "mips"

    def __init__(self, debugger):
        """Perform MIPS front-end instance initialization."""
        FrontEnd.__init__(self, MipsGccIdiomAnalyzer, debugger)

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

    def is_call_instruction(self, lir_inst):
        """Determine if the specified instruction is a call instruction or
        not.

        """
        # TODO / FIXME : make this right.
        return bool(
            lir_inst.type == self.iset.PPC_b and \
            lir_inst._aux == 8 and \
            len(lir_inst) == 1 and \
            lir_inst[0].type in [O_NEAR, O_FAR])

    def _extract_callee_address(self, lir_inst):
        """Return the callee address from a call instruction, if any."""
        if not self.is_call_instruction(lir_inst):
            return None

        if len(lir_inst) == 1:
            return lir_inst[0].value

        return None

    def analyze_callee(self, callee_address):
        """Analyze the callee function by performing a live analysis on it."""
        lir_function = self.debugger.generate_lir(callee_address)
        #print lir_function
        return lir_function
