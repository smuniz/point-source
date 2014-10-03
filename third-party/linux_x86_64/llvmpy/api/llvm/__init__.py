from llvmpy import _api, capsule
from . import sys
from . import cl
from . import Reloc
from . import CodeModel
from . import TLSModel
from . import CodeGenOpt
from . import LibFunc
from . import CallingConv
from . import EngineKind
from . import Intrinsic

def getGlobalContext(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.getGlobalContext(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

def InitializeNativeTarget(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.InitializeNativeTarget(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

def InitializeNativeTargetAsmPrinter(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.InitializeNativeTargetAsmPrinter(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

def InitializeNativeTargetAsmParser(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.InitializeNativeTargetAsmParser(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

def InitializeNativeTargetDisassembler(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.InitializeNativeTargetDisassembler(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

def ParseAssemblyString(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.ParseAssemblyString(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

def verifyModule(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.verifyModule(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

def verifyFunction(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.verifyFunction(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

def ParseBitCodeFile(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.ParseBitCodeFile(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

def WriteBitcodeToFile(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.WriteBitcodeToFile(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

def getBitcodeTargetTriple(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.getBitcodeTargetTriple(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

def initializeCore(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.initializeCore(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

def initializeScalarOpts(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.initializeScalarOpts(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

def initializeVectorization(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.initializeVectorization(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

def initializeIPO(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.initializeIPO(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

def initializeAnalysis(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.initializeAnalysis(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

def initializeIPA(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.initializeIPA(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

def initializeTransformUtils(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.initializeTransformUtils(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

def initializeInstCombine(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.initializeInstCombine(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

def initializeInstrumentation(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.initializeInstrumentation(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

def initializeTarget(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.initializeTarget(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

def createFunctionInliningPass(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.createFunctionInliningPass(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

def SplitBlockAndInsertIfThen(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.SplitBlockAndInsertIfThen(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

def ReplaceInstWithInst(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.ReplaceInstWithInst(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

def CloneModule(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.CloneModule(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

def InlineFunction(*args):
    unwrapped = list(map(capsule.unwrap, args))
    ret = _api.llvm.InlineFunction(*unwrapped)
    wrapped = capsule.wrap(ret, False)
    return wrapped

@capsule.register_class("llvm::SmallVector<llvm::Type*,8>")
class SmallVector_Type(capsule.Wrapper):
    _llvm_type_ = "llvm::SmallVector<llvm::Type*,8>"
    _delete_ = _api.llvm.SmallVector_Type.delete

@capsule.register_class("llvm::SmallVector<llvm::Value*,8>")
class SmallVector_Value(capsule.Wrapper):
    _llvm_type_ = "llvm::SmallVector<llvm::Value*,8>"
    _delete_ = _api.llvm.SmallVector_Value.delete

@capsule.register_class("llvm::SmallVector<unsigned,8>")
class SmallVector_Unsigned(capsule.Wrapper):
    _llvm_type_ = "llvm::SmallVector<unsigned,8>"
    _delete_ = _api.llvm.SmallVector_Unsigned.delete

@capsule.register_class("llvm::StringRef")
class StringRef(capsule.Wrapper):
    _llvm_type_ = "llvm::StringRef"

@capsule.register_class("llvm::Triple")
class Triple(capsule.Wrapper):
    _llvm_type_ = "llvm::Triple"
    def isEnvironmentMachO(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Triple.isEnvironmentMachO(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isOSDarwin(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Triple.isOSDarwin(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isMacOSXVersionLT(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Triple.isMacOSXVersionLT(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getTriple(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Triple.getTriple(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isOSVersionLT(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Triple.isOSVersionLT(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getOSAndEnvironmentName(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Triple.getOSAndEnvironmentName(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getVendorName(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Triple.getVendorName(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getOSName(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Triple.getOSName(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getEnvironmentName(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Triple.getEnvironmentName(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def new(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Triple.new(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isArch32Bit(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Triple.isArch32Bit(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isOSBinFormatELF(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Triple.isOSBinFormatELF(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def get32BitArchVariant(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Triple.get32BitArchVariant(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isOSCygMing(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Triple.isOSCygMing(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isArch16Bit(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Triple.isArch16Bit(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isMacOSX(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Triple.isMacOSX(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getArchName(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Triple.getArchName(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isOSBinFormatCOFF(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Triple.isOSBinFormatCOFF(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isArch64Bit(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Triple.isArch64Bit(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isOSWindows(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Triple.isOSWindows(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def get64BitArchVariant(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Triple.get64BitArchVariant(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def __str__(self):
        return self.getTriple()

@capsule.register_class("llvm::Module")
class Module(capsule.Wrapper):
    _llvm_type_ = "llvm::Module"
    class Endianness:
        _llvm_type_ = "llvm::Module::Endianness"
        AnyEndianness = _api.llvm.Module.AnyEndianness()
        LittleEndian = _api.llvm.Module.LittleEndian()
        BigEndian = _api.llvm.Module.BigEndian()
    
    class PointerSize:
        _llvm_type_ = "llvm::Module::PointerSize"
        AnyPointerSize = _api.llvm.Module.AnyPointerSize()
        Pointer32 = _api.llvm.Module.Pointer32()
        Pointer64 = _api.llvm.Module.Pointer64()
    
    def getOrInsertGlobal(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Module.getOrInsertGlobal(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def dump(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Module.dump(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getTargetTriple(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Module.getTargetTriple(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setModuleIdentifier(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Module.setModuleIdentifier(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getContext(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Module.getContext(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getTypeByName(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Module.getTypeByName(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getNamedMetadata(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Module.getNamedMetadata(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getNamedGlobal(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Module.getNamedGlobal(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getPointerSize(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Module.getPointerSize(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def appendModuleInlineAsm(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Module.appendModuleInlineAsm(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getModuleInlineAsm(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Module.getModuleInlineAsm(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def eraseNamedMetadata(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Module.eraseNamedMetadata(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def print_(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Module.print_(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getOrInsertFunction(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Module.getOrInsertFunction(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def list_named_metadata(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Module.list_named_metadata(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def list_functions(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Module.list_functions(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def new(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Module.new(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def dropAllReferences(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Module.dropAllReferences(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getGlobalVariable(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Module.getGlobalVariable(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setDataLayout(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Module.setDataLayout(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def list_globals(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Module.list_globals(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setModuleInlineAsm(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Module.setModuleInlineAsm(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getFunction(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Module.getFunction(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getOrInsertNamedMetadata(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Module.getOrInsertNamedMetadata(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getEndianness(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Module.getEndianness(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getDataLayout(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Module.getDataLayout(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setTargetTriple(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Module.setTargetTriple(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getModuleIdentifier(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Module.getModuleIdentifier(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    _delete_ = _api.llvm.Module.delete
    def __str__(self):
        from llvmpy import extra
        os = extra.make_raw_ostream_for_printing()
        self.print_(os, None)
        return os.str()

@capsule.register_class("llvm::LLVMContext")
class LLVMContext(capsule.Wrapper):
    _llvm_type_ = "llvm::LLVMContext"

@capsule.register_class("llvm::Value")
class Value(capsule.Wrapper):
    _llvm_type_ = "llvm::Value"
    class ValueTy:
        _llvm_type_ = "llvm::Value::ValueTy"
        ArgumentVal = _api.llvm.Value.ArgumentVal()
        BasicBlockVal = _api.llvm.Value.BasicBlockVal()
        FunctionVal = _api.llvm.Value.FunctionVal()
        GlobalAliasVal = _api.llvm.Value.GlobalAliasVal()
        GlobalVariableVal = _api.llvm.Value.GlobalVariableVal()
        UndefValueVal = _api.llvm.Value.UndefValueVal()
        BlockAddressVal = _api.llvm.Value.BlockAddressVal()
        ConstantExprVal = _api.llvm.Value.ConstantExprVal()
        ConstantAggregateZeroVal = _api.llvm.Value.ConstantAggregateZeroVal()
        ConstantDataArrayVal = _api.llvm.Value.ConstantDataArrayVal()
        ConstantDataVectorVal = _api.llvm.Value.ConstantDataVectorVal()
        ConstantIntVal = _api.llvm.Value.ConstantIntVal()
        ConstantFPVal = _api.llvm.Value.ConstantFPVal()
        ConstantArrayVal = _api.llvm.Value.ConstantArrayVal()
        ConstantStructVal = _api.llvm.Value.ConstantStructVal()
        ConstantVectorVal = _api.llvm.Value.ConstantVectorVal()
        ConstantPointerNullVal = _api.llvm.Value.ConstantPointerNullVal()
        MDNodeVal = _api.llvm.Value.MDNodeVal()
        MDStringVal = _api.llvm.Value.MDStringVal()
        InlineAsmVal = _api.llvm.Value.InlineAsmVal()
        PseudoSourceValueVal = _api.llvm.Value.PseudoSourceValueVal()
        FixedStackPseudoSourceValueVal = _api.llvm.Value.FixedStackPseudoSourceValueVal()
        InstructionVal = _api.llvm.Value.InstructionVal()
        ConstantFirstVal = _api.llvm.Value.ConstantFirstVal()
        ConstantLastVal = _api.llvm.Value.ConstantLastVal()
    
    def replaceAllUsesWith(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Value.replaceAllUsesWith(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setName(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Value.setName(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def dump(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Value.dump(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getName(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Value.getName(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getType(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Value.getType(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def print_(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Value.print_(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getContext(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Value.getContext(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getNumUses(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Value.getNumUses(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def list_use(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Value.list_use(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def hasNUses(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Value.hasNUses(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def hasOneUse(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Value.hasOneUse(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getValueID(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Value.getValueID(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def mutateType(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Value.mutateType(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isUsedInBasicBlock(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Value.isUsedInBasicBlock(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def hasName(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Value.hasName(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def __str__(self):
        from llvmpy import extra
        os = extra.make_raw_ostream_for_printing()
        self.print_(os, None)
        return os.str()

@capsule.register_class("llvm::Argument")
class Argument(Value):
    _llvm_type_ = "llvm::Argument"
    def hasStructRetAttr(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Argument.hasStructRetAttr(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def addAttr(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Argument.addAttr(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def hasNoAliasAttr(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Argument.hasNoAliasAttr(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def hasByValAttr(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Argument.hasByValAttr(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def hasNestAttr(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Argument.hasNestAttr(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getParamAlignment(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Argument.getParamAlignment(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def removeAttr(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Argument.removeAttr(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def hasNoCaptureAttr(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Argument.hasNoCaptureAttr(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getArgNo(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Argument.getArgNo(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::MDNode")
class MDNode(Value):
    _llvm_type_ = "llvm::MDNode"
    def replaceOperandWith(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.MDNode.replaceOperandWith(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isFunctionLocal(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.MDNode.isFunctionLocal(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getFunction(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.MDNode.getFunction(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def get(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.MDNode.get(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getOperand(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.MDNode.getOperand(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getNumOperands(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.MDNode.getNumOperands(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::MDString")
class MDString(Value):
    _llvm_type_ = "llvm::MDString"
    def getString(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.MDString.getString(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def get(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.MDString.get(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getLength(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.MDString.getLength(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::User")
class User(Value):
    _llvm_type_ = "llvm::User"
    def getOperand(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.User.getOperand(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setOperand(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.User.setOperand(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getNumOperands(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.User.getNumOperands(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::BasicBlock")
class BasicBlock(Value):
    _llvm_type_ = "llvm::BasicBlock"
    def isLandingPad(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.BasicBlock.isLandingPad(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def dropAllReferences(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.BasicBlock.dropAllReferences(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getParent(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.BasicBlock.getParent(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getInstList(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.BasicBlock.getInstList(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def Create(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.BasicBlock.Create(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def removePredecessor(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.BasicBlock.removePredecessor(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getTerminator(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.BasicBlock.getTerminator(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def splitBasicBlock(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.BasicBlock.splitBasicBlock(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def eraseFromParent(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.BasicBlock.eraseFromParent(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def empty(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.BasicBlock.empty(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::ValueSymbolTable")
class ValueSymbolTable(capsule.Wrapper):
    _llvm_type_ = "llvm::ValueSymbolTable"
    def dump(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ValueSymbolTable.dump(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def lookup(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ValueSymbolTable.lookup(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def new(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ValueSymbolTable.new(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def size(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ValueSymbolTable.size(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def empty(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ValueSymbolTable.empty(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    _delete_ = _api.llvm.ValueSymbolTable.delete

@capsule.register_class("llvm::Constant")
class Constant(User):
    _llvm_type_ = "llvm::Constant"
    def isNegativeZeroValue(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Constant.isNegativeZeroValue(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def canTrap(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Constant.canTrap(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isNullValue(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Constant.isNullValue(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def _getAggregateElement_by_int(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Constant._getAggregateElement_by_int(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isConstantUsed(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Constant.isConstantUsed(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getNullValue(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Constant.getNullValue(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def _getAggregateElement_by_const(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Constant._getAggregateElement_by_const(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getIntegerValue(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Constant.getIntegerValue(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getAllOnesValue(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Constant.getAllOnesValue(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isThreadDependent(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Constant.isThreadDependent(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isAllOnesValue(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Constant.isAllOnesValue(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def removeDeadConstantUsers(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Constant.removeDeadConstantUsers(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getAggregateElement(self, elt):
        if isinstance(elt, Constant):
            return self._getAggregateElement_by_const(elt)
        else:
            return self._getAggregateElement_by_int(elt)

@capsule.register_class("llvm::GlobalValue")
class GlobalValue(Constant):
    _llvm_type_ = "llvm::GlobalValue"
    class LinkageTypes:
        _llvm_type_ = "llvm::GlobalValue::LinkageTypes"
        ExternalLinkage = _api.llvm.GlobalValue.ExternalLinkage()
        AvailableExternallyLinkage = _api.llvm.GlobalValue.AvailableExternallyLinkage()
        LinkOnceAnyLinkage = _api.llvm.GlobalValue.LinkOnceAnyLinkage()
        LinkOnceODRLinkage = _api.llvm.GlobalValue.LinkOnceODRLinkage()
        LinkOnceODRAutoHideLinkage = _api.llvm.GlobalValue.LinkOnceODRAutoHideLinkage()
        WeakAnyLinkage = _api.llvm.GlobalValue.WeakAnyLinkage()
        WeakODRLinkage = _api.llvm.GlobalValue.WeakODRLinkage()
        AppendingLinkage = _api.llvm.GlobalValue.AppendingLinkage()
        InternalLinkage = _api.llvm.GlobalValue.InternalLinkage()
        PrivateLinkage = _api.llvm.GlobalValue.PrivateLinkage()
        LinkerPrivateLinkage = _api.llvm.GlobalValue.LinkerPrivateLinkage()
        LinkerPrivateWeakLinkage = _api.llvm.GlobalValue.LinkerPrivateWeakLinkage()
        DLLImportLinkage = _api.llvm.GlobalValue.DLLImportLinkage()
        DLLExportLinkage = _api.llvm.GlobalValue.DLLExportLinkage()
        ExternalWeakLinkage = _api.llvm.GlobalValue.ExternalWeakLinkage()
        CommonLinkage = _api.llvm.GlobalValue.CommonLinkage()
    
    class VisibilityTypes:
        _llvm_type_ = "llvm::GlobalValue::VisibilityTypes"
        DefaultVisibility = _api.llvm.GlobalValue.DefaultVisibility()
        HiddenVisibility = _api.llvm.GlobalValue.HiddenVisibility()
        ProtectedVisibility = _api.llvm.GlobalValue.ProtectedVisibility()
    
    def setSection(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GlobalValue.setSection(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getAlignment(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GlobalValue.getAlignment(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isDeclaration(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GlobalValue.isDeclaration(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def eraseFromParent(self, *args):
        unwrapped = capsule.unwrap(self)
        capsule.release_ownership(unwrapped)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GlobalValue.eraseFromParent(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isDiscardableIfUnused(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GlobalValue.isDiscardableIfUnused(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getSection(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GlobalValue.getSection(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setVisibility(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GlobalValue.setVisibility(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def hasSection(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GlobalValue.hasSection(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def destroyConstant(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GlobalValue.destroyConstant(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setLinkage(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GlobalValue.setLinkage(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getLinkage(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GlobalValue.getLinkage(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def removeFromParent(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GlobalValue.removeFromParent(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isWeakForLinker(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GlobalValue.isWeakForLinker(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def copyAttributesFrom(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GlobalValue.copyAttributesFrom(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getParent(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GlobalValue.getParent(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, True)
        return wrapped
        
    def setAlignment(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GlobalValue.setAlignment(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getVisibility(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GlobalValue.getVisibility(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def mayBeOverridden(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GlobalValue.mayBeOverridden(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::Function")
class Function(GlobalValue):
    _llvm_type_ = "llvm::Function"
    def doesNotAccessMemory(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.doesNotAccessMemory(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getBasicBlockList(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.getBasicBlockList(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def Create(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.Create(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def doesNotThrow(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.doesNotThrow(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getArgumentList(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.getArgumentList(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getContext(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.getContext(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def doesNotReturn(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.doesNotReturn(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def eraseFromParent(self, *args):
        unwrapped = capsule.unwrap(self)
        capsule.release_ownership(unwrapped)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.eraseFromParent(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setDoesNotAccessMemory(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.setDoesNotAccessMemory(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def viewCFGOnly(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.viewCFGOnly(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getGC(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.getGC(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getEntryBlock(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.getEntryBlock(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getReturnType(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.getReturnType(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setOnlyReadsMemory(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.setOnlyReadsMemory(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def onlyReadsMemory(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.onlyReadsMemory(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setCallingConv(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.setCallingConv(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isIntrinsic(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.isIntrinsic(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setDoesNotThrow(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.setDoesNotThrow(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def removeFnAttr(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.removeFnAttr(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getValueSymbolTable(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.getValueSymbolTable(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def hasGC(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.hasGC(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def addFnAttr(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.addFnAttr(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getCallingConv(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.getCallingConv(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setGC(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.setGC(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getIntrinsicID(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.getIntrinsicID(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def copyAttributesFrom(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.copyAttributesFrom(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isVarArg(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.isVarArg(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getFunctionType(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.getFunctionType(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setDoesNotReturn(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.setDoesNotReturn(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def viewCFG(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.viewCFG(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def deleteBody(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Function.deleteBody(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::UndefValue")
class UndefValue(Constant):
    _llvm_type_ = "llvm::UndefValue"
    def _getElementValue_by_const(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.UndefValue._getElementValue_by_const(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getStructElement(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.UndefValue.getStructElement(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def get(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.UndefValue.get(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def destroyConstant(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.UndefValue.destroyConstant(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def _getElementValue_by_int(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.UndefValue._getElementValue_by_int(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getSequentialElement(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.UndefValue.getSequentialElement(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getElementValue(self, idx):
        if isinstance(idx, Constant):
            return self._getElementValue_by_const(idx)
        else:
            return self._getElementValue_by_int(idx)

@capsule.register_class("llvm::ConstantInt")
class ConstantInt(Constant):
    _llvm_type_ = "llvm::ConstantInt"
    @staticmethod
    def isValueValidForType(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantInt.isValueValidForType(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def get(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantInt.get(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getSExtValue(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantInt.getSExtValue(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getZExtValue(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantInt.getZExtValue(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::ConstantFP")
class ConstantFP(Constant):
    _llvm_type_ = "llvm::ConstantFP"
    @staticmethod
    def get(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantFP.get(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isNegative(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantFP.isNegative(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isNaN(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantFP.isNaN(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getNegativeZero(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantFP.getNegativeZero(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isZero(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantFP.isZero(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getInfinity(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantFP.getInfinity(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::ConstantArray")
class ConstantArray(Constant):
    _llvm_type_ = "llvm::ConstantArray"
    @staticmethod
    def get(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantArray.get(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::ConstantStruct")
class ConstantStruct(Constant):
    _llvm_type_ = "llvm::ConstantStruct"
    @staticmethod
    def getAnon(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantStruct.getAnon(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def get(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantStruct.get(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::ConstantVector")
class ConstantVector(Constant):
    _llvm_type_ = "llvm::ConstantVector"
    @staticmethod
    def get(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantVector.get(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::ConstantDataSequential")
class ConstantDataSequential(Constant):
    _llvm_type_ = "llvm::ConstantDataSequential"

@capsule.register_class("llvm::ConstantDataArray")
class ConstantDataArray(ConstantDataSequential):
    _llvm_type_ = "llvm::ConstantDataArray"
    @staticmethod
    def getString(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantDataArray.getString(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::ConstantExpr")
class ConstantExpr(Constant):
    _llvm_type_ = "llvm::ConstantExpr"
    @staticmethod
    def getCompare(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getCompare(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getFDiv(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getFDiv(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getNeg(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getNeg(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getNot(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getNot(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getAlignOf(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getAlignOf(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getFMul(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getFMul(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def _getGEP(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr._getGEP(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getIntToPtr(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getIntToPtr(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getFSub(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getFSub(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getTrunc(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getTrunc(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getSDiv(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getSDiv(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getFPToSI(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getFPToSI(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isCast(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.isCast(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getFNeg(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getFNeg(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getSExt(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getSExt(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getInsertElement(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getInsertElement(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getIntegerCast(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getIntegerCast(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getFRem(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getFRem(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getAdd(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getAdd(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getUIToFP(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getUIToFP(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getSizeOf(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getSizeOf(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getSRem(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getSRem(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getZExt(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getZExt(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getOffsetOf(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getOffsetOf(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getPtrToInt(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getPtrToInt(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getAnd(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getAnd(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getUDiv(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getUDiv(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getOr(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getOr(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getSelect(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getSelect(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getPointerCast(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getPointerCast(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getLShr(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getLShr(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getMul(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getMul(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getFPCast(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getFPCast(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def _getExtractValue(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr._getExtractValue(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getXor(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getXor(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getFAdd(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getFAdd(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isCompare(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.isCompare(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getSIToFP(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getSIToFP(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isGEPWithNoNotionalOverIndexing(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.isGEPWithNoNotionalOverIndexing(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getFPTrunc(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getFPTrunc(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getFCmp(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getFCmp(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getSub(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getSub(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getOpcodeName(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getOpcodeName(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getURem(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getURem(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getFPExtend(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getFPExtend(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getICmp(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getICmp(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def _getInsertValue(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr._getInsertValue(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getOpcode(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getOpcode(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getBitCast(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getBitCast(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getShl(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getShl(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getShuffleVector(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getShuffleVector(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getAShr(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getAShr(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getExtractElement(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getExtractElement(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def hasIndices(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.hasIndices(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getFPToUI(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ConstantExpr.getFPToUI(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getExtractValue(*args):
        from llvmpy import extra
        args = list(args)
        valuelist = args[1]
        args[1] = extra.make_small_vector_from_unsigned(*valuelist)
        return ConstantExpr._getExtractValue(*args)
    @staticmethod
    def getInsertValue(*args):
        from llvmpy import extra
        args = list(args)
        valuelist = args[2]
        args[1] = extra.make_small_vector_from_unsigned(*valuelist)
        return ConstantExpr._getInsertValue(*args)
    @staticmethod
    def getGetElementPtr(*args):
        from llvmpy import extra
        args = list(args)
        valuelist = args[1]
        args[1] = extra.make_small_vector_from_values(*valuelist)
        return ConstantExpr._getGEP(*args)

@capsule.register_class("llvm::raw_ostream")
class raw_ostream(capsule.Wrapper):
    _llvm_type_ = "llvm::raw_ostream"
    def flush(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.raw_ostream.flush(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    _delete_ = _api.llvm.raw_ostream.delete

@capsule.register_class("llvm::raw_svector_ostream")
class raw_svector_ostream(raw_ostream):
    _llvm_type_ = "llvm::raw_svector_ostream"
    def bytes(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.raw_svector_ostream.bytes(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def str(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.raw_svector_ostream.str(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::formatted_raw_ostream")
class formatted_raw_ostream(raw_ostream):
    _llvm_type_ = "llvm::formatted_raw_ostream"
    @staticmethod
    def _new(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.formatted_raw_ostream._new(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def new(stream, destroy=False):
        inst = formatted_raw_ostream._new(stream, destroy)
        inst.__underlying_stream = stream # to prevent it being freed first
        return inst

@capsule.register_class("llvm::SMDiagnostic")
class SMDiagnostic(capsule.Wrapper):
    _llvm_type_ = "llvm::SMDiagnostic"
    @staticmethod
    def new(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.SMDiagnostic.new(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    _delete_ = _api.llvm.SMDiagnostic.delete

@capsule.register_class("llvm::Target")
class Target(capsule.Wrapper):
    _llvm_type_ = "llvm::Target"
    def getNext(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Target.getNext(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def createTargetMachine(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Target.createTargetMachine(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def hasMCDisassembler(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Target.hasMCDisassembler(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def hasMCObjectStreamer(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Target.hasMCObjectStreamer(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def hasAsmStreamer(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Target.hasAsmStreamer(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getName(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Target.getName(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getShortDescription(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Target.getShortDescription(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def hasMCAsmBackend(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Target.hasMCAsmBackend(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def hasMCInstPrinter(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Target.hasMCInstPrinter(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def hasMCAsmParser(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Target.hasMCAsmParser(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def hasMCCodeEmitter(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Target.hasMCCodeEmitter(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def hasAsmPrinter(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Target.hasAsmPrinter(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def hasTargetMachine(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Target.hasTargetMachine(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def hasJIT(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Target.hasJIT(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::TargetRegistry")
class TargetRegistry(capsule.Wrapper):
    _llvm_type_ = "llvm::TargetRegistry"
    @staticmethod
    def lookupTarget(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.TargetRegistry.lookupTarget(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getClosestTargetForJIT(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.TargetRegistry.getClosestTargetForJIT(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def printRegisteredTargetsForVersion(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.TargetRegistry.printRegisteredTargetsForVersion(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::Pass")
class Pass(capsule.Wrapper):
    _llvm_type_ = "llvm::Pass"
    def dump(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Pass.dump(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getPassName(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Pass.getPassName(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    _delete_ = _api.llvm.Pass.delete

@capsule.register_class("llvm::ModulePass")
class ModulePass(Pass):
    _llvm_type_ = "llvm::ModulePass"
    def runOnModule(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ModulePass.runOnModule(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::FunctionPass")
class FunctionPass(Pass):
    _llvm_type_ = "llvm::FunctionPass"
    def doFinalization(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.FunctionPass.doFinalization(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def doInitialization(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.FunctionPass.doInitialization(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::ImmutablePass")
class ImmutablePass(ModulePass):
    _llvm_type_ = "llvm::ImmutablePass"

@capsule.register_class("llvm::TargetLibraryInfo")
class TargetLibraryInfo(ImmutablePass):
    _llvm_type_ = "llvm::TargetLibraryInfo"
    def setUnavailable(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.TargetLibraryInfo.setUnavailable(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setAvailable(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.TargetLibraryInfo.setAvailable(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def disableAllFunctions(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.TargetLibraryInfo.disableAllFunctions(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getName(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.TargetLibraryInfo.getName(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def new(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.TargetLibraryInfo.new(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def has(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.TargetLibraryInfo.has(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setAvailableWithName(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.TargetLibraryInfo.setAvailableWithName(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def hasOptimizedCodeGen(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.TargetLibraryInfo.hasOptimizedCodeGen(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    _delete_ = _api.llvm.TargetLibraryInfo.delete

@capsule.register_class("llvm::TargetMachine")
class TargetMachine(capsule.Wrapper):
    _llvm_type_ = "llvm::TargetMachine"
    class CodeGenFileType:
        _llvm_type_ = "llvm::TargetMachine::CodeGenFileType"
        CGFT_AssemblyFile = _api.llvm.TargetMachine.CGFT_AssemblyFile()
        CGFT_ObjectFile = _api.llvm.TargetMachine.CGFT_ObjectFile()
        CGFT_Null = _api.llvm.TargetMachine.CGFT_Null()
    
    def getCodeModel(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.TargetMachine.getCodeModel(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getScalarTargetTransformInfo(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.TargetMachine.getScalarTargetTransformInfo(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, True)
        return wrapped
        
    def getTargetTriple(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.TargetMachine.getTargetTriple(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setMCUseDwarfDirectory(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.TargetMachine.setMCUseDwarfDirectory(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getOptLevel(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.TargetMachine.getOptLevel(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getTLSModel(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.TargetMachine.getTLSModel(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getTarget(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.TargetMachine.getTarget(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getTargetCPU(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.TargetMachine.getTargetCPU(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getDataLayout(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.TargetMachine.getDataLayout(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, True)
        return wrapped
        
    def hasMCUseDwarfDirectory(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.TargetMachine.hasMCUseDwarfDirectory(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getTargetFeatureString(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.TargetMachine.getTargetFeatureString(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def addPassesToEmitFile(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.TargetMachine.addPassesToEmitFile(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getRelocationModel(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.TargetMachine.getRelocationModel(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getVectorTargetTransformInfo(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.TargetMachine.getVectorTargetTransformInfo(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, True)
        return wrapped
        
    _delete_ = _api.llvm.TargetMachine.delete

@capsule.register_class("llvm::DataLayout")
class DataLayout(ImmutablePass):
    _llvm_type_ = "llvm::DataLayout"
    def getPointerPrefAlignment(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.DataLayout.getPointerPrefAlignment(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getTypeSizeInBits(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.DataLayout.getTypeSizeInBits(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getCallFrameTypeAlignment(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.DataLayout.getCallFrameTypeAlignment(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getPointerSizeInBits(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.DataLayout.getPointerSizeInBits(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getABIIntegerTypeAlignment(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.DataLayout.getABIIntegerTypeAlignment(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getPointerSize(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.DataLayout.getPointerSize(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isLegalInteger(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.DataLayout.isLegalInteger(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getStringRepresentation(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.DataLayout.getStringRepresentation(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getPreferredTypeAlignmentShift(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.DataLayout.getPreferredTypeAlignmentShift(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getTypeAllocSizeInBits(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.DataLayout.getTypeAllocSizeInBits(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def _new_module(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.DataLayout._new_module(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isLittleEndian(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.DataLayout.isLittleEndian(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isBigEndian(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.DataLayout.isBigEndian(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def _getIndexedOffset(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.DataLayout._getIndexedOffset(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def _getIntPtrType(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.DataLayout._getIntPtrType(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getPreferredAlignment(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.DataLayout.getPreferredAlignment(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getTypeStoreSize(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.DataLayout.getTypeStoreSize(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getTypeStoreSizeInBits(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.DataLayout.getTypeStoreSizeInBits(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getPrefTypeAlignment(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.DataLayout.getPrefTypeAlignment(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getPreferredAlignmentLog(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.DataLayout.getPreferredAlignmentLog(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isIllegalInteger(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.DataLayout.isIllegalInteger(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def _getIntPtrType2(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.DataLayout._getIntPtrType2(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def _new_string(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.DataLayout._new_string(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def fitsInLegalInteger(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.DataLayout.fitsInLegalInteger(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getPointerABIAlignment(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.DataLayout.getPointerABIAlignment(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getStructLayout(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.DataLayout.getStructLayout(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getTypeAllocSize(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.DataLayout.getTypeAllocSize(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def exceedsNaturalStackAlignment(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.DataLayout.exceedsNaturalStackAlignment(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getABITypeAlignment(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.DataLayout.getABITypeAlignment(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def __str__(self):
        return self.getStringRepresentation()
    def getIndexedOffset(self, *args):
        from llvmpy import extra
        args = list(args)
        args[1] = extra.make_small_vector_from_values(args[1])
        return self.getIndexedOffset(*args)
    def getIntPtrType(self, *args):
        if isinstance(args[0], LLVMContext):
            return self._getIntPtrType(*args)
        else:
            return self._getIntPtrType(*args)
    @staticmethod
    def new(arg):
        if isinstance(arg, Module):
            return DataLayout._new_module(arg)
        else:
            return DataLayout._new_string(arg)

@capsule.register_class("llvm::StructLayout")
class StructLayout(capsule.Wrapper):
    _llvm_type_ = "llvm::StructLayout"
    def getElementContainingOffset(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.StructLayout.getElementContainingOffset(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getSizeInBytes(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.StructLayout.getSizeInBytes(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getSizeInBits(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.StructLayout.getSizeInBits(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getElementOffset(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.StructLayout.getElementOffset(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getAlignment(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.StructLayout.getAlignment(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getElementOffsetInBits(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.StructLayout.getElementOffsetInBits(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::Type")
class Type(capsule.Wrapper):
    _llvm_type_ = "llvm::Type"
    class TypeID:
        _llvm_type_ = "llvm::Type::TypeID"
        VoidTyID = _api.llvm.Type.VoidTyID()
        HalfTyID = _api.llvm.Type.HalfTyID()
        FloatTyID = _api.llvm.Type.FloatTyID()
        DoubleTyID = _api.llvm.Type.DoubleTyID()
        X86_FP80TyID = _api.llvm.Type.X86_FP80TyID()
        FP128TyID = _api.llvm.Type.FP128TyID()
        PPC_FP128TyID = _api.llvm.Type.PPC_FP128TyID()
        LabelTyID = _api.llvm.Type.LabelTyID()
        MetadataTyID = _api.llvm.Type.MetadataTyID()
        X86_MMXTyID = _api.llvm.Type.X86_MMXTyID()
        IntegerTyID = _api.llvm.Type.IntegerTyID()
        FunctionTyID = _api.llvm.Type.FunctionTyID()
        StructTyID = _api.llvm.Type.StructTyID()
        ArrayTyID = _api.llvm.Type.ArrayTyID()
        PointerTyID = _api.llvm.Type.PointerTyID()
        VectorTyID = _api.llvm.Type.VectorTyID()
        NumTypeIDs = _api.llvm.Type.NumTypeIDs()
        LastPrimitiveTyID = _api.llvm.Type.LastPrimitiveTyID()
        FirstDerivedTyID = _api.llvm.Type.FirstDerivedTyID()
    
    def isFunctionVarArg(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.isFunctionVarArg(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isLabelTy(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.isLabelTy(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getContext(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getContext(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getPointerTo(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getPointerTo(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isHalfTy(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.isHalfTy(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isStructTy(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.isStructTy(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isVoidTy(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.isVoidTy(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getX86_MMXPtrTy(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getX86_MMXPtrTy(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isFloatingPointTy(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.isFloatingPointTy(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getVectorElementType(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getVectorElementType(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isFPOrFPVectorTy(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.isFPOrFPVectorTy(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getLabelTy(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getLabelTy(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isX86_FP80Ty(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.isX86_FP80Ty(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getMetadataTy(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getMetadataTy(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getArrayNumElements(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getArrayNumElements(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getStructNumElements(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getStructNumElements(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getX86_MMXTy(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getX86_MMXTy(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getInt1PtrTy(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getInt1PtrTy(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isPointerTy(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.isPointerTy(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def dump(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.dump(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getInt8Ty(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getInt8Ty(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getIntNTy(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getIntNTy(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getVoidTy(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getVoidTy(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isPPC_FP128Ty(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.isPPC_FP128Ty(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getIntegerBitWidth(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getIntegerBitWidth(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isMetadataTy(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.isMetadataTy(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getX86_FP80Ty(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getX86_FP80Ty(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getPointerAddressSpace(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getPointerAddressSpace(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isIntOrIntVectorTy(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.isIntOrIntVectorTy(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isVectorTy(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.isVectorTy(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getInt16Ty(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getInt16Ty(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getInt32PtrTy(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getInt32PtrTy(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getFloatTy(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getFloatTy(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isIntegerTy(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.isIntegerTy(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getDoublePtrTy(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getDoublePtrTy(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getContainedType(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getContainedType(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isDoubleTy(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.isDoubleTy(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getFP128PtrTy(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getFP128PtrTy(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getTypeID(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getTypeID(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getFP128Ty(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getFP128Ty(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getX86_FP80PtrTy(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getX86_FP80PtrTy(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def print_(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.print_(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getFunctionNumParams(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getFunctionNumParams(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getSequentialElementType(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getSequentialElementType(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getStructName(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getStructName(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getArrayElementType(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getArrayElementType(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getPPC_FP128PtrTy(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getPPC_FP128PtrTy(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getHalfPtrTy(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getHalfPtrTy(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isSingleValueType(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.isSingleValueType(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getDoubleTy(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getDoubleTy(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getInt16PtrTy(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getInt16PtrTy(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getHalfTy(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getHalfTy(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getPPC_FP128Ty(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getPPC_FP128Ty(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getFunctionParamType(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getFunctionParamType(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isAggregateType(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.isAggregateType(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getIntNPtrTy(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getIntNPtrTy(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getNumContainedTypes(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getNumContainedTypes(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isPtrOrPtrVectorTy(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.isPtrOrPtrVectorTy(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getInt64Ty(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getInt64Ty(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isFloatTy(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.isFloatTy(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isX86_MMXTy(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.isX86_MMXTy(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getInt64PtrTy(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getInt64PtrTy(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isDerivedType(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.isDerivedType(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isEmptyTy(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.isEmptyTy(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getStructElementType(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getStructElementType(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getInt32Ty(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getInt32Ty(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getInt8PtrTy(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getInt8PtrTy(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isFP128Ty(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.isFP128Ty(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isSized(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.isSized(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getVectorNumElements(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getVectorNumElements(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isFunctionTy(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.isFunctionTy(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getFloatPtrTy(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getFloatPtrTy(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isPrimitiveType(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.isPrimitiveType(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getInt1Ty(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getInt1Ty(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getPointerElementType(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.getPointerElementType(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isFirstClassType(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.isFirstClassType(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isArrayTy(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Type.isArrayTy(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def __str__(self):
        from llvmpy import extra
        os = extra.make_raw_ostream_for_printing()
        self.print_(os)
        return os.str()

@capsule.register_class("llvm::IntegerType")
class IntegerType(Type):
    _llvm_type_ = "llvm::IntegerType"

@capsule.register_class("llvm::CompositeType")
class CompositeType(Type):
    _llvm_type_ = "llvm::CompositeType"

@capsule.register_class("llvm::StructType")
class StructType(CompositeType):
    _llvm_type_ = "llvm::StructType"
    @staticmethod
    def isValidElementType(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.StructType.isValidElementType(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setName(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.StructType.setName(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def get(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.StructType.get(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getNumElements(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.StructType.getNumElements(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getName(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.StructType.getName(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isOpaque(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.StructType.isOpaque(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setBody(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.StructType.setBody(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isLiteral(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.StructType.isLiteral(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isLayoutIdentical(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.StructType.isLayoutIdentical(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isPacked(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.StructType.isPacked(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def create(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.StructType.create(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getElementType(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.StructType.getElementType(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def hasName(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.StructType.hasName(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::SequentialType")
class SequentialType(CompositeType):
    _llvm_type_ = "llvm::SequentialType"

@capsule.register_class("llvm::ArrayType")
class ArrayType(SequentialType):
    _llvm_type_ = "llvm::ArrayType"
    @staticmethod
    def isValidElementType(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ArrayType.isValidElementType(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def get(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.ArrayType.get(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getNumElements(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ArrayType.getNumElements(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::PointerType")
class PointerType(SequentialType):
    _llvm_type_ = "llvm::PointerType"
    @staticmethod
    def getUnqual(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.PointerType.getUnqual(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def isValidElementType(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.PointerType.isValidElementType(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def get(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.PointerType.get(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getAddressSpace(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.PointerType.getAddressSpace(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::VectorType")
class VectorType(SequentialType):
    _llvm_type_ = "llvm::VectorType"
    @staticmethod
    def isValidElementType(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.VectorType.isValidElementType(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def get(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.VectorType.get(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getInteger(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.VectorType.getInteger(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getNumElements(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.VectorType.getNumElements(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getTruncatedElementVectorType(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.VectorType.getTruncatedElementVectorType(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def getExtendedElementVectorType(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.VectorType.getExtendedElementVectorType(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getBitWidth(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.VectorType.getBitWidth(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::GlobalVariable")
class GlobalVariable(GlobalValue):
    _llvm_type_ = "llvm::GlobalVariable"
    class ThreadLocalMode:
        _llvm_type_ = "llvm::GlobalVariable::ThreadLocalMode"
        NotThreadLocal = _api.llvm.GlobalVariable.NotThreadLocal()
        GeneralDynamicTLSModel = _api.llvm.GlobalVariable.GeneralDynamicTLSModel()
        LocalDynamicTLSModel = _api.llvm.GlobalVariable.LocalDynamicTLSModel()
        InitialExecTLSModel = _api.llvm.GlobalVariable.InitialExecTLSModel()
        LocalExecTLSModel = _api.llvm.GlobalVariable.LocalExecTLSModel()
    
    def hasDefinitiveInitializer(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GlobalVariable.hasDefinitiveInitializer(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setConstant(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GlobalVariable.setConstant(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setInitializer(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GlobalVariable.setInitializer(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getInitializer(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GlobalVariable.getInitializer(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setThreadLocalMode(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GlobalVariable.setThreadLocalMode(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def hasInitializer(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GlobalVariable.hasInitializer(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isConstant(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GlobalVariable.isConstant(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setThreadLocal(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GlobalVariable.setThreadLocal(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def hasUniqueInitializer(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GlobalVariable.hasUniqueInitializer(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def new(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.GlobalVariable.new(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isThreadLocal(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GlobalVariable.isThreadLocal(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::TargetTransformInfo")
class TargetTransformInfo(ImmutablePass):
    _llvm_type_ = "llvm::TargetTransformInfo"
    @staticmethod
    def new(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.TargetTransformInfo.new(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::ScalarTargetTransformInfo")
class ScalarTargetTransformInfo(capsule.Wrapper):
    _llvm_type_ = "llvm::ScalarTargetTransformInfo"
    _delete_ = _api.llvm.ScalarTargetTransformInfo.delete

@capsule.register_class("llvm::VectorTargetTransformInfo")
class VectorTargetTransformInfo(capsule.Wrapper):
    _llvm_type_ = "llvm::VectorTargetTransformInfo"
    _delete_ = _api.llvm.VectorTargetTransformInfo.delete

@capsule.register_class("llvm::PassManagerBase")
class PassManagerBase(capsule.Wrapper):
    _llvm_type_ = "llvm::PassManagerBase"
    def add(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        if len(unwrapped1) > 0:
            capsule.release_ownership(unwrapped1[0])
        ret = _api.llvm.PassManagerBase.add(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    _delete_ = _api.llvm.PassManagerBase.delete

@capsule.register_class("llvm::PassManager")
class PassManager(PassManagerBase):
    _llvm_type_ = "llvm::PassManager"
    @staticmethod
    def new(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.PassManager.new(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def run(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.PassManager.run(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::FunctionPassManager")
class FunctionPassManager(PassManagerBase):
    _llvm_type_ = "llvm::FunctionPassManager"
    def run(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.FunctionPassManager.run(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def doFinalization(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.FunctionPassManager.doFinalization(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def new(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.FunctionPassManager.new(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def doInitialization(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.FunctionPassManager.doInitialization(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::TargetOptions")
class TargetOptions(capsule.Wrapper):
    _llvm_type_ = "llvm::TargetOptions"
    @staticmethod
    def new(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.TargetOptions.new(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    _delete_ = _api.llvm.TargetOptions.delete

@capsule.register_class("llvm::AssemblyAnnotationWriter")
class AssemblyAnnotationWriter(capsule.Wrapper):
    _llvm_type_ = "llvm::AssemblyAnnotationWriter"

@capsule.register_class("llvm::Instruction")
class Instruction(User):
    _llvm_type_ = "llvm::Instruction"
    def mayThrow(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Instruction.mayThrow(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getMetadata(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Instruction.getMetadata(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isBinaryOp(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Instruction.isBinaryOp(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isAssociative(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Instruction.isAssociative(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isArithmeticShift(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Instruction.isArithmeticShift(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isCast(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Instruction.isCast(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setMetadata(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Instruction.setMetadata(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def eraseFromParent(self, *args):
        unwrapped = capsule.unwrap(self)
        capsule.release_ownership(unwrapped)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Instruction.eraseFromParent(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getPrevNode(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Instruction.getPrevNode(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def hasMetadataOtherThanDebugLoc(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Instruction.hasMetadataOtherThanDebugLoc(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def moveBefore(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Instruction.moveBefore(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getNextNode(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Instruction.getNextNode(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def insertAfter(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Instruction.insertAfter(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isNilpotent(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Instruction.isNilpotent(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isTerminator(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Instruction.isTerminator(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def insertBefore(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Instruction.insertBefore(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def mayReadFromMemory(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Instruction.mayReadFromMemory(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def removeFromParent(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Instruction.removeFromParent(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def clone(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Instruction.clone(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isCommutative(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Instruction.isCommutative(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isShift(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Instruction.isShift(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def hasMetadata(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Instruction.hasMetadata(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getOpcodeName(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Instruction.getOpcodeName(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isIdempotent(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Instruction.isIdempotent(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getParent(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Instruction.getParent(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def mayWriteToMemory(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Instruction.mayWriteToMemory(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getOpcode(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Instruction.getOpcode(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def mayHaveSideEffects(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Instruction.mayHaveSideEffects(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isLogicalShift(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Instruction.isLogicalShift(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def mayReadOrWriteMemory(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Instruction.mayReadOrWriteMemory(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::AtomicCmpXchgInst")
class AtomicCmpXchgInst(Instruction):
    _llvm_type_ = "llvm::AtomicCmpXchgInst"

@capsule.register_class("llvm::AtomicRMWInst")
class AtomicRMWInst(Instruction):
    _llvm_type_ = "llvm::AtomicRMWInst"
    class BinOp:
        _llvm_type_ = "llvm::AtomicRMWInst::BinOp"
        Xchg = _api.llvm.AtomicRMWInst.Xchg()
        Add = _api.llvm.AtomicRMWInst.Add()
        Sub = _api.llvm.AtomicRMWInst.Sub()
        And = _api.llvm.AtomicRMWInst.And()
        Nand = _api.llvm.AtomicRMWInst.Nand()
        Or = _api.llvm.AtomicRMWInst.Or()
        Xor = _api.llvm.AtomicRMWInst.Xor()
        Max = _api.llvm.AtomicRMWInst.Max()
        Min = _api.llvm.AtomicRMWInst.Min()
        UMax = _api.llvm.AtomicRMWInst.UMax()
        UMin = _api.llvm.AtomicRMWInst.UMin()
        FIRST_BINOP = _api.llvm.AtomicRMWInst.FIRST_BINOP()
        LAST_BINOP = _api.llvm.AtomicRMWInst.LAST_BINOP()
        BAD_BINOP = _api.llvm.AtomicRMWInst.BAD_BINOP()
    

@capsule.register_class("llvm::BinaryOperator")
class BinaryOperator(Instruction):
    _llvm_type_ = "llvm::BinaryOperator"

@capsule.register_class("llvm::CallInst")
class CallInst(Instruction):
    _llvm_type_ = "llvm::CallInst"
    def setCallingConv(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.CallInst.setCallingConv(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setArgOperand(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.CallInst.setArgOperand(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setCalledFunction(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.CallInst.setCalledFunction(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def removeAttribute(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.CallInst.removeAttribute(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getCalledValue(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.CallInst.getCalledValue(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getArgOperand(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.CallInst.getArgOperand(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getNumArgOperands(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.CallInst.getNumArgOperands(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def addAttribute(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.CallInst.addAttribute(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getCallingConv(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.CallInst.getCallingConv(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getParamAlignment(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.CallInst.getParamAlignment(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def CreateFree(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.CallInst.CreateFree(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getCalledFunction(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.CallInst.getCalledFunction(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isInlineAsm(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.CallInst.isInlineAsm(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def CreateMalloc(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.CallInst.CreateMalloc(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::CmpInst")
class CmpInst(Instruction):
    _llvm_type_ = "llvm::CmpInst"
    class Predicate:
        _llvm_type_ = "llvm::CmpInst::Predicate"
        FCMP_FALSE = _api.llvm.CmpInst.FCMP_FALSE()
        FCMP_OEQ = _api.llvm.CmpInst.FCMP_OEQ()
        FCMP_OGT = _api.llvm.CmpInst.FCMP_OGT()
        FCMP_OGE = _api.llvm.CmpInst.FCMP_OGE()
        FCMP_OLT = _api.llvm.CmpInst.FCMP_OLT()
        FCMP_OLE = _api.llvm.CmpInst.FCMP_OLE()
        FCMP_ONE = _api.llvm.CmpInst.FCMP_ONE()
        FCMP_ORD = _api.llvm.CmpInst.FCMP_ORD()
        FCMP_UNO = _api.llvm.CmpInst.FCMP_UNO()
        FCMP_UEQ = _api.llvm.CmpInst.FCMP_UEQ()
        FCMP_UGT = _api.llvm.CmpInst.FCMP_UGT()
        FCMP_UGE = _api.llvm.CmpInst.FCMP_UGE()
        FCMP_ULT = _api.llvm.CmpInst.FCMP_ULT()
        FCMP_ULE = _api.llvm.CmpInst.FCMP_ULE()
        FCMP_UNE = _api.llvm.CmpInst.FCMP_UNE()
        FCMP_TRUE = _api.llvm.CmpInst.FCMP_TRUE()
        FIRST_FCMP_PREDICATE = _api.llvm.CmpInst.FIRST_FCMP_PREDICATE()
        LAST_FCMP_PREDICATE = _api.llvm.CmpInst.LAST_FCMP_PREDICATE()
        BAD_FCMP_PREDICATE = _api.llvm.CmpInst.BAD_FCMP_PREDICATE()
        ICMP_EQ = _api.llvm.CmpInst.ICMP_EQ()
        ICMP_NE = _api.llvm.CmpInst.ICMP_NE()
        ICMP_UGT = _api.llvm.CmpInst.ICMP_UGT()
        ICMP_UGE = _api.llvm.CmpInst.ICMP_UGE()
        ICMP_ULT = _api.llvm.CmpInst.ICMP_ULT()
        ICMP_ULE = _api.llvm.CmpInst.ICMP_ULE()
        ICMP_SGT = _api.llvm.CmpInst.ICMP_SGT()
        ICMP_SGE = _api.llvm.CmpInst.ICMP_SGE()
        ICMP_SLT = _api.llvm.CmpInst.ICMP_SLT()
        ICMP_SLE = _api.llvm.CmpInst.ICMP_SLE()
        FIRST_ICMP_PREDICATE = _api.llvm.CmpInst.FIRST_ICMP_PREDICATE()
        LAST_ICMP_PREDICATE = _api.llvm.CmpInst.LAST_ICMP_PREDICATE()
        BAD_ICMP_PREDICATE = _api.llvm.CmpInst.BAD_ICMP_PREDICATE()
    
    def getPredicate(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.CmpInst.getPredicate(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::ExtractElementInst")
class ExtractElementInst(Instruction):
    _llvm_type_ = "llvm::ExtractElementInst"

@capsule.register_class("llvm::FenceInst")
class FenceInst(Instruction):
    _llvm_type_ = "llvm::FenceInst"

@capsule.register_class("llvm::GetElementPtrInst")
class GetElementPtrInst(Instruction):
    _llvm_type_ = "llvm::GetElementPtrInst"

@capsule.register_class("llvm::InsertElementInst")
class InsertElementInst(Instruction):
    _llvm_type_ = "llvm::InsertElementInst"

@capsule.register_class("llvm::InsertValueInst")
class InsertValueInst(Instruction):
    _llvm_type_ = "llvm::InsertValueInst"

@capsule.register_class("llvm::LandingPadInst")
class LandingPadInst(Instruction):
    _llvm_type_ = "llvm::LandingPadInst"

@capsule.register_class("llvm::PHINode")
class PHINode(Instruction):
    _llvm_type_ = "llvm::PHINode"
    def getIncomingBlock(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.PHINode.getIncomingBlock(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getIncomingValue(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.PHINode.getIncomingValue(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def hasConstantValue(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.PHINode.hasConstantValue(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getBasicBlockIndex(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.PHINode.getBasicBlockIndex(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setIncomingBlock(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.PHINode.setIncomingBlock(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def addIncoming(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.PHINode.addIncoming(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getNumIncomingValues(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.PHINode.getNumIncomingValues(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setIncomingValue(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.PHINode.setIncomingValue(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::SelectInst")
class SelectInst(Instruction):
    _llvm_type_ = "llvm::SelectInst"

@capsule.register_class("llvm::ShuffleVectorInst")
class ShuffleVectorInst(Instruction):
    _llvm_type_ = "llvm::ShuffleVectorInst"

@capsule.register_class("llvm::StoreInst")
class StoreInst(Instruction):
    _llvm_type_ = "llvm::StoreInst"
    def isUnordered(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.StoreInst.isUnordered(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getPointerOperand(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.StoreInst.getPointerOperand(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getAlignment(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.StoreInst.getAlignment(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isSimple(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.StoreInst.isSimple(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isAtomic(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.StoreInst.isAtomic(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def classof(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.StoreInst.classof(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isVolatile(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.StoreInst.isVolatile(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getPointerAddressSpace(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.StoreInst.getPointerAddressSpace(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setVolatile(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.StoreInst.setVolatile(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setAtomic(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.StoreInst.setAtomic(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setAlignment(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.StoreInst.setAlignment(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getValueOperand(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.StoreInst.getValueOperand(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::TerminatorInst")
class TerminatorInst(Instruction):
    _llvm_type_ = "llvm::TerminatorInst"
    def getSuccessor(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.TerminatorInst.getSuccessor(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getNumSuccessors(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.TerminatorInst.getNumSuccessors(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setSuccessor(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.TerminatorInst.setSuccessor(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::UnaryInstruction")
class UnaryInstruction(Instruction):
    _llvm_type_ = "llvm::UnaryInstruction"

@capsule.register_class("llvm::IntrinsicInst")
class IntrinsicInst(CallInst):
    _llvm_type_ = "llvm::IntrinsicInst"

@capsule.register_class("llvm::FCmpInst")
class FCmpInst(CmpInst):
    _llvm_type_ = "llvm::FCmpInst"

@capsule.register_class("llvm::ICmpInst")
class ICmpInst(CmpInst):
    _llvm_type_ = "llvm::ICmpInst"

@capsule.register_class("llvm::BranchInst")
class BranchInst(TerminatorInst):
    _llvm_type_ = "llvm::BranchInst"

@capsule.register_class("llvm::IndirectBrInst")
class IndirectBrInst(TerminatorInst):
    _llvm_type_ = "llvm::IndirectBrInst"

@capsule.register_class("llvm::InvokeInst")
class InvokeInst(TerminatorInst):
    _llvm_type_ = "llvm::InvokeInst"
    def setCallingConv(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.InvokeInst.setCallingConv(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setCalledFunction(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.InvokeInst.setCalledFunction(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def removeAttribute(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.InvokeInst.removeAttribute(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getCalledValue(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.InvokeInst.getCalledValue(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def addAttribute(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.InvokeInst.addAttribute(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getCallingConv(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.InvokeInst.getCallingConv(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getParamAlignment(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.InvokeInst.getParamAlignment(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getCalledFunction(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.InvokeInst.getCalledFunction(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::ResumeInst")
class ResumeInst(TerminatorInst):
    _llvm_type_ = "llvm::ResumeInst"

@capsule.register_class("llvm::ReturnInst")
class ReturnInst(TerminatorInst):
    _llvm_type_ = "llvm::ReturnInst"
    def getNumSuccessors(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ReturnInst.getNumSuccessors(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getReturnValue(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ReturnInst.getReturnValue(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::SwitchInst")
class SwitchInst(TerminatorInst):
    _llvm_type_ = "llvm::SwitchInst"
    def setDefaultDest(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.SwitchInst.setDefaultDest(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def addCase(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.SwitchInst.addCase(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getNumCases(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.SwitchInst.getNumCases(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getDefaultDest(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.SwitchInst.getDefaultDest(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getCondition(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.SwitchInst.getCondition(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setCondition(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.SwitchInst.setCondition(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::UnreachableInst")
class UnreachableInst(TerminatorInst):
    _llvm_type_ = "llvm::UnreachableInst"

@capsule.register_class("llvm::AllocaInst")
class AllocaInst(UnaryInstruction):
    _llvm_type_ = "llvm::AllocaInst"
    def isArrayAllocation(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.AllocaInst.isArrayAllocation(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isStaticAlloca(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.AllocaInst.isStaticAlloca(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getAllocatedType(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.AllocaInst.getAllocatedType(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getArraySize(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.AllocaInst.getArraySize(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::CastInst")
class CastInst(UnaryInstruction):
    _llvm_type_ = "llvm::CastInst"

@capsule.register_class("llvm::ExtractValueInst")
class ExtractValueInst(UnaryInstruction):
    _llvm_type_ = "llvm::ExtractValueInst"

@capsule.register_class("llvm::LoadInst")
class LoadInst(UnaryInstruction):
    _llvm_type_ = "llvm::LoadInst"
    def isUnordered(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.LoadInst.isUnordered(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getPointerOperand(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.LoadInst.getPointerOperand(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getAlignment(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.LoadInst.getAlignment(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isSimple(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.LoadInst.isSimple(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isAtomic(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.LoadInst.isAtomic(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def classof(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.LoadInst.classof(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isVolatile(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.LoadInst.isVolatile(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setVolatile(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.LoadInst.setVolatile(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setAtomic(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.LoadInst.setAtomic(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setAlignment(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.LoadInst.setAlignment(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::VAArgInst")
class VAArgInst(UnaryInstruction):
    _llvm_type_ = "llvm::VAArgInst"

@capsule.register_class("llvm::DbgInfoIntrinsic")
class DbgInfoIntrinsic(IntrinsicInst):
    _llvm_type_ = "llvm::DbgInfoIntrinsic"

@capsule.register_class("llvm::MemIntrinsic")
class MemIntrinsic(IntrinsicInst):
    _llvm_type_ = "llvm::MemIntrinsic"

@capsule.register_class("llvm::VACopyInst")
class VACopyInst(IntrinsicInst):
    _llvm_type_ = "llvm::VACopyInst"

@capsule.register_class("llvm::VAEndInst")
class VAEndInst(IntrinsicInst):
    _llvm_type_ = "llvm::VAEndInst"

@capsule.register_class("llvm::VAStartInst")
class VAStartInst(IntrinsicInst):
    _llvm_type_ = "llvm::VAStartInst"

@capsule.register_class("llvm::BitCastInst")
class BitCastInst(CastInst):
    _llvm_type_ = "llvm::BitCastInst"

@capsule.register_class("llvm::FPExtInst")
class FPExtInst(CastInst):
    _llvm_type_ = "llvm::FPExtInst"

@capsule.register_class("llvm::FPToSIInst")
class FPToSIInst(CastInst):
    _llvm_type_ = "llvm::FPToSIInst"

@capsule.register_class("llvm::FPToUIInst")
class FPToUIInst(CastInst):
    _llvm_type_ = "llvm::FPToUIInst"

@capsule.register_class("llvm::FPTruncInst")
class FPTruncInst(CastInst):
    _llvm_type_ = "llvm::FPTruncInst"

@capsule.register_class("llvm::Attributes")
class Attributes(capsule.Wrapper):
    _llvm_type_ = "llvm::Attributes"
    class AttrVal:
        _llvm_type_ = "llvm::Attributes::AttrVal"
        None_ = getattr(_api.llvm.Attributes, "None")()
        AddressSafety = _api.llvm.Attributes.AddressSafety()
        Alignment = _api.llvm.Attributes.Alignment()
        AlwaysInline = _api.llvm.Attributes.AlwaysInline()
        ByVal = _api.llvm.Attributes.ByVal()
        InlineHint = _api.llvm.Attributes.InlineHint()
        InReg = _api.llvm.Attributes.InReg()
        MinSize = _api.llvm.Attributes.MinSize()
        Naked = _api.llvm.Attributes.Naked()
        Nest = _api.llvm.Attributes.Nest()
        NoAlias = _api.llvm.Attributes.NoAlias()
        NoCapture = _api.llvm.Attributes.NoCapture()
        NoImplicitFloat = _api.llvm.Attributes.NoImplicitFloat()
        NoInline = _api.llvm.Attributes.NoInline()
        NonLazyBind = _api.llvm.Attributes.NonLazyBind()
        NoRedZone = _api.llvm.Attributes.NoRedZone()
        NoReturn = _api.llvm.Attributes.NoReturn()
        NoUnwind = _api.llvm.Attributes.NoUnwind()
        OptimizeForSize = _api.llvm.Attributes.OptimizeForSize()
        ReadNone = _api.llvm.Attributes.ReadNone()
        ReadOnly = _api.llvm.Attributes.ReadOnly()
        ReturnsTwice = _api.llvm.Attributes.ReturnsTwice()
        SExt = _api.llvm.Attributes.SExt()
        StackAlignment = _api.llvm.Attributes.StackAlignment()
        StackProtect = _api.llvm.Attributes.StackProtect()
        StackProtectReq = _api.llvm.Attributes.StackProtectReq()
        StructRet = _api.llvm.Attributes.StructRet()
        UWTable = _api.llvm.Attributes.UWTable()
        ZExt = _api.llvm.Attributes.ZExt()
    
    @staticmethod
    def get(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Attributes.get(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    _delete_ = _api.llvm.Attributes.delete

@capsule.register_class("llvm::AttrBuilder")
class AttrBuilder(capsule.Wrapper):
    _llvm_type_ = "llvm::AttrBuilder"
    def addAlignmentAttr(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.AttrBuilder.addAlignmentAttr(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def removeAttribute(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.AttrBuilder.removeAttribute(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def clear(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.AttrBuilder.clear(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def addAttribute(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.AttrBuilder.addAttribute(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def new(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.AttrBuilder.new(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    _delete_ = _api.llvm.AttrBuilder.delete

@capsule.register_class("llvm::FunctionType")
class FunctionType(Type):
    _llvm_type_ = "llvm::FunctionType"
    def isVarArg(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.FunctionType.isVarArg(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getParamType(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.FunctionType.getParamType(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def _get(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.FunctionType._get(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getNumParams(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.FunctionType.getNumParams(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getReturnType(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.FunctionType.getReturnType(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def get(*args):
        from llvmpy import extra
        if len(args) == 3:
            typelist = args[1]
            sv = extra.make_small_vector_from_types(*typelist)
            return FunctionType._get(args[0], sv, args[2])
        else:
            return FunctionType._get(*args)

@capsule.register_class("llvm::NamedMDNode")
class NamedMDNode(capsule.Wrapper):
    _llvm_type_ = "llvm::NamedMDNode"
    def dropAllReferences(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.NamedMDNode.dropAllReferences(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getParent(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.NamedMDNode.getParent(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def dump(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.NamedMDNode.dump(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getName(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.NamedMDNode.getName(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def addOperand(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.NamedMDNode.addOperand(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getOperand(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.NamedMDNode.getOperand(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def print_(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.NamedMDNode.print_(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getNumOperands(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.NamedMDNode.getNumOperands(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def eraseFromParent(self, *args):
        unwrapped = capsule.unwrap(self)
        capsule.release_ownership(unwrapped)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.NamedMDNode.eraseFromParent(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def __str__(self):
        from llvmpy import extra
        os = extra.make_raw_ostream_for_printing()
        self.print_(os, None)
        return os.str()

@capsule.register_class("llvm::MachineCodeInfo")
class MachineCodeInfo(capsule.Wrapper):
    _llvm_type_ = "llvm::MachineCodeInfo"
    def address(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.MachineCodeInfo.address(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setAddress(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.MachineCodeInfo.setAddress(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setSize(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.MachineCodeInfo.setSize(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def size(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.MachineCodeInfo.size(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::JITMemoryManager")
class JITMemoryManager(capsule.Wrapper):
    _llvm_type_ = "llvm::JITMemoryManager"

@capsule.register_class("llvm::GenericValue")
class GenericValue(capsule.Wrapper):
    _llvm_type_ = "llvm::GenericValue"
    def toSignedInt(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GenericValue.toSignedInt(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def CreateInt(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.GenericValue.CreateInt(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def CreateFloat(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.GenericValue.CreateFloat(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def toPointer(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GenericValue.toPointer(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def toFloat(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GenericValue.toFloat(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def CreatePointer(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.GenericValue.CreatePointer(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def valueIntWidth(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GenericValue.valueIntWidth(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    _delete_ = _api.llvm.GenericValue.delete
    def toUnsignedInt(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.GenericValue.toUnsignedInt(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def CreateDouble(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.GenericValue.CreateDouble(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::ExecutionEngine")
class ExecutionEngine(capsule.Wrapper):
    _llvm_type_ = "llvm::ExecutionEngine"
    def freeMachineCodeForFunction(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ExecutionEngine.freeMachineCodeForFunction(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getPointerToGlobalIfAvailable(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ExecutionEngine.getPointerToGlobalIfAvailable(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def RegisterTable(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ExecutionEngine.RegisterTable(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getPointerToFunction(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ExecutionEngine.getPointerToFunction(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def FindFunctionNamed(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ExecutionEngine.FindFunctionNamed(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def DisableGVCompilation(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ExecutionEngine.DisableGVCompilation(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getPointerToBasicBlock(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ExecutionEngine.getPointerToBasicBlock(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def DisableLazyCompilation(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ExecutionEngine.DisableLazyCompilation(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def clearGlobalMappingsFromModule(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ExecutionEngine.clearGlobalMappingsFromModule(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def create(*args):
        unwrapped = list(map(capsule.unwrap, args))
        if len(unwrapped) > 0:
            capsule.release_ownership(unwrapped[0])
        ret = _api.llvm.ExecutionEngine.create(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getOrEmitGlobalVariable(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ExecutionEngine.getOrEmitGlobalVariable(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isLazyCompilationDisabled(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ExecutionEngine.isLazyCompilationDisabled(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getPointerToFunctionOrStub(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ExecutionEngine.getPointerToFunctionOrStub(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def addGlobalMapping(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ExecutionEngine.addGlobalMapping(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getGlobalValueAtAddress(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ExecutionEngine.getGlobalValueAtAddress(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def recompileAndRelinkFunction(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ExecutionEngine.recompileAndRelinkFunction(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def addModule(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        if len(unwrapped1) > 0:
            capsule.release_ownership(unwrapped1[0])
        ret = _api.llvm.ExecutionEngine.addModule(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isCompilingLazily(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ExecutionEngine.isCompilingLazily(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def runJITOnFunction(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ExecutionEngine.runJITOnFunction(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def _runFunction(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ExecutionEngine._runFunction(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def _removeModule(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ExecutionEngine._removeModule(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def InitializeMemory(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ExecutionEngine.InitializeMemory(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def StoreValueToMemory(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ExecutionEngine.StoreValueToMemory(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def updateGlobalMapping(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ExecutionEngine.updateGlobalMapping(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def DeregisterTable(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ExecutionEngine.DeregisterTable(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def clearAllGlobalMappings(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ExecutionEngine.clearAllGlobalMappings(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getDataLayout(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ExecutionEngine.getDataLayout(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, True)
        return wrapped
        
    @staticmethod
    def createJIT(*args):
        unwrapped = list(map(capsule.unwrap, args))
        if len(unwrapped) > 0:
            capsule.release_ownership(unwrapped[0])
        ret = _api.llvm.ExecutionEngine.createJIT(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def DeregisterAllTables(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ExecutionEngine.DeregisterAllTables(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isSymbolSearchingDisabled(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ExecutionEngine.isSymbolSearchingDisabled(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def runStaticConstructorsDestructors(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ExecutionEngine.runStaticConstructorsDestructors(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getPointerToGlobal(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ExecutionEngine.getPointerToGlobal(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getPointerToNamedFunction(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.ExecutionEngine.getPointerToNamedFunction(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    _delete_ = _api.llvm.ExecutionEngine.delete
    def runFunction(self, fn, args):
        from llvmpy import capsule
        unwrapped = list(map(capsule.unwrap, args))
        return self._runFunction(fn, tuple(unwrapped))
    def removeModule(self, module):
        if self._removeModule(module):
            capsule.obtain_ownership(module._capsule)
            return True
        return False

@capsule.register_class("llvm::EngineBuilder")
class EngineBuilder(capsule.Wrapper):
    _llvm_type_ = "llvm::EngineBuilder"
    def setAllocateGVsWithCode(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.EngineBuilder.setAllocateGVsWithCode(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def _setMAttrs(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.EngineBuilder._setMAttrs(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def _selectTarget0(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.EngineBuilder._selectTarget0(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setMCPU(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.EngineBuilder.setMCPU(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setRelocationModel(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.EngineBuilder.setRelocationModel(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setMArch(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.EngineBuilder.setMArch(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def create(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        if len(unwrapped1) > 0:
            capsule.release_ownership(unwrapped1[0])
        ret = _api.llvm.EngineBuilder.create(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def _selectTarget1(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.EngineBuilder._selectTarget1(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setCodeModel(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.EngineBuilder.setCodeModel(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setOptLevel(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.EngineBuilder.setOptLevel(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setEngineKind(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.EngineBuilder.setEngineKind(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setJITMemoryManager(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.EngineBuilder.setJITMemoryManager(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def setUseMCJIT(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.EngineBuilder.setUseMCJIT(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def new(*args):
        unwrapped = list(map(capsule.unwrap, args))
        if len(unwrapped) > 0:
            capsule.release_ownership(unwrapped[0])
        ret = _api.llvm.EngineBuilder.new(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    _delete_ = _api.llvm.EngineBuilder.delete
    def selectTarget(self, *args):
        if not args:
            return self._selectTarget0()
        else:
            return self._selectTarget1(*args)
    def setMAttrs(self, attrs):
        attrlist = list(str(a) for a in attrs)
        return self._setMAttrs(attrlist)

@capsule.register_class("llvm::IRBuilder<>")
class IRBuilder(capsule.Wrapper):
    _llvm_type_ = "llvm::IRBuilder<>"
    def CreateInsertElement(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateInsertElement(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateSwitch(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateSwitch(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateLoad(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateLoad(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def _CreateInvoke(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder._CreateInvoke(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateFPToUI(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateFPToUI(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def _CreateInBoundsGEP(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder._CreateInBoundsGEP(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateSub(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateSub(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def _SetInsertPoint_end_of_bb(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder._SetInsertPoint_end_of_bb(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateSRem(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateSRem(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateFNeg(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateFNeg(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateTruncOrBitCast(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateTruncOrBitCast(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateBr(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateBr(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateExtractElement(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateExtractElement(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateNot(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateNot(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateFDiv(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateFDiv(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateFSub(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateFSub(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateIntToPtr(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateIntToPtr(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateSDiv(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateSDiv(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def GetInsertBlock(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.GetInsertBlock(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateAShr(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateAShr(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateUDiv(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateUDiv(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def _SetInsertPoint_before_instr(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder._SetInsertPoint_before_instr(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateCondBr(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateCondBr(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateFPToSI(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateFPToSI(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateFAdd(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateFAdd(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateStructGEP(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateStructGEP(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateAlignedLoad(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateAlignedLoad(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateAnd(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateAnd(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateAggregateRet(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateAggregateRet(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def _CreateExtractValue(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder._CreateExtractValue(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def new(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.new(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateNeg(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateNeg(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateFPTrunc(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateFPTrunc(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateZExtOrTrunc(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateZExtOrTrunc(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateURem(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateURem(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def isNamePreserving(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.isNamePreserving(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateBitCast(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateBitCast(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateShuffleVector(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateShuffleVector(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateSExt(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateSExt(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateSelect(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateSelect(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateRetVoid(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateRetVoid(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateAdd(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateAdd(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateIsNull(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateIsNull(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateSExtOrTrunc(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateSExtOrTrunc(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreatePtrToInt(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreatePtrToInt(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def _CreateGEP(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder._CreateGEP(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateIntCast(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateIntCast(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateZExt(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateZExt(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateFMul(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateFMul(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateLandingPad(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateLandingPad(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateResume(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateResume(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateAlloca(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateAlloca(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateSIToFP(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateSIToFP(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateMul(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateMul(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateICmp(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateICmp(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateIsNotNull(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateIsNotNull(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateStore(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateStore(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateAlignedStore(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateAlignedStore(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateAtomicRMW(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateAtomicRMW(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateSExtOrBitCast(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateSExtOrBitCast(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    _delete_ = _api.llvm.IRBuilder.delete
    def CreateLShr(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateLShr(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateIndirectBr(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateIndirectBr(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateFRem(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateFRem(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreatePtrDiff(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreatePtrDiff(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateZExtOrBitCast(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateZExtOrBitCast(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateFPCast(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateFPCast(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateRet(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateRet(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateFence(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateFence(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def _CreateInsertValue(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder._CreateInsertValue(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def Insert(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.Insert(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateShl(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateShl(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def _CreateCall(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder._CreateCall(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateGlobalStringPtr(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateGlobalStringPtr(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateVAArg(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateVAArg(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateFPExt(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateFPExt(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreatePHI(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreatePHI(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateXor(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateXor(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateTrunc(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateTrunc(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateAtomicCmpXchg(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateAtomicCmpXchg(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateUIToFP(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateUIToFP(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateOr(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateOr(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateFCmp(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateFCmp(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateUnreachable(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.IRBuilder.CreateUnreachable(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def CreateInvoke(self, *args):
        from llvmpy import extra
        args = list(args)
        valuelist = args[3]
        args[3] = extra.make_small_vector_from_values(*valuelist)
        return self._CreateInvoke(*args)
    def CreateInsertValue(self, *args):
        from llvmpy import extra
        args = list(args)
        valuelist = args[2]
        args[2] = extra.make_small_vector_from_unsigned(*valuelist)
        return self._CreateInsertValue(*args)
    def CreateGEP(self, *args):
        from llvmpy import extra
        args = list(args)
        valuelist = args[1]
        args[1] = extra.make_small_vector_from_values(*valuelist)
        return self._CreateGEP(*args)
    def CreateExtractValue(self, *args):
        from llvmpy import extra
        args = list(args)
        valuelist = args[1]
        args[1] = extra.make_small_vector_from_unsigned(*valuelist)
        return self._CreateExtractValue(*args)
    def CreateCall(self, *args):
        from llvmpy import extra
        args = list(args)
        valuelist = args[1]
        args[1] = extra.make_small_vector_from_values(*valuelist)
        return self._CreateCall(*args)
    def SetInsertPoint(self, pt):
        if isinstance(pt, Instruction):
            return self._SetInsertPoint_before_instr(pt)
        elif isinstance(pt, BasicBlock):
            return self._SetInsertPoint_end_of_bb(pt)
        else:
            raise ValueError("Expected either an Instruction or a BasicBlock")
    def CreateInBoundsGEP(self, *args):
        from llvmpy import extra
        args = list(args)
        valuelist = args[1]
        args[1] = extra.make_small_vector_from_values(*valuelist)
        return self._CreateInBoundsGEP(*args)

@capsule.register_class("llvm::InlineAsm")
class InlineAsm(Value):
    _llvm_type_ = "llvm::InlineAsm"
    class ConstraintPrefix:
        _llvm_type_ = "llvm::InlineAsm::ConstraintPrefix"
        isInput = _api.llvm.InlineAsm.isInput()
        isOutput = _api.llvm.InlineAsm.isOutput()
        isClobber = _api.llvm.InlineAsm.isClobber()
    
    class AsmDialect:
        _llvm_type_ = "llvm::InlineAsm::AsmDialect"
        AD_ATT = _api.llvm.InlineAsm.AD_ATT()
        AD_Intel = _api.llvm.InlineAsm.AD_Intel()
    
    @staticmethod
    def get(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.InlineAsm.get(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::Linker")
class Linker(capsule.Wrapper):
    _llvm_type_ = "llvm::Linker"
    class ControlFlags:
        _llvm_type_ = "llvm::Linker::ControlFlags"
        Verbose = _api.llvm.Linker.Verbose()
        QuietWarnings = _api.llvm.Linker.QuietWarnings()
        QuietErrors = _api.llvm.Linker.QuietErrors()
    
    class LinkerMode:
        _llvm_type_ = "llvm::Linker::LinkerMode"
        DestroySource = _api.llvm.Linker.DestroySource()
        PreserveSource = _api.llvm.Linker.PreserveSource()
    
    def getLastError(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Linker.getLastError(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def LinkInModule(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Linker.LinkInModule(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def _new_w_existing(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Linker._new_w_existing(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def getModule(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Linker.getModule(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def _LinkModules(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Linker._LinkModules(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def _new_w_empty(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.Linker._new_w_empty(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def releaseModule(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.Linker.releaseModule(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    _delete_ = _api.llvm.Linker.delete
    @staticmethod
    def LinkModules(module, other, mode, errmsg):
        failed = Linker._LinkModules(module, other, mode, errmsg)
        if not failed and mode != Linker.LinkerMode.PreserveSource:
            capsule.release_ownership(other._ptr)
        return failed
    @staticmethod
    def new(progname, module_or_name, *args):
        if isinstance(module_or_name, Module):
            return _new_w_existing(progname, module_or_name, *args)
        else:
            return _new_w_empty(progname, module_or_name, *args)

@capsule.register_class("llvm::PassRegistry")
class PassRegistry(capsule.Wrapper):
    _llvm_type_ = "llvm::PassRegistry"
    @staticmethod
    def getPassRegistry(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.PassRegistry.getPassRegistry(*unwrapped)
        wrapped = capsule.wrap(ret, True)
        return wrapped
        
    def getPassInfo(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.PassRegistry.getPassInfo(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def enumerate(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.PassRegistry.enumerate(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    _delete_ = _api.llvm.PassRegistry.delete

@capsule.register_class("llvm::PassInfo")
class PassInfo(capsule.Wrapper):
    _llvm_type_ = "llvm::PassInfo"
    def createPass(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.PassInfo.createPass(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        

@capsule.register_class("llvm::PassManagerBuilder")
class PassManagerBuilder(capsule.Wrapper):
    _llvm_type_ = "llvm::PassManagerBuilder"
    def populateModulePassManager(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.PassManagerBuilder.populateModulePassManager(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    @staticmethod
    def new(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.PassManagerBuilder.new(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def populateFunctionPassManager(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.PassManagerBuilder.populateFunctionPassManager(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    def populateLTOPassManager(self, *args):
        unwrapped = capsule.unwrap(self)
        unwrapped1 = list(map(capsule.unwrap, args))
        ret = _api.llvm.PassManagerBuilder.populateLTOPassManager(unwrapped, *unwrapped1)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    _delete_ = _api.llvm.PassManagerBuilder.delete
    @property
    def Vectorize(self):
        unwrapped = capsule.unwrap(self)
        ret = _api.llvm.PassManagerBuilder.Vectorize_get(unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
    
    @Vectorize.setter
    def Vectorize(self, value):
        unwrapped1 = capsule.unwrap(self)
        unwrapped2 = capsule.unwrap(value)
        return _api.llvm.PassManagerBuilder.Vectorize_set(unwrapped1, unwrapped2)
    
    @property
    def DisableUnrollLoops(self):
        unwrapped3 = capsule.unwrap(self)
        ret1 = _api.llvm.PassManagerBuilder.DisableUnrollLoops_get(unwrapped3)
        wrapped1 = capsule.wrap(ret1, False)
        return wrapped1
    
    @DisableUnrollLoops.setter
    def DisableUnrollLoops(self, value):
        unwrapped4 = capsule.unwrap(self)
        unwrapped5 = capsule.unwrap(value)
        return _api.llvm.PassManagerBuilder.DisableUnrollLoops_set(unwrapped4, unwrapped5)
    
    @property
    def Inliner(self):
        unwrapped6 = capsule.unwrap(self)
        ret2 = _api.llvm.PassManagerBuilder.Inliner_get(unwrapped6)
        wrapped2 = capsule.wrap(ret2, True)
        return wrapped2
    
    @Inliner.setter
    def Inliner(self, value):
        unwrapped7 = capsule.unwrap(self)
        unwrapped8 = capsule.unwrap(value)
        capsule.release_ownership(unwrapped8)
        return _api.llvm.PassManagerBuilder.Inliner_set(unwrapped7, unwrapped8)
    
    @property
    def SizeLevel(self):
        unwrapped9 = capsule.unwrap(self)
        ret3 = _api.llvm.PassManagerBuilder.SizeLevel_get(unwrapped9)
        wrapped3 = capsule.wrap(ret3, False)
        return wrapped3
    
    @SizeLevel.setter
    def SizeLevel(self, value):
        unwrapped10 = capsule.unwrap(self)
        unwrapped11 = capsule.unwrap(value)
        return _api.llvm.PassManagerBuilder.SizeLevel_set(unwrapped10, unwrapped11)
    
    @property
    def LoopVectorize(self):
        unwrapped12 = capsule.unwrap(self)
        ret4 = _api.llvm.PassManagerBuilder.LoopVectorize_get(unwrapped12)
        wrapped4 = capsule.wrap(ret4, False)
        return wrapped4
    
    @LoopVectorize.setter
    def LoopVectorize(self, value):
        unwrapped13 = capsule.unwrap(self)
        unwrapped14 = capsule.unwrap(value)
        return _api.llvm.PassManagerBuilder.LoopVectorize_set(unwrapped13, unwrapped14)
    
    @property
    def OptLevel(self):
        unwrapped15 = capsule.unwrap(self)
        ret5 = _api.llvm.PassManagerBuilder.OptLevel_get(unwrapped15)
        wrapped5 = capsule.wrap(ret5, False)
        return wrapped5
    
    @OptLevel.setter
    def OptLevel(self, value):
        unwrapped16 = capsule.unwrap(self)
        unwrapped17 = capsule.unwrap(value)
        return _api.llvm.PassManagerBuilder.OptLevel_set(unwrapped16, unwrapped17)
    
    @property
    def DisableSimplifyLibCalls(self):
        unwrapped18 = capsule.unwrap(self)
        ret6 = _api.llvm.PassManagerBuilder.DisableSimplifyLibCalls_get(unwrapped18)
        wrapped6 = capsule.wrap(ret6, False)
        return wrapped6
    
    @DisableSimplifyLibCalls.setter
    def DisableSimplifyLibCalls(self, value):
        unwrapped19 = capsule.unwrap(self)
        unwrapped20 = capsule.unwrap(value)
        return _api.llvm.PassManagerBuilder.DisableSimplifyLibCalls_set(unwrapped19, unwrapped20)
    
    @property
    def DisableUnitAtATime(self):
        unwrapped21 = capsule.unwrap(self)
        ret7 = _api.llvm.PassManagerBuilder.DisableUnitAtATime_get(unwrapped21)
        wrapped7 = capsule.wrap(ret7, False)
        return wrapped7
    
    @DisableUnitAtATime.setter
    def DisableUnitAtATime(self, value):
        unwrapped22 = capsule.unwrap(self)
        unwrapped23 = capsule.unwrap(value)
        return _api.llvm.PassManagerBuilder.DisableUnitAtATime_set(unwrapped22, unwrapped23)
    
    @property
    def LibraryInfo(self):
        unwrapped24 = capsule.unwrap(self)
        ret8 = _api.llvm.PassManagerBuilder.LibraryInfo_get(unwrapped24)
        wrapped8 = capsule.wrap(ret8, True)
        return wrapped8
    
    @LibraryInfo.setter
    def LibraryInfo(self, value):
        unwrapped25 = capsule.unwrap(self)
        unwrapped26 = capsule.unwrap(value)
        capsule.release_ownership(unwrapped26)
        return _api.llvm.PassManagerBuilder.LibraryInfo_set(unwrapped25, unwrapped26)
    

@capsule.register_class("llvm::InlineFunctionInfo")
class InlineFunctionInfo(capsule.Wrapper):
    _llvm_type_ = "llvm::InlineFunctionInfo"
    @staticmethod
    def new(*args):
        unwrapped = list(map(capsule.unwrap, args))
        ret = _api.llvm.InlineFunctionInfo.new(*unwrapped)
        wrapped = capsule.wrap(ret, False)
        return wrapped
        
    _delete_ = _api.llvm.InlineFunctionInfo.delete

class AtomicOrdering:
    _llvm_type_ = "llvm::AtomicOrdering"
    NotAtomic = _api.llvm.NotAtomic()
    Unordered = _api.llvm.Unordered()
    Monotonic = _api.llvm.Monotonic()
    Acquire = _api.llvm.Acquire()
    Release = _api.llvm.Release()
    AcquireRelease = _api.llvm.AcquireRelease()
    SequentiallyConsistent = _api.llvm.SequentiallyConsistent()

class SynchronizationScope:
    _llvm_type_ = "llvm::SynchronizationScope"
    SingleThread = _api.llvm.SingleThread()
    CrossThread = _api.llvm.CrossThread()

class VerifierFailureAction:
    _llvm_type_ = "llvm::VerifierFailureAction"
    AbortProcessAction = _api.llvm.AbortProcessAction()
    PrintMessageAction = _api.llvm.PrintMessageAction()
    ReturnStatusAction = _api.llvm.ReturnStatusAction()

