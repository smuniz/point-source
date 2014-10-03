from llvmpy import _api, capsule

class Model:
    _llvm_type_ = "llvm::TLSModel::Model"
    GeneralDynamic = _api.llvm.TLSModel.GeneralDynamic()
    LocalDynamic = _api.llvm.TLSModel.LocalDynamic()
    InitialExec = _api.llvm.TLSModel.InitialExec()
    LocalExec = _api.llvm.TLSModel.LocalExec()

