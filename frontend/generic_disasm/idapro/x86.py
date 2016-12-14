# 
# Copyright (c) 2017 Sebastian Muniz
# 
# This code is part of point source decompiler
#

import idaapi


class InstructionSet:
    NN_aaa = idaapi.NN_aaa,         # ASCII Adjust after Addition
    NN_aad = idaapi.NN_aad,         # ASCII Adjust AX before Division
    NN_aam = idaapi.NN_aam,         # ASCII Adjust AX after Multiply
    NN_aas = idaapi.NN_aas,         # ASCII Adjust AL after Subtraction
    NN_adc = idaapi.NN_adc,         # Add with Carry
    NN_add = idaapi.NN_add,         # Add
    NN_and = idaapi.NN_and,         # Logical AND
    NN_arpl = idaapi.NN_arpl,           # Adjust RPL Field of Selector
    NN_bound = idaapi.NN_bound,         # Check Array Index Against Bounds
    NN_bsf = idaapi.NN_bsf,         # Bit Scan Forward
    NN_bsr = idaapi.NN_bsr,         # Bit Scan Reverse
    NN_bt = idaapi.NN_bt,           # Bit Test
    NN_btc = idaapi.NN_btc,         # Bit Test and Complement
    NN_btr = idaapi.NN_btr,         # Bit Test and Reset
    NN_bts = idaapi.NN_bts,         # Bit Test and Set
    NN_call = idaapi.NN_call,           # Call Procedure
    NN_callfi = idaapi.NN_callfi,           # Indirect Call Far Procedure
    NN_callni = idaapi.NN_callni,           # Indirect Call Near Procedure
    NN_cbw = idaapi.NN_cbw,         # AL -> AX (with sign)
    NN_cwde = idaapi.NN_cwde,           # AX -> EAX (with sign)
    NN_cdqe = idaapi.NN_cdqe,           # EAX -> RAX (with sign)
    NN_clc = idaapi.NN_clc,         # Clear Carry Flag
    NN_cld = idaapi.NN_cld,         # Clear Direction Flag
    NN_cli = idaapi.NN_cli,         # Clear Interrupt Flag
    NN_clts = idaapi.NN_clts,           # Clear Task-Switched Flag in CR0
    NN_cmc = idaapi.NN_cmc,         # Complement Carry Flag
    NN_cmp = idaapi.NN_cmp,         # Compare Two Operands
    NN_cmps = idaapi.NN_cmps,           # Compare Strings
    NN_cwd = idaapi.NN_cwd,         # AX -> DX:AX (with sign)
    NN_cdq = idaapi.NN_cdq,         # EAX -> EDX:EAX (with sign)
    NN_cqo = idaapi.NN_cqo,         # RAX -> RDX:RAX (with sign)
    NN_daa = idaapi.NN_daa,         # Decimal Adjust AL after Addition
    NN_das = idaapi.NN_das,         # Decimal Adjust AL after Subtraction
    NN_dec = idaapi.NN_dec,         # Decrement by 1
    NN_div = idaapi.NN_div,         # Unsigned Divide
    NN_enterw = idaapi.NN_enterw,           # Make Stack Frame for Procedure Parameters
    NN_enter = idaapi.NN_enter,         # Make Stack Frame for Procedure Parameters
    NN_enterd = idaapi.NN_enterd,           # Make Stack Frame for Procedure Parameters
    NN_enterq = idaapi.NN_enterq,           # Make Stack Frame for Procedure Parameters
    NN_hlt = idaapi.NN_hlt,         # Halt
    NN_idiv = idaapi.NN_idiv,           # Signed Divide
    NN_imul = idaapi.NN_imul,           # Signed Multiply
    NN_in = idaapi.NN_in,           # Input from Port
    NN_inc = idaapi.NN_inc,         # Increment by 1
    NN_ins = idaapi.NN_ins,         # Input Byte(s) from Port to String
    NN_int = idaapi.NN_int,         # Call to Interrupt Procedure
    NN_into = idaapi.NN_into,           # Call to Interrupt Procedure if Overflow Flag = 1
    NN_int3 = idaapi.NN_int3,           # Trap to Debugger
    NN_iretw = idaapi.NN_iretw,         # Interrupt Return
    NN_iret = idaapi.NN_iret,           # Interrupt Return
    NN_iretd = idaapi.NN_iretd,         # Interrupt Return (use32)
    NN_iretq = idaapi.NN_iretq,         # Interrupt Return (use64)
    NN_ja = idaapi.NN_ja,           # Jump if Above (CF=0 & ZF=0)
    NN_jae = idaapi.NN_jae,         # Jump if Above or Equal (CF=0)
    NN_jb = idaapi.NN_jb,           # Jump if Below (CF=1)
    NN_jbe = idaapi.NN_jbe,         # Jump if Below or Equal (CF=1 | ZF=1)
    NN_jc = idaapi.NN_jc,           # Jump if Carry (CF=1)
    NN_jcxz = idaapi.NN_jcxz,           # Jump if CX is 0
    NN_jecxz = idaapi.NN_jecxz,         # Jump if ECX is 0
    NN_jrcxz = idaapi.NN_jrcxz,         # Jump if RCX is 0
    NN_je = idaapi.NN_je,           # Jump if Equal (ZF=1)
    NN_jg = idaapi.NN_jg,           # Jump if Greater (ZF=0 & SF=OF)
    NN_jge = idaapi.NN_jge,         # Jump if Greater or Equal (SF=OF)
    NN_jl = idaapi.NN_jl,           # Jump if Less (SF!=OF)
    NN_jle = idaapi.NN_jle,         # Jump if Less or Equal (ZF=1 | SF!=OF)
    NN_jna = idaapi.NN_jna,         # Jump if Not Above (CF=1 | ZF=1)
    NN_jnae = idaapi.NN_jnae,           # Jump if Not Above or Equal (CF=1)
    NN_jnb = idaapi.NN_jnb,         # Jump if Not Below (CF=0)
    NN_jnbe = idaapi.NN_jnbe,           # Jump if Not Below or Equal (CF=0 & ZF=0)
    NN_jnc = idaapi.NN_jnc,         # Jump if Not Carry (CF=0)
    NN_jne = idaapi.NN_jne,         # Jump if Not Equal (ZF=0)
    NN_jng = idaapi.NN_jng,         # Jump if Not Greater (ZF=1 | SF!=OF)
    NN_jnge = idaapi.NN_jnge,           # Jump if Not Greater or Equal (ZF=1)
    NN_jnl = idaapi.NN_jnl,         # Jump if Not Less (SF=OF)
    NN_jnle = idaapi.NN_jnle,           # Jump if Not Less or Equal (ZF=0 & SF=OF)
    NN_jno = idaapi.NN_jno,         # Jump if Not Overflow (OF=0)
    NN_jnp = idaapi.NN_jnp,         # Jump if Not Parity (PF=0)
    NN_jns = idaapi.NN_jns,         # Jump if Not Sign (SF=0)
    NN_jnz = idaapi.NN_jnz,         # Jump if Not Zero (ZF=0)
    NN_jo = idaapi.NN_jo,           # Jump if Overflow (OF=1)
    NN_jp = idaapi.NN_jp,           # Jump if Parity (PF=1)
    NN_jpe = idaapi.NN_jpe,         # Jump if Parity Even (PF=1)
    NN_jpo = idaapi.NN_jpo,         # Jump if Parity Odd  (PF=0)
    NN_js = idaapi.NN_js,           # Jump if Sign (SF=1)
    NN_jz = idaapi.NN_jz,           # Jump if Zero (ZF=1)
    NN_jmp = idaapi.NN_jmp,         # Jump
    NN_jmpfi = idaapi.NN_jmpfi,         # Indirect Far Jump
    NN_jmpni = idaapi.NN_jmpni,         # Indirect Near Jump
    NN_jmpshort = idaapi.NN_jmpshort,           # Jump Short (not used)
    NN_lahf = idaapi.NN_lahf,           # Load Flags into AH Register
    NN_lar = idaapi.NN_lar,         # Load Access Right Byte
    NN_lea = idaapi.NN_lea,         # Load Effective Address
    NN_leavew = idaapi.NN_leavew,           # High Level Procedure Exit
    NN_leave = idaapi.NN_leave,         # High Level Procedure Exit
    NN_leaved = idaapi.NN_leaved,           # High Level Procedure Exit
    NN_leaveq = idaapi.NN_leaveq,           # High Level Procedure Exit
    NN_lgdt = idaapi.NN_lgdt,           # Load Global Descriptor Table Register
    NN_lidt = idaapi.NN_lidt,           # Load Interrupt Descriptor Table Register
    NN_lgs = idaapi.NN_lgs,         # Load Full Pointer to GS:xx
    NN_lss = idaapi.NN_lss,         # Load Full Pointer to SS:xx
    NN_lds = idaapi.NN_lds,         # Load Full Pointer to DS:xx
    NN_les = idaapi.NN_les,         # Load Full Pointer to ES:xx
    NN_lfs = idaapi.NN_lfs,         # Load Full Pointer to FS:xx
    NN_lldt = idaapi.NN_lldt,           # Load Local Descriptor Table Register
    NN_lmsw = idaapi.NN_lmsw,           # Load Machine Status Word
    NN_lock = idaapi.NN_lock,           # Assert LOCK# Signal Prefix
    NN_lods = idaapi.NN_lods,           # Load String
    NN_loopw = idaapi.NN_loopw,         # Loop while ECX != 0
    NN_loop = idaapi.NN_loop,           # Loop while CX != 0
    NN_loopd = idaapi.NN_loopd,         # Loop while ECX != 0
    NN_loopq = idaapi.NN_loopq,         # Loop while RCX != 0
    NN_loopwe = idaapi.NN_loopwe,           # Loop while CX != 0 and ZF=1
    NN_loope = idaapi.NN_loope,         # Loop while rCX != 0 and ZF=1
    NN_loopde = idaapi.NN_loopde,           # Loop while ECX != 0 and ZF=1
    NN_loopqe = idaapi.NN_loopqe,           # Loop while RCX != 0 and ZF=1
    NN_loopwne = idaapi.NN_loopwne,         # Loop while CX != 0 and ZF=0
    NN_loopne = idaapi.NN_loopne,           # Loop while rCX != 0 and ZF=0
    NN_loopdne = idaapi.NN_loopdne,         # Loop while ECX != 0 and ZF=0
    NN_loopqne = idaapi.NN_loopqne,         # Loop while RCX != 0 and ZF=0
    NN_lsl = idaapi.NN_lsl,         # Load Segment Limit
    NN_ltr = idaapi.NN_ltr,         # Load Task Register
    NN_mov = idaapi.NN_mov,         # Move Data
    NN_movsp = idaapi.NN_movsp,         # Move to/from Special Registers
    NN_movs = idaapi.NN_movs,           # Move Byte(s) from String to String
    NN_movsx = idaapi.NN_movsx,         # Move with Sign-Extend
    NN_movzx = idaapi.NN_movzx,         # Move with Zero-Extend
    NN_mul = idaapi.NN_mul,         # Unsigned Multiplication of AL or AX
    NN_neg = idaapi.NN_neg,         # Two's Complement Negation
    NN_nop = idaapi.NN_nop,         # No Operation
    NN_not = idaapi.NN_not,         # One's Complement Negation
    NN_or = idaapi.NN_or,           # Logical Inclusive OR
    NN_out = idaapi.NN_out,         # Output to Port
    NN_outs = idaapi.NN_outs,           # Output Byte(s) to Port
    NN_pop = idaapi.NN_pop,         # Pop a word from the Stack
    NN_popaw = idaapi.NN_popaw,         # Pop all General Registers
    NN_popa = idaapi.NN_popa,           # Pop all General Registers
    NN_popad = idaapi.NN_popad,         # Pop all General Registers (use32)
    NN_popaq = idaapi.NN_popaq,         # Pop all General Registers (use64)
    NN_popfw = idaapi.NN_popfw,         # Pop Stack into Flags Register
    NN_popf = idaapi.NN_popf,           # Pop Stack into Flags Register
    NN_popfd = idaapi.NN_popfd,         # Pop Stack into Eflags Register
    NN_popfq = idaapi.NN_popfq,         # Pop Stack into Rflags Register
    NN_push = idaapi.NN_push,           # Push Operand onto the Stack
    NN_pushaw = idaapi.NN_pushaw,           # Push all General Registers
    NN_pusha = idaapi.NN_pusha,         # Push all General Registers
    NN_pushad = idaapi.NN_pushad,           # Push all General Registers (use32)
    NN_pushaq = idaapi.NN_pushaq,           # Push all General Registers (use64)
    NN_pushfw = idaapi.NN_pushfw,           # Push Flags Register onto the Stack
    NN_pushf = idaapi.NN_pushf,         # Push Flags Register onto the Stack
    NN_pushfd = idaapi.NN_pushfd,           # Push Flags Register onto the Stack (use32)
    NN_pushfq = idaapi.NN_pushfq,           # Push Flags Register onto the Stack (use64)
    NN_rcl = idaapi.NN_rcl,         # Rotate Through Carry Left
    NN_rcr = idaapi.NN_rcr,         # Rotate Through Carry Right
    NN_rol = idaapi.NN_rol,         # Rotate Left
    NN_ror = idaapi.NN_ror,         # Rotate Right
    NN_rep = idaapi.NN_rep,         # Repeat String Operation
    NN_repe = idaapi.NN_repe,           # Repeat String Operation while ZF=1
    NN_repne = idaapi.NN_repne,         # Repeat String Operation while ZF=0
    NN_retn = idaapi.NN_retn,           # Return Near from Procedure
    NN_retf = idaapi.NN_retf,           # Return Far from Procedure
    NN_sahf = idaapi.NN_sahf,           # Store AH into Flags Register
    NN_sal = idaapi.NN_sal,         # Shift Arithmetic Left
    NN_sar = idaapi.NN_sar,         # Shift Arithmetic Right
    NN_shl = idaapi.NN_shl,         # Shift Logical Left
    NN_shr = idaapi.NN_shr,         # Shift Logical Right
    NN_sbb = idaapi.NN_sbb,         # Integer Subtraction with Borrow
    NN_scas = idaapi.NN_scas,           # Compare String
    NN_seta = idaapi.NN_seta,           # Set Byte if Above (CF=0 & ZF=0)
    NN_setae = idaapi.NN_setae,         # Set Byte if Above or Equal (CF=0)
    NN_setb = idaapi.NN_setb,           # Set Byte if Below (CF=1)
    NN_setbe = idaapi.NN_setbe,         # Set Byte if Below or Equal (CF=1 | ZF=1)
    NN_setc = idaapi.NN_setc,           # Set Byte if Carry (CF=1)
    NN_sete = idaapi.NN_sete,           # Set Byte if Equal (ZF=1)
    NN_setg = idaapi.NN_setg,           # Set Byte if Greater (ZF=0 & SF=OF)
    NN_setge = idaapi.NN_setge,         # Set Byte if Greater or Equal (SF=OF)
    NN_setl = idaapi.NN_setl,           # Set Byte if Less (SF!=OF)
    NN_setle = idaapi.NN_setle,         # Set Byte if Less or Equal (ZF=1 | SF!=OF)
    NN_setna = idaapi.NN_setna,         # Set Byte if Not Above (CF=1 | ZF=1)
    NN_setnae = idaapi.NN_setnae,           # Set Byte if Not Above or Equal (CF=1)
    NN_setnb = idaapi.NN_setnb,         # Set Byte if Not Below (CF=0)
    NN_setnbe = idaapi.NN_setnbe,           # Set Byte if Not Below or Equal (CF=0 & ZF=0)
    NN_setnc = idaapi.NN_setnc,         # Set Byte if Not Carry (CF=0)
    NN_setne = idaapi.NN_setne,         # Set Byte if Not Equal (ZF=0)
    NN_setng = idaapi.NN_setng,         # Set Byte if Not Greater (ZF=1 | SF!=OF)
    NN_setnge = idaapi.NN_setnge,           # Set Byte if Not Greater or Equal (ZF=1)
    NN_setnl = idaapi.NN_setnl,         # Set Byte if Not Less (SF=OF)
    NN_setnle = idaapi.NN_setnle,           # Set Byte if Not Less or Equal (ZF=0 & SF=OF)
    NN_setno = idaapi.NN_setno,         # Set Byte if Not Overflow (OF=0)
    NN_setnp = idaapi.NN_setnp,         # Set Byte if Not Parity (PF=0)
    NN_setns = idaapi.NN_setns,         # Set Byte if Not Sign (SF=0)
    NN_setnz = idaapi.NN_setnz,         # Set Byte if Not Zero (ZF=0)
    NN_seto = idaapi.NN_seto,           # Set Byte if Overflow (OF=1)
    NN_setp = idaapi.NN_setp,           # Set Byte if Parity (PF=1)
    NN_setpe = idaapi.NN_setpe,         # Set Byte if Parity Even (PF=1)
    NN_setpo = idaapi.NN_setpo,         # Set Byte if Parity Odd  (PF=0)
    NN_sets = idaapi.NN_sets,           # Set Byte if Sign (SF=1)
    NN_setz = idaapi.NN_setz,           # Set Byte if Zero (ZF=1)
    NN_sgdt = idaapi.NN_sgdt,           # Store Global Descriptor Table Register
    NN_sidt = idaapi.NN_sidt,           # Store Interrupt Descriptor Table Register
    NN_shld = idaapi.NN_shld,           # Double Precision Shift Left
    NN_shrd = idaapi.NN_shrd,           # Double Precision Shift Right
    NN_sldt = idaapi.NN_sldt,           # Store Local Descriptor Table Register
    NN_smsw = idaapi.NN_smsw,           # Store Machine Status Word
    NN_stc = idaapi.NN_stc,         # Set Carry Flag
    NN_std = idaapi.NN_std,         # Set Direction Flag
    NN_sti = idaapi.NN_sti,         # Set Interrupt Flag
    NN_stos = idaapi.NN_stos,           # Store String
    NN_str = idaapi.NN_str,         # Store Task Register
    NN_sub = idaapi.NN_sub,         # Integer Subtraction
    NN_test = idaapi.NN_test,           # Logical Compare
    NN_verr = idaapi.NN_verr,           # Verify a Segment for Reading
    NN_verw = idaapi.NN_verw,           # Verify a Segment for Writing
    NN_wait = idaapi.NN_wait,           # Wait until BUSY# Pin is Inactive (HIGH)
    NN_xchg = idaapi.NN_xchg,           # Exchange Register/Memory with Register
    NN_xlat = idaapi.NN_xlat,           # Table Lookup Translation
    NN_xor = idaapi.NN_xor,         # Logical Exclusive OR

    #
    #      486 instructions
    #

    NN_cmpxchg = idaapi.NN_cmpxchg,         # Compare and Exchange
    NN_bswap = idaapi.NN_bswap,         # Swap bits in EAX
    NN_xadd = idaapi.NN_xadd,           # t<-dest; dest<-src+dest; src<-t
    NN_invd = idaapi.NN_invd,           # Invalidate Data Cache
    NN_wbinvd = idaapi.NN_wbinvd,           # Invalidate Data Cache (write changes)
    NN_invlpg = idaapi.NN_invlpg,           # Invalidate TLB entry

    #
    #      Pentium instructions
    #

    NN_rdmsr = idaapi.NN_rdmsr,         # Read Machine Status Register
    NN_wrmsr = idaapi.NN_wrmsr,         # Write Machine Status Register
    NN_cpuid = idaapi.NN_cpuid,         # Get CPU ID
    NN_cmpxchg8b = idaapi.NN_cmpxchg8b,         # Compare and Exchange Eight Bytes
    NN_rdtsc = idaapi.NN_rdtsc,         # Read Time Stamp Counter
    NN_rsm = idaapi.NN_rsm,         # Resume from System Management Mode

    #
    #      Pentium Pro instructions
    #

    NN_cmova = idaapi.NN_cmova,         # Move if Above (CF=0 & ZF=0)
    NN_cmovb = idaapi.NN_cmovb,         # Move if Below (CF=1)
    NN_cmovbe = idaapi.NN_cmovbe,           # Move if Below or Equal (CF=1 | ZF=1)
    NN_cmovg = idaapi.NN_cmovg,         # Move if Greater (ZF=0 & SF=OF)
    NN_cmovge = idaapi.NN_cmovge,           # Move if Greater or Equal (SF=OF)
    NN_cmovl = idaapi.NN_cmovl,         # Move if Less (SF!=OF)
    NN_cmovle = idaapi.NN_cmovle,           # Move if Less or Equal (ZF=1 | SF!=OF)
    NN_cmovnb = idaapi.NN_cmovnb,           # Move if Not Below (CF=0)
    NN_cmovno = idaapi.NN_cmovno,           # Move if Not Overflow (OF=0)
    NN_cmovnp = idaapi.NN_cmovnp,           # Move if Not Parity (PF=0)
    NN_cmovns = idaapi.NN_cmovns,           # Move if Not Sign (SF=0)
    NN_cmovnz = idaapi.NN_cmovnz,           # Move if Not Zero (ZF=0)
    NN_cmovo = idaapi.NN_cmovo,         # Move if Overflow (OF=1)
    NN_cmovp = idaapi.NN_cmovp,         # Move if Parity (PF=1)
    NN_cmovs = idaapi.NN_cmovs,         # Move if Sign (SF=1)
    NN_cmovz = idaapi.NN_cmovz,         # Move if Zero (ZF=1)
    NN_fcmovb = idaapi.NN_fcmovb,           # Floating Move if Below
    NN_fcmove = idaapi.NN_fcmove,           # Floating Move if Equal
    NN_fcmovbe = idaapi.NN_fcmovbe,         # Floating Move if Below or Equal
    NN_fcmovu = idaapi.NN_fcmovu,           # Floating Move if Unordered
    NN_fcmovnb = idaapi.NN_fcmovnb,         # Floating Move if Not Below
    NN_fcmovne = idaapi.NN_fcmovne,         # Floating Move if Not Equal
    NN_fcmovnbe = idaapi.NN_fcmovnbe,           # Floating Move if Not Below or Equal
    NN_fcmovnu = idaapi.NN_fcmovnu,         # Floating Move if Not Unordered
    NN_fcomi = idaapi.NN_fcomi,         # FP Compare, result in EFLAGS
    NN_fucomi = idaapi.NN_fucomi,           # FP Unordered Compare, result in EFLAGS
    NN_fcomip = idaapi.NN_fcomip,           # FP Compare, result in EFLAGS, pop stack
    NN_fucomip = idaapi.NN_fucomip,         # FP Unordered Compare, result in EFLAGS, pop stack
    NN_rdpmc = idaapi.NN_rdpmc,         # Read Performance Monitor Counter

    #
    #      FPP instructuions
    #

    NN_fld = idaapi.NN_fld,         # Load Real
    NN_fst = idaapi.NN_fst,         # Store Real
    NN_fstp = idaapi.NN_fstp,           # Store Real and Pop
    NN_fxch = idaapi.NN_fxch,           # Exchange Registers
    NN_fild = idaapi.NN_fild,           # Load Integer
    NN_fist = idaapi.NN_fist,           # Store Integer
    NN_fistp = idaapi.NN_fistp,         # Store Integer and Pop
    NN_fbld = idaapi.NN_fbld,           # Load BCD
    NN_fbstp = idaapi.NN_fbstp,         # Store BCD and Pop
    NN_fadd = idaapi.NN_fadd,           # Add Real
    NN_faddp = idaapi.NN_faddp,         # Add Real and Pop
    NN_fiadd = idaapi.NN_fiadd,         # Add Integer
    NN_fsub = idaapi.NN_fsub,           # Subtract Real
    NN_fsubp = idaapi.NN_fsubp,         # Subtract Real and Pop
    NN_fisub = idaapi.NN_fisub,         # Subtract Integer
    NN_fsubr = idaapi.NN_fsubr,         # Subtract Real Reversed
    NN_fsubrp = idaapi.NN_fsubrp,           # Subtract Real Reversed and Pop
    NN_fisubr = idaapi.NN_fisubr,           # Subtract Integer Reversed
    NN_fmul = idaapi.NN_fmul,           # Multiply Real
    NN_fmulp = idaapi.NN_fmulp,         # Multiply Real and Pop
    NN_fimul = idaapi.NN_fimul,         # Multiply Integer
    NN_fdiv = idaapi.NN_fdiv,           # Divide Real
    NN_fdivp = idaapi.NN_fdivp,         # Divide Real and Pop
    NN_fidiv = idaapi.NN_fidiv,         # Divide Integer
    NN_fdivr = idaapi.NN_fdivr,         # Divide Real Reversed
    NN_fdivrp = idaapi.NN_fdivrp,           # Divide Real Reversed and Pop
    NN_fidivr = idaapi.NN_fidivr,           # Divide Integer Reversed
    NN_fsqrt = idaapi.NN_fsqrt,         # Square Root
    NN_fscale = idaapi.NN_fscale,           # Scale:  st(0) <- st(0) * 2^st(1)
    NN_fprem = idaapi.NN_fprem,         # Partial Remainder
    NN_frndint = idaapi.NN_frndint,         # Round to Integer
    NN_fxtract = idaapi.NN_fxtract,         # Extract exponent and significand
    NN_fabs = idaapi.NN_fabs,           # Absolute value
    NN_fchs = idaapi.NN_fchs,           # Change Sign
    NN_fcom = idaapi.NN_fcom,           # Compare Real
    NN_fcomp = idaapi.NN_fcomp,         # Compare Real and Pop
    NN_fcompp = idaapi.NN_fcompp,           # Compare Real and Pop Twice
    NN_ficom = idaapi.NN_ficom,         # Compare Integer
    NN_ficomp = idaapi.NN_ficomp,           # Compare Integer and Pop
    NN_ftst = idaapi.NN_ftst,           # Test
    NN_fxam = idaapi.NN_fxam,           # Examine
    NN_fptan = idaapi.NN_fptan,         # Partial tangent
    NN_fpatan = idaapi.NN_fpatan,           # Partial arctangent
    NN_f2xm1 = idaapi.NN_f2xm1,         # 2^x - 1
    NN_fyl2x = idaapi.NN_fyl2x,         # Y * lg2(X)
    NN_fyl2xp1 = idaapi.NN_fyl2xp1,         # Y * lg2(X+1)
    NN_fldz = idaapi.NN_fldz,           # Load +0.0
    NN_fld1 = idaapi.NN_fld1,           # Load +1.0
    NN_fldpi = idaapi.NN_fldpi,         # Load PI=3.14...
    NN_fldl2t = idaapi.NN_fldl2t,           # Load lg2(10)
    NN_fldl2e = idaapi.NN_fldl2e,           # Load lg2(e)
    NN_fldlg2 = idaapi.NN_fldlg2,           # Load lg10(2)
    NN_fldln2 = idaapi.NN_fldln2,           # Load ln(2)
    NN_finit = idaapi.NN_finit,         # Initialize Processor
    NN_fninit = idaapi.NN_fninit,           # Initialize Processor (no wait)
    NN_fsetpm = idaapi.NN_fsetpm,           # Set Protected Mode
    NN_fldcw = idaapi.NN_fldcw,         # Load Control Word
    NN_fstcw = idaapi.NN_fstcw,         # Store Control Word
    NN_fnstcw = idaapi.NN_fnstcw,           # Store Control Word (no wait)
    NN_fstsw = idaapi.NN_fstsw,         # Store Status Word
    NN_fnstsw = idaapi.NN_fnstsw,           # Store Status Word (no wait)
    NN_fclex = idaapi.NN_fclex,         # Clear Exceptions
    NN_fnclex = idaapi.NN_fnclex,           # Clear Exceptions (no wait)
    NN_fstenv = idaapi.NN_fstenv,           # Store Environment
    NN_fnstenv = idaapi.NN_fnstenv,         # Store Environment (no wait)
    NN_fldenv = idaapi.NN_fldenv,           # Load Environment
    NN_fsave = idaapi.NN_fsave,         # Save State
    NN_fnsave = idaapi.NN_fnsave,           # Save State (no wait)
    NN_frstor = idaapi.NN_frstor,           # Restore State
    NN_fincstp = idaapi.NN_fincstp,         # Increment Stack Pointer
    NN_fdecstp = idaapi.NN_fdecstp,         # Decrement Stack Pointer
    NN_ffree = idaapi.NN_ffree,         # Free Register
    NN_fnop = idaapi.NN_fnop,           # No Operation
    NN_feni = idaapi.NN_feni,           # (8087 only)
    NN_fneni = idaapi.NN_fneni,         # (no wait) (8087 only)
    NN_fdisi = idaapi.NN_fdisi,         # (8087 only)
    NN_fndisi = idaapi.NN_fndisi,           # (no wait) (8087 only)

    #
    #      80387 instructions
    #

    NN_fprem1 = idaapi.NN_fprem1,           # Partial Remainder ( < half )
    NN_fsincos = idaapi.NN_fsincos,         # t<-cos(st); st<-sin(st); push t
    NN_fsin = idaapi.NN_fsin,           # Sine
    NN_fcos = idaapi.NN_fcos,           # Cosine
    NN_fucom = idaapi.NN_fucom,         # Compare Unordered Real
    NN_fucomp = idaapi.NN_fucomp,           # Compare Unordered Real and Pop
    NN_fucompp = idaapi.NN_fucompp,         # Compare Unordered Real and Pop Twice

    #
    #      Instructions added 28.02.96
    #

    NN_setalc = idaapi.NN_setalc,           # Set AL to Carry Flag
    NN_svdc = idaapi.NN_svdc,           # Save Register and Descriptor
    NN_rsdc = idaapi.NN_rsdc,           # Restore Register and Descriptor
    NN_svldt = idaapi.NN_svldt,         # Save LDTR and Descriptor
    NN_rsldt = idaapi.NN_rsldt,         # Restore LDTR and Descriptor
    NN_svts = idaapi.NN_svts,           # Save TR and Descriptor
    NN_rsts = idaapi.NN_rsts,           # Restore TR and Descriptor
    NN_icebp = idaapi.NN_icebp,         # ICE Break Point
    NN_loadall = idaapi.NN_loadall,         # Load the entire CPU state from ES:EDI

    #
    #      MMX instructions
    #

    NN_emms = idaapi.NN_emms,           # Empty MMX state
    NN_movd = idaapi.NN_movd,           # Move 32 bits
    NN_movq = idaapi.NN_movq,           # Move 64 bits
    NN_packsswb = idaapi.NN_packsswb,           # Pack with Signed Saturation (Word->Byte)
    NN_packssdw = idaapi.NN_packssdw,           # Pack with Signed Saturation (Dword->Word)
    NN_packuswb = idaapi.NN_packuswb,           # Pack with Unsigned Saturation (Word->Byte)
    NN_paddb = idaapi.NN_paddb,         # Packed Add Byte
    NN_paddw = idaapi.NN_paddw,         # Packed Add Word
    NN_paddd = idaapi.NN_paddd,         # Packed Add Dword
    NN_paddsb = idaapi.NN_paddsb,           # Packed Add with Saturation (Byte)
    NN_paddsw = idaapi.NN_paddsw,           # Packed Add with Saturation (Word)
    NN_paddusb = idaapi.NN_paddusb,         # Packed Add Unsigned with Saturation (Byte)
    NN_paddusw = idaapi.NN_paddusw,         # Packed Add Unsigned with Saturation (Word)
    NN_pand = idaapi.NN_pand,           # Bitwise Logical And
    NN_pandn = idaapi.NN_pandn,         # Bitwise Logical And Not
    NN_pcmpeqb = idaapi.NN_pcmpeqb,         # Packed Compare for Equal (Byte)
    NN_pcmpeqw = idaapi.NN_pcmpeqw,         # Packed Compare for Equal (Word)
    NN_pcmpeqd = idaapi.NN_pcmpeqd,         # Packed Compare for Equal (Dword)
    NN_pcmpgtb = idaapi.NN_pcmpgtb,         # Packed Compare for Greater Than (Byte)
    NN_pcmpgtw = idaapi.NN_pcmpgtw,         # Packed Compare for Greater Than (Word)
    NN_pcmpgtd = idaapi.NN_pcmpgtd,         # Packed Compare for Greater Than (Dword)
    NN_pmaddwd = idaapi.NN_pmaddwd,         # Packed Multiply and Add
    NN_pmulhw = idaapi.NN_pmulhw,           # Packed Multiply High
    NN_pmullw = idaapi.NN_pmullw,           # Packed Multiply Low
    NN_por = idaapi.NN_por,         # Bitwise Logical Or
    NN_psllw = idaapi.NN_psllw,         # Packed Shift Left Logical (Word)
    NN_pslld = idaapi.NN_pslld,         # Packed Shift Left Logical (Dword)
    NN_psllq = idaapi.NN_psllq,         # Packed Shift Left Logical (Qword)
    NN_psraw = idaapi.NN_psraw,         # Packed Shift Right Arithmetic (Word)
    NN_psrad = idaapi.NN_psrad,         # Packed Shift Right Arithmetic (Dword)
    NN_psrlw = idaapi.NN_psrlw,         # Packed Shift Right Logical (Word)
    NN_psrld = idaapi.NN_psrld,         # Packed Shift Right Logical (Dword)
    NN_psrlq = idaapi.NN_psrlq,         # Packed Shift Right Logical (Qword)
    NN_psubb = idaapi.NN_psubb,         # Packed Subtract Byte
    NN_psubw = idaapi.NN_psubw,         # Packed Subtract Word
    NN_psubd = idaapi.NN_psubd,         # Packed Subtract Dword
    NN_psubsb = idaapi.NN_psubsb,           # Packed Subtract with Saturation (Byte)
    NN_psubsw = idaapi.NN_psubsw,           # Packed Subtract with Saturation (Word)
    NN_psubusb = idaapi.NN_psubusb,         # Packed Subtract Unsigned with Saturation (Byte)
    NN_psubusw = idaapi.NN_psubusw,         # Packed Subtract Unsigned with Saturation (Word)
    NN_punpckhbw = idaapi.NN_punpckhbw,         # Unpack High Packed Data (Byte->Word)
    NN_punpckhwd = idaapi.NN_punpckhwd,         # Unpack High Packed Data (Word->Dword)
    NN_punpckhdq = idaapi.NN_punpckhdq,         # Unpack High Packed Data (Dword->Qword)
    NN_punpcklbw = idaapi.NN_punpcklbw,         # Unpack Low Packed Data (Byte->Word)
    NN_punpcklwd = idaapi.NN_punpcklwd,         # Unpack Low Packed Data (Word->Dword)
    NN_punpckldq = idaapi.NN_punpckldq,         # Unpack Low Packed Data (Dword->Qword)
    NN_pxor = idaapi.NN_pxor,           # Bitwise Logical Exclusive Or

    #
    #      Undocumented Deschutes processor instructions
    #

    NN_fxsave = idaapi.NN_fxsave,           # Fast save FP context
    NN_fxrstor = idaapi.NN_fxrstor,         # Fast restore FP context

    #      Pentium II instructions

    NN_sysenter = idaapi.NN_sysenter,           # Fast Transition to System Call Entry Point
    NN_sysexit = idaapi.NN_sysexit,         # Fast Transition from System Call Entry Point

    #      3DNow! instructions

    NN_pavgusb = idaapi.NN_pavgusb,         # Packed 8-bit Unsigned Integer Averaging
    NN_pfadd = idaapi.NN_pfadd,         # Packed Floating-Point Addition
    NN_pfsub = idaapi.NN_pfsub,         # Packed Floating-Point Subtraction
    NN_pfsubr = idaapi.NN_pfsubr,           # Packed Floating-Point Reverse Subtraction
    NN_pfacc = idaapi.NN_pfacc,         # Packed Floating-Point Accumulate
    NN_pfcmpge = idaapi.NN_pfcmpge,         # Packed Floating-Point Comparison, Greater or Equal
    NN_pfcmpgt = idaapi.NN_pfcmpgt,         # Packed Floating-Point Comparison, Greater
    NN_pfcmpeq = idaapi.NN_pfcmpeq,         # Packed Floating-Point Comparison, Equal
    NN_pfmin = idaapi.NN_pfmin,         # Packed Floating-Point Minimum
    NN_pfmax = idaapi.NN_pfmax,         # Packed Floating-Point Maximum
    NN_pi2fd = idaapi.NN_pi2fd,         # Packed 32-bit Integer to Floating-Point
    NN_pf2id = idaapi.NN_pf2id,         # Packed Floating-Point to 32-bit Integer
    NN_pfrcp = idaapi.NN_pfrcp,         # Packed Floating-Point Reciprocal Approximation
    NN_pfrsqrt = idaapi.NN_pfrsqrt,         # Packed Floating-Point Reciprocal Square Root Approximation
    NN_pfmul = idaapi.NN_pfmul,         # Packed Floating-Point Multiplication
    NN_pfrcpit1 = idaapi.NN_pfrcpit1,           # Packed Floating-Point Reciprocal First Iteration Step
    NN_pfrsqit1 = idaapi.NN_pfrsqit1,           # Packed Floating-Point Reciprocal Square Root First Iteration Step
    NN_pfrcpit2 = idaapi.NN_pfrcpit2,           # Packed Floating-Point Reciprocal Second Iteration Step
    NN_pmulhrw = idaapi.NN_pmulhrw,         # Packed Floating-Point 16-bit Integer Multiply with rounding
    NN_femms = idaapi.NN_femms,         # Faster entry/exit of the MMX or floating-point state
    NN_prefetch = idaapi.NN_prefetch,           # Prefetch at least a 32-byte line into L1 data cache
    NN_prefetchw = idaapi.NN_prefetchw,         # Prefetch processor cache line into L1 data cache (mark as modified)


    #      Pentium III instructions

    NN_addps = idaapi.NN_addps,         # Packed Single-FP Add
    NN_addss = idaapi.NN_addss,         # Scalar Single-FP Add
    NN_andnps = idaapi.NN_andnps,           # Bitwise Logical And Not for Single-FP
    NN_andps = idaapi.NN_andps,         # Bitwise Logical And for Single-FP
    NN_cmpps = idaapi.NN_cmpps,         # Packed Single-FP Compare
    NN_cmpss = idaapi.NN_cmpss,         # Scalar Single-FP Compare
    NN_comiss = idaapi.NN_comiss,           # Scalar Ordered Single-FP Compare and Set EFLAGS
    NN_cvtpi2ps = idaapi.NN_cvtpi2ps,           # Packed signed INT32 to Packed Single-FP conversion
    NN_cvtps2pi = idaapi.NN_cvtps2pi,           # Packed Single-FP to Packed INT32 conversion
    NN_cvtsi2ss = idaapi.NN_cvtsi2ss,           # Scalar signed INT32 to Single-FP conversion
    NN_cvtss2si = idaapi.NN_cvtss2si,           # Scalar Single-FP to signed INT32 conversion
    NN_cvttps2pi = idaapi.NN_cvttps2pi,         # Packed Single-FP to Packed INT32 conversion (truncate)
    NN_cvttss2si = idaapi.NN_cvttss2si,         # Scalar Single-FP to signed INT32 conversion (truncate)
    NN_divps = idaapi.NN_divps,         # Packed Single-FP Divide
    NN_divss = idaapi.NN_divss,         # Scalar Single-FP Divide
    NN_ldmxcsr = idaapi.NN_ldmxcsr,         # Load Streaming SIMD Extensions Technology Control/Status Register
    NN_maxps = idaapi.NN_maxps,         # Packed Single-FP Maximum
    NN_maxss = idaapi.NN_maxss,         # Scalar Single-FP Maximum
    NN_minps = idaapi.NN_minps,         # Packed Single-FP Minimum
    NN_minss = idaapi.NN_minss,         # Scalar Single-FP Minimum
    NN_movaps = idaapi.NN_movaps,           # Move Aligned Four Packed Single-FP
    NN_movhlps = idaapi.NN_movhlps,         # Move High to Low Packed Single-FP
    NN_movhps = idaapi.NN_movhps,           # Move High Packed Single-FP
    NN_movlhps = idaapi.NN_movlhps,         # Move Low to High Packed Single-FP
    NN_movlps = idaapi.NN_movlps,           # Move Low Packed Single-FP
    NN_movmskps = idaapi.NN_movmskps,           # Move Mask to Register
    NN_movss = idaapi.NN_movss,         # Move Scalar Single-FP
    NN_movups = idaapi.NN_movups,           # Move Unaligned Four Packed Single-FP
    NN_mulps = idaapi.NN_mulps,         # Packed Single-FP Multiply
    NN_mulss = idaapi.NN_mulss,         # Scalar Single-FP Multiply
    NN_orps = idaapi.NN_orps,           # Bitwise Logical OR for Single-FP Data
    NN_rcpps = idaapi.NN_rcpps,         # Packed Single-FP Reciprocal
    NN_rcpss = idaapi.NN_rcpss,         # Scalar Single-FP Reciprocal
    NN_rsqrtps = idaapi.NN_rsqrtps,         # Packed Single-FP Square Root Reciprocal
    NN_rsqrtss = idaapi.NN_rsqrtss,         # Scalar Single-FP Square Root Reciprocal
    NN_shufps = idaapi.NN_shufps,           # Shuffle Single-FP
    NN_sqrtps = idaapi.NN_sqrtps,           # Packed Single-FP Square Root
    NN_sqrtss = idaapi.NN_sqrtss,           # Scalar Single-FP Square Root
    NN_stmxcsr = idaapi.NN_stmxcsr,         # Store Streaming SIMD Extensions Technology Control/Status Register
    NN_subps = idaapi.NN_subps,         # Packed Single-FP Subtract
    NN_subss = idaapi.NN_subss,         # Scalar Single-FP Subtract
    NN_ucomiss = idaapi.NN_ucomiss,         # Scalar Unordered Single-FP Compare and Set EFLAGS
    NN_unpckhps = idaapi.NN_unpckhps,           # Unpack High Packed Single-FP Data
    NN_unpcklps = idaapi.NN_unpcklps,           # Unpack Low Packed Single-FP Data
    NN_xorps = idaapi.NN_xorps,         # Bitwise Logical XOR for Single-FP Data
    NN_pavgb = idaapi.NN_pavgb,         # Packed Average (Byte)
    NN_pavgw = idaapi.NN_pavgw,         # Packed Average (Word)
    NN_pextrw = idaapi.NN_pextrw,           # Extract Word
    NN_pinsrw = idaapi.NN_pinsrw,           # Insert Word
    NN_pmaxsw = idaapi.NN_pmaxsw,           # Packed Signed Integer Word Maximum
    NN_pmaxub = idaapi.NN_pmaxub,           # Packed Unsigned Integer Byte Maximum
    NN_pminsw = idaapi.NN_pminsw,           # Packed Signed Integer Word Minimum
    NN_pminub = idaapi.NN_pminub,           # Packed Unsigned Integer Byte Minimum
    NN_pmovmskb = idaapi.NN_pmovmskb,           # Move Byte Mask to Integer
    NN_pmulhuw = idaapi.NN_pmulhuw,         # Packed Multiply High Unsigned
    NN_psadbw = idaapi.NN_psadbw,           # Packed Sum of Absolute Differences
    NN_pshufw = idaapi.NN_pshufw,           # Packed Shuffle Word
    NN_maskmovq = idaapi.NN_maskmovq,           # Byte Mask write
    NN_movntps = idaapi.NN_movntps,         # Move Aligned Four Packed Single-FP Non Temporal
    NN_movntq = idaapi.NN_movntq,           # Move 64 Bits Non Temporal
    NN_prefetcht0 = idaapi.NN_prefetcht0,           # Prefetch to all cache levels
    NN_prefetcht1 = idaapi.NN_prefetcht1,           # Prefetch to all cache levels
    NN_prefetcht2 = idaapi.NN_prefetcht2,           # Prefetch to L2 cache
    NN_prefetchnta = idaapi.NN_prefetchnta,         # Prefetch to L1 cache
    NN_sfence = idaapi.NN_sfence,           # Store Fence

    # Pentium III Pseudo instructions

    NN_cmpeqps = idaapi.NN_cmpeqps,         # Packed Single-FP Compare EQ
    NN_cmpltps = idaapi.NN_cmpltps,         # Packed Single-FP Compare LT
    NN_cmpleps = idaapi.NN_cmpleps,         # Packed Single-FP Compare LE
    NN_cmpunordps = idaapi.NN_cmpunordps,           # Packed Single-FP Compare UNORD
    NN_cmpneqps = idaapi.NN_cmpneqps,           # Packed Single-FP Compare NOT EQ
    NN_cmpnltps = idaapi.NN_cmpnltps,           # Packed Single-FP Compare NOT LT
    NN_cmpnleps = idaapi.NN_cmpnleps,           # Packed Single-FP Compare NOT LE
    NN_cmpordps = idaapi.NN_cmpordps,           # Packed Single-FP Compare ORDERED
    NN_cmpeqss = idaapi.NN_cmpeqss,         # Scalar Single-FP Compare EQ
    NN_cmpltss = idaapi.NN_cmpltss,         # Scalar Single-FP Compare LT
    NN_cmpless = idaapi.NN_cmpless,         # Scalar Single-FP Compare LE
    NN_cmpunordss = idaapi.NN_cmpunordss,           # Scalar Single-FP Compare UNORD
    NN_cmpneqss = idaapi.NN_cmpneqss,           # Scalar Single-FP Compare NOT EQ
    NN_cmpnltss = idaapi.NN_cmpnltss,           # Scalar Single-FP Compare NOT LT
    NN_cmpnless = idaapi.NN_cmpnless,           # Scalar Single-FP Compare NOT LE
    NN_cmpordss = idaapi.NN_cmpordss,           # Scalar Single-FP Compare ORDERED

    # AMD K7 instructions

    NN_pf2iw = idaapi.NN_pf2iw,         # Packed Floating-Point to Integer with Sign Extend
    NN_pfnacc = idaapi.NN_pfnacc,           # Packed Floating-Point Negative Accumulate
    NN_pfpnacc = idaapi.NN_pfpnacc,         # Packed Floating-Point Mixed Positive-Negative Accumulate
    NN_pi2fw = idaapi.NN_pi2fw,         # Packed 16-bit Integer to Floating-Point
    NN_pswapd = idaapi.NN_pswapd,           # Packed Swap Double Word

    # Undocumented FP instructions (thanks to norbert.juffa@adm.com)

    NN_fstp1 = idaapi.NN_fstp1,         # Alias of Store Real and Pop
    NN_fcom2 = idaapi.NN_fcom2,         # Alias of Compare Real
    NN_fcomp3 = idaapi.NN_fcomp3,           # Alias of Compare Real and Pop
    NN_fxch4 = idaapi.NN_fxch4,         # Alias of Exchange Registers
    NN_fcomp5 = idaapi.NN_fcomp5,           # Alias of Compare Real and Pop
    NN_ffreep = idaapi.NN_ffreep,           # Free Register and Pop
    NN_fxch7 = idaapi.NN_fxch7,         # Alias of Exchange Registers
    NN_fstp8 = idaapi.NN_fstp8,         # Alias of Store Real and Pop
    NN_fstp9 = idaapi.NN_fstp9,         # Alias of Store Real and Pop

    # Pentium 4 instructions

    NN_addpd = idaapi.NN_addpd,         # Add Packed Double-Precision Floating-Point Values
    NN_addsd = idaapi.NN_addsd,         # Add Scalar Double-Precision Floating-Point Values
    NN_andnpd = idaapi.NN_andnpd,           # Bitwise Logical AND NOT of Packed Double-Precision Floating-Point Values
    NN_andpd = idaapi.NN_andpd,         # Bitwise Logical AND of Packed Double-Precision Floating-Point Values
    NN_clflush = idaapi.NN_clflush,         # Flush Cache Line
    NN_cmppd = idaapi.NN_cmppd,         # Compare Packed Double-Precision Floating-Point Values
    NN_cmpsd = idaapi.NN_cmpsd,         # Compare Scalar Double-Precision Floating-Point Values
    NN_comisd = idaapi.NN_comisd,           # Compare Scalar Ordered Double-Precision Floating-Point Values and Set EFLAGS
    NN_cvtdq2pd = idaapi.NN_cvtdq2pd,           # Convert Packed Doubleword Integers to Packed Single-Precision Floating-Point Values
    NN_cvtdq2ps = idaapi.NN_cvtdq2ps,           # Convert Packed Doubleword Integers to Packed Double-Precision Floating-Point Values
    NN_cvtpd2dq = idaapi.NN_cvtpd2dq,           # Convert Packed Double-Precision Floating-Point Values to Packed Doubleword Integers
    NN_cvtpd2pi = idaapi.NN_cvtpd2pi,           # Convert Packed Double-Precision Floating-Point Values to Packed Doubleword Integers
    NN_cvtpd2ps = idaapi.NN_cvtpd2ps,           # Convert Packed Double-Precision Floating-Point Values to Packed Single-Precision Floating-Point Values
    NN_cvtpi2pd = idaapi.NN_cvtpi2pd,           # Convert Packed Doubleword Integers to Packed Double-Precision Floating-Point Values
    NN_cvtps2dq = idaapi.NN_cvtps2dq,           # Convert Packed Single-Precision Floating-Point Values to Packed Doubleword Integers
    NN_cvtps2pd = idaapi.NN_cvtps2pd,           # Convert Packed Single-Precision Floating-Point Values to Packed Double-Precision Floating-Point Values
    NN_cvtsd2si = idaapi.NN_cvtsd2si,           # Convert Scalar Double-Precision Floating-Point Value to Doubleword Integer
    NN_cvtsd2ss = idaapi.NN_cvtsd2ss,           # Convert Scalar Double-Precision Floating-Point Value to Scalar Single-Precision Floating-Point Value
    NN_cvtsi2sd = idaapi.NN_cvtsi2sd,           # Convert Doubleword Integer to Scalar Double-Precision Floating-Point Value
    NN_cvtss2sd = idaapi.NN_cvtss2sd,           # Convert Scalar Single-Precision Floating-Point Value to Scalar Double-Precision Floating-Point Value
    NN_cvttpd2dq = idaapi.NN_cvttpd2dq,         # Convert With Truncation Packed Double-Precision Floating-Point Values to Packed Doubleword Integers
    NN_cvttpd2pi = idaapi.NN_cvttpd2pi,         # Convert with Truncation Packed Double-Precision Floating-Point Values to Packed Doubleword Integers
    NN_cvttps2dq = idaapi.NN_cvttps2dq,         # Convert With Truncation Packed Single-Precision Floating-Point Values to Packed Doubleword Integers
    NN_cvttsd2si = idaapi.NN_cvttsd2si,         # Convert with Truncation Scalar Double-Precision Floating-Point Value to Doubleword Integer
    NN_divpd = idaapi.NN_divpd,         # Divide Packed Double-Precision Floating-Point Values
    NN_divsd = idaapi.NN_divsd,         # Divide Scalar Double-Precision Floating-Point Values
    NN_lfence = idaapi.NN_lfence,           # Load Fence
    NN_maskmovdqu = idaapi.NN_maskmovdqu,           # Store Selected Bytes of Double Quadword
    NN_maxpd = idaapi.NN_maxpd,         # Return Maximum Packed Double-Precision Floating-Point Values
    NN_maxsd = idaapi.NN_maxsd,         # Return Maximum Scalar Double-Precision Floating-Point Value
    NN_mfence = idaapi.NN_mfence,           # Memory Fence
    NN_minpd = idaapi.NN_minpd,         # Return Minimum Packed Double-Precision Floating-Point Values
    NN_minsd = idaapi.NN_minsd,         # Return Minimum Scalar Double-Precision Floating-Point Value
    NN_movapd = idaapi.NN_movapd,           # Move Aligned Packed Double-Precision Floating-Point Values
    NN_movdq2q = idaapi.NN_movdq2q,         # Move Quadword from XMM to MMX Register
    NN_movdqa = idaapi.NN_movdqa,           # Move Aligned Double Quadword
    NN_movdqu = idaapi.NN_movdqu,           # Move Unaligned Double Quadword
    NN_movhpd = idaapi.NN_movhpd,           # Move High Packed Double-Precision Floating-Point Values
    NN_movlpd = idaapi.NN_movlpd,           # Move Low Packed Double-Precision Floating-Point Values
    NN_movmskpd = idaapi.NN_movmskpd,           # Extract Packed Double-Precision Floating-Point Sign Mask
    NN_movntdq = idaapi.NN_movntdq,         # Store Double Quadword Using Non-Temporal Hint
    NN_movnti = idaapi.NN_movnti,           # Store Doubleword Using Non-Temporal Hint
    NN_movntpd = idaapi.NN_movntpd,         # Store Packed Double-Precision Floating-Point Values Using Non-Temporal Hint
    NN_movq2dq = idaapi.NN_movq2dq,         # Move Quadword from MMX to XMM Register
    NN_movsd = idaapi.NN_movsd,         # Move Scalar Double-Precision Floating-Point Values
    NN_movupd = idaapi.NN_movupd,           # Move Unaligned Packed Double-Precision Floating-Point Values
    NN_mulpd = idaapi.NN_mulpd,         # Multiply Packed Double-Precision Floating-Point Values
    NN_mulsd = idaapi.NN_mulsd,         # Multiply Scalar Double-Precision Floating-Point Values
    NN_orpd = idaapi.NN_orpd,           # Bitwise Logical OR of Double-Precision Floating-Point Values
    NN_paddq = idaapi.NN_paddq,         # Add Packed Quadword Integers
    NN_pause = idaapi.NN_pause,         # Spin Loop Hint
    NN_pmuludq = idaapi.NN_pmuludq,         # Multiply Packed Unsigned Doubleword Integers
    NN_pshufd = idaapi.NN_pshufd,           # Shuffle Packed Doublewords
    NN_pshufhw = idaapi.NN_pshufhw,         # Shuffle Packed High Words
    NN_pshuflw = idaapi.NN_pshuflw,         # Shuffle Packed Low Words
    NN_pslldq = idaapi.NN_pslldq,           # Shift Double Quadword Left Logical
    NN_psrldq = idaapi.NN_psrldq,           # Shift Double Quadword Right Logical
    NN_psubq = idaapi.NN_psubq,         # Subtract Packed Quadword Integers
    NN_punpckhqdq = idaapi.NN_punpckhqdq,           # Unpack High Data
    NN_punpcklqdq = idaapi.NN_punpcklqdq,           # Unpack Low Data
    NN_shufpd = idaapi.NN_shufpd,           # Shuffle Packed Double-Precision Floating-Point Values
    NN_sqrtpd = idaapi.NN_sqrtpd,           # Compute Square Roots of Packed Double-Precision Floating-Point Values
    NN_sqrtsd = idaapi.NN_sqrtsd,           # Compute Square Rootof Scalar Double-Precision Floating-Point Value
    NN_subpd = idaapi.NN_subpd,         # Subtract Packed Double-Precision Floating-Point Values
    NN_subsd = idaapi.NN_subsd,         # Subtract Scalar Double-Precision Floating-Point Values
    NN_ucomisd = idaapi.NN_ucomisd,         # Unordered Compare Scalar Ordered Double-Precision Floating-Point Values and Set EFLAGS
    NN_unpckhpd = idaapi.NN_unpckhpd,           # Unpack and Interleave High Packed Double-Precision Floating-Point Values
    NN_unpcklpd = idaapi.NN_unpcklpd,           # Unpack and Interleave Low Packed Double-Precision Floating-Point Values
    NN_xorpd = idaapi.NN_xorpd,         # Bitwise Logical OR of Double-Precision Floating-Point Values

    # AMD syscall/sysret instructions

    NN_syscall = idaapi.NN_syscall,         # Low latency system call
    NN_sysret = idaapi.NN_sysret,           # Return from system call

    # AMD64 instructions

    NN_swapgs = idaapi.NN_swapgs,           # Exchange GS base with KernelGSBase MSR

    # New Pentium instructions (SSE3)

    NN_movddup = idaapi.NN_movddup,         # Move One Double-FP and Duplicate
    NN_movshdup = idaapi.NN_movshdup,           # Move Packed Single-FP High and Duplicate
    NN_movsldup = idaapi.NN_movsldup,           # Move Packed Single-FP Low and Duplicate

    # Missing AMD64 instructions

    NN_movsxd = idaapi.NN_movsxd,           # Move with Sign-Extend Doubleword
    NN_cmpxchg16b = idaapi.NN_cmpxchg16b,           # Compare and Exchange 16 Bytes

    # SSE3 instructions

    NN_addsubpd = idaapi.NN_addsubpd,           # Add /Sub packed DP FP numbers
    NN_addsubps = idaapi.NN_addsubps,           # Add /Sub packed SP FP numbers
    NN_haddpd = idaapi.NN_haddpd,           # Add horizontally packed DP FP numbers
    NN_haddps = idaapi.NN_haddps,           # Add horizontally packed SP FP numbers
    NN_hsubpd = idaapi.NN_hsubpd,           # Sub horizontally packed DP FP numbers
    NN_hsubps = idaapi.NN_hsubps,           # Sub horizontally packed SP FP numbers
    NN_monitor = idaapi.NN_monitor,         # Set up a linear address range to be monitored by hardware
    NN_mwait = idaapi.NN_mwait,         # Wait until write-back store performed within the range specified by the MONITOR instruction
    NN_fisttp = idaapi.NN_fisttp,           # Store ST in intXX (chop) and pop
    NN_lddqu = idaapi.NN_lddqu,         # Load unaligned integer 128-bit

    # SSSE3 instructions

    NN_psignb = idaapi.NN_psignb,           # Packed SIGN Byte
    NN_psignw = idaapi.NN_psignw,           # Packed SIGN Word
    NN_psignd = idaapi.NN_psignd,           # Packed SIGN Doubleword
    NN_pshufb = idaapi.NN_pshufb,           # Packed Shuffle Bytes
    NN_pmulhrsw = idaapi.NN_pmulhrsw,           # Packed Multiply High with Round and Scale
    NN_pmaddubsw = idaapi.NN_pmaddubsw,         # Multiply and Add Packed Signed and Unsigned Bytes
    NN_phsubsw = idaapi.NN_phsubsw,         # Packed Horizontal Subtract and Saturate
    NN_phaddsw = idaapi.NN_phaddsw,         # Packed Horizontal Add and Saturate
    NN_phaddw = idaapi.NN_phaddw,           # Packed Horizontal Add Word
    NN_phaddd = idaapi.NN_phaddd,           # Packed Horizontal Add Doubleword
    NN_phsubw = idaapi.NN_phsubw,           # Packed Horizontal Subtract Word
    NN_phsubd = idaapi.NN_phsubd,           # Packed Horizontal Subtract Doubleword
    NN_palignr = idaapi.NN_palignr,         # Packed Align Right
    NN_pabsb = idaapi.NN_pabsb,         # Packed Absolute Value Byte
    NN_pabsw = idaapi.NN_pabsw,         # Packed Absolute Value Word
    NN_pabsd = idaapi.NN_pabsd,         # Packed Absolute Value Doubleword

    # VMX instructions

    NN_vmcall = idaapi.NN_vmcall,           # Call to VM Monitor
    NN_vmclear = idaapi.NN_vmclear,         # Clear Virtual Machine Control Structure
    NN_vmlaunch = idaapi.NN_vmlaunch,           # Launch Virtual Machine
    NN_vmresume = idaapi.NN_vmresume,           # Resume Virtual Machine
    NN_vmptrld = idaapi.NN_vmptrld,         # Load Pointer to Virtual Machine Control Structure
    NN_vmptrst = idaapi.NN_vmptrst,         # Store Pointer to Virtual Machine Control Structure
    NN_vmread = idaapi.NN_vmread,           # Read Field from Virtual Machine Control Structure
    NN_vmwrite = idaapi.NN_vmwrite,         # Write Field from Virtual Machine Control Structure
    NN_vmxoff = idaapi.NN_vmxoff,           # Leave VMX Operation
    NN_vmxon = idaapi.NN_vmxon,         # Enter VMX Operation

    # Undefined Instruction

    NN_ud2 = idaapi.NN_ud2,         # Undefined Instruction

    # Added with x86-64

    NN_rdtscp = idaapi.NN_rdtscp,           # Read Time-Stamp Counter and Processor ID

    # Geode LX 3DNow! extensions

    NN_pfrcpv = idaapi.NN_pfrcpv,           # Reciprocal Approximation for a Pair of 32-bit Floats
    NN_pfrsqrtv = idaapi.NN_pfrsqrtv,           # Reciprocal Square Root Approximation for a Pair of 32-bit Floats

    # SSE2 pseudoinstructions

    NN_cmpeqpd = idaapi.NN_cmpeqpd,         # Packed Double-FP Compare EQ
    NN_cmpltpd = idaapi.NN_cmpltpd,         # Packed Double-FP Compare LT
    NN_cmplepd = idaapi.NN_cmplepd,         # Packed Double-FP Compare LE
    NN_cmpunordpd = idaapi.NN_cmpunordpd,           # Packed Double-FP Compare UNORD
    NN_cmpneqpd = idaapi.NN_cmpneqpd,           # Packed Double-FP Compare NOT EQ
    NN_cmpnltpd = idaapi.NN_cmpnltpd,           # Packed Double-FP Compare NOT LT
    NN_cmpnlepd = idaapi.NN_cmpnlepd,           # Packed Double-FP Compare NOT LE
    NN_cmpordpd = idaapi.NN_cmpordpd,           # Packed Double-FP Compare ORDERED
    NN_cmpeqsd = idaapi.NN_cmpeqsd,         # Scalar Double-FP Compare EQ
    NN_cmpltsd = idaapi.NN_cmpltsd,         # Scalar Double-FP Compare LT
    NN_cmplesd = idaapi.NN_cmplesd,         # Scalar Double-FP Compare LE
    NN_cmpunordsd = idaapi.NN_cmpunordsd,           # Scalar Double-FP Compare UNORD
    NN_cmpneqsd = idaapi.NN_cmpneqsd,           # Scalar Double-FP Compare NOT EQ
    NN_cmpnltsd = idaapi.NN_cmpnltsd,           # Scalar Double-FP Compare NOT LT
    NN_cmpnlesd = idaapi.NN_cmpnlesd,           # Scalar Double-FP Compare NOT LE
    NN_cmpordsd = idaapi.NN_cmpordsd,           # Scalar Double-FP Compare ORDERED

    # SSSE4.1 instructions

    NN_blendpd = idaapi.NN_blendpd,         # Blend Packed Double Precision Floating-Point Values
    NN_blendps = idaapi.NN_blendps,         # Blend Packed Single Precision Floating-Point Values
    NN_blendvpd = idaapi.NN_blendvpd,           # Variable Blend Packed Double Precision Floating-Point Values
    NN_blendvps = idaapi.NN_blendvps,           # Variable Blend Packed Single Precision Floating-Point Values
    NN_dppd = idaapi.NN_dppd,           # Dot Product of Packed Double Precision Floating-Point Values
    NN_dpps = idaapi.NN_dpps,           # Dot Product of Packed Single Precision Floating-Point Values
    NN_extractps = idaapi.NN_extractps,         # Extract Packed Single Precision Floating-Point Value
    NN_insertps = idaapi.NN_insertps,           # Insert Packed Single Precision Floating-Point Value
    NN_movntdqa = idaapi.NN_movntdqa,           # Load Double Quadword Non-Temporal Aligned Hint
    NN_mpsadbw = idaapi.NN_mpsadbw,         # Compute Multiple Packed Sums of Absolute Difference
    NN_packusdw = idaapi.NN_packusdw,           # Pack with Unsigned Saturation
    NN_pblendvb = idaapi.NN_pblendvb,           # Variable Blend Packed Bytes
    NN_pblendw = idaapi.NN_pblendw,         # Blend Packed Words
    NN_pcmpeqq = idaapi.NN_pcmpeqq,         # Compare Packed Qword Data for Equal
    NN_pextrb = idaapi.NN_pextrb,           # Extract Byte
    NN_pextrd = idaapi.NN_pextrd,           # Extract Dword
    NN_pextrq = idaapi.NN_pextrq,           # Extract Qword
    NN_phminposuw = idaapi.NN_phminposuw,           # Packed Horizontal Word Minimum
    NN_pinsrb = idaapi.NN_pinsrb,           # Insert Byte
    NN_pinsrd = idaapi.NN_pinsrd,           # Insert Dword
    NN_pinsrq = idaapi.NN_pinsrq,           # Insert Qword
    NN_pmaxsb = idaapi.NN_pmaxsb,           # Maximum of Packed Signed Byte Integers
    NN_pmaxsd = idaapi.NN_pmaxsd,           # Maximum of Packed Signed Dword Integers
    NN_pmaxud = idaapi.NN_pmaxud,           # Maximum of Packed Unsigned Dword Integers
    NN_pmaxuw = idaapi.NN_pmaxuw,           # Maximum of Packed Word Integers
    NN_pminsb = idaapi.NN_pminsb,           # Minimum of Packed Signed Byte Integers
    NN_pminsd = idaapi.NN_pminsd,           # Minimum of Packed Signed Dword Integers
    NN_pminud = idaapi.NN_pminud,           # Minimum of Packed Unsigned Dword Integers
    NN_pminuw = idaapi.NN_pminuw,           # Minimum of Packed Word Integers
    NN_pmovsxbw = idaapi.NN_pmovsxbw,           # Packed Move with Sign Extend
    NN_pmovsxbd = idaapi.NN_pmovsxbd,           # Packed Move with Sign Extend
    NN_pmovsxbq = idaapi.NN_pmovsxbq,           # Packed Move with Sign Extend
    NN_pmovsxwd = idaapi.NN_pmovsxwd,           # Packed Move with Sign Extend
    NN_pmovsxwq = idaapi.NN_pmovsxwq,           # Packed Move with Sign Extend
    NN_pmovsxdq = idaapi.NN_pmovsxdq,           # Packed Move with Sign Extend
    NN_pmovzxbw = idaapi.NN_pmovzxbw,           # Packed Move with Zero Extend
    NN_pmovzxbd = idaapi.NN_pmovzxbd,           # Packed Move with Zero Extend
    NN_pmovzxbq = idaapi.NN_pmovzxbq,           # Packed Move with Zero Extend
    NN_pmovzxwd = idaapi.NN_pmovzxwd,           # Packed Move with Zero Extend
    NN_pmovzxwq = idaapi.NN_pmovzxwq,           # Packed Move with Zero Extend
    NN_pmovzxdq = idaapi.NN_pmovzxdq,           # Packed Move with Zero Extend
    NN_pmuldq = idaapi.NN_pmuldq,           # Multiply Packed Signed Dword Integers
    NN_pmulld = idaapi.NN_pmulld,           # Multiply Packed Signed Dword Integers and Store Low Result
    NN_ptest = idaapi.NN_ptest,         # Logical Compare
    NN_roundpd = idaapi.NN_roundpd,         # Round Packed Double Precision Floating-Point Values
    NN_roundps = idaapi.NN_roundps,         # Round Packed Single Precision Floating-Point Values
    NN_roundsd = idaapi.NN_roundsd,         # Round Scalar Double Precision Floating-Point Values
    NN_roundss = idaapi.NN_roundss,         # Round Scalar Single Precision Floating-Point Values

    # SSSE4.2 instructions

    NN_crc32 = idaapi.NN_crc32,         # Accumulate CRC32 Value
    NN_pcmpestri = idaapi.NN_pcmpestri,         # Packed Compare Explicit Length Strings, Return Index
    NN_pcmpestrm = idaapi.NN_pcmpestrm,         # Packed Compare Explicit Length Strings, Return Mask
    NN_pcmpistri = idaapi.NN_pcmpistri,         # Packed Compare Implicit Length Strings, Return Index
    NN_pcmpistrm = idaapi.NN_pcmpistrm,         # Packed Compare Implicit Length Strings, Return Mask
    NN_pcmpgtq = idaapi.NN_pcmpgtq,         # Compare Packed Data for Greater Than
    NN_popcnt = idaapi.NN_popcnt,           # Return the Count of Number of Bits Set to 1

    # AMD SSE4a instructions

    NN_extrq = idaapi.NN_extrq,         # Extract Field From Register
    NN_insertq = idaapi.NN_insertq,         # Insert Field
    NN_movntsd = idaapi.NN_movntsd,         # Move Non-Temporal Scalar Double-Precision Floating-Point
    NN_movntss = idaapi.NN_movntss,         # Move Non-Temporal Scalar Single-Precision Floating-Point
    NN_lzcnt = idaapi.NN_lzcnt,         # Leading Zero Count

    # xsave/xrstor instructions

    NN_xgetbv = idaapi.NN_xgetbv,           # Get Value of Extended Control Register
    NN_xrstor = idaapi.NN_xrstor,           # Restore Processor Extended States
    NN_xsave = idaapi.NN_xsave,         # Save Processor Extended States
    NN_xsetbv = idaapi.NN_xsetbv,           # Set Value of Extended Control Register

    # Intel Safer Mode Extensions (SMX)

    NN_getsec = idaapi.NN_getsec,           # Safer Mode Extensions (SMX) Instruction

    # AMD-V Virtualization ISA Extension

    NN_clgi = idaapi.NN_clgi,           # Clear Global Interrupt Flag
    NN_invlpga = idaapi.NN_invlpga,         # Invalidate TLB Entry in a Specified ASID
    NN_skinit = idaapi.NN_skinit,           # Secure Init and Jump with Attestation
    NN_stgi = idaapi.NN_stgi,           # Set Global Interrupt Flag
    NN_vmexit = idaapi.NN_vmexit,           # Stop Executing Guest, Begin Executing Host
    NN_vmload = idaapi.NN_vmload,           # Load State from VMCB
    NN_vmmcall = idaapi.NN_vmmcall,         # Call VMM
    NN_vmrun = idaapi.NN_vmrun,         # Run Virtual Machine
    NN_vmsave = idaapi.NN_vmsave,           # Save State to VMCB

    # VMX+ instructions

    NN_invept = idaapi.NN_invept,           # Invalidate Translations Derived from EPT
    NN_invvpid = idaapi.NN_invvpid,         # Invalidate Translations Based on VPID

    # Intel Atom instructions

    NN_movbe = idaapi.NN_movbe,         # Move Data After Swapping Bytes

    # Intel AES instructions

    NN_aesenc = idaapi.NN_aesenc,           # Perform One Round of an AES Encryption Flow
    NN_aesenclast = idaapi.NN_aesenclast,           # Perform the Last Round of an AES Encryption Flow
    NN_aesdec = idaapi.NN_aesdec,           # Perform One Round of an AES Decryption Flow
    NN_aesdeclast = idaapi.NN_aesdeclast,           # Perform the Last Round of an AES Decryption Flow
    NN_aesimc = idaapi.NN_aesimc,           # Perform the AES InvMixColumn Transformation
    NN_aeskeygenassist = idaapi.NN_aeskeygenassist,         # AES Round Key Generation Assist

    # Carryless multiplication

    NN_pclmulqdq = idaapi.NN_pclmulqdq,         # Carry-Less Multiplication Quadword

    # Returns modifies by operand size prefixes

    NN_retnw = idaapi.NN_retnw,         # Return Near from Procedure (use16)
    NN_retnd = idaapi.NN_retnd,         # Return Near from Procedure (use32)
    NN_retnq = idaapi.NN_retnq,         # Return Near from Procedure (use64)
    NN_retfw = idaapi.NN_retfw,         # Return Far from Procedure (use16)
    NN_retfd = idaapi.NN_retfd,         # Return Far from Procedure (use32)
    NN_retfq = idaapi.NN_retfq,         # Return Far from Procedure (use64)

    # RDRAND support

    NN_rdrand = idaapi.NN_rdrand,           # Read Random Number

    # new GPR instructions

    NN_adcx = idaapi.NN_adcx,           # Unsigned Integer Addition of Two Operands with Carry Flag
    NN_adox = idaapi.NN_adox,           # Unsigned Integer Addition of Two Operands with Overflow Flag
    NN_andn = idaapi.NN_andn,           # Logical AND NOT
    NN_bextr = idaapi.NN_bextr,         # Bit Field Extract
    NN_blsi = idaapi.NN_blsi,           # Extract Lowest Set Isolated Bit
    NN_blsmsk = idaapi.NN_blsmsk,           # Get Mask Up to Lowest Set Bit
    NN_blsr = idaapi.NN_blsr,           # Reset Lowest Set Bit
    NN_bzhi = idaapi.NN_bzhi,           # Zero High Bits Starting with Specified Bit Position
    NN_clac = idaapi.NN_clac,           # Clear AC Flag in EFLAGS Register
    NN_mulx = idaapi.NN_mulx,           # Unsigned Multiply Without Affecting Flags
    NN_pdep = idaapi.NN_pdep,           # Parallel Bits Deposit
    NN_pext = idaapi.NN_pext,           # Parallel Bits Extract
    NN_rorx = idaapi.NN_rorx,           # Rotate Right Logical Without Affecting Flags
    NN_sarx = idaapi.NN_sarx,           # Shift Arithmetically Right Without Affecting Flags
    NN_shlx = idaapi.NN_shlx,           # Shift Logically Left Without Affecting Flags
    NN_shrx = idaapi.NN_shrx,           # Shift Logically Right Without Affecting Flags
    NN_stac = idaapi.NN_stac,           # Set AC Flag in EFLAGS Register
    NN_tzcnt = idaapi.NN_tzcnt,         # Count the Number of Trailing Zero Bits
    NN_xsaveopt = idaapi.NN_xsaveopt,           # Save Processor Extended States Optimized
    NN_invpcid = idaapi.NN_invpcid,         # Invalidate Processor Context ID
    NN_rdseed = idaapi.NN_rdseed,           # Read Random Seed
    NN_rdfsbase = idaapi.NN_rdfsbase,           # Read FS Segment Base
    NN_rdgsbase = idaapi.NN_rdgsbase,           # Read GS Segment Base
    NN_wrfsbase = idaapi.NN_wrfsbase,           # Write FS Segment Base
    NN_wrgsbase = idaapi.NN_wrgsbase,           # Write GS Segment Base

    # new AVX instructions
    NN_vaddpd = idaapi.NN_vaddpd,           # Add Packed Double-Precision Floating-Point Values
    NN_vaddps = idaapi.NN_vaddps,           # Packed Single-FP Add
    NN_vaddsd = idaapi.NN_vaddsd,           # Add Scalar Double-Precision Floating-Point Values
    NN_vaddss = idaapi.NN_vaddss,           # Scalar Single-FP Add
    NN_vaddsubpd = idaapi.NN_vaddsubpd,         # Add /Sub packed DP FP numbers
    NN_vaddsubps = idaapi.NN_vaddsubps,         # Add /Sub packed SP FP numbers
    NN_vaesdec = idaapi.NN_vaesdec,         # Perform One Round of an AES Decryption Flow
    NN_vaesdeclast = idaapi.NN_vaesdeclast,         # Perform the Last Round of an AES Decryption Flow
    NN_vaesenc = idaapi.NN_vaesenc,         # Perform One Round of an AES Encryption Flow
    NN_vaesenclast = idaapi.NN_vaesenclast,         # Perform the Last Round of an AES Encryption Flow
    NN_vaesimc = idaapi.NN_vaesimc,         # Perform the AES InvMixColumn Transformation
    NN_vaeskeygenassist = idaapi.NN_vaeskeygenassist,           # AES Round Key Generation Assist
    NN_vandnpd = idaapi.NN_vandnpd,         # Bitwise Logical AND NOT of Packed Double-Precision Floating-Point Values
    NN_vandnps = idaapi.NN_vandnps,         # Bitwise Logical And Not for Single-FP
    NN_vandpd = idaapi.NN_vandpd,           # Bitwise Logical AND of Packed Double-Precision Floating-Point Values
    NN_vandps = idaapi.NN_vandps,           # Bitwise Logical And for Single-FP
    NN_vblendpd = idaapi.NN_vblendpd,           # Blend Packed Double Precision Floating-Point Values
    NN_vblendps = idaapi.NN_vblendps,           # Blend Packed Single Precision Floating-Point Values
    NN_vblendvpd = idaapi.NN_vblendvpd,         # Variable Blend Packed Double Precision Floating-Point Values
    NN_vblendvps = idaapi.NN_vblendvps,         # Variable Blend Packed Single Precision Floating-Point Values
    NN_vbroadcastf128 = idaapi.NN_vbroadcastf128,           # Broadcast 128 Bits of Floating-Point Data
    NN_vbroadcasti128 = idaapi.NN_vbroadcasti128,           # Broadcast 128 Bits of Integer Data
    NN_vbroadcastsd = idaapi.NN_vbroadcastsd,           # Broadcast Double-Precision Floating-Point Element
    NN_vbroadcastss = idaapi.NN_vbroadcastss,           # Broadcast Single-Precision Floating-Point Element
    NN_vcmppd = idaapi.NN_vcmppd,           # Compare Packed Double-Precision Floating-Point Values
    NN_vcmpps = idaapi.NN_vcmpps,           # Packed Single-FP Compare
    NN_vcmpsd = idaapi.NN_vcmpsd,           # Compare Scalar Double-Precision Floating-Point Values
    NN_vcmpss = idaapi.NN_vcmpss,           # Scalar Single-FP Compare
    NN_vcomisd = idaapi.NN_vcomisd,         # Compare Scalar Ordered Double-Precision Floating-Point Values and Set EFLAGS
    NN_vcomiss = idaapi.NN_vcomiss,         # Scalar Ordered Single-FP Compare and Set EFLAGS
    NN_vcvtdq2pd = idaapi.NN_vcvtdq2pd,         # Convert Packed Doubleword Integers to Packed Single-Precision Floating-Point Values
    NN_vcvtdq2ps = idaapi.NN_vcvtdq2ps,         # Convert Packed Doubleword Integers to Packed Double-Precision Floating-Point Values
    NN_vcvtpd2dq = idaapi.NN_vcvtpd2dq,         # Convert Packed Double-Precision Floating-Point Values to Packed Doubleword Integers
    NN_vcvtpd2ps = idaapi.NN_vcvtpd2ps,         # Convert Packed Double-Precision Floating-Point Values to Packed Single-Precision Floating-Point Values
    NN_vcvtph2ps = idaapi.NN_vcvtph2ps,         # Convert 16-bit FP Values to Single-Precision FP Values
    NN_vcvtps2dq = idaapi.NN_vcvtps2dq,         # Convert Packed Single-Precision Floating-Point Values to Packed Doubleword Integers
    NN_vcvtps2pd = idaapi.NN_vcvtps2pd,         # Convert Packed Single-Precision Floating-Point Values to Packed Double-Precision Floating-Point Values
    NN_vcvtps2ph = idaapi.NN_vcvtps2ph,         # Convert Single-Precision FP value to 16-bit FP value
    NN_vcvtsd2si = idaapi.NN_vcvtsd2si,         # Convert Scalar Double-Precision Floating-Point Value to Doubleword Integer
    NN_vcvtsd2ss = idaapi.NN_vcvtsd2ss,         # Convert Scalar Double-Precision Floating-Point Value to Scalar Single-Precision Floating-Point Value
    NN_vcvtsi2sd = idaapi.NN_vcvtsi2sd,         # Convert Doubleword Integer to Scalar Double-Precision Floating-Point Value
    NN_vcvtsi2ss = idaapi.NN_vcvtsi2ss,         # Scalar signed INT32 to Single-FP conversion
    NN_vcvtss2sd = idaapi.NN_vcvtss2sd,         # Convert Scalar Single-Precision Floating-Point Value to Scalar Double-Precision Floating-Point Value
    NN_vcvtss2si = idaapi.NN_vcvtss2si,         # Scalar Single-FP to signed INT32 conversion
    NN_vcvttpd2dq = idaapi.NN_vcvttpd2dq,           # Convert With Truncation Packed Double-Precision Floating-Point Values to Packed Doubleword Integers
    NN_vcvttps2dq = idaapi.NN_vcvttps2dq,           # Convert With Truncation Packed Single-Precision Floating-Point Values to Packed Doubleword Integers
    NN_vcvttsd2si = idaapi.NN_vcvttsd2si,           # Convert with Truncation Scalar Double-Precision Floating-Point Value to Doubleword Integer
    NN_vcvttss2si = idaapi.NN_vcvttss2si,           # Scalar Single-FP to signed INT32 conversion (truncate)
    NN_vdivpd = idaapi.NN_vdivpd,           # Divide Packed Double-Precision Floating-Point Values
    NN_vdivps = idaapi.NN_vdivps,           # Packed Single-FP Divide
    NN_vdivsd = idaapi.NN_vdivsd,           # Divide Scalar Double-Precision Floating-Point Values
    NN_vdivss = idaapi.NN_vdivss,           # Scalar Single-FP Divide
    NN_vdppd = idaapi.NN_vdppd,         # Dot Product of Packed Double Precision Floating-Point Values
    NN_vdpps = idaapi.NN_vdpps,         # Dot Product of Packed Single Precision Floating-Point Values
    NN_vextractf128 = idaapi.NN_vextractf128,           # Extract Packed Floating-Point Values
    NN_vextracti128 = idaapi.NN_vextracti128,           # Extract Packed Integer Values
    NN_vextractps = idaapi.NN_vextractps,           # Extract Packed Floating-Point Values
    NN_vfmadd132pd = idaapi.NN_vfmadd132pd,         # Fused Multiply-Add of Packed Double-Precision Floating-Point Values
    NN_vfmadd132ps = idaapi.NN_vfmadd132ps,         # Fused Multiply-Add of Packed Single-Precision Floating-Point Values
    NN_vfmadd132sd = idaapi.NN_vfmadd132sd,         # Fused Multiply-Add of Scalar Double-Precision Floating-Point Values
    NN_vfmadd132ss = idaapi.NN_vfmadd132ss,         # Fused Multiply-Add of Scalar Single-Precision Floating-Point Values
    NN_vfmadd213pd = idaapi.NN_vfmadd213pd,         # Fused Multiply-Add of Packed Double-Precision Floating-Point Values
    NN_vfmadd213ps = idaapi.NN_vfmadd213ps,         # Fused Multiply-Add of Packed Single-Precision Floating-Point Values
    NN_vfmadd213sd = idaapi.NN_vfmadd213sd,         # Fused Multiply-Add of Scalar Double-Precision Floating-Point Values
    NN_vfmadd213ss = idaapi.NN_vfmadd213ss,         # Fused Multiply-Add of Scalar Single-Precision Floating-Point Values
    NN_vfmadd231pd = idaapi.NN_vfmadd231pd,         # Fused Multiply-Add of Packed Double-Precision Floating-Point Values
    NN_vfmadd231ps = idaapi.NN_vfmadd231ps,         # Fused Multiply-Add of Packed Single-Precision Floating-Point Values
    NN_vfmadd231sd = idaapi.NN_vfmadd231sd,         # Fused Multiply-Add of Scalar Double-Precision Floating-Point Values
    NN_vfmadd231ss = idaapi.NN_vfmadd231ss,         # Fused Multiply-Add of Scalar Single-Precision Floating-Point Values
    NN_vfmaddsub132pd = idaapi.NN_vfmaddsub132pd,           # Fused Multiply-Alternating Add/Subtract of Packed Double-Precision Floating-Point Values
    NN_vfmaddsub132ps = idaapi.NN_vfmaddsub132ps,           # Fused Multiply-Alternating Add/Subtract of Packed Single-Precision Floating-Point Values
    NN_vfmaddsub213pd = idaapi.NN_vfmaddsub213pd,           # Fused Multiply-Alternating Add/Subtract of Packed Double-Precision Floating-Point Values
    NN_vfmaddsub213ps = idaapi.NN_vfmaddsub213ps,           # Fused Multiply-Alternating Add/Subtract of Packed Single-Precision Floating-Point Values
    NN_vfmaddsub231pd = idaapi.NN_vfmaddsub231pd,           # Fused Multiply-Alternating Add/Subtract of Packed Double-Precision Floating-Point Values
    NN_vfmaddsub231ps = idaapi.NN_vfmaddsub231ps,           # Fused Multiply-Alternating Add/Subtract of Packed Single-Precision Floating-Point Values
    NN_vfmsub132pd = idaapi.NN_vfmsub132pd,         # Fused Multiply-Subtract of Packed Double-Precision Floating-Point Values
    NN_vfmsub132ps = idaapi.NN_vfmsub132ps,         # Fused Multiply-Subtract of Packed Single-Precision Floating-Point Values
    NN_vfmsub132sd = idaapi.NN_vfmsub132sd,         # Fused Multiply-Subtract of Scalar Double-Precision Floating-Point Values
    NN_vfmsub132ss = idaapi.NN_vfmsub132ss,         # Fused Multiply-Subtract of Scalar Single-Precision Floating-Point Values
    NN_vfmsub213pd = idaapi.NN_vfmsub213pd,         # Fused Multiply-Subtract of Packed Double-Precision Floating-Point Values
    NN_vfmsub213ps = idaapi.NN_vfmsub213ps,         # Fused Multiply-Subtract of Packed Single-Precision Floating-Point Values
    NN_vfmsub213sd = idaapi.NN_vfmsub213sd,         # Fused Multiply-Subtract of Scalar Double-Precision Floating-Point Values
    NN_vfmsub213ss = idaapi.NN_vfmsub213ss,         # Fused Multiply-Subtract of Scalar Single-Precision Floating-Point Values
    NN_vfmsub231pd = idaapi.NN_vfmsub231pd,         # Fused Multiply-Subtract of Packed Double-Precision Floating-Point Values
    NN_vfmsub231ps = idaapi.NN_vfmsub231ps,         # Fused Multiply-Subtract of Packed Single-Precision Floating-Point Values
    NN_vfmsub231sd = idaapi.NN_vfmsub231sd,         # Fused Multiply-Subtract of Scalar Double-Precision Floating-Point Values
    NN_vfmsub231ss = idaapi.NN_vfmsub231ss,         # Fused Multiply-Subtract of Scalar Single-Precision Floating-Point Values
    NN_vfmsubadd132pd = idaapi.NN_vfmsubadd132pd,           # Fused Multiply-Alternating Subtract/Add of Packed Double-Precision Floating-Point Values
    NN_vfmsubadd132ps = idaapi.NN_vfmsubadd132ps,           # Fused Multiply-Alternating Subtract/Add of Packed Single-Precision Floating-Point Values
    NN_vfmsubadd213pd = idaapi.NN_vfmsubadd213pd,           # Fused Multiply-Alternating Subtract/Add of Packed Double-Precision Floating-Point Values
    NN_vfmsubadd213ps = idaapi.NN_vfmsubadd213ps,           # Fused Multiply-Alternating Subtract/Add of Packed Single-Precision Floating-Point Values
    NN_vfmsubadd231pd = idaapi.NN_vfmsubadd231pd,           # Fused Multiply-Alternating Subtract/Add of Packed Double-Precision Floating-Point Values
    NN_vfmsubadd231ps = idaapi.NN_vfmsubadd231ps,           # Fused Multiply-Alternating Subtract/Add of Packed Single-Precision Floating-Point Values
    NN_vfnmadd132pd = idaapi.NN_vfnmadd132pd,           # Fused Negative Multiply-Add of Packed Double-Precision Floating-Point Values
    NN_vfnmadd132ps = idaapi.NN_vfnmadd132ps,           # Fused Negative Multiply-Add of Packed Single-Precision Floating-Point Values
    NN_vfnmadd132sd = idaapi.NN_vfnmadd132sd,           # Fused Negative Multiply-Add of Scalar Double-Precision Floating-Point Values
    NN_vfnmadd132ss = idaapi.NN_vfnmadd132ss,           # Fused Negative Multiply-Add of Scalar Single-Precision Floating-Point Values
    NN_vfnmadd213pd = idaapi.NN_vfnmadd213pd,           # Fused Negative Multiply-Add of Packed Double-Precision Floating-Point Values
    NN_vfnmadd213ps = idaapi.NN_vfnmadd213ps,           # Fused Negative Multiply-Add of Packed Single-Precision Floating-Point Values
    NN_vfnmadd213sd = idaapi.NN_vfnmadd213sd,           # Fused Negative Multiply-Add of Scalar Double-Precision Floating-Point Values
    NN_vfnmadd213ss = idaapi.NN_vfnmadd213ss,           # Fused Negative Multiply-Add of Scalar Single-Precision Floating-Point Values
    NN_vfnmadd231pd = idaapi.NN_vfnmadd231pd,           # Fused Negative Multiply-Add of Packed Double-Precision Floating-Point Values
    NN_vfnmadd231ps = idaapi.NN_vfnmadd231ps,           # Fused Negative Multiply-Add of Packed Single-Precision Floating-Point Values
    NN_vfnmadd231sd = idaapi.NN_vfnmadd231sd,           # Fused Negative Multiply-Add of Scalar Double-Precision Floating-Point Values
    NN_vfnmadd231ss = idaapi.NN_vfnmadd231ss,           # Fused Negative Multiply-Add of Scalar Single-Precision Floating-Point Values
    NN_vfnmsub132pd = idaapi.NN_vfnmsub132pd,           # Fused Negative Multiply-Subtract of Packed Double-Precision Floating-Point Values
    NN_vfnmsub132ps = idaapi.NN_vfnmsub132ps,           # Fused Negative Multiply-Subtract of Packed Single-Precision Floating-Point Values
    NN_vfnmsub132sd = idaapi.NN_vfnmsub132sd,           # Fused Negative Multiply-Subtract of Scalar Double-Precision Floating-Point Values
    NN_vfnmsub132ss = idaapi.NN_vfnmsub132ss,           # Fused Negative Multiply-Subtract of Scalar Single-Precision Floating-Point Values
    NN_vfnmsub213pd = idaapi.NN_vfnmsub213pd,           # Fused Negative Multiply-Subtract of Packed Double-Precision Floating-Point Values
    NN_vfnmsub213ps = idaapi.NN_vfnmsub213ps,           # Fused Negative Multiply-Subtract of Packed Single-Precision Floating-Point Values
    NN_vfnmsub213sd = idaapi.NN_vfnmsub213sd,           # Fused Negative Multiply-Subtract of Scalar Double-Precision Floating-Point Values
    NN_vfnmsub213ss = idaapi.NN_vfnmsub213ss,           # Fused Negative Multiply-Subtract of Scalar Single-Precision Floating-Point Values
    NN_vfnmsub231pd = idaapi.NN_vfnmsub231pd,           # Fused Negative Multiply-Subtract of Packed Double-Precision Floating-Point Values
    NN_vfnmsub231ps = idaapi.NN_vfnmsub231ps,           # Fused Negative Multiply-Subtract of Packed Single-Precision Floating-Point Values
    NN_vfnmsub231sd = idaapi.NN_vfnmsub231sd,           # Fused Negative Multiply-Subtract of Scalar Double-Precision Floating-Point Values
    NN_vfnmsub231ss = idaapi.NN_vfnmsub231ss,           # Fused Negative Multiply-Subtract of Scalar Single-Precision Floating-Point Values
    NN_vgatherdps = idaapi.NN_vgatherdps,           # Gather Packed SP FP Values Using Signed Dword Indices
    NN_vgatherdpd = idaapi.NN_vgatherdpd,           # Gather Packed DP FP Values Using Signed Dword Indices
    NN_vgatherqps = idaapi.NN_vgatherqps,           # Gather Packed SP FP Values Using Signed Qword Indices
    NN_vgatherqpd = idaapi.NN_vgatherqpd,           # Gather Packed DP FP Values Using Signed Qword Indices
    NN_vhaddpd = idaapi.NN_vhaddpd,         # Add horizontally packed DP FP numbers
    NN_vhaddps = idaapi.NN_vhaddps,         # Add horizontally packed SP FP numbers
    NN_vhsubpd = idaapi.NN_vhsubpd,         # Sub horizontally packed DP FP numbers
    NN_vhsubps = idaapi.NN_vhsubps,         # Sub horizontally packed SP FP numbers
    NN_vinsertf128 = idaapi.NN_vinsertf128,         # Insert Packed Floating-Point Values
    NN_vinserti128 = idaapi.NN_vinserti128,         # Insert Packed Integer Values
    NN_vinsertps = idaapi.NN_vinsertps,         # Insert Packed Single Precision Floating-Point Value
    NN_vlddqu = idaapi.NN_vlddqu,           # Load Unaligned Packed Integer Values
    NN_vldmxcsr = idaapi.NN_vldmxcsr,           # Load Streaming SIMD Extensions Technology Control/Status Register
    NN_vmaskmovdqu = idaapi.NN_vmaskmovdqu,         # Store Selected Bytes of Double Quadword with NT Hint
    NN_vmaskmovpd = idaapi.NN_vmaskmovpd,           # Conditionally Load Packed Double-Precision Floating-Point Values
    NN_vmaskmovps = idaapi.NN_vmaskmovps,           # Conditionally Load Packed Single-Precision Floating-Point Values
    NN_vmaxpd = idaapi.NN_vmaxpd,           # Return Maximum Packed Double-Precision Floating-Point Values
    NN_vmaxps = idaapi.NN_vmaxps,           # Packed Single-FP Maximum
    NN_vmaxsd = idaapi.NN_vmaxsd,           # Return Maximum Scalar Double-Precision Floating-Point Value
    NN_vmaxss = idaapi.NN_vmaxss,           # Scalar Single-FP Maximum
    NN_vminpd = idaapi.NN_vminpd,           # Return Minimum Packed Double-Precision Floating-Point Values
    NN_vminps = idaapi.NN_vminps,           # Packed Single-FP Minimum
    NN_vminsd = idaapi.NN_vminsd,           # Return Minimum Scalar Double-Precision Floating-Point Value
    NN_vminss = idaapi.NN_vminss,           # Scalar Single-FP Minimum
    NN_vmovapd = idaapi.NN_vmovapd,         # Move Aligned Packed Double-Precision Floating-Point Values
    NN_vmovaps = idaapi.NN_vmovaps,         # Move Aligned Four Packed Single-FP
    NN_vmovd = idaapi.NN_vmovd,         # Move 32 bits
    NN_vmovddup = idaapi.NN_vmovddup,           # Move One Double-FP and Duplicate
    NN_vmovdqa = idaapi.NN_vmovdqa,         # Move Aligned Double Quadword
    NN_vmovdqu = idaapi.NN_vmovdqu,         # Move Unaligned Double Quadword
    NN_vmovhlps = idaapi.NN_vmovhlps,           # Move High to Low Packed Single-FP
    NN_vmovhpd = idaapi.NN_vmovhpd,         # Move High Packed Double-Precision Floating-Point Values
    NN_vmovhps = idaapi.NN_vmovhps,         # Move High Packed Single-FP
    NN_vmovlhps = idaapi.NN_vmovlhps,           # Move Low to High Packed Single-FP
    NN_vmovlpd = idaapi.NN_vmovlpd,         # Move Low Packed Double-Precision Floating-Point Values
    NN_vmovlps = idaapi.NN_vmovlps,         # Move Low Packed Single-FP
    NN_vmovmskpd = idaapi.NN_vmovmskpd,         # Extract Packed Double-Precision Floating-Point Sign Mask
    NN_vmovmskps = idaapi.NN_vmovmskps,         # Move Mask to Register
    NN_vmovntdq = idaapi.NN_vmovntdq,           # Store Double Quadword Using Non-Temporal Hint
    NN_vmovntdqa = idaapi.NN_vmovntdqa,         # Load Double Quadword Non-Temporal Aligned Hint
    NN_vmovntpd = idaapi.NN_vmovntpd,           # Store Packed Double-Precision Floating-Point Values Using Non-Temporal Hint
    NN_vmovntps = idaapi.NN_vmovntps,           # Move Aligned Four Packed Single-FP Non Temporal
    NN_vmovntsd = idaapi.NN_vmovntsd,           # Move Non-Temporal Scalar Double-Precision Floating-Point
    NN_vmovntss = idaapi.NN_vmovntss,           # Move Non-Temporal Scalar Single-Precision Floating-Point
    NN_vmovq = idaapi.NN_vmovq,         # Move 64 bits
    NN_vmovsd = idaapi.NN_vmovsd,           # Move Scalar Double-Precision Floating-Point Values
    NN_vmovshdup = idaapi.NN_vmovshdup,         # Move Packed Single-FP High and Duplicate
    NN_vmovsldup = idaapi.NN_vmovsldup,         # Move Packed Single-FP Low and Duplicate
    NN_vmovss = idaapi.NN_vmovss,           # Move Scalar Single-FP
    NN_vmovupd = idaapi.NN_vmovupd,         # Move Unaligned Packed Double-Precision Floating-Point Values
    NN_vmovups = idaapi.NN_vmovups,         # Move Unaligned Four Packed Single-FP
    NN_vmpsadbw = idaapi.NN_vmpsadbw,           # Compute Multiple Packed Sums of Absolute Difference
    NN_vmulpd = idaapi.NN_vmulpd,           # Multiply Packed Double-Precision Floating-Point Values
    NN_vmulps = idaapi.NN_vmulps,           # Packed Single-FP Multiply
    NN_vmulsd = idaapi.NN_vmulsd,           # Multiply Scalar Double-Precision Floating-Point Values
    NN_vmulss = idaapi.NN_vmulss,           # Scalar Single-FP Multiply
    NN_vorpd = idaapi.NN_vorpd,         # Bitwise Logical OR of Double-Precision Floating-Point Values
    NN_vorps = idaapi.NN_vorps,         # Bitwise Logical OR for Single-FP Data
    NN_vpabsb = idaapi.NN_vpabsb,           # Packed Absolute Value Byte
    NN_vpabsd = idaapi.NN_vpabsd,           # Packed Absolute Value Doubleword
    NN_vpabsw = idaapi.NN_vpabsw,           # Packed Absolute Value Word
    NN_vpackssdw = idaapi.NN_vpackssdw,         # Pack with Signed Saturation (Dword->Word)
    NN_vpacksswb = idaapi.NN_vpacksswb,         # Pack with Signed Saturation (Word->Byte)
    NN_vpackusdw = idaapi.NN_vpackusdw,         # Pack with Unsigned Saturation
    NN_vpackuswb = idaapi.NN_vpackuswb,         # Pack with Unsigned Saturation (Word->Byte)
    NN_vpaddb = idaapi.NN_vpaddb,           # Packed Add Byte
    NN_vpaddd = idaapi.NN_vpaddd,           # Packed Add Dword
    NN_vpaddq = idaapi.NN_vpaddq,           # Add Packed Quadword Integers
    NN_vpaddsb = idaapi.NN_vpaddsb,         # Packed Add with Saturation (Byte)
    NN_vpaddsw = idaapi.NN_vpaddsw,         # Packed Add with Saturation (Word)
    NN_vpaddusb = idaapi.NN_vpaddusb,           # Packed Add Unsigned with Saturation (Byte)
    NN_vpaddusw = idaapi.NN_vpaddusw,           # Packed Add Unsigned with Saturation (Word)
    NN_vpaddw = idaapi.NN_vpaddw,           # Packed Add Word
    NN_vpalignr = idaapi.NN_vpalignr,           # Packed Align Right
    NN_vpand = idaapi.NN_vpand,         # Bitwise Logical And
    NN_vpandn = idaapi.NN_vpandn,           # Bitwise Logical And Not
    NN_vpavgb = idaapi.NN_vpavgb,           # Packed Average (Byte)
    NN_vpavgw = idaapi.NN_vpavgw,           # Packed Average (Word)
    NN_vpblendd = idaapi.NN_vpblendd,           # Blend Packed Dwords
    NN_vpblendvb = idaapi.NN_vpblendvb,         # Variable Blend Packed Bytes
    NN_vpblendw = idaapi.NN_vpblendw,           # Blend Packed Words
    NN_vpbroadcastb = idaapi.NN_vpbroadcastb,           # Broadcast a Byte Integer
    NN_vpbroadcastd = idaapi.NN_vpbroadcastd,           # Broadcast a Dword Integer
    NN_vpbroadcastq = idaapi.NN_vpbroadcastq,           # Broadcast a Qword Integer
    NN_vpbroadcastw = idaapi.NN_vpbroadcastw,           # Broadcast a Word Integer
    NN_vpclmulqdq = idaapi.NN_vpclmulqdq,           # Carry-Less Multiplication Quadword
    NN_vpcmpeqb = idaapi.NN_vpcmpeqb,           # Packed Compare for Equal (Byte)
    NN_vpcmpeqd = idaapi.NN_vpcmpeqd,           # Packed Compare for Equal (Dword)
    NN_vpcmpeqq = idaapi.NN_vpcmpeqq,           # Compare Packed Qword Data for Equal
    NN_vpcmpeqw = idaapi.NN_vpcmpeqw,           # Packed Compare for Equal (Word)
    NN_vpcmpestri = idaapi.NN_vpcmpestri,           # Packed Compare Explicit Length Strings, Return Index
    NN_vpcmpestrm = idaapi.NN_vpcmpestrm,           # Packed Compare Explicit Length Strings, Return Mask
    NN_vpcmpgtb = idaapi.NN_vpcmpgtb,           # Packed Compare for Greater Than (Byte)
    NN_vpcmpgtd = idaapi.NN_vpcmpgtd,           # Packed Compare for Greater Than (Dword)
    NN_vpcmpgtq = idaapi.NN_vpcmpgtq,           # Compare Packed Data for Greater Than
    NN_vpcmpgtw = idaapi.NN_vpcmpgtw,           # Packed Compare for Greater Than (Word)
    NN_vpcmpistri = idaapi.NN_vpcmpistri,           # Packed Compare Implicit Length Strings, Return Index
    NN_vpcmpistrm = idaapi.NN_vpcmpistrm,           # Packed Compare Implicit Length Strings, Return Mask
    NN_vperm2f128 = idaapi.NN_vperm2f128,           # Permute Floating-Point Values
    NN_vperm2i128 = idaapi.NN_vperm2i128,           # Permute Integer Values
    NN_vpermd = idaapi.NN_vpermd,           # Full Doublewords Element Permutation
    NN_vpermilpd = idaapi.NN_vpermilpd,         # Permute Double-Precision Floating-Point Values
    NN_vpermilps = idaapi.NN_vpermilps,         # Permute Single-Precision Floating-Point Values
    NN_vpermpd = idaapi.NN_vpermpd,         # Permute Double-Precision Floating-Point Elements
    NN_vpermps = idaapi.NN_vpermps,         # Permute Single-Precision Floating-Point Elements
    NN_vpermq = idaapi.NN_vpermq,           # Qwords Element Permutation
    NN_vpextrb = idaapi.NN_vpextrb,         # Extract Byte
    NN_vpextrd = idaapi.NN_vpextrd,         # Extract Dword
    NN_vpextrq = idaapi.NN_vpextrq,         # Extract Qword
    NN_vpextrw = idaapi.NN_vpextrw,         # Extract Word
    NN_vpgatherdd = idaapi.NN_vpgatherdd,           # Gather Packed Dword Values Using Signed Dword Indices
    NN_vpgatherdq = idaapi.NN_vpgatherdq,           # Gather Packed Qword Values Using Signed Dword Indices
    NN_vpgatherqd = idaapi.NN_vpgatherqd,           # Gather Packed Dword Values Using Signed Qword Indices
    NN_vpgatherqq = idaapi.NN_vpgatherqq,           # Gather Packed Qword Values Using Signed Qword Indices
    NN_vphaddd = idaapi.NN_vphaddd,         # Packed Horizontal Add Doubleword
    NN_vphaddsw = idaapi.NN_vphaddsw,           # Packed Horizontal Add and Saturate
    NN_vphaddw = idaapi.NN_vphaddw,         # Packed Horizontal Add Word
    NN_vphminposuw = idaapi.NN_vphminposuw,         # Packed Horizontal Word Minimum
    NN_vphsubd = idaapi.NN_vphsubd,         # Packed Horizontal Subtract Doubleword
    NN_vphsubsw = idaapi.NN_vphsubsw,           # Packed Horizontal Subtract and Saturate
    NN_vphsubw = idaapi.NN_vphsubw,         # Packed Horizontal Subtract Word
    NN_vpinsrb = idaapi.NN_vpinsrb,         # Insert Byte
    NN_vpinsrd = idaapi.NN_vpinsrd,         # Insert Dword
    NN_vpinsrq = idaapi.NN_vpinsrq,         # Insert Qword
    NN_vpinsrw = idaapi.NN_vpinsrw,         # Insert Word
    NN_vpmaddubsw = idaapi.NN_vpmaddubsw,           # Multiply and Add Packed Signed and Unsigned Bytes
    NN_vpmaddwd = idaapi.NN_vpmaddwd,           # Packed Multiply and Add
    NN_vpmaskmovd = idaapi.NN_vpmaskmovd,           # Conditionally Store Dword Values Using Mask
    NN_vpmaskmovq = idaapi.NN_vpmaskmovq,           # Conditionally Store Qword Values Using Mask
    NN_vpmaxsb = idaapi.NN_vpmaxsb,         # Maximum of Packed Signed Byte Integers
    NN_vpmaxsd = idaapi.NN_vpmaxsd,         # Maximum of Packed Signed Dword Integers
    NN_vpmaxsw = idaapi.NN_vpmaxsw,         # Packed Signed Integer Word Maximum
    NN_vpmaxub = idaapi.NN_vpmaxub,         # Packed Unsigned Integer Byte Maximum
    NN_vpmaxud = idaapi.NN_vpmaxud,         # Maximum of Packed Unsigned Dword Integers
    NN_vpmaxuw = idaapi.NN_vpmaxuw,         # Maximum of Packed Word Integers
    NN_vpminsb = idaapi.NN_vpminsb,         # Minimum of Packed Signed Byte Integers
    NN_vpminsd = idaapi.NN_vpminsd,         # Minimum of Packed Signed Dword Integers
    NN_vpminsw = idaapi.NN_vpminsw,         # Packed Signed Integer Word Minimum
    NN_vpminub = idaapi.NN_vpminub,         # Packed Unsigned Integer Byte Minimum
    NN_vpminud = idaapi.NN_vpminud,         # Minimum of Packed Unsigned Dword Integers
    NN_vpminuw = idaapi.NN_vpminuw,         # Minimum of Packed Word Integers
    NN_vpmovmskb = idaapi.NN_vpmovmskb,         # Move Byte Mask to Integer
    NN_vpmovsxbd = idaapi.NN_vpmovsxbd,         # Packed Move with Sign Extend
    NN_vpmovsxbq = idaapi.NN_vpmovsxbq,         # Packed Move with Sign Extend
    NN_vpmovsxbw = idaapi.NN_vpmovsxbw,         # Packed Move with Sign Extend
    NN_vpmovsxdq = idaapi.NN_vpmovsxdq,         # Packed Move with Sign Extend
    NN_vpmovsxwd = idaapi.NN_vpmovsxwd,         # Packed Move with Sign Extend
    NN_vpmovsxwq = idaapi.NN_vpmovsxwq,         # Packed Move with Sign Extend
    NN_vpmovzxbd = idaapi.NN_vpmovzxbd,         # Packed Move with Zero Extend
    NN_vpmovzxbq = idaapi.NN_vpmovzxbq,         # Packed Move with Zero Extend
    NN_vpmovzxbw = idaapi.NN_vpmovzxbw,         # Packed Move with Zero Extend
    NN_vpmovzxdq = idaapi.NN_vpmovzxdq,         # Packed Move with Zero Extend
    NN_vpmovzxwd = idaapi.NN_vpmovzxwd,         # Packed Move with Zero Extend
    NN_vpmovzxwq = idaapi.NN_vpmovzxwq,         # Packed Move with Zero Extend
    NN_vpmuldq = idaapi.NN_vpmuldq,         # Multiply Packed Signed Dword Integers
    NN_vpmulhrsw = idaapi.NN_vpmulhrsw,         # Packed Multiply High with Round and Scale
    NN_vpmulhuw = idaapi.NN_vpmulhuw,           # Packed Multiply High Unsigned
    NN_vpmulhw = idaapi.NN_vpmulhw,         # Packed Multiply High
    NN_vpmulld = idaapi.NN_vpmulld,         # Multiply Packed Signed Dword Integers and Store Low Result
    NN_vpmullw = idaapi.NN_vpmullw,         # Packed Multiply Low
    NN_vpmuludq = idaapi.NN_vpmuludq,           # Multiply Packed Unsigned Doubleword Integers
    NN_vpor = idaapi.NN_vpor,           # Bitwise Logical Or
    NN_vpsadbw = idaapi.NN_vpsadbw,         # Packed Sum of Absolute Differences
    NN_vpshufb = idaapi.NN_vpshufb,         # Packed Shuffle Bytes
    NN_vpshufd = idaapi.NN_vpshufd,         # Shuffle Packed Doublewords
    NN_vpshufhw = idaapi.NN_vpshufhw,           # Shuffle Packed High Words
    NN_vpshuflw = idaapi.NN_vpshuflw,           # Shuffle Packed Low Words
    NN_vpsignb = idaapi.NN_vpsignb,         # Packed SIGN Byte
    NN_vpsignd = idaapi.NN_vpsignd,         # Packed SIGN Doubleword
    NN_vpsignw = idaapi.NN_vpsignw,         # Packed SIGN Word
    NN_vpslld = idaapi.NN_vpslld,           # Packed Shift Left Logical (Dword)
    NN_vpslldq = idaapi.NN_vpslldq,         # Shift Double Quadword Left Logical
    NN_vpsllq = idaapi.NN_vpsllq,           # Packed Shift Left Logical (Qword)
    NN_vpsllvd = idaapi.NN_vpsllvd,         # Variable Bit Shift Left Logical (Dword)
    NN_vpsllvq = idaapi.NN_vpsllvq,         # Variable Bit Shift Left Logical (Qword)
    NN_vpsllw = idaapi.NN_vpsllw,           # Packed Shift Left Logical (Word)
    NN_vpsrad = idaapi.NN_vpsrad,           # Packed Shift Right Arithmetic (Dword)
    NN_vpsravd = idaapi.NN_vpsravd,         # Variable Bit Shift Right Arithmetic
    NN_vpsraw = idaapi.NN_vpsraw,           # Packed Shift Right Arithmetic (Word)
    NN_vpsrld = idaapi.NN_vpsrld,           # Packed Shift Right Logical (Dword)
    NN_vpsrldq = idaapi.NN_vpsrldq,         # Shift Double Quadword Right Logical (Qword)
    NN_vpsrlq = idaapi.NN_vpsrlq,           # Packed Shift Right Logical (Qword)
    NN_vpsrlvd = idaapi.NN_vpsrlvd,         # Variable Bit Shift Right Logical (Dword)
    NN_vpsrlvq = idaapi.NN_vpsrlvq,         # Variable Bit Shift Right Logical (Qword)
    NN_vpsrlw = idaapi.NN_vpsrlw,           # Packed Shift Right Logical (Word)
    NN_vpsubb = idaapi.NN_vpsubb,           # Packed Subtract Byte
    NN_vpsubd = idaapi.NN_vpsubd,           # Packed Subtract Dword
    NN_vpsubq = idaapi.NN_vpsubq,           # Subtract Packed Quadword Integers
    NN_vpsubsb = idaapi.NN_vpsubsb,         # Packed Subtract with Saturation (Byte)
    NN_vpsubsw = idaapi.NN_vpsubsw,         # Packed Subtract with Saturation (Word)
    NN_vpsubusb = idaapi.NN_vpsubusb,           # Packed Subtract Unsigned with Saturation (Byte)
    NN_vpsubusw = idaapi.NN_vpsubusw,           # Packed Subtract Unsigned with Saturation (Word)
    NN_vpsubw = idaapi.NN_vpsubw,           # Packed Subtract Word
    NN_vptest = idaapi.NN_vptest,           # Logical Compare
    NN_vpunpckhbw = idaapi.NN_vpunpckhbw,           # Unpack High Packed Data (Byte->Word)
    NN_vpunpckhdq = idaapi.NN_vpunpckhdq,           # Unpack High Packed Data (Dword->Qword)
    NN_vpunpckhqdq = idaapi.NN_vpunpckhqdq,         # Unpack High Packed Data (Qword->Xmmword)
    NN_vpunpckhwd = idaapi.NN_vpunpckhwd,           # Unpack High Packed Data (Word->Dword)
    NN_vpunpcklbw = idaapi.NN_vpunpcklbw,           # Unpack Low Packed Data (Byte->Word)
    NN_vpunpckldq = idaapi.NN_vpunpckldq,           # Unpack Low Packed Data (Dword->Qword)
    NN_vpunpcklqdq = idaapi.NN_vpunpcklqdq,         # Unpack Low Packed Data (Qword->Xmmword)
    NN_vpunpcklwd = idaapi.NN_vpunpcklwd,           # Unpack Low Packed Data (Word->Dword)
    NN_vpxor = idaapi.NN_vpxor,         # Bitwise Logical Exclusive Or
    NN_vrcpps = idaapi.NN_vrcpps,           # Packed Single-FP Reciprocal
    NN_vrcpss = idaapi.NN_vrcpss,           # Scalar Single-FP Reciprocal
    NN_vroundpd = idaapi.NN_vroundpd,           # Round Packed Double Precision Floating-Point Values
    NN_vroundps = idaapi.NN_vroundps,           # Round Packed Single Precision Floating-Point Values
    NN_vroundsd = idaapi.NN_vroundsd,           # Round Scalar Double Precision Floating-Point Values
    NN_vroundss = idaapi.NN_vroundss,           # Round Scalar Single Precision Floating-Point Values
    NN_vrsqrtps = idaapi.NN_vrsqrtps,           # Packed Single-FP Square Root Reciprocal
    NN_vrsqrtss = idaapi.NN_vrsqrtss,           # Scalar Single-FP Square Root Reciprocal
    NN_vshufpd = idaapi.NN_vshufpd,         # Shuffle Packed Double-Precision Floating-Point Values
    NN_vshufps = idaapi.NN_vshufps,         # Shuffle Single-FP
    NN_vsqrtpd = idaapi.NN_vsqrtpd,         # Compute Square Roots of Packed Double-Precision Floating-Point Values
    NN_vsqrtps = idaapi.NN_vsqrtps,         # Packed Single-FP Square Root
    NN_vsqrtsd = idaapi.NN_vsqrtsd,         # Compute Square Rootof Scalar Double-Precision Floating-Point Value
    NN_vsqrtss = idaapi.NN_vsqrtss,         # Scalar Single-FP Square Root
    NN_vstmxcsr = idaapi.NN_vstmxcsr,           # Store Streaming SIMD Extensions Technology Control/Status Register
    NN_vsubpd = idaapi.NN_vsubpd,           # Subtract Packed Double-Precision Floating-Point Values
    NN_vsubps = idaapi.NN_vsubps,           # Packed Single-FP Subtract
    NN_vsubsd = idaapi.NN_vsubsd,           # Subtract Scalar Double-Precision Floating-Point Values
    NN_vsubss = idaapi.NN_vsubss,           # Scalar Single-FP Subtract
    NN_vtestpd = idaapi.NN_vtestpd,         # Packed Double-Precision Floating-Point Bit Test
    NN_vtestps = idaapi.NN_vtestps,         # Packed Single-Precision Floating-Point Bit Test
    NN_vucomisd = idaapi.NN_vucomisd,           # Unordered Compare Scalar Ordered Double-Precision Floating-Point Values and Set EFLAGS
    NN_vucomiss = idaapi.NN_vucomiss,           # Scalar Unordered Single-FP Compare and Set EFLAGS
    NN_vunpckhpd = idaapi.NN_vunpckhpd,         # Unpack and Interleave High Packed Double-Precision Floating-Point Values
    NN_vunpckhps = idaapi.NN_vunpckhps,         # Unpack High Packed Single-FP Data
    NN_vunpcklpd = idaapi.NN_vunpcklpd,         # Unpack and Interleave Low Packed Double-Precision Floating-Point Values
    NN_vunpcklps = idaapi.NN_vunpcklps,         # Unpack Low Packed Single-FP Data
    NN_vxorpd = idaapi.NN_vxorpd,           # Bitwise Logical OR of Double-Precision Floating-Point Values
    NN_vxorps = idaapi.NN_vxorps,           # Bitwise Logical XOR for Single-FP Data
    NN_vzeroall = idaapi.NN_vzeroall,           # Zero All YMM Registers
    NN_vzeroupper = idaapi.NN_vzeroupper,           # Zero Upper Bits of YMM Registers

    # Transactional Synchronization Extensions

    NN_xabort = idaapi.NN_xabort,           # Transaction Abort
    NN_xbegin = idaapi.NN_xbegin,           # Transaction Begin
    NN_xend = idaapi.NN_xend,           # Transaction End
    NN_xtest = idaapi.NN_xtest,         # Test If In Transactional Execution

    # Virtual PC synthetic instructions

    NN_vmgetinfo = idaapi.NN_vmgetinfo,         # Virtual PC - Get VM Information
    NN_vmsetinfo = idaapi.NN_vmsetinfo,         # Virtual PC - Set VM Information
    NN_vmdxdsbl = idaapi.NN_vmdxdsbl,           # Virtual PC - Disable Direct Execution
    NN_vmdxenbl = idaapi.NN_vmdxenbl,           # Virtual PC - Enable Direct Execution
    NN_vmcpuid = idaapi.NN_vmcpuid,         # Virtual PC - Virtualized CPU Information
    NN_vmhlt = idaapi.NN_vmhlt,         # Virtual PC - Halt
    NN_vmsplaf = idaapi.NN_vmsplaf,         # Virtual PC - Spin Lock Acquisition Failed
    NN_vmpushfd = idaapi.NN_vmpushfd,           # Virtual PC - Push virtualized flags register
    NN_vmpopfd = idaapi.NN_vmpopfd,         # Virtual PC - Pop virtualized flags register
    NN_vmcli = idaapi.NN_vmcli,         # Virtual PC - Clear Interrupt Flag
    NN_vmsti = idaapi.NN_vmsti,         # Virtual PC - Set Interrupt Flag
    NN_vmiretd = idaapi.NN_vmiretd,         # Virtual PC - Return From Interrupt
    NN_vmsgdt = idaapi.NN_vmsgdt,           # Virtual PC - Store Global Descriptor Table
    NN_vmsidt = idaapi.NN_vmsidt,           # Virtual PC - Store Interrupt Descriptor Table
    NN_vmsldt = idaapi.NN_vmsldt,           # Virtual PC - Store Local Descriptor Table
    NN_vmstr = idaapi.NN_vmstr,         # Virtual PC - Store Task Register
    NN_vmsdte = idaapi.NN_vmsdte,           # Virtual PC - Store to Descriptor Table Entry
    NN_vpcext = idaapi.NN_vpcext,           # Virtual PC - ISA extension

    # FMA4
    NN_vfmaddsubps = idaapi.NN_vfmaddsubps,         # Multiply with Alternating Add/Subtract of Packed Single-Precision Floating-Point
    NN_vfmaddsubpd = idaapi.NN_vfmaddsubpd,         # Multiply with Alternating Add/Subtract of Packed Double-Precision Floating-Point
    NN_vfmsubaddps = idaapi.NN_vfmsubaddps,         # Multiply with Alternating Subtract/Add of Packed Single-Precision Floating-Point
    NN_vfmsubaddpd = idaapi.NN_vfmsubaddpd,         # Multiply with Alternating Subtract/Add of Packed Double-Precision Floating-Point
    NN_vfmaddps = idaapi.NN_vfmaddps,           # Multiply and Add Packed Single-Precision Floating-Point
    NN_vfmaddpd = idaapi.NN_vfmaddpd,           # Multiply and Add Packed Double-Precision Floating-Point
    NN_vfmaddss = idaapi.NN_vfmaddss,           # Multiply and Add Scalar Single-Precision Floating-Point
    NN_vfmaddsd = idaapi.NN_vfmaddsd,           # Multiply and Add Scalar Double-Precision Floating-Point
    NN_vfmsubps = idaapi.NN_vfmsubps,           # Multiply and Subtract Packed Single-Precision Floating-Point
    NN_vfmsubpd = idaapi.NN_vfmsubpd,           # Multiply and Subtract Packed Double-Precision Floating-Point
    NN_vfmsubss = idaapi.NN_vfmsubss,           # Multiply and Subtract Scalar Single-Precision Floating-Point
    NN_vfmsubsd = idaapi.NN_vfmsubsd,           # Multiply and Subtract Scalar Double-Precision Floating-Point
    NN_vfnmaddps = idaapi.NN_vfnmaddps,         # Negative Multiply and Add Packed Single-Precision Floating-Point
    NN_vfnmaddpd = idaapi.NN_vfnmaddpd,         # Negative Multiply and Add Packed Double-Precision Floating-Point
    NN_vfnmaddss = idaapi.NN_vfnmaddss,         # Negative Multiply and Add Scalar Single-Precision Floating-Point
    NN_vfnmaddsd = idaapi.NN_vfnmaddsd,         # Negative Multiply and Add Double Single-Precision Floating-Point
    NN_vfnmsubps = idaapi.NN_vfnmsubps,         # Negative Multiply and Subtract Packed Single-Precision Floating-Point
    NN_vfnmsubpd = idaapi.NN_vfnmsubpd,         # Negative Multiply and Subtract Packed Double-Precision Floating-Point
    NN_vfnmsubss = idaapi.NN_vfnmsubss,         # Negative Multiply and Subtract Scalar Single-Precision Floating-Point
    NN_vfnmsubsd = idaapi.NN_vfnmsubsd,         # Negative Multiply and Subtract Double Single-Precision Floating-Point



ASSIGNMENT_TYPES = [
]

UNCONDITIONAL_BRANCH_TYPES = [
]

CONDITIONAL_BRANCH_TYPES = [
]

UNIMPLEMENTED_TYPES = [
]
