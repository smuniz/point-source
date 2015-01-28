#!/usr/bin/env python

#
# This script attempts to achieve 100% function and branch coverage for
# all APIs in the llvm package. It only exercises the APIs, doesn't test
# them for correctness.
#

#from llvm import *
#from llvm.core import *
#from llvm.ee import *
#from llvm.passes import *
from middleend.mir.mir_module import *
from middleend.mir.mir_function import *
from middleend.mir.mir_basicblock import *
from middleend.mir.mir_instruction import *
from middleend.mir.mir_constants import *
from middleend.mir.mir_type import *
from middleend.mir.mir_global_variable import *

ti = MiddleIrTypeInt()

def do_llvmexception():
    print("    Testing class LLVMExceptions")
    e = MiddleIrModuleException
    e = MiddleIrFunctionException
    e = MiddleIrBasicBlockException
    e = MiddleIrInstructionBuilderException
    e = MiddleIrInstructionException


def do_misc():
    print("    Testing miscellaneous functions")
#    try:
#        load_library_permanently("/usr/lib/libm.so")
#    except LLVMException:
#        pass
#    try:
#        print("        ... second one now")
#        load_library_permanently("no*such*so")
#    except LLVMException:
#        pass


def do_llvm():
    print("  Testing module llvm")
    do_llvmexception()
    do_misc()


def do_module():
    print("    Testing class MiddleIrModule")
    m = MiddleIrModule('test')
    m.target = 'a'
    a = m.target
#    m.data_layout = 'a'
#    a = m.data_layout
    # m.add_type_name('a', ti)
    # m.delete_type_name('a')
    MiddleIrTypeStruct([ti], name='a')
#    m.get_type_by_name('a').name=''

    s = str(m)
    s = m == MiddleIrModule.new('a')
    #gvar = MiddleIrGlobalVariable(ti, 'b')
    #m.add_global_variable(gvar)
    gvar = MiddleIrGlobalVariable.new(m, ti, 'b')
#    m.get_global_variable_by_name('b')
#    gvs = list(m.global_variables)
    #ft = MiddleIrTypeFunction(ti, [ti])
    func = MiddleIrFunction("func", ti, [ti])
    m.add_function(func)
    m.get_function_by_name("func")
#    m.get_or_insert_function(ft, "func")
#    m.get_or_insert_function(MiddleIrTypeFunction(ti, []), "func")
#    m.get_or_insert_function(ft, "func2")
    fns = list(m.functions)
    try:
        m.verify()
    except LLVMException:
        pass

    class strstream(object):
        def __init__(self):
            self.s = b''

        def write(self, data):
            if not isinstance(data, bytes):
                data = data.encode('utf-8')
            self.s += data

        def read(self):
            return self.s

    ss = strstream()
    m2 = MiddleIrModule.new('test')
    # m2.add_type_name('myint', ti)
    MiddleIrTypeStruct([ti], 'myint')

    #m2.to_bitcode(ss)
    #m3 = MiddleIrModule.from_bitcode(ss)
    #t = m2 == m3
#    ss2 = strstream()
#    ss2.write(str(m))
#    m4 = MiddleIrModule.from_assembly(ss2)
#    t = m4 == m
#    t = m4.pointer_size
#    mA = MiddleIrModule.new('ma')
#    mB = MiddleIrModule.new('mb')
#    mA.link_in(mB)


