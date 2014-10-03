from llvmpy import _api, capsule

def getDeclaration(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.Intrinsic.getDeclaration(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

