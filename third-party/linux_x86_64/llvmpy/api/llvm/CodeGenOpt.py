from llvmpy import _api, capsule

class Level:
    _llvm_type_ = "llvm::CodeGenOpt::Level"
    None_ = getattr(_api.llvm.CodeGenOpt, "None")()
    Less = _api.llvm.CodeGenOpt.Less()
    Default = _api.llvm.CodeGenOpt.Default()
    Aggressive = _api.llvm.CodeGenOpt.Aggressive()