def do_type():
    print("    Testing class Type")
    for i in range(1,100):
        MiddleIrTypeInt(i)
    MiddleIrTypeFloat()
    MiddleIrTypeDouble()
    MiddleIrTypeX86Fp80()
    MiddleIrTypeFp128()
    MiddleIrTypePpcFp128()
    MiddleIrTypeFunction(ti, [ti]*100, True)
    MiddleIrTypeFunction(ti, [ti]*100, False)
    MiddleIrTypeStruct([ti]*100)
    MiddleIrTypePackedStruct([ti]*100)
    MiddleIrTypeArray(ti, 100)
    ptr = MiddleIrTypePointer(ti, 4)
    pte = ptr.type
    MiddleIrTypeVector(ti, 100)
    MiddleIrTypeVoid()
    MiddleIrTypeLabel()

    MiddleIrTypeOpaque('an_opaque_type')
    s = str(ti)
    s = ti == MiddleIrTypeFloat()
    MiddleIrTypeOpaque('whatever').set_body([MiddleIrTypeInt()])
    s = ti.width
    ft = MiddleIrTypeFunction(ti, [ti]*10)
#    ft.return_type
#    ft.vararg
#    s = list(ft.args)
#    ft.arg_count
#    st = MiddleIrTypeStruct([ti]*10)
#    s = st.element_count
#    s = list(st.elements)
#    s = st.packed
#    st = MiddleIrTypePackedStruct([ti]*10)
#    s = st.element_count
#    s = list(st.elements)
#    s = st.packed
#    at = MiddleIrTypeArray(ti, 100)
#    s = at.element
#    s = at.count
    pt = MiddleIrTypePointer(ti, 10)
#    pt.address_space
    vt = MiddleIrTypeVector(ti, 100)
#    s = vt.element
#    s = vt.count
    MiddleIrTypeInt(32) == MiddleIrTypeInt(64)
    MiddleIrTypeInt(32) != MiddleIrTypeInt(64)
    MiddleIrTypeInt(32) != MiddleIrTypeFloat()

#### Removed
##def do_typehandle():
##    print("    Testing class TypeHandle")
##    th = TypeHandle.new(MiddleIrTypeOpaque())
##    ts = MiddleIrTypeStruct([ MiddleIrTypeInt(), MiddleIrTypePointer(th.type) ])
##    th.type.refine(ts)


def do_value():
    print("    Testing class Value")
    k = MiddleIrConstantInt(ti, 42)
    k.name = 'a'
    s = k.name
    t = k.type
    s = str(k)
    s = k == MiddleIrConstantInt(ti, 43)
#    i = k.value_id
#    i = k.use_count
#    i = k.uses


def do_user():
    m = MiddleIrModule.new('a')
    #ft = MiddleIrTypeFunction(ti, [ti]*2)
    ft = (ti, [ti]*2)
#    f = MiddleIrFunction.new(m, 'func', *ft)
#    b = f.append_basic_block('a')
#    bb = Builder.new(b)
#    i1 = bb.add(f.args[0], f.args[1])
#    i2 = bb.ret(i1)
#    i1.operand_count == 2
#    i2.operand_count == 1
#    i1.operands[0] is f.args[0]
#    i1.operands[1] is f.args[1]
#    i2.operands[0] is i1


def do_constant():
    print("    Testing class Constant")
    MiddleIrConstantNull(ti)
    MiddleIrConstantAllOnes(ti)
    MiddleIrConstantUndef(ti)
    MiddleIrConstantInt(ti, 10)
    MiddleIrConstantIntSignExtend(ti, 10)
    MiddleIrConstantReal(MiddleIrTypeFloat(), "10.0")
    MiddleIrConstantReal(MiddleIrTypeFloat(), 3.14)
    MiddleIrConstantString("test")
    MiddleIrConstantStringZ("test2")
    MiddleIrConstantArray(ti, [MiddleIrConstantInt(ti,42)]*10)
    MiddleIrConstantStruct([MiddleIrConstantInt(ti,42)]*10)
    MiddleIrConstantPackedStruct([MiddleIrConstantInt(ti,42)]*10)
    MiddleIrConstantVector([MiddleIrConstantInt(ti,42)]*10)

    MiddleIrConstantSizeof(ti)

    k = MiddleIrConstantInt(ti, 10)
    f = MiddleIrConstantReal(MiddleIrTypeFloat(), 3.1415)
    # TODO / FIXME : Add all operations
