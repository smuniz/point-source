# 
# Copyright (c) 2014 Sebastian Muniz
# 
# This code is part of point source decompiler
#

import output_media.text_output_media.text_output_media
reload(output_media.text_output_media.text_output_media)
from output_media.text_output_media.text_output_media import TextOutputMedia, \
    TextOutputMediaException

__all__ = ["HirTextOutput", "HirTextOutputException"]


class HirTextOutputException(TextOutputMediaException):
    """Generic exception for HIR text output media."""
    pass


class HirTextOutput(TextOutputMedia):
    """Display appropiately the HIR translated code and perform callbacks if
    applicable.

    """

    STATEMENTS = [
        "for",
        "do",
        "while",
        "goto",
        "continue",
        "break",
        "if",
        "else",
        "return",
        "switch",
        "case",
        "default",
        ]

    KEYWORDS = [
        "auto",
        "const",
        "enum",
        "extern",
        "inline", #(since C99)
        "register",
        "restrict", #(since C99)
        "short",
        "signed",
        "sizeof",
        "static",
        "struct",
        "typedef",
        "union",
        "unsigned",
        "void",
        "volatile",
        "_Alignas", #(since C11)
        "_Alignof", #(since C11)
        "_Atomic", #(since C11)
        "_Bool", #(since C99)
        "_Complex", #(since C99)
        "_Generic", #(since C11)
        "_Imaginary", #(since C99)
        "_Noreturn", #(since C11)
        "_Static_assert", #(since C11)
        "_Thread_local", #(since C11)
        ]

    TYPES = [
        "char",
        "float",
        "int",
        "long",
        "double",
        ]

    def __init__(self, hir=None):
        """Instance initialization."""
        super(HirTextOutput, self).__init__()

        self.hir = hir

        # Update HIR map for addresses relations.
        self.address_map = dict()
        self.addresses_coloured = dict()

    @property
    def hir(self):
        """Return the high level IR."""
        return self._hir

    @hir.setter
    def hir(self, hir):
        """Store the high level IR for further usage."""
        self._hir = hir

    def generate_output(self, title):
        """Generate C-like readble output in the log window."""
        if not self.hir:
            raise HirTextOutputException("No High-level IR available.")

        super(HirTextOutput, self).generate_output(title)

    def colorize(self):
        """Fill the recently created window with the text."""
        line_number = 0

        #
        # Generate function prologue.
        #
        func_opening = self.generate_function_opening()

        self.add_lines(func_opening)

        for cur_line_number in xrange(len(func_opening)):
            print "prologue : cur_line_number %d - line_number %d" % (cur_line_number, line_number)
            self.address_map[cur_line_number] = self.hir.prologue_addresses
            line_number += 1 # Move forward line number index.

        #
        # Generate function body.
        #
        self.label_indent = 1
        indent_level = 1
        indent = " " * (indent_level * 4)

        for block in self.hir.blocks:

            if len(self.hir.blocks) > 1 and block.label is not None:
                label = block.label
                s = self.as_string("%(indent)s%(label)s" % vars())

                self.add_line(s)

            block_repr = ""
            for stmt in block.statements:
                #print "---> stmt : %s" % stmt
                #block_repr += "%s\n" % stmt

            #block_repr = str(block)
            #for stmt in block_repr.splitlines():
                stmt_fmt = "%(indent)s%(stmt)s" % vars()
                stmt_fmt = "%-40s" % stmt_fmt
                self.__colorize_line(stmt_fmt)

                self.address_map[line_number] = stmt.addresses
                print "statement : cur_line_number %d - line_number %d" % (cur_line_number, line_number)
                line_number += 1 # Move forward line number index.

        #
        # Generate function epilogue.
        #
        func_closure = self.generate_function_closure()

        self.add_lines(func_closure)

        for cur_line_number in xrange(len(func_closure)):
            print "epilogue : cur_line_number %d - line_number %d" % (cur_line_number, line_number)
            self.address_map[cur_line_number] = self.hir.prologue_addresses
            line_number += 1 # Move forward line number index.


        return True

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
            elif ch == '/' and line[x + 1] == '/':
                s += self.as_comment(line[x : ])
                # Done with this line
                break

            #elif ch == '.' and x + 1 < e:
            #    x, w = self.get_identifier(line, x + 1, e)
            #    s += self.as_directive(ch + w)

            # Identifiers?
            elif self.is_identifier(ch):

                x, w = self.get_identifier(line, x, e)

                # Number?
                if ch.isdigit():
                    s += self.as_number(w)
                else:
                    # Other identifier
                    s += self.as_identifier(w)

            ## Variable name?
            #elif ch == '%':

            #    w = ch + line[x + 1 : ].split(" ")[0]
            #    s += self.as_variable_name(w)
            #    x += len(w)

            ## Function name?
            #elif ch == '@':

            #    w = ch + line[x + 1 : ].split(" ")[0]
            #    s += self.as_function_name(w)
            #    x += len(w)

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

    def generate_function_opening(self):
        """Create the C functions opening text to represent."""
        # Store the function code representation for the prologue.
        func_repr = list()

        ret_type = self.as_identifier(self.hir.return_type)

        if not self.hir.is_calling_convention_c:
            call_conv = "%s " % \
                self.as_identifier(self.hir.calling_convention_name)
        else:
            call_conv = ""

        name = self.as_function_name(self.hir.name)

        params = ""
        if self.hir.has_parameters:
            params = "%s" % (" ".join(self.hir.get_parameter_n[0]))

            params += ", ".join([param_tuple \
                for param_tuple in self.hir.paramters[1 : ]])

        func_repr.append(
            "%(ret_type)s %(call_conv)s%(name)s (%(params)s)" % vars())

        func_repr.append(self.as_string("{"))

        return func_repr

    def generate_function_closure(self):
        """Create the C functions closure text to represent."""
        # Store the function code representation for the epilogue.
        func_repr = list()

        func_repr.append(self.as_string("}"))

        return func_repr

    def on_key_down(self, vkey, shift):
        """
        User pressed a key
        @param vkey: Virtual key code
        @param shift: Shift flag
        @return: Boolean. True if you handled the event
        """
        if vkey in [ord("R"), ord("r")]:
            #print "refreshing (forced)..."
            self.refresh()
        else:
            # An unknown key was pressed.
            return False

        return True

    def on_curor_position_changed(self):
        """Cursor position changed callback."""
        cur_line_number = self.GetLineNo()
        addresses = self.address_map.get(cur_line_number, None)

        print ", ".join(
            ["0x%08x" % addr for addr in addresses])

        if not addresses:
            print "No address(es) for line number %d" % cur_line_number
            return

        # First we restablish the previously coloured lines.
        for address, colour in self.addresses_coloured.iteritems():
            self.set_colour(address, colour)

        self.addresses_coloured.clear()
            
        for address in addresses:
            self.addresses_coloured[address] = self.get_colour(address)
        
