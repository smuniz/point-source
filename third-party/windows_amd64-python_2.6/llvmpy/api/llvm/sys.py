from llvmpy import _api, capsule

def isLittleEndianHost(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.sys.isLittleEndianHost(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

def isBigEndianHost(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.sys.isBigEndianHost(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

def getDefaultTargetTriple(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.sys.getDefaultTargetTriple(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

def getHostCPUName(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.sys.getHostCPUName(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

def getHostCPUFeatures(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.sys.getHostCPUFeatures(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

@capsule.register_class("llvm::sys::DynamicLibrary")
class DynamicLibrary(capsule.Wrapper):
    _llvm_type_ = "llvm::sys::DynamicLibrary"
    @staticmethod
    def LoadPermanentLibrary(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.sys.DynamicLibrary.LoadPermanentLibrary(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isValid(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.sys.DynamicLibrary.isValid(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getAddressOfSymbol(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.sys.DynamicLibrary.getAddressOfSymbol(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def SearchForAddressOfSymbol(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.sys.DynamicLibrary.SearchForAddressOfSymbol(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def AddSymbol(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.sys.DynamicLibrary.AddSymbol(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