#    k.neg().not_().add(k).sub(k).mul(k).udiv(k).sdiv(k).urem(k)
#    k.srem(k).and_(k).or_(k).xor(k).icmp(IPRED_ULT, k)
#    f.fdiv(f).frem(f).fcmp(RPRED_ULT, f)
#    f.fadd(f).fmul(f).fsub(f)
    vi = MiddleIrConstantVector([MiddleIrConstantInt(ti,42)]*10)
    vf = MiddleIrConstantVector([MiddleIrConstantReal(MiddleIrTypeFloat(), 3.14)]*10)
#    k.shl(k).lshr(k).ashr(k)
    return
    # TODO gep
#    k.trunc(MiddleIrTypeInt(1))
#    k.sext(MiddleIrTypeInt(64))
#    k.zext(MiddleIrTypeInt(64))
#    MiddleIrConstantReal(MiddleIrTypeDouble(), 1.0).fptrunc(MiddleIrTypeFloat())
#    MiddleIrConstantReal(MiddleIrTypeFloat(), 1.0).fpext(MiddleIrTypeDouble())
#    k.uitofp(MiddleIrTypeFloat())
#    k.sitofp(MiddleIrTypeFloat())
#    f.fptoui(ti)
#    f.fptosi(ti)
#    p = MiddleIrTypePointer(ti)
#    # TODO ptrtoint
#    k.inttoptr(p)
#    f.bitcast(MiddleIrTypeInt(32))
#    k.trunc(MiddleIrTypeInt(1)).select(k, k)
#    vi.extract_element( MiddleIrConstantInt(ti,0) )
#    vi.insert_element( k, k )
#    vi.shuffle_vector( vi, vi )


def do_global_value():
    print("    Testing class GlobalValue")
    m = MiddleIrModule.new('a')
    gv = MiddleIrGlobalVariable.new(m, MiddleIrTypeInt(), 'b')
    s = gv.is_declaration
    m = gv.module
#    gv.linkage = LINKAGE_EXTERNAL
#    s = gv.linkage
#    gv.section = '.text'
#    s = gv.section
#    gv.visibility = VISIBILITY_HIDDEN
#    s = gv.visibility
    gv.alignment = 8
    s = gv.alignment


def do_global_variable():
    print("    Testing class MiddleIrGlobalVariable")
    m = MiddleIrModule.new('a')
    gv = MiddleIrGlobalVariable.new(m, MiddleIrTypeInt(), 'b')
    gv = MiddleIrGlobalVariable.get(m, 'b')
    gv.delete()
    gv = MiddleIrGlobalVariable.new(m, MiddleIrTypeInt(), 'c')
    gv.initializer = MiddleIrConstantInt( ti, 10 )
    s = gv.initializer
#    gv.global_constant = True
#    s = gv.global_constant


def do_argument():
    print("    Testing class Argument")
    m = MiddleIrModule.new('a')
    tip = MiddleIrTypePointer(ti)
    #ft = MiddleIrTypeFunction()
    f = MiddleIrFunction.new(m, 'func', tip, [tip,])
    a = f.arguments[0]
#    a.add_attribute(ATTR_NEST)
#    a.remove_attribute(ATTR_NEST)
    a.alignment = 16
    a1 = a.alignment


def do_function():
    print("    Testing class MiddleIrFunction")
    #ft = MiddleIrTypeFunction(ti, [ti]*20)
    zz = MiddleIrFunction.new(MiddleIrModule.new('z'), 'foobar', ti, [ti]*20)
    del zz
    MiddleIrFunction.new(MiddleIrModule.new('zz'), 'foobar', ti, [ti]*20)
    m = MiddleIrModule.new('a')
    f = MiddleIrFunction.new(m, 'func', ti, [ti]*20)
    f.delete()
    ft = MiddleIrTypeFunction(ti, [ti]*20)
    f = MiddleIrFunction.new(m, 'func2', ti, [ti]*20)
