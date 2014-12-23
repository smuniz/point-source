# 
# Copyright (c) 2014 Sebastian Muniz
# 
# This code is part of point source decompiler
#
from collections import MutableMapping

__all__ = ["SymbolsManager", "SymbolsManagerException"]


class Symbol:
    __slots__ = ["name", "type", "scope"]

    def __init__(self, name, _type, scope):
        self.name = name
        self.type = _type
        self.scope = scope


class SymbolsTable:

    def __init__(self):
        self.vars = dict()

    def __setitem__(self, key, value):
        self.vars[key] = value

    def __getitem__(self, key):
        try:
            return self.vars[key]
        except KeyError, err:
            return None


class SymbolsManagerException(Exception):
    """Generic exception class for symbols manager."""
    pass


class SymbolsManager:
    """Symbol storage for all the module defined symbols found during the
    analysis and also containing user-defined information.

    This class contains multiple symbol tables, one for each function defined
    and also additional tables for global variables.
    """

    def __init__(self):
        self.functions_symbols = dict() # key = address | value = symbol table
        self.global_symbols = dict() # key = address | value = symbol table

    @property
    def globals_symbols(self):
        """Return a dictionary with all the global symbols."""
        return self._globals_symbols

    @globals_symbols.setter
    def globals_symbols(self, tables):
        """Store a dictionary of all the global symbols."""
        self._globals_symbols = tables

    @property
    def functions_symbols(self):
        """Return a dictionary of all the symbols tables ordered by its
        addresses in the binary under analysis.

        """
        return self._functions_symbols

    @functions_symbols.setter
    def functions_symbols(self, tables):
        """Store a dictionary of all the symbols tables."""
        self._functions_symbols = tables

    def symbols(self, address):
        """Return the of symbols for the given address."""
        if type(address) is not int:
            raise SymbolsManagerException(
                "Invalid symbol address specified (%r)" % address)

        return self.functions_symbols.setdefault(address, SymbolsTable())
