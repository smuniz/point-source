from llvmpy import _api, capsule

class Model:
    _llvm_type_ = "llvm::CodeModel::Model"
    Default = _api.llvm.CodeModel.Default()
    JITDefault = _api.llvm.CodeModel.JITDefault()
    Small = _api.llvm.CodeModel.Small()
    Kernel = _api.llvm.CodeModel.Kernel()
    Medium = _api.llvm.CodeModel.Medium()
    Large = _api.llvm.CodeModel.Large()