#    has_nounwind = f.does_not_throw
#    f.does_not_throw = True
#    f2 = MiddleIrFunction.intrinsic(m, INTR_COS, [ti])
#    g = f.intrinsic_id
    f.calling_convenion = CC_FASTCALL
    g = f.calling_convention
#    f.collector = 'a'
#    c = f.collector
    a = list(f.arguments)
    g = f.basic_block_count
##    g = f.entry_basic_block
##    g = f.append_basic_block('a')
##    g = f.entry_basic_block
    g = list(f.basic_blocks)
#    f.add_attribute(ATTR_NO_RETURN)
#    f.add_attribute(ATTR_ALWAYS_INLINE)
#    #for some reason removeFnAttr is just gone in 3.3
#    if version <= (3, 2):
#        f.remove_attribute(ATTR_NO_RETURN)

    # LLVM misbehaves:
    #try:
    #    f.verify()
    #except LLVMException:
    #    pass


def do_instruction():
    print("    Testing class Instruction")
    m = MiddleIrModule.new('a')
    #ft = MiddleIrTypeFunction(ti, [ti]*20)
    f = MiddleIrFunction.new(m, 'func', ti, [ti]*20)
    b = MiddleIrBasicBlock('a')
    f.add_basic_block(b)
    bb = MiddleIrInstructionBuilder.new(b)
    i = bb.ret()
#    bb2 = i.basic_block
#    ops = i.operands
#    opcount = i.operand_count


def do_callorinvokeinstruction():
    print("    Testing class CallOrInvokeInstruction")
    m = MiddleIrModule.new('a')
    #ft = MiddleIrTypeFunction(ti, [ti])
    f = MiddleIrFunction.new(m, 'func', ti, [ti])
    b = MiddleIrBasicBlock('a')
    f.add_basic_block(b)
    bb = MiddleIrInstructionBuilder.new(b)
#    i = bb.invoke(f, [MiddleIrConstantInt(ti, 10)], b, b)
#    a = i.calling_convention
#    i.calling_convention = CC_FASTCALL
#    if version <= (3, 2):
#        i.add_parameter_attribute(0, ATTR_SEXT)
#        i.remove_parameter_attribute(0, ATTR_SEXT)
#        i.set_parameter_alignment(0, 8)
#    #tc = i.tail_call
#    #i.tail_call = 1


#def do_phinode():
#    print("    Testing class PhiNode")
#    m = MiddleIrModule.new('a')
#    ft = MiddleIrTypeFunction(ti, [ti])
#    f = MiddleIrFunction.new(m, ft, 'func')
#    b = f.append_basic_block('b')
#    c = f.append_basic_block('c')
#    d = f.append_basic_block('d')
#    bb = Builder.new(d)
#    p = bb.phi(ti)
#    v = p.incoming_count
#    p.add_incoming( MiddleIrConstantInt(ti, 10), b )
#    p.add_incoming( MiddleIrConstantInt(ti, 10), c )
#    p.get_incoming_value(0)
#    p.get_incoming_block(0)
#
#
#def do_switchinstruction():
#    print("    Testing class SwitchInstruction")
#    m = MiddleIrModule.new('a')
#    ft = MiddleIrTypeFunction(ti, [ti])
#    f = MiddleIrFunction.new(m, ft, 'func')
#    b = f.append_basic_block('b')
#    bb = Builder.new(b)
#    s = bb.switch(f.args[0], b)
#    s.add_case(MiddleIrConstantInt(ti, 10), b)
#
#
#def do_basicblock():
#    print("    Testing class BasicBlock")
#    m = MiddleIrModule.new('a')
#    ft = MiddleIrTypeFunction(ti, [ti])
#    f = MiddleIrFunction.new(m, ft, 'func')
#    b = f.append_basic_block('b')
#    bb = Builder.new(b)
#    s = bb.switch(f.args[0], b)
#    s.add_case(MiddleIrConstantInt(ti, 10), b)
#    s = list(b.instructions)
#    b2 = b.insert_before('before')
#    b2.delete()
#    ff = b.function
#    m2 = ff.module
#    t = m == m2
#
#
#def _do_builder_mrv():
#    m = MiddleIrModule.new('mrv')
#    ft = MiddleIrTypeFunction(MiddleIrTypeArray(ti, 2), [ti])
#    f = MiddleIrFunction.new(m, ft, 'divrem')
#    blk = f.append_basic_block('b')
#    b = Builder.new(blk)
#    v = b.call(f, [MiddleIrConstantInt(ti, 1)])
#    v1 = b.extract_value(v, 0)
#    v2 = b.extract_value(v, 1)
#    b.ret_many([v1, v2])
#    #print f


