# 
# Copyright (c) 2014 Sebastian Muniz
# 
# This code is part of point source decompiler
#

import output_media.text_output_media.text_output_media
reload(output_media.text_output_media.text_output_media)
from output_media.text_output_media.text_output_media import TextOutputMedia, \
    TextOutputMediaException

__all__ = ["MirTextOutput", "MirTextOutputException"]


class MirTextOutputException(TextOutputMediaException):
    """Generic exception for MIR text output media."""
    pass


class MirTextOutput(TextOutputMedia):
    """
    Display the Middle level IR with syntax highlighting and correct
    tabulation.

    """

    STATEMENTS = [
        "add", "fadd", "sub", "fsub", "mul", "fmul",
        "sdiv", "udiv", "fdiv", "srem", "urem", "frem",
        "and", "or", "xor",
        "icmp", "fcmp",
        "eq", "ne", "ugt", "uge", "ult", "ule", "sgt", "sge", "slt", "sle",
        "oeq", "ogt", "oge", "olt", "ole", "one", "ord", "ueq", "ugt", "uge",
        "ult", "ule", "une", "uno",
        "nuw", "nsw", "exact", "inbounds",
        "phi", "call", "select", "shl", "lshr", "ashr", "va_arg",
        "trunc", "zext", "sext",
        "fptrunc", "fpext", "fptoui", "fptosi", "uitofp", "sitofp",
        "ptrtoint", "inttoptr", "bitcast",
        "ret", "br", "switch", "invoke", "unwind", "unreachable",
        "malloc", "alloca", "free", "load", "store", "getelementptr",
        "extractelement", "insertelement", "shufflevector",
        "extractvalue", "insertvalue"]

    KEYWORDS = [
        "define", "declare", "global", "constant",
        "internal", "external", "private",
        "linkonce", "linkonce_odr", "weak", "weak_odr", "appending",
        "common", "extern_weak",
        "thread_local", "dllimport", "dllexport",
        "hidden", "protected", "default",
        "except", "deplibs",
        "volatile", "fastcc", "coldcc", "cc", "ccc",
        "x86_stdcallcc", "x86_fastcallcc",
        "signext", "zeroext", "inreg", "sret", "nounwind", "noreturn",
        "nocapture", "byval", "nest", "readnone", "readonly", "noalias",
        "noinline", "alwaysinline", "optsize", "ssp", "sspreq",
        "noredzone", "noimplicitfloat", "naked",
        "module", "asm", "align", "tail", "to",
        "addrspace", "section", "alias", "sideeffect", "c", "gc",
        "target", "datalayout", "triple"]

    TYPES = [
        "void", "float", "double",
        "x86_fp80", "fp128", "ppc_fp128",
        "type", "label", "opaque"]

    def __init__(self, mir=None):
        """Instance initialization."""
        super(MirTextOutput, self).__init__()

        self.mir = mir

    @property
    def mir(self):
        """Return the middle-end intermediate representation of the entire
        module.

        """
        return self._mir

    @mir.setter
    def mir(self, mir):
        """Store the middle-end intermediate representation of the entire
        module.

        """
        self._mir = mir

    def colorize(self):
        """Fill the recently created window with the text."""
        # Iterate through every function present in the MIR.
        for line in str(self.mir).splitlines():
            self.__colorize_line(line)

    def __colorize_line(self, line):
        """Apply the appropriate colour to the currently specified line."""
        if not line:
            self.add_line()
            return

        x = 0
        e = len(line)
        s = ""

        while x < e:

            ch = line[x]

            # String?
            if ch == '"' or ch == "'":
                x, w = self.get_quoted_string(line, x, e)
                s += self.as_string(w)

            # Tab?
            elif ch == '\t':
                s += ' ' * 4
                x += 1

            # Comment?
            elif ch == ';':
                s += self.as_comment(line[x : ])
                # Done with this line
                break

            elif ch == '.' and x + 1 < e:
                x, w = self.get_identifier(line, x + 1, e)
                s += self.as_directive(ch + w)

            # Identifiers?
            elif self.is_identifier(ch):

                x, w = self.get_identifier(line, x, e)

                # Number?
                if ch.isdigit():
                    s += self.as_number(w)
                else:
                    # Other identifier
                    s += self.as_identifier(w)

            # Variable name?
            elif ch == '%':

                w = ch + line[x + 1 : ].split(" ")[0]
                s += self.as_variable_name(w)
                x += len(w)

            # Function name?
            elif ch == '@':

                w = ch + line[x + 1 : ].split(" ")[0]
                s += self.as_function_name(w)
                x += len(w)

            # Output as is
            else:
                #s += self.as_default(ch)
                s += ch
                x += 1

        # Display the processed string in the window.
        self.add_line(s)

    def is_identifier(self, ch):
        """Indicate whether this is an identifier or not."""
        return ch == '_' or ch.isalpha() or '0' <= ch <= '9'

    def get_identifier(self, line, x, e):
        """..."""
        i = x

        is_digit = line[i].isdigit()

        while i < e:

            ch = line[i]

            if not self.is_identifier(ch):
                if ch != '.' or not is_digit:
                    break
            i += 1

        return (i, line[x:i])

    def get_quoted_string(self, line, x, e):
        """Return the string inside the quote at the specified position
        contained in the line passed as parameter.
        
        """
        quote   = line[x]   # Store the quote used (either " or ')
        cur_pos = x + 1

        while cur_pos < e:

            ch = line[cur_pos]

            if ch == '\\' and line[cur_pos + 1] == quote:
                cur_pos += 1

            elif ch == quote:
                cur_pos += 1 # also take the quote
                break

            cur_pos += 1

        return (cur_pos, line[x : cur_pos])

    def on_close(self):
        """Close event."""
        pass

    def OnKeydown(self, vkey, shift):
        """Handle every key pressed in the newly created window."""
        pass
