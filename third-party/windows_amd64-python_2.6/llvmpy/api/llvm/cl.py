from llvmpy import _api, capsule

def ParseEnvironmentOptions(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.cl.ParseEnvironmentOptions(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