def do_builder():
    print("    Testing class Builder")
    m = MiddleIrModule.new('a')
    #ft = MiddleIrTypeFunction(ti, [ti])
    #f = MiddleIrFunction.new(m, ft, 'func')
    f = MiddleIrFunction("func", ti, [ti])
    m.add_function(f)
    f._llvm_definition.args[0].name = "a"
    blk = MiddleIrBasicBlock('b')
    f.add_basic_block(blk)
    b = MiddleIrInstructionBuilder.new(blk)
#    b.ret(MiddleIrConstantInt(ti, 10))
#    b.position_at_beginning(blk)
#    b.position_at_end(blk)
#    b.position_before(blk.instructions[0])
#    blk2 = b.basic_block
#    b.ret_void()
#    b.ret(MiddleIrConstantInt(ti, 10))
#    _do_builder_mrv()
#    #b.ret_many([MiddleIrConstantInt(ti, 10)]*10)
#    b.branch(blk)
#    b.cbranch(MiddleIrConstantInt(MiddleIrTypeInt(1), 1), blk, blk)
#    b.switch(f.args[0], blk)
#    b.invoke(f, [MiddleIrConstantInt(ti,10)], blk, blk)
#    # b.unwind() # removed
#    b.unreachable()
    v = f.arguments[0]
#    fv = MiddleIrConstantReal(MiddleIrTypeFloat(), "1.0")
    k = MiddleIrConstantInt(ti, 10)
    b.add(v, v)
#    b.fadd(fv, fv)
#    b.sub(v, v)
#    b.fsub(fv, fv)
#    b.mul(v, v)
#    b.fmul(fv, fv)
#    b.udiv(v, v)
#    b.sdiv(v, v)
#    b.fdiv(fv, fv)
#    b.urem(v, v)
#    b.srem(v, v)
#    b.frem(fv, fv)
#    b.shl(v, k)
#    b.lshr(v, k)
#    b.ashr(v, k)
#    b.and_(v, v)
#    b.or_(v, v)
#    b.xor(v, v)
#    b.neg(v)
#    b.not_(v)
    p = b.alloca(MiddleIrTypeInt(32))
    #p = b.malloc(MiddleIrTypeInt())
    #b.malloc_array(MiddleIrTypeInt(), k)
    #b.alloca(MiddleIrTypeInt())
    #b.alloca_array(MiddleIrTypeInt(), k)
#    b.free(p)
#    b.load(p)
    k = f.arguments[0]
    x = b.store(k, p)
#    # TODO gep
#    b.trunc(v, MiddleIrTypeInt(1))
#    b.zext(v, MiddleIrTypeInt(64))
#    b.sext(v, MiddleIrTypeInt(64))
#    b.fptoui(fv, ti)
#    b.fptosi(fv, ti)
#    b.uitofp(k, MiddleIrTypeFloat())
#    b.sitofp(k, MiddleIrTypeFloat())
#    b.fptrunc(MiddleIrConstantReal(MiddleIrTypeDouble(), "1.0"), MiddleIrTypeFloat())
#    b.fpext(MiddleIrConstantReal(MiddleIrTypeFloat(), "1.0"), MiddleIrTypeDouble())
    b.ptrtoint(p, ti)
    b.inttoptr(k, MiddleIrTypePointer(MiddleIrTypeInt()))
