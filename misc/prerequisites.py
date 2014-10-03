#!/usr/bin/env python
# 
# Copyright (c) 2013 Sebastian Muniz
# 
# This code is part Point Source decompiler.
#

from sys import stdout, modules
#from os import geteuid # Only Linux
from imp import find_module, load_module

from logger.logger import Logger

# Shameless copied from newer idaapi.py to have in in older IDAPython versions.
def require(modulename, package=None):
    """
    Load, or reload a module.

    When under heavy development, a user's tool might consist of multiple
    modules. If those are imported using the standard 'import' mechanism,
    there is no guarantee that the Python implementation will re-read
    and re-evaluate the module's Python code. In fact, it usually doesn't.
    What should be done instead is 'reload()'-ing that module.

    This is a simple helper function that will do just that: In case the
    module doesn't exist, it 'import's it, and if it does exist,
    'reload()'s it.

    For more information, see: <http://www.hexblog.com/?p=749>.
    """
    if modulename in modules.keys():
        reload(modules[modulename])
    else:
        import importlib
        import inspect
        m = importlib.import_module(modulename, package)
        frame_obj, filename, line_number, function_name, lines, index = inspect.stack()[1]
        importer_module = inspect.getmodule(frame_obj)
        if importer_module is None: # No importer module; called from command line
            importer_module = modules['__main__']
        setattr(importer_module, modulename, m)
        modules[modulename] = m

#def is_root():
#    """Indicate if the current user has root/administrative privileges."""
#    return geteuid() == 0

def dependancy_check(dependancy_list):
    """Check every dependancy and inform anyone missing."""
    log  = Logger(stdout)

    # Store missing modules.
    missing_modules = list()

    for dependancy in dependancy_list:
        try:
            find_module(dependancy)
        except ImportError, err:
            # Add the missing module to the return list.
            missing_modules.append(dependancy)

            # Inform the user about the missing module.
            log.critical("Module unavailable : %s (%s)" % \
                (dependancy, dependancy_list[dependancy]))

    return missing_modules


# List of modules required to operate Binary Scope.
dependancy_list = {
    "llvm" : "Python bindings for LLVM",
    }

def run_dependancy_check():
    if len(dependancy_check(dependancy_list)) > 0:
        exit(1)

