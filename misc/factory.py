# 
# Copyright (c) 2017 Sebastian Muniz
# 
# This code is part of point source decompiler
#
__all__ = ["Factory", "FactoryException"]


class FactoryException(Exception):
    """Generic factory base exception class."""
    pass

class Factory(object):
    """
    Factory for different front-ends to support multiple decompilable
    architectures.

    """

    def __init__(self):
        """Perform factory instance initialization."""
        pass

    def register(self, methodName, constructor, *args, **kargs):
        """register a constructor"""
        _args = [constructor]
        _args.extend(args)
        setattr(self, methodName,apply(Functor,_args, kargs))

    def unregister(self, methodName):
        """unregister a constructor"""
        delattr(self, methodName)

    @classmethod
    def build(cls, build_data, params):
        """Return a new instance of the requested object."""
        try:
            method = "create_" + "_".join(["%s" % d for d in build_data])
            return getattr(cls(), method)(*params)
        except AttributeError, err:
            raise FactoryException("Unavailable method %s" % method)


class Functor:
    def __init__(self, function, *args, **kargs):
        assert callable(function), "function should be a callable obj"
        self._function = function
        self._args = args
        self._kargs = kargs

    def __call__(self, *args, **kargs):
        """call function"""
        _args = list(self._args)
        _args.extend(args)
        _kargs = self._kargs.copy()
        _kargs.update(kargs)
        return apply(self._function,_args,_kargs)