#    b.bitcast(v, MiddleIrTypeFloat())
    b.icmp(IPRED_ULT, v, v)
#    b.fcmp(RPRED_ULT, fv, fv)
#    vi = MiddleIrConstantVector([MiddleIrConstantInt(ti,42)]*10)
#    vi_mask = MiddleIrConstantVector([MiddleIrConstantInt(ti, X) for X in range(20)])
#    vf = MiddleIrConstantVector([MiddleIrConstantReal(MiddleIrTypeFloat(), 3.14)]*10)
#    # TODO b.extract_value(v, 0)
#    b.call(f, [v])
#    b.select(MiddleIrConstantInt(MiddleIrTypeInt(1), 1), blk, blk)
#    b.vaarg(v, MiddleIrTypeInt())
#    b.extract_element(vi, v)
#    b.insert_element(vi, v, v)
#    b.shuffle_vector(vi, vi, vi_mask)
#    # NOTE: phi nodes without incoming values segfaults in LLVM during
#    # destruction.
#    i = b.phi(MiddleIrTypeInt())
#    i.add_incoming(v, blk)
#    t = i.is_terminator == False
#    t = i.is_binary_op == False
#    t = i.is_shift == False
#    t = i.is_cast == False
#    t = i.is_logical_shift == False
#    t = i.is_arithmetic_shift == False
#    t = i.is_associative == False
#    t = i.is_commutative == False
#    t = i.is_volatile == False
#    t = i.opcode
#    t = i.opcode_name


def do_llvm_core():
    print("  Testing module llvm.core")
    do_module()
    do_type()
    #    do_typehandle()
    do_value()
    do_user()
    do_constant()
    do_global_value()
    do_global_variable()
    do_argument()
    do_function()
    do_instruction()
    do_callorinvokeinstruction()
#    do_phinode()
#    do_switchinstruction()
#    do_basicblock()
    do_builder()


