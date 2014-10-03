from llvmpy import _api, capsule

class Kind:
    _llvm_type_ = "llvm::EngineKind::Kind"
    JIT = _api.llvm.EngineKind.JIT()
    Interpreter = _api.llvm.EngineKind.Interpreter()

