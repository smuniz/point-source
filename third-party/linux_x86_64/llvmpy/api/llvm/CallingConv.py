from llvmpy import _api, capsule

class ID:
    _llvm_type_ = "llvm::CallingConv::ID"
    C = _api.llvm.CallingConv.C()
    Fast = _api.llvm.CallingConv.Fast()
    Cold = _api.llvm.CallingConv.Cold()
    GHC = _api.llvm.CallingConv.GHC()
    FirstTargetCC = _api.llvm.CallingConv.FirstTargetCC()
    X86_StdCall = _api.llvm.CallingConv.X86_StdCall()
    X86_FastCall = _api.llvm.CallingConv.X86_FastCall()
    ARM_APCS = _api.llvm.CallingConv.ARM_APCS()
    ARM_AAPCS = _api.llvm.CallingConv.ARM_AAPCS()
    ARM_AAPCS_VFP = _api.llvm.CallingConv.ARM_AAPCS_VFP()
    MSP430_INTR = _api.llvm.CallingConv.MSP430_INTR()
    X86_ThisCall = _api.llvm.CallingConv.X86_ThisCall()
    PTX_Kernel = _api.llvm.CallingConv.PTX_Kernel()
    PTX_Device = _api.llvm.CallingConv.PTX_Device()
    MBLAZE_INTR = _api.llvm.CallingConv.MBLAZE_INTR()
    MBLAZE_SVOL = _api.llvm.CallingConv.MBLAZE_SVOL()
    SPIR_FUNC = _api.llvm.CallingConv.SPIR_FUNC()
    SPIR_KERNEL = _api.llvm.CallingConv.SPIR_KERNEL()
    Intel_OCL_BI = _api.llvm.CallingConv.Intel_OCL_BI()

