from llvmpy import _api, capsule

class Model:
    _llvm_type_ = "llvm::Reloc::Model"
    Default = _api.llvm.Reloc.Default()
    Static = _api.llvm.Reloc.Static()
    PIC_ = _api.llvm.Reloc.PIC_()
    DynamicNoPIC = _api.llvm.Reloc.DynamicNoPIC()

