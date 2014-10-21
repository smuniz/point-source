# 
# Copyright (c) 2013 Sebastian Muniz
# 
# This code is part of point source decompiler
#

import idaapi

import abc
from traceback import format_exc
from output_media.output_media_base import OutputMediaBase, \
    OutputMediaBaseException


class TextOutputMediaException(OutputMediaBaseException):
    """Generic exception for text output media."""
    pass


class TextOutputMedia(OutputMediaBase, idaapi.simplecustviewer_t):
    """
    Translate the MIR into a C/C++ readable code, display it appropiately and
    perform callbacks if applicable.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Initialize instance."""
        OutputMediaBase.__init__(self)
        idaapi.simplecustviewer_t.__init__(self)
        self.title = ""

        self.statements = self.STATEMENTS
        self.keywords   = self.KEYWORDS
        self.types      = self.TYPES

    def generate_output(self, title):
        """Generate readble output in a new IDA view window."""
        try:
            # First create the window inside the application used to hold it.
            # Then proceed to show the newly created window and fill it with
            # the data we want to display.
            self.title = title

            crea = self.create()

            if not crea:
                self.ClearLines()
                #self.add_line("hola manola")
                self.refresh()
            else:
                #print "1 OK..."
                pass

            self.show()
            self.colorize() # This must be implemented in the
                                        # derived class.
            #self.refresh()

        except Exception, err:
            print format_exc()
            self.close()
            raise TextOutputMediaException(
                "Error creating viewer called \"%s\"" % title)

    def close(self):
        """Close the current window."""
        self.Close()

    def create(self):
        """Create the new window with the specified title."""
        if not self.Create(self.title):
            #raise TextOutputMediaException("Unable to create custom viewer")
            return False
        return True

    def show(self):
        """Display the window inside the current application."""
        self.Show()

    @abc.abstractmethod
    def colorize(self):
        """Fill the recently created window with the text."""
        return

    def add_lines(self, lines):
        """Add multiple lines to the current display."""
        # Make sure this is a line or a list of lines.
        if isinstance(lines, str):
            self.add_lines(lines)
        else:
            for line in lines:
                self.add_line(line)

    def add_line(self, string=None):
        """Display the specified text at the current line."""
        if not string:
            string = ""

        # Invoke the simple viewer method.
        self.AddLine(string)

    @abc.abstractmethod
    def on_close(self):
        return

    def OnClose(self):
        """Handle close event."""
        self.on_close()

    def OnKeydown(self, vkey, shift):
        """Handle every key pressed in the newly created window."""
        if vkey == 27:
            # The ESC key was pressed so close the window and leave.
            self.Close()
        else:
            # An unknown key was pressed.
            return self.on_key_down(vkey, shift)

        return True

    def OnCursorPosChanged(self):
        """
        Cursor position changed.
        @return: Nothing
        """
        self.on_curor_position_changed()

    def refresh(self):
        """Refresh the current output."""
        self.Refresh()

    #
    # Colorize specific output.
    #
    def as_comment(self, s):
        """Display the specified text as a comment."""
        return idaapi.COLSTR(s, idaapi.SCOLOR_RPTCMT)

    def as_identifier(self, string):
        """Display the specified text as an id."""
        t = string.lower()

        if t in self.keywords:
            return idaapi.COLSTR(string, idaapi.SCOLOR_ASMDIR)

        elif t in self.statements:
            return idaapi.COLSTR(string, idaapi.SCOLOR_LOCNAME)

        elif t in self.types:
            return idaapi.COLSTR(string, idaapi.SCOLOR_IMPNAME)

        else:
            return string

    def as_string(self, string):
        """Display the specified text as a string."""
        return idaapi.COLSTR(string, idaapi.SCOLOR_CHAR)

    def as_number(self, string):
        """Display the specified text as a number."""
        return idaapi.COLSTR(string, idaapi.SCOLOR_NUMBER)

    def as_directive(self, string):
        """Display the specified text as a directive."""
        return idaapi.COLSTR(string, idaapi.SCOLOR_KEYWORD)

    def as_default(self, string):
        """Display the specified text as a default text."""
        return idaapi.COLSTR(string, idaapi.SCOLOR_DEFAULT)

    def as_variable_name(self, string):
        """Display the specified text as a variable name."""
        return idaapi.COLSTR(string, idaapi.SCOLOR_REG)

    def as_function_name(self, string):
        """Display the specified text as a function name."""
        return idaapi.COLSTR(string, idaapi.SCOLOR_CNAME)

    def get_colour(self, address):
        """Return the items colour."""
        return idaapi.get_item_color(address)

    def set_colour(self, address, colour):
        """Store an item colour."""
        idaapi.set_item_color(address, colour)