#def do_targetdata():
#    print("    Testing class TargetData")
#    t = TargetData.new('')
#    v = str(t)
#    v = t.byte_order
#    v = t.pointer_size
#    v = t.target_integer_type
#    ty = MiddleIrTypeInt()
#    v = t.size(ty)
#    v = t.store_size(ty)
#    v = t.abi_size(ty)
#    v = t.abi_alignment(ty)
#    v = t.callframe_alignment(ty)
#    v = t.preferred_alignment(ty)
#    sty = MiddleIrTypeStruct([ty, ty])
#    v = t.element_at_offset(sty, 0)
#    v = t.offset_of_element(sty, 0)
#    m = MiddleIrModule.new('a')
#    gv = m.add_global_variable(ty, 'gv')
#    v = t.preferred_alignment(gv)
#
#
#def do_genericvalue():
#    print("    Testing class GenericValue")
#    v = GenericValue.int(ti, 1)
#    v = GenericValue.int_signed(ti, 1)
#    v = GenericValue.real(MiddleIrTypeFloat(), 3.14)
#    a = v.as_int()
#    a = v.as_int_signed()
#    a = v.as_real(MiddleIrTypeFloat())
#
#
#def do_executionengine():
#    print("    Testing class ExecutionEngine")
#    m = MiddleIrModule.new('a')
#    ee = ExecutionEngine.new(m, False) # True)
#    ft = MiddleIrTypeFunction(ti, [])
#    f = m.add_function(ft, 'func')
#    bb = f.append_basic_block('entry')
#    b = Builder.new(bb)
#    b.ret(MiddleIrConstantInt(ti, 42))
#    ee.run_static_ctors()
#    gv = ee.run_function(f, [])
#    is42 = gv.as_int() == 42
#    ee.run_static_dtors()
#    ee.free_machine_code_for(f)
#    t = ee.target_data
#    m2 = MiddleIrModule.new('b')
#    ee.add_module(m2)
#    m3 = MiddleIrModule.new('c')
#    ee2 = ExecutionEngine.new(m3, False)
#    m4 = MiddleIrModule.new('d')
#    m5 = MiddleIrModule.new('e')
#    #ee3 = ExecutionEngine.new(m4, False)
#    #ee3.add_module(m5)
#    #x = ee3.remove_module(m5)
#    #isinstance(x, MiddleIrModule)
#
#
#def do_llvm_ee():
#    print("  Testing module llvm.ee")
#    do_targetdata()
#    do_genericvalue()
#    do_executionengine()
#
#
#def do_passmanager():
#    print("    Testing class PassManager")
#    pm = PassManager.new()
#    pm.add(TargetData.new(''))
#
#    print('.........Begging for rewrite!!!')
#    ### It is not practical to maintain all PASS_* constants.
#    #
#    #    passes = ('PASS_OPTIMAL_EDGE_PROFILER', 'PASS_EDGE_PROFILER',
#    #              'PASS_PROFILE_LOADER', 'PASS_AAEVAL')
#    #    all_these = [getattr(llvm.passes, x)
#    #                    for x in dir(llvm.passes)
#    #                        if x.startswith('PASS_') and x not in passes]
#    #    for i in all_these:
#    #        print i
#    #        pm.add(i)
#    pm.run(MiddleIrModule.new('a'))
#
#
#def do_functionpassmanager():
#    print("    Testing class FunctionPassManager")
#    m = MiddleIrModule.new('a')
#    ft = MiddleIrTypeFunction(ti, [])
#    f = m.add_function(ft, 'func')
#    bb = f.append_basic_block('entry')
#    b = Builder.new(bb)
#    b.ret(MiddleIrConstantInt(ti, 42))
#    fpm = FunctionPassManager.new(m)
#    fpm.add(TargetData.new(''))
#    fpm.add(PASS_ADCE)
#    fpm.initialize()
#    fpm.run(f)
#    fpm.finalize()
#
#
#def do_llvm_passes():
#    print("  Testing module llvm.passes")
#    do_passmanager()
#    do_functionpassmanager()
#
#def do_llvm_target():
#    print("  Testing module llvm.target")
#    from llvm import target
#
#    target.initialize_all()
#    target.print_registered_targets()
#    target.get_host_cpu_name()
#    target.get_default_triple()
#
#    tm = TargetMachine.new()
#    tm = TargetMachine.lookup("arm")
#    tm = TargetMachine.arm()
#    tm = TargetMachine.thumb()
#    tm = TargetMachine.x86()
#    tm = TargetMachine.x86_64()
#    tm.target_data
#    tm.target_name
#    tm.target_short_description
#    tm.triple
#    tm.cpu
#    tm.feature_string
#    tm.target
#
#    if llvm.version >= (3, 4):
#         tm.reg_info
#         tm.subtarget_info
#         tm.asm_info
#         tm.instr_info
#         tm.instr_analysis
#         tm.disassembler
#         tm.is_little_endian()
#
#def do_llvm_mc():
#    if llvm.version < (3, 4):
#        return
#
#    from llvm import target
#    from llvm import mc
#
#    target.initialize_all()
#    tm = TargetMachine.x86()
#    dasm = mc.Disassembler(tm)
#
#    for (offset, data, instr) in dasm.decode("c3", 0):
#        pass

def main():
    print("Testing package Middle-end")
    do_llvm()
    do_llvm_core()
#    do_llvm_ee()
#    do_llvm_passes()
#    do_llvm_target()
#    do_llvm_mc()

if __name__ == '__main__':
    main()

## to add:
## IntegerType
## FunctionType
## StructType
## ArrayType
## PointerType
## VectorType
## ConstantExpr
## ConstantAggregateZero
## ConstantInt
## ConstantFP
## ConstantArray
## ConstantStruct
## ConstantVector
## ConstantPointerNull
## MemoryBuffer

