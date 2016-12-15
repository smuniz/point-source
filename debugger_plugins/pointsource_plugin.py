#!/usr/bin/env python
# 
# Copyright (c) 2017 Sebastian Muniz
# 
# This code is part of point source decompiler
#

from sys import path as sys_path, exit, stdout
from inspect import getfile, currentframe
from os import path
from traceback import format_exc

#
# Add path to system paths.
#
#current_filename = getfile(currentframe())
#print "-----> %s" % current_filename
#path_to_current_module = os.path.realpath(os.path.dirname(current_filename))
path_to_current_module = r"z:\home\oem\projects\decompiler\point-source.git"

if path_to_current_module not in sys_path:
    print "[+] Fixing Python modules path..."
    sys_path.append(path_to_current_module)

#print "-----> %s" % path_to_current_module

import idaapi

from pointsource import PointSource, PointSourceException

__description__ = "Point Source Decompiler plugin"
__version__ = "0.1"


class PointSourcePlugin(idaapi.plugin_t):
    flags = idaapi.PLUGIN_UNL
    comment = "Point source C decompiler"

    help = "Point source C decompiler help"
    wanted_name = "Point source decompiler"
    wanted_hotkey = ""

    DECOMPILE_HOTKEY = "Alt-F5"

    def init(self):
        """Initialize the plugin."""
        # Set debugging flag during development
        self.debug = True

        self.print_banner()
        try:
            #
            # Initializing decompiler in order to know if the current
            # architecture is supported or not.
            #
            self.decompiler = PointSource()

            #
            # Registering shortcuts.
            #
            new_menu = idaapi.add_menu_item("Edit/Plugins", "-", None, 0, self.do_nothing, ())
            if not new_menu:
                #print "[-] Unable to add menu separator."
                del new_menu
            new_menu = idaapi.add_menu_item("Edit/Plugins", "PointSource : Decompile function", self.DECOMPILE_HOTKEY, 0, self.decompile_function, ())
            if not new_menu:
                #print "[-] Unable to add menu item."
                del new_menu
            
            new_hotkey = idaapi.add_hotkey(self.DECOMPILE_HOTKEY, self.decompile_function)
            if not new_hotkey:
                #print "[-] Unable to add hotkey."
                del new_hotkey

            # Remain in memory because this is a supported architecture and
            # we'll get some work to do.
            return idaapi.PLUGIN_KEEP

        except PointSourceException, err:
            print "[-] Unable to initialize decompiler : %s" % err

        # This architecture is unsupported so we unload ourselves and leave.
        return idaapi.PLUGIN_UNL

    def run(self, argument):
        """Execute the script when invoked."""
        try:
            # Remove the modal dialogue 
            old = idaapi.disable_script_timeout()

            idaapi.show_wait_box("Decompiling function...")

            self.decompiler.set_screen_address_to_decompile()
            self.decompiler.decompile()

            # Re-enable the original timeout.
            idaapi.set_script_timeout(old)

        except PointSourceException, err:
            print "[-] Unable to run decompiler : %s" % err

        except Exception, err:
            if self.debug:
                print format_exc()
            print "[-] Exception : %s" % err

    def term(self):
        """Terminate the plugin."""
        print "Terminating plugin : %s" % __description__

    def print_banner(self):
        banner = [
          "%s has been loaded (v%s)" % (__description__, __version__),
          "  The hotkeys are : %s -> decompile" % self.DECOMPILE_HOTKEY,
          "  Additional options available in the Edit/Plugins menu.",
          "  contact Point Source Team on Slack at: point-source.slack.com",
        ]
        sepline = '-' * (max([len(s) for s in banner])+1)

        print(sepline)
        print("\n".join(banner))
        print(sepline)

    def do_nothing(self):
        """Empty stub for blank menu line."""
        pass

    def decompile_function(self):
        """Decompile the function under the cursor."""
        #print "Decompile function at 0x%X" % idaapi.get_screen_ea()
        self.run(0)

def PLUGIN_ENTRY():
    return PointSourcePlugin()
