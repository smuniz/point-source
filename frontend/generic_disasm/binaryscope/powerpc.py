#
# Copyright (c) 2013 Sebastian Muniz
# 
# This code is part of point source decompiler
#

from pybfd.bfd_arch_powerpc import InstructionSet as iset
from pybfd.bfd_arch_powerpc import Registers as regs


class InstructionSet:
    PPC_add = iset.PPC_add          # Add
    PPC_addc = iset.PPC_addc        # Add Carrying
    PPC_adde = iset.PPC_adde        # Add Extended
    PPC_addi = iset.PPC_addi        # Add Immediate
    PPC_addic = iset.PPC_addic      # Add Immediate Carrying
    PPC_addis = iset.PPC_addis      # Add Immediate Shifted
    PPC_addme = iset.PPC_addme      # Add to Minus One Extended
    PPC_addze = iset.PPC_addze      # Add to Zero Extended
    PPC_and = iset.PPC_and          # AND
    PPC_andc = iset.PPC_andc        # AND with Complement
    PPC_andi = iset.PPC_andi        # AND Immediate
    PPC_andis = iset.PPC_andis      # AND Immediate Shifted
    PPC_divd = iset.PPC_divd        # Divide Double Word
    PPC_divdu = iset.PPC_divdu      # Divide Double Word Unsigned
    PPC_divw = iset.PPC_divw        # Divide Word
    PPC_divwu = iset.PPC_divwu      # Divide Word Unsigned
    PPC_lbz = iset.PPC_lbz          # Load Byte and Zero
    PPC_lbzu = iset.PPC_lbzu        # Load Byte and Zero with Update
    PPC_lbzux = iset.PPC_lbzux      # Load Byte and Zero with Update Indexed
    PPC_lbzx = iset.PPC_lbzx        # Load Byte and Zero Indexed
    PPC_ld = iset.PPC_ld            # Load Double Word
    PPC_ldarx = iset.PPC_ldarx      # Load Double Word and Reserve Indexed
    PPC_ldu = iset.PPC_ldu          # Load Double Word with Update
    PPC_ldux = iset.PPC_ldux        # Load Double Word with Update Indexed
    PPC_ldx = iset.PPC_ldx          # Load Double Word Indexed
    PPC_lha = iset.PPC_lha          # Load Half Word Algebraic
    PPC_lhau = iset.PPC_lhau        # Load Half Word Algebraic with Update
    PPC_lhaux = iset.PPC_lhaux          # Load Half Word Algebraic with Update Indexed
    PPC_lhax = iset.PPC_lhax        # Load Half Word Algebraic Indexed
    PPC_lhbrx = iset.PPC_lhbrx          # Load Half Word Byte-reverse Indexed
    PPC_lhz = iset.PPC_lhz          # Load Half Word and Zero
    PPC_lhzu = iset.PPC_lhzu        # Load Half Word and Zero with Update
    PPC_lhzux = iset.PPC_lhzux          # Load Half Word and Zero with Update Indexed
    PPC_lhzx = iset.PPC_lhzx        # Load Half Word and Zero Indexed
    PPC_lmw = iset.PPC_lmw          # Load Multiple Word
    PPC_lswi = iset.PPC_lswi        # Load String Word Immediate
    PPC_lswx = iset.PPC_lswx        # Load String Word Indexed
    PPC_lwa = iset.PPC_lwa          # Load Word Algebraic
    PPC_lwarx = iset.PPC_lwarx          # Load Word and Reserve Indexed
    PPC_lwaux = iset.PPC_lwaux          # Load Word Algebraic with Update Indexed
    PPC_lwax = iset.PPC_lwax        # Load Word Algebraic Indexed
    PPC_lwbrx = iset.PPC_lwbrx          # Load Word Byte-Reverse Indexed
    PPC_lwz = iset.PPC_lwz          # Load Word and Zero
    PPC_lwzu = iset.PPC_lwzu        # Load Word and Zero with Update
    PPC_lwzux = iset.PPC_lwzux          # Load Word and Zero with Update Indexed
    PPC_lwzx = iset.PPC_lwzx        # Load Word and Zero Indexed
    PPC_mcrf = iset.PPC_mcrf        # Move Condition register Field
    PPC_mcrfs = iset.PPC_mcrfs          # Move to Condition Register from FPSCR
    PPC_mcrxr = iset.PPC_mcrxr          # Move to Condition Register from XER
    PPC_mfcr = iset.PPC_mfcr        # Move from Condition Register
    PPC_mffs = iset.PPC_mffs        # Move from FPSCR
    PPC_mfmsr = iset.PPC_mfmsr          # Move from Machine State Register
    PPC_mfspr = iset.PPC_mfspr          # Move from Special Purpose Register
    PPC_mfsr = iset.PPC_mfsr        # Move from Segment Register
    PPC_mfsrin = iset.PPC_mfsrin        # Move from Segment Register Indexed
    PPC_mftb = iset.PPC_mftb        # Move from Time Base
    PPC_mtcrf = iset.PPC_mtcrf          # Move to Condition Register Fields
    PPC_mtfsb0 = iset.PPC_mtfsb0        # Move to FPSCR Bit 0
    PPC_mtfsb1 = iset.PPC_mtfsb1        # Move to FPSCR Bit 1
    PPC_mtfsf = iset.PPC_mtfsf          # Move to FPSCR Fields
    PPC_mtfsfi = iset.PPC_mtfsfi        # Move to FPSCR Field Immediate
    PPC_mtmsr = iset.PPC_mtmsr          # Move to Machine State Register
    PPC_mtmsrd = iset.PPC_mtmsrd        # Move to Machine State Register Double Word
    PPC_mtspr = iset.PPC_mtspr          # Move to Special Purpose Register
    PPC_mtsr = iset.PPC_mtsr        # Move to Segment Register
    PPC_mtsrd = iset.PPC_mtsrd          # Move to Segment Register Double Word
    PPC_mtsrdin = iset.PPC_mtsrdin          # Move to Segment Register Indirect Double
    PPC_mtsrin = iset.PPC_mtsrin        # Move to Segment Register Indirect
    PPC_mulhd = iset.PPC_mulhd          # Multiply High Double Word
    PPC_mulhdu = iset.PPC_mulhdu        # Multiply High Double Word Unsigned
    PPC_mulhw = iset.PPC_mulhw          # Multiply High Word
    PPC_mulhwu = iset.PPC_mulhwu        # Multiply High Word Unsigned
    PPC_mulld = iset.PPC_mulld          # Multiply Low Double Word
    PPC_mulli = iset.PPC_mulli          # Multiply Low Immediate
    PPC_mullw = iset.PPC_mullw          # Multiply Low
    PPC_nand = iset.PPC_nand        # NAND (not AND)
    PPC_neg = iset.PPC_neg          # Negate
    PPC_nor = iset.PPC_nor          # NOR (not OR)
    PPC_or = iset.PPC_or        # OR
    PPC_orc = iset.PPC_orc          # OR with Complement
    PPC_ori = iset.PPC_ori          # OR Immediate
    PPC_oris = iset.PPC_oris        # OR Immediate Shifted
    PPC_rldcl = iset.PPC_rldcl          # Rotate Left Double Word then Clear Left
    PPC_rldcr = iset.PPC_rldcr          # Rotate Left Double Word then Clear Right
    PPC_rldic = iset.PPC_rldic          # Rotate Left Double Word Immediate then Clear
    PPC_rldicl = iset.PPC_rldicl        # Rotate Left Double Word Immediate then Clear Left
    PPC_rldicr = iset.PPC_rldicr        # Rotate Left Double Word Immediate then Clear Right
    PPC_rldimi = iset.PPC_rldimi        # Rotate Left Double Word Immediate then Mask Insert
    PPC_rlwimi = iset.PPC_rlwimi        # Rotate Left Word Immediate then Mask Insert
    PPC_rlwinm = iset.PPC_rlwinm        # Rotate Left Word Immediate then AND with Mask
    PPC_rlwnm = iset.PPC_rlwnm          # Rotate Left Word then AND with Mask
    PPC_sld = iset.PPC_sld          # Shift Left Double Word
    PPC_slw = iset.PPC_slw          # Shift Left Word
    PPC_srad = iset.PPC_srad        # Shift Right Algebraic Double Word
    PPC_sradi = iset.PPC_sradi          # Shift Right Algebraic Double Word Immediate
    PPC_sraw = iset.PPC_sraw        # Shift Right Algebraic Word
    PPC_srawi = iset.PPC_srawi          # Shift Right Algebraic Word Immediate
    PPC_srd = iset.PPC_srd          # Shift Right Double Word
    PPC_srw = iset.PPC_srw          # Shift Right Word
    PPC_stb = iset.PPC_stb          # Store Byte
    PPC_stbu = iset.PPC_stbu        # Store Byte with Update
    PPC_stbux = iset.PPC_stbux          # Store Byte with Update Indexed
    PPC_stbx = iset.PPC_stbx        # Store Byte Indexed
    PPC_std = iset.PPC_std          # Store Double Word
    PPC_stdcx = iset.PPC_stdcx          # Store Double Word Conditional Indexed
    PPC_stdu = iset.PPC_stdu        # Store Double Word with Update
    PPC_stdux = iset.PPC_stdux          # Store Double Word with Update Indexed
    PPC_stdx = iset.PPC_stdx        # Store Double Word Indexed
    PPC_sth = iset.PPC_sth          # Store Half Word
    PPC_sthbrx = iset.PPC_sthbrx        # Store Half Word Byte-Reverse Indexed
    PPC_sthu = iset.PPC_sthu        # Store Half Word with Update
    PPC_sthux = iset.PPC_sthux          # Store Half Word with Update Indexed
    PPC_sthx = iset.PPC_sthx        # Store Half Word Indexed
    PPC_stmw = iset.PPC_stmw        # Store Multiple Word
    PPC_stswi = iset.PPC_stswi          # Store String Word Immediate
    PPC_stswx = iset.PPC_stswx          # Store String Word Indexed
    PPC_stw = iset.PPC_stw          # Store Word
    PPC_stwbrx = iset.PPC_stwbrx        # Store Word Byte-Reverse Indexed
    PPC_stwcx = iset.PPC_stwcx          # Store Word Conditional Indexed
    PPC_stwu = iset.PPC_stwu        # Store Word with Update
    PPC_stwux = iset.PPC_stwux          # Store Word with Update Indexed
    PPC_stwx = iset.PPC_stwx        # Store Word Indexed
    PPC_subf = iset.PPC_subf        # Subtract from
    PPC_subfc = iset.PPC_subfc          # Subtract from Carrying
    PPC_subfe = iset.PPC_subfe          # Subtract from Extended
    PPC_subfic = iset.PPC_subfic        # Subtract from Immediate Carrying
    PPC_subfme = iset.PPC_subfme        # Subtract from Minus One Extended
    PPC_subfze = iset.PPC_subfze        # Subtract from Zero Extended
    PPC_xor = iset.PPC_xor          # XOR
    PPC_xori = iset.PPC_xori        # XOR Immediate
    PPC_xoris = iset.PPC_xoris          # XOR Immediate Shifted

    PPC_nop = iset.PPC_nop          # No Operation
    PPC_not = iset.PPC_not          # Complement Register
    PPC_mr = iset.PPC_mr        # Move Register

    PPC_subi = iset.PPC_subi        # Subtract Immediate
    PPC_subic = iset.PPC_subic          # Subtract Immediate Carrying
    PPC_subis = iset.PPC_subis          # Subtract Immediate Shifted
    PPC_li = iset.PPC_li        # Load Immediate
    PPC_lis = iset.PPC_lis          # Load Immediate Shifted

    PPC_mtxer = iset.PPC_mtxer          # Move to integer unit exception register
    PPC_mtlr = iset.PPC_mtlr        # Move to link register
    PPC_mtctr = iset.PPC_mtctr          # Move to count register
    PPC_mtdsisr = iset.PPC_mtdsisr          # Move to DAE/source instruction service register
    PPC_mtdar = iset.PPC_mtdar          # Move to data address register
    PPC_mtdec = iset.PPC_mtdec          # Move to decrementer register
    PPC_mtsrr0 = iset.PPC_mtsrr0        # Move to status save/restore register 0
    PPC_mtsrr1 = iset.PPC_mtsrr1        # Move to status save/restore register 1
    PPC_mtsprg0 = iset.PPC_mtsprg0          # Move to general special purpose register 0
    PPC_mtsprg1 = iset.PPC_mtsprg1          # Move to general special purpose register 1
    PPC_mtsprg2 = iset.PPC_mtsprg2          # Move to general special purpose register 2
    PPC_mtsprg3 = iset.PPC_mtsprg3          # Move to general special purpose register 3
    PPC_mttbl = iset.PPC_mttbl          # Move to time base register (lower)
    PPC_mttbu = iset.PPC_mttbu          # Move to time base register (upper)
    PPC_mfxer = iset.PPC_mfxer          # Move from integer unit exception register
    PPC_mflr = iset.PPC_mflr        # Move from link register
    PPC_mfctr = iset.PPC_mfctr          # Move from count register
    PPC_mfdsisr = iset.PPC_mfdsisr          # Move from DAE/source instruction service register
    PPC_mfdar = iset.PPC_mfdar          # Move from data address register
    PPC_mfdec = iset.PPC_mfdec          # Move from decrementer register
    PPC_mfsrr0 = iset.PPC_mfsrr0        # Move from status save/restore register 0
    PPC_mfsrr1 = iset.PPC_mfsrr1        # Move from status save/restore register 1
    PPC_mfsprg0 = iset.PPC_mfsprg0          # Move from general special purpose register 0
    PPC_mfsprg1 = iset.PPC_mfsprg1          # Move from general special purpose register 1
    PPC_mfsprg2 = iset.PPC_mfsprg2          # Move from general special purpose register 2
    PPC_mfsprg3 = iset.PPC_mfsprg3          # Move from general special purpose register 3
    #PPC_mftbl = iset.PPC_mftbl          # Move from time base register (lower)
    PPC_mftbu = iset.PPC_mftbu          # Move from time base register (upper)
    PPC_mfpvr = iset.PPC_mfpvr          # Move from processor version register

    # UNCONDITIONAL_BRANCH_TYPES
    PPC_b = iset.PPC_b          # Branch
    #PPC_balways = iset.PPC_balways          # Branch unconditionally

    # CONDITIONAL_BRANCH_TYPES
    PPC_bc = iset.PPC_bc        # Branch Conditional
    PPC_bcctr = iset.PPC_bcctr          # Branch Conditional to Count Register
    PPC_bclr = iset.PPC_bclr        # Branch Conditional to Link Register

    # suffixes:
    #      lr      - goto lr
    #      ctr     - goto ctr
    #      l       - update lr
    #      a       - absolute

    PPC_bt = iset.PPC_bt        # Branch if true
    PPC_bf = iset.PPC_bf        # Branch if false
    PPC_bdnz = iset.PPC_bdnz        # CTR--; branch if CTR non-zero
    PPC_bdnzt = iset.PPC_bdnzt          # CTR--; branch if CTR non-zero and condition is true
    PPC_bdnzf = iset.PPC_bdnzf          # CTR--; branch if CTR non-zero and condition is false
    PPC_bdz = iset.PPC_bdz          # CTR--; branch if CTR zero
    PPC_bdzt = iset.PPC_bdzt        # CTR--; branch if CTR zero and condition is true
    PPC_bdzf = iset.PPC_bdzf        # CTR--; branch if CTR zero and condition is false

    PPC_blt = iset.PPC_blt          # Branch if less than
    PPC_ble = iset.PPC_ble          # Branch if less than or equal
    PPC_beq = iset.PPC_beq          # Branch if equal
    PPC_bge = iset.PPC_bge          # Branch if greater than or equal
    PPC_bgt = iset.PPC_bgt          # Branch if greater than
    PPC_bne = iset.PPC_bne          # Branch if not equal
    PPC_bso = iset.PPC_bso          # Branch if summary overflow
    PPC_bns = iset.PPC_bns          # Branch if not summary overflow

    # UNIMPLEMENTED_TYPES
    PPC_cmp = iset.PPC_cmp          # Compare
    PPC_cmpi = iset.PPC_cmpi        # Compare Immediate
    PPC_cmpl = iset.PPC_cmpl        # Compare Logical
    PPC_cmpli = iset.PPC_cmpli          # Compare Logical Immediate
    PPC_cntlzd = iset.PPC_cntlzd        # Count Leading Zeros Double Word
    PPC_cntlzw = iset.PPC_cntlzw        # Count Leading Zeros Word
    PPC_crand = iset.PPC_crand          # Condition Register AND
    PPC_crandc = iset.PPC_crandc        # Condition Register AND with Complement
    PPC_creqv = iset.PPC_creqv          # Condition Register Equivalent
    PPC_crnand = iset.PPC_crnand        # Condition Register NAND
    PPC_crnor = iset.PPC_crnor          # Condition Register NOR
    PPC_cror = iset.PPC_cror        # Condiiton Register OR
    PPC_crorc = iset.PPC_crorc          # Condition Register OR with Comlement
    PPC_crxor = iset.PPC_crxor          # Condition Register XOR
    #PPC_dcba = iset.PPC_dcba           #
    #PPC_dcbf = iset.PPC_dcbf           # Data Cache Block Flush
    #PPC_dcbi = iset.PPC_dcbi           # Data Cache Block Invalidate
    #PPC_dcbst = iset.PPC_dcbst         # Data Cache Block Store
    #PPC_dcbt = iset.PPC_dcbt           # Data Cache Block Touch
    #PPC_dcbtst = iset.PPC_dcbtst           # Data Cache Block Touch for Store
    #PPC_dcbz = iset.PPC_dcbz           # Data Cache Block Set to Zero
    PPC_eciwx = iset.PPC_eciwx          # External Control In Word Indexed
    PPC_ecowx = iset.PPC_ecowx          # External Control Out Word Indexed
    PPC_eieio = iset.PPC_eieio          # Enforce In-Order Execution of I/O
    PPC_eqv = iset.PPC_eqv          # Equivalent
    PPC_extsb = iset.PPC_extsb          # Extend Sign Byte
    PPC_extsh = iset.PPC_extsh          # Extend Sign Half Word
    PPC_extsw = iset.PPC_extsw          # Extend Sign Word
    #PPC_fabs = iset.PPC_fabs           # Floating-Point Absolute Value
    #PPC_fadd = iset.PPC_fadd           # Floating-Point Add
    #PPC_fadds = iset.PPC_fadds         # Floating-Point Add (Single-Precision)
    #PPC_fcfid = iset.PPC_fcfid         # Floating-Point Convert from Integer Double Word
    #PPC_fcmpo = iset.PPC_fcmpo         # Floating-Point Compare Ordered
    #PPC_fcmpu = iset.PPC_fcmpu         # Floating-Point Compare Unordered
    #PPC_fctid = iset.PPC_fctid         # Floating-Point Convert to Integer Double Word
    #PPC_fctidz = iset.PPC_fctidz           # Floating-Point Convert to Integer Double Word with Round toward Zero
    #PPC_fctiw = iset.PPC_fctiw         # Floating-Point Convert to Integer Word
    #PPC_fctiwz = iset.PPC_fctiwz           # Floating-Point Convert to Integer Word with Round toward Zero
    #PPC_fdiv = iset.PPC_fdiv           # Floating-Point Divide
    #PPC_fdivs = iset.PPC_fdivs         # Floating-Point Divide Single-Precision
    #PPC_fmadd = iset.PPC_fmadd         # Floating-Point Multiply-Add
    #PPC_fmadds = iset.PPC_fmadds           # Floating-Point Multiply-Add Single-Precision
    #PPC_fmr = iset.PPC_fmr         # Floating-Point Move Register
    #PPC_fmsub = iset.PPC_fmsub         # Floating-Point Multiply-Subtract
    #PPC_fmsubs = iset.PPC_fmsubs           # Floating-Point Multiply-Subtract (Single-Precision)
    #PPC_fmul = iset.PPC_fmul           # Floating-Point Multiply
    #PPC_fmuls = iset.PPC_fmuls         # Floating-Point Multiply Single-Precision
    #PPC_fnabs = iset.PPC_fnabs         # Floating-Point Negative Absolute Value
    #PPC_fneg = iset.PPC_fneg           # Floating-Point Negate
    #PPC_fnmadd = iset.PPC_fnmadd           # Floating-Point Negative Multiply-Add
    #PPC_fnmadds = iset.PPC_fnmadds         # Floating-Point Negative Multiply-Add Single-Precision
    #PPC_fnmsub = iset.PPC_fnmsub           # Floating-Point Negative Multiply-Subtract
    #PPC_fnmsubs = iset.PPC_fnmsubs         # Floating-Point Negative Multiply-Subtract Single-Precision
    #PPC_fres = iset.PPC_fres           # Floating-Point Reciprocal Estimate Single-Precision
    #PPC_frsp = iset.PPC_frsp           # Floating-Point Round to Single-Precision
    #PPC_frsqrte = iset.PPC_frsqrte         # Floating-Point Reciprocal Square Root Estimate
    #PPC_fsel = iset.PPC_fsel           # Floating-Point Select
    #PPC_fsqrt = iset.PPC_fsqrt         # Floating-Point Square Root
    #PPC_fsqrts = iset.PPC_fsqrts           # Floating-Point Square Root Single-Precision
    #PPC_fsub = iset.PPC_fsub           # Floating-Point Subtract
    #PPC_fsubs = iset.PPC_fsubs         # Floating-Point Subtract Single-Precision
    #PPC_icbi = iset.PPC_icbi           # Instruction Cache Block Invalidate
    #PPC_isync = iset.PPC_isync         # Instruction Synchronize
    #PPC_lfd = iset.PPC_lfd         # Load Floating-Point Double-Precision
    #PPC_lfdu = iset.PPC_lfdu           # Load Floating-Point Double-Precision with Update
    #PPC_lfdux = iset.PPC_lfdux         # Load Floating-Point Double-Precision with Update Indexed
    #PPC_lfdx = iset.PPC_lfdx           # Load Floating-Point Double-Precision Indexed
    #PPC_lfs = iset.PPC_lfs         # Load Floating-Point Single-Precision
    #PPC_lfsu = iset.PPC_lfsu           # Load Floating-Point Single-Precision with Update
    #PPC_lfsux = iset.PPC_lfsux         # Load Floating-Point Single-Precision with Update Indexed
    #PPC_lfsx = iset.PPC_lfsx           # Load Floating-Point Single-Precision Indexed
    #PPC_rfi = iset.PPC_rfi         # Return from Interrupt
    #PPC_rfid = iset.PPC_rfid           # Return from Interrupt Double Word
    #PPC_sc = iset.PPC_sc           # System Call
    #PPC_slbia = iset.PPC_slbia         # SLB Invalidate All
    #PPC_slbie = iset.PPC_slbie         # SLB Invalidate Entry
    #PPC_stfd = iset.PPC_stfd           # Store Floating-Point Double-Precision
    #PPC_stfdu = iset.PPC_stfdu         # Store Floating-Point Double-Precision wiht Update
    #PPC_stfdux = iset.PPC_stfdux           # Store Floating-Point Double-Precision wiht Update Indexed
    #PPC_stfdx = iset.PPC_stfdx         # Store Floating-Point Double-Precision Indexed
    #PPC_stfiwx = iset.PPC_stfiwx           # Store Floating-Point as Integer Word Indexed
    #PPC_stfs = iset.PPC_stfs           # Store Floating-Point Single-Precision
    #PPC_stfsu = iset.PPC_stfsu         # Store Floating-Point Single-Precision with Update
    #PPC_stfsux = iset.PPC_stfsux           # Store Floating-Point Single-Precision with Update Indexed
    #PPC_stfsx = iset.PPC_stfsx         # Store Floating-Point Single-Precision Indexed
    #PPC_sync = iset.PPC_sync           # Synchronize
    #PPC_td = iset.PPC_td           # Trap Double Word
    #PPC_tdi = iset.PPC_tdi         # Trap Double Word Immediate
    #PPC_tlbia = iset.PPC_tlbia         # TLB Invalidate All
    #PPC_tlbie = iset.PPC_tlbie         # TLB Invalidate Entry
    #PPC_tlbsync = iset.PPC_tlbsync         # TLB Synchronize
    #PPC_tw = iset.PPC_tw           # Trap Word
    #PPC_twi = iset.PPC_twi         # Trap Word Immediate

    #-------------

    PPC_cmpwi = iset.PPC_cmpwi          # Compare Word Immediate
    PPC_cmpw = iset.PPC_cmpw        # Compare Word
    PPC_cmplwi = iset.PPC_cmplwi        # Compare Logical Word Immediate
    PPC_cmplw = iset.PPC_cmplw          # Compare Logical Word
    PPC_cmpdi = iset.PPC_cmpdi          # Compare Double Word Immediate
    PPC_cmpd = iset.PPC_cmpd        # Compare Double Word
    PPC_cmpldi = iset.PPC_cmpldi        # Compare Logical Double Word Immediate
    PPC_cmpld = iset.PPC_cmpld          # Compare Logical Double Word

    #PPC_trap = iset.PPC_trap           # Trap Word Unconditionally
    #PPC_trapd = iset.PPC_trapd         # Trap Double Word Unconditionally
    #PPC_twlgt = iset.PPC_twlgt         # Trap Word if Logically Greater Than
    #PPC_twllt = iset.PPC_twllt         # Trap Word if Logically Less Than
    #PPC_tweq = iset.PPC_tweq           # Trap Word if Equal
    #PPC_twlge = iset.PPC_twlge         # Trap Word if Logically Greater Than or Equal
    #PPC_twlle = iset.PPC_twlle         # Trap Word if Logically Less Than or Equal
    #PPC_twgt = iset.PPC_twgt           # Trap Word if Greater Than
    #PPC_twge = iset.PPC_twge           # Trap Word if Greater Than or Equal
    #PPC_twlt = iset.PPC_twlt           # Trap Word if Less Than
    #PPC_twle = iset.PPC_twle           # Trap Word if Less Than oe Equal
    #PPC_twne = iset.PPC_twne           # Trap Word if Not Equal
    #PPC_twlgti = iset.PPC_twlgti           # Trap Word Immediate if Logically Greater Than
    #PPC_twllti = iset.PPC_twllti           # Trap Word Immediate if Logically Less Than
    #PPC_tweqi = iset.PPC_tweqi         # Trap Word Immediate if Equal
    #PPC_twlgei = iset.PPC_twlgei           # Trap Word Immediate if Logically Greater Than or Equal
    #PPC_twllei = iset.PPC_twllei           # Trap Word Immediate if Logically Less Than or Equal
    #PPC_twgti = iset.PPC_twgti         # Trap Word Immediate if Greater Than
    #PPC_twgei = iset.PPC_twgei         # Trap Word Immediate if Greater Than or Equal
    #PPC_twlti = iset.PPC_twlti         # Trap Word Immediate if Less Than
    #PPC_twlei = iset.PPC_twlei         # Trap Word Immediate if Less Than oe Equal
    #PPC_twnei = iset.PPC_twnei         # Trap Word Immediate if Not Equal
    #PPC_tdlgt = iset.PPC_tdlgt         # Trap Double Word if Logically Greater Than
    #PPC_tdllt = iset.PPC_tdllt         # Trap Double Word if Logically Less Than
    #PPC_tdeq = iset.PPC_tdeq           # Trap Double Word if Equal
    #PPC_tdlge = iset.PPC_tdlge         # Trap Double Word if Logically Greater Than or Equal
    #PPC_tdlle = iset.PPC_tdlle         # Trap Double Word if Logically Less Than or Equal
    #PPC_tdgt = iset.PPC_tdgt           # Trap Double Word if Greater Than
    #PPC_tdge = iset.PPC_tdge           # Trap Double Word if Greater Than or Equal
    #PPC_tdlt = iset.PPC_tdlt           # Trap Double Word if Less Than
    #PPC_tdle = iset.PPC_tdle           # Trap Double Word if Less Than oe Equal
    #PPC_tdne = iset.PPC_tdne           # Trap Double Word if Not Equal
    #PPC_tdlgti = iset.PPC_tdlgti           # Trap Double Word Immediate if Logically Greater Than
    #PPC_tdllti = iset.PPC_tdllti           # Trap Double Word Immediate if Logically Less Than
    #PPC_tdeqi = iset.PPC_tdeqi         # Trap Double Word Immediate if Equal
    #PPC_tdlgei = iset.PPC_tdlgei           # Trap Double Word Immediate if Logically Greater Than or Equal
    #PPC_tdllei = iset.PPC_tdllei           # Trap Double Word Immediate if Logically Less Than or Equal
    #PPC_tdgti = iset.PPC_tdgti         # Trap Double Word Immediate if Greater Than
    #PPC_tdgei = iset.PPC_tdgei         # Trap Double Word Immediate if Greater Than or Equal
    #PPC_tdlti = iset.PPC_tdlti         # Trap Double Word Immediate if Less Than
    #PPC_tdlei = iset.PPC_tdlei         # Trap Double Word Immediate if Less Than oe Equal
    #PPC_tdnei = iset.PPC_tdnei         # Trap Double Word Immediate if Not Equal

    PPC_crset = iset.PPC_crset          # Condition Register Set
    PPC_crnot = iset.PPC_crnot          # Condition Register NOT
    PPC_crmove = iset.PPC_crmove        # Condition Register Move
    PPC_crclr = iset.PPC_crclr          # Condition Register Clear

    PPC_extlwi = iset.PPC_extlwi        # Extract and Left Justify Immediate
    PPC_extrwi = iset.PPC_extrwi        # Extract and Right Justify Immediate
    PPC_inslwi = iset.PPC_inslwi        # Insert from Left Immediate
    PPC_insrwi = iset.PPC_insrwi        # Insert from Right Immediate
    PPC_rotlwi = iset.PPC_rotlwi        # Rotate Left Immediate
    PPC_rotrwi = iset.PPC_rotrwi        # Rotate Right Immediate
    PPC_rotlw = iset.PPC_rotlw          # Rotate Left
    PPC_slwi = iset.PPC_slwi        # Shift Left Immediate
    PPC_srwi = iset.PPC_srwi        # Shift Right Immediate
    PPC_clrlwi = iset.PPC_clrlwi        # Clear Left Immediate
    PPC_clrrwi = iset.PPC_clrrwi        # Clear Right Immediate
    PPC_clrlslwi = iset.PPC_clrlslwi        # Clear Left and Shift Left Immediate

    #
    #  PowerPC Embedded Controller Instructions
    #

    #PPC_dccci = iset.PPC_dccci         # Data cache congruence class invalidate (p.438-439)
    #PPC_dcread = iset.PPC_dcread           # Data cache read (p.440-441)
    #PPC_icbt = iset.PPC_icbt           # Instruction cache block touch (p.450-451)
    #PPC_iccci = iset.PPC_iccci         # Instruction cache congruence class invalidate (p.452-453)
    #PPC_icread = iset.PPC_icread           # Instruction cache read (p.454-455)
    #PPC_mfdcr = iset.PPC_mfdcr         # Move from device control register (p.484-485)
    #PPC_mtdcr = iset.PPC_mtdcr         # Move to device control register (p.491-492)
    #PPC_rfci = iset.PPC_rfci           # Return from critical interrupt (p.507)
    #PPC_tlbre = iset.PPC_tlbre         # TLB read entry (p.548-549)
    #PPC_tlbsx = iset.PPC_tlbsx         # TLB search indexed (p.550)
    #PPC_tlbwe = iset.PPC_tlbwe         # TLB write entry (p.552-553)
    #PPC_wrtee = iset.PPC_wrtee         # Write external enable (p.560)
    #PPC_wrteei = iset.PPC_wrteei           # Write external enable immediate (p.561)

    #
    #  New PowerPC instructions
    #

    #PPC_abs = iset.PPC_abs         # Absolute
    #PPC_clcs = iset.PPC_clcs           # Cache Lines Compute Size
    #PPC_clf = iset.PPC_clf         # Cache Line Flush
    #PPC_cli = iset.PPC_cli         # Cache Line Invalidate
    #PPC_dclst = iset.PPC_dclst         # Data Cache Line Store
    #PPC_div = iset.PPC_div         # Divide
    #PPC_divs = iset.PPC_divs           # Divide Short
    #PPC_doz = iset.PPC_doz         # Different Or Zero
    #PPC_dozi = iset.PPC_dozi           # Different Or Zero Immediate
    #PPC_frsqrtes = iset.PPC_frsqrtes           # Floating Reciprocal Square Root Estimate Single
    #PPC_hrfid = iset.PPC_hrfid         # Hypervisor Return from Interrupt Doubleword
    #PPC_lscbx = iset.PPC_lscbx         # Load String And Compare Byte Indexed
    #PPC_maskg = iset.PPC_maskg         # Mask Generate
    #PPC_maskir = iset.PPC_maskir           # Mask Insert From Register
    #PPC_mfsri = iset.PPC_mfsri         # Move From Segment Register Indirect
    #PPC_mul = iset.PPC_mul         # Multiply
    #PPC_nabs = iset.PPC_nabs           # Negative Absolute
    #PPC_popcntb = iset.PPC_popcntb         # Population Count Bytes
    #PPC_rac = iset.PPC_rac         # Real Address Compute
    #PPC_rfsvc = iset.PPC_rfsvc         # Return From SVC
    #PPC_rlmi = iset.PPC_rlmi           # Rotate Left Then Mask Insert
    #PPC_rrib = iset.PPC_rrib           # Rotate Right And Insert Bit
    #PPC_slbmfee = iset.PPC_slbmfee         # SLB Move From Entry ESID
    #PPC_slbmfev = iset.PPC_slbmfev         # SLB Move From Entry VSID
    #PPC_slbmte = iset.PPC_slbmte           # SLB Move To Entry
    #PPC_sle = iset.PPC_sle         # Shift Left Extended
    #PPC_sleq = iset.PPC_sleq           # Shift Left Extended With MQ
    #PPC_sliq = iset.PPC_sliq           # Shift Left Immediate With MQ
    #PPC_slliq = iset.PPC_slliq         # Shift Left Long Immediate With MQ
    #PPC_sllq = iset.PPC_sllq           # Shift Left Long With MQ
    #PPC_slq = iset.PPC_slq         # Shift Left With MQ
    #PPC_sraiq = iset.PPC_sraiq         # Shift Right Algebraic Immediate With MQ
    #PPC_sraq = iset.PPC_sraq           # Shift Right Algebraic With MQ
    #PPC_sre = iset.PPC_sre         # Shift Right Extended
    #PPC_srea = iset.PPC_srea           # Shift Right Extended Algebraic
    #PPC_sreq = iset.PPC_sreq           # Shift Right Extended With MQ
    #PPC_sriq = iset.PPC_sriq           # Shift Right Immediate With MQ
    #PPC_srliq = iset.PPC_srliq         # Shift Right Long Immediate With MQ
    #PPC_srlq = iset.PPC_srlq           # Shift Right Long With MQ
    #PPC_srq = iset.PPC_srq         # Shift Right With MQ

    #
    #   New PowerPC instructions
    #

    #PPC_mtocrf = iset.PPC_mtocrf           # Move To One Condition Register Field
    #PPC_mfocrf = iset.PPC_mfocrf           # Move From One Condition Register Field

    R0 = regs.R0
    R1 = regs.R1
    SP = R1
    R2 = regs.R2
    TOC = R2
    R3 = regs.R3
    R4 = regs.R4
    R5 = regs.R5
    R6 = regs.R6
    R7 = regs.R7
    R8 = regs.R8
    R9 = regs.R9
    R10 = regs.R10
    R11 = regs.R11
    R12 = regs.R12 
    R13 = regs.R13
    R14 = regs.R14
    R15 = regs.R15
    R16 = regs.R16
    R17 = regs.R17
    R18 = regs.R18
    R19 = regs.R19
    R20 = regs.R20
    R21 = regs.R21
    R22 = regs.R22
    R23 = regs.R23
    R24 = regs.R24
    R25 = regs.R25
    R26 = regs.R26
    R27 = regs.R27
    R28 = regs.R28
    R29 = regs.R29
    R30 = regs.R30
    R31 = regs.R31

    TOTAL_GPR = 32      # Number of general purpose registers.

    #
    # Special purpose registers in PowerPC
    #
    o_spr       = 7       # Special purpose register
    o_twofpr    = 8       # Two FPPR_s
    o_shmbme    = 9       # SH & MB & ME
    o_crf       = 10      # crfield      x.reg
    o_crb       = 11      # crbit        x.reg
    o_dcr       = 12      # Device control register

    ARGUMENT_REGISTERS = [R3, R4, R5, R6, R7, R8, R9, R10]

ASSIGNMENT_TYPES = [
    InstructionSet.PPC_add,         # Add
    InstructionSet.PPC_addc,        # Add Carrying
    InstructionSet.PPC_adde,        # Add Extended
    InstructionSet.PPC_addi,        # Add Immediate
    InstructionSet.PPC_addic,       # Add Immediate Carrying
    InstructionSet.PPC_addis,       # Add Immediate Shifted
    InstructionSet.PPC_addme,       # Add to Minus One Extended
    InstructionSet.PPC_addze,       # Add to Zero Extended
    InstructionSet.PPC_and,         # AND
    InstructionSet.PPC_andc,        # AND with Complement
    InstructionSet.PPC_andi,        # AND Immediate
    InstructionSet.PPC_andis,       # AND Immediate Shifted
    InstructionSet.PPC_divd,        # Divide Double Word
    InstructionSet.PPC_divdu,       # Divide Double Word Unsigned
    InstructionSet.PPC_divw,        # Divide Word
    InstructionSet.PPC_divwu,       # Divide Word Unsigned
    InstructionSet.PPC_lbz,         # Load Byte and Zero
    InstructionSet.PPC_lbzu,        # Load Byte and Zero with Update
    InstructionSet.PPC_lbzux,       # Load Byte and Zero with Update Indexed
    InstructionSet.PPC_lbzx,        # Load Byte and Zero Indexed
    InstructionSet.PPC_ld,          # Load Double Word
    InstructionSet.PPC_ldarx,       # Load Double Word and Reserve Indexed
    InstructionSet.PPC_ldu,         # Load Double Word with Update
    InstructionSet.PPC_ldux,        # Load Double Word with Update Indexed
    InstructionSet.PPC_ldx,         # Load Double Word Indexed
    InstructionSet.PPC_lha,         # Load Half Word Algebraic
    InstructionSet.PPC_lhau,        # Load Half Word Algebraic with Update
    InstructionSet.PPC_lhaux,       # Load Half Word Algebraic with Update Indexed
    InstructionSet.PPC_lhax,        # Load Half Word Algebraic Indexed
    InstructionSet.PPC_lhbrx,       # Load Half Word Byte-reverse Indexed
    InstructionSet.PPC_lhz,         # Load Half Word and Zero
    InstructionSet.PPC_lhzu,        # Load Half Word and Zero with Update
    InstructionSet.PPC_lhzux,       # Load Half Word and Zero with Update Indexed
    InstructionSet.PPC_lhzx,        # Load Half Word and Zero Indexed
    InstructionSet.PPC_lmw,         # Load Multiple Word
    InstructionSet.PPC_lswi,        # Load String Word Immediate
    InstructionSet.PPC_lswx,        # Load String Word Indexed
    InstructionSet.PPC_lwa,         # Load Word Algebraic
    InstructionSet.PPC_lwarx,       # Load Word and Reserve Indexed
    InstructionSet.PPC_lwaux,       # Load Word Algebraic with Update Indexed
    InstructionSet.PPC_lwax,        # Load Word Algebraic Indexed
    InstructionSet.PPC_lwbrx,       # Load Word Byte-Reverse Indexed
    InstructionSet.PPC_lwz,         # Load Word and Zero
    InstructionSet.PPC_lwzu,        # Load Word and Zero with Update
    InstructionSet.PPC_lwzux,       # Load Word and Zero with Update Indexed
    InstructionSet.PPC_lwzx,        # Load Word and Zero Indexed
    InstructionSet.PPC_mcrf,        # Move Condition register Field
    InstructionSet.PPC_mcrfs,       # Move to Condition Register from FPSCR
    InstructionSet.PPC_mcrxr,       # Move to Condition Register from XER
    InstructionSet.PPC_mfcr,        # Move from Condition Register
    InstructionSet.PPC_mffs,        # Move from FPSCR
    InstructionSet.PPC_mfmsr,       # Move from Machine State Register
    InstructionSet.PPC_mfspr,       # Move from Special Purpose Register
    InstructionSet.PPC_mfsr,        # Move from Segment Register
    InstructionSet.PPC_mfsrin,      # Move from Segment Register Indexed
    InstructionSet.PPC_mftb,        # Move from Time Base
    InstructionSet.PPC_mtcrf,       # Move to Condition Register Fields
    InstructionSet.PPC_mtfsb0,      # Move to FPSCR Bit 0
    InstructionSet.PPC_mtfsb1,      # Move to FPSCR Bit 1
    InstructionSet.PPC_mtfsf,       # Move to FPSCR Fields
    InstructionSet.PPC_mtfsfi,      # Move to FPSCR Field Immediate
    InstructionSet.PPC_mtmsr,       # Move to Machine State Register
    InstructionSet.PPC_mtmsrd,      # Move to Machine State Register Double Word
    InstructionSet.PPC_mtspr,       # Move to Special Purpose Register
    InstructionSet.PPC_mtsr,        # Move to Segment Register
    InstructionSet.PPC_mtsrd,       # Move to Segment Register Double Word
    InstructionSet.PPC_mtsrdin,     # Move to Segment Register Indirect Double
    InstructionSet.PPC_mtsrin,      # Move to Segment Register Indirect
    InstructionSet.PPC_mulhd,       # Multiply High Double Word
    InstructionSet.PPC_mulhdu,      # Multiply High Double Word Unsigned
    InstructionSet.PPC_mulhw,       # Multiply High Word
    InstructionSet.PPC_mulhwu,      # Multiply High Word Unsigned
    InstructionSet.PPC_mulld,       # Multiply Low Double Word
    InstructionSet.PPC_mulli,       # Multiply Low Immediate
    InstructionSet.PPC_mullw,       # Multiply Low
    InstructionSet.PPC_nand,        # NAND (not AND)
    InstructionSet.PPC_neg,         # Negate
    InstructionSet.PPC_nor,         # NOR (not OR)
    InstructionSet.PPC_or,          # OR
    InstructionSet.PPC_orc,         # OR with Complement
    InstructionSet.PPC_ori,         # OR Immediate
    InstructionSet.PPC_oris,        # OR Immediate Shifted
    InstructionSet.PPC_rldcl,       # Rotate Left Double Word then Clear Left
    InstructionSet.PPC_rldcr,       # Rotate Left Double Word then Clear Right
    InstructionSet.PPC_rldic,       # Rotate Left Double Word Immediate then Clear
    InstructionSet.PPC_rldicl,      # Rotate Left Double Word Immediate then Clear Left
    InstructionSet.PPC_rldicr,      # Rotate Left Double Word Immediate then Clear Right
    InstructionSet.PPC_rldimi,      # Rotate Left Double Word Immediate then Mask Insert
    InstructionSet.PPC_rlwimi,      # Rotate Left Word Immediate then Mask Insert
    InstructionSet.PPC_rlwinm,      # Rotate Left Word Immediate then AND with Mask
    InstructionSet.PPC_rlwnm,       # Rotate Left Word then AND with Mask
    InstructionSet.PPC_sld,         # Shift Left Double Word
    InstructionSet.PPC_slw,         # Shift Left Word
    InstructionSet.PPC_srad,        # Shift Right Algebraic Double Word
    InstructionSet.PPC_sradi,       # Shift Right Algebraic Double Word Immediate
    InstructionSet.PPC_sraw,        # Shift Right Algebraic Word
    InstructionSet.PPC_srawi,       # Shift Right Algebraic Word Immediate
    InstructionSet.PPC_srd,         # Shift Right Double Word
    InstructionSet.PPC_srw,         # Shift Right Word
    InstructionSet.PPC_stb,         # Store Byte
    InstructionSet.PPC_stbu,        # Store Byte with Update
    InstructionSet.PPC_stbux,       # Store Byte with Update Indexed
    InstructionSet.PPC_stbx,        # Store Byte Indexed
    InstructionSet.PPC_std,         # Store Double Word
    InstructionSet.PPC_stdcx,       # Store Double Word Conditional Indexed
    InstructionSet.PPC_stdu,        # Store Double Word with Update
    InstructionSet.PPC_stdux,       # Store Double Word with Update Indexed
    InstructionSet.PPC_stdx,        # Store Double Word Indexed
    InstructionSet.PPC_sth,         # Store Half Word
    InstructionSet.PPC_sthbrx,      # Store Half Word Byte-Reverse Indexed
    InstructionSet.PPC_sthu,        # Store Half Word with Update
    InstructionSet.PPC_sthux,       # Store Half Word with Update Indexed
    InstructionSet.PPC_sthx,        # Store Half Word Indexed
    InstructionSet.PPC_stmw,        # Store Multiple Word
    InstructionSet.PPC_stswi,       # Store String Word Immediate
    InstructionSet.PPC_stswx,       # Store String Word Indexed
    InstructionSet.PPC_stw,         # Store Word
    InstructionSet.PPC_stwbrx,      # Store Word Byte-Reverse Indexed
    InstructionSet.PPC_stwcx,       # Store Word Conditional Indexed
    InstructionSet.PPC_stwu,        # Store Word with Update
    InstructionSet.PPC_stwux,       # Store Word with Update Indexed
    InstructionSet.PPC_stwx,        # Store Word Indexed
    InstructionSet.PPC_subf,        # Subtract from
    InstructionSet.PPC_subfc,       # Subtract from Carrying
    InstructionSet.PPC_subfe,       # Subtract from Extended
    InstructionSet.PPC_subfic,      # Subtract from Immediate Carrying
    InstructionSet.PPC_subfme,      # Subtract from Minus One Extended
    InstructionSet.PPC_subfze,      # Subtract from Zero Extended
    InstructionSet.PPC_xor,         # XOR
    InstructionSet.PPC_xori,        # XOR Immediate
    InstructionSet.PPC_xoris,       # XOR Immediate Shifted

    InstructionSet.PPC_nop,         # No Operation
    InstructionSet.PPC_not,         # Complement Register
    InstructionSet.PPC_mr,          # Move Register

    InstructionSet.PPC_subi,        # Subtract Immediate
    InstructionSet.PPC_subic,       # Subtract Immediate Carrying
    InstructionSet.PPC_subis,       # Subtract Immediate Shifted
    InstructionSet.PPC_li,          # Load Immediate
    InstructionSet.PPC_lis,         # Load Immediate Shifted

    InstructionSet.PPC_mtxer,       # Move to integer unit exception register
    InstructionSet.PPC_mtlr,        # Move to link register
    InstructionSet.PPC_mtctr,       # Move to count register
    InstructionSet.PPC_mtdsisr,     # Move to DAE/source instruction service register
    InstructionSet.PPC_mtdar,       # Move to data address register
    InstructionSet.PPC_mtdec,       # Move to decrementer register
    InstructionSet.PPC_mtsrr0,      # Move to status save/restore register 0
    InstructionSet.PPC_mtsrr1,      # Move to status save/restore register 1
    InstructionSet.PPC_mtsprg0,     # Move to general special purpose register 0
    InstructionSet.PPC_mtsprg1,     # Move to general special purpose register 1
    InstructionSet.PPC_mtsprg2,     # Move to general special purpose register 2
    InstructionSet.PPC_mtsprg3,     # Move to general special purpose register 3
    InstructionSet.PPC_mttbl,       # Move to time base register (lower)
    InstructionSet.PPC_mttbu,       # Move to time base register (upper)
    InstructionSet.PPC_mfxer,       # Move from integer unit exception register
    InstructionSet.PPC_mflr,        # Move from link register
    InstructionSet.PPC_mfctr,       # Move from count register
    InstructionSet.PPC_mfdsisr,     # Move from DAE/source instruction service register
    InstructionSet.PPC_mfdar,       # Move from data address register
    InstructionSet.PPC_mfdec,       # Move from decrementer register
    InstructionSet.PPC_mfsrr0,      # Move from status save/restore register 0
    InstructionSet.PPC_mfsrr1,      # Move from status save/restore register 1
    InstructionSet.PPC_mfsprg0,     # Move from general special purpose register 0
    InstructionSet.PPC_mfsprg1,     # Move from general special purpose register 1
    InstructionSet.PPC_mfsprg2,     # Move from general special purpose register 2
    InstructionSet.PPC_mfsprg3,     # Move from general special purpose register 3
    #InstructionSet.PPC_mftbl,       # Move from time base register (lower)
    InstructionSet.PPC_mftbu,       # Move from time base register (upper)
    InstructionSet.PPC_mfpvr,       # Move from processor version register
]

UNCONDITIONAL_BRANCH_TYPES = [
    InstructionSet.PPC_b,           # Branch
    #InstructionSet.PPC_balways,     # Branch unconditionally
]

CONDITIONAL_BRANCH_TYPES = [
    InstructionSet.PPC_bc,          # Branch Conditional
    InstructionSet.PPC_bcctr,       # Branch Conditional to Count Register
    InstructionSet.PPC_bclr,        # Branch Conditional to Link Register

    # suffixes:
    #      lr      - goto lr
    #      ctr     - goto ctr
    #      l       - update lr
    #      a       - absolute

    InstructionSet.PPC_bt,          # Branch if true
    InstructionSet.PPC_bf,          # Branch if false
    InstructionSet.PPC_bdnz,        # CTR--; branch if CTR non-zero
    InstructionSet.PPC_bdnzt,       # CTR--; branch if CTR non-zero and condition is true
    InstructionSet.PPC_bdnzf,       # CTR--; branch if CTR non-zero and condition is false
    InstructionSet.PPC_bdz,         # CTR--; branch if CTR zero
    InstructionSet.PPC_bdzt,        # CTR--; branch if CTR zero and condition is true
    InstructionSet.PPC_bdzf,        # CTR--; branch if CTR zero and condition is false

    InstructionSet.PPC_blt,         # Branch if less than
    InstructionSet.PPC_ble,         # Branch if less than or equal
    InstructionSet.PPC_beq,         # Branch if equal
    InstructionSet.PPC_bge,         # Branch if greater than or equal
    InstructionSet.PPC_bgt,         # Branch if greater than
    InstructionSet.PPC_bne,         # Branch if not equal
    InstructionSet.PPC_bso,         # Branch if summary overflow
    InstructionSet.PPC_bns,         # Branch if not summary overflow

]

UNIMPLEMENTED_TYPES = [
    InstructionSet.PPC_cmp,         # Compare
    InstructionSet.PPC_cmpi,        # Compare Immediate
    InstructionSet.PPC_cmpl,        # Compare Logical
    InstructionSet.PPC_cmpli,       # Compare Logical Immediate
    InstructionSet.PPC_cntlzd,      # Count Leading Zeros Double Word
    InstructionSet.PPC_cntlzw,      # Count Leading Zeros Word
    InstructionSet.PPC_crand,       # Condition Register AND
    InstructionSet.PPC_crandc,      # Condition Register AND with Complement
    InstructionSet.PPC_creqv,       # Condition Register Equivalent
    InstructionSet.PPC_crnand,      # Condition Register NAND
    InstructionSet.PPC_crnor,       # Condition Register NOR
    InstructionSet.PPC_cror,        # Condiiton Register OR
    InstructionSet.PPC_crorc,       # Condition Register OR with Comlement
    InstructionSet.PPC_crxor,       # Condition Register XOR
    #InstructionSet.PPC_dcba,       #
    #InstructionSet.PPC_dcbf,       # Data Cache Block Flush
    #InstructionSet.PPC_dcbi,       # Data Cache Block Invalidate
    #InstructionSet.PPC_dcbst,      # Data Cache Block Store
    #InstructionSet.PPC_dcbt,       # Data Cache Block Touch
    #InstructionSet.PPC_dcbtst,     # Data Cache Block Touch for Store
    #InstructionSet.PPC_dcbz,       # Data Cache Block Set to Zero
    InstructionSet.PPC_eciwx,       # External Control In Word Indexed
    InstructionSet.PPC_ecowx,       # External Control Out Word Indexed
    InstructionSet.PPC_eieio,       # Enforce In-Order Execution of I/O
    InstructionSet.PPC_eqv,         # Equivalent
    InstructionSet.PPC_extsb,       # Extend Sign Byte
    InstructionSet.PPC_extsh,       # Extend Sign Half Word
    InstructionSet.PPC_extsw,       # Extend Sign Word
    #InstructionSet.PPC_fabs,       # Floating-Point Absolute Value
    #InstructionSet.PPC_fadd,       # Floating-Point Add
    #InstructionSet.PPC_fadds,      # Floating-Point Add (Single-Precision)
    #InstructionSet.PPC_fcfid,      # Floating-Point Convert from Integer Double Word
    #InstructionSet.PPC_fcmpo,      # Floating-Point Compare Ordered
    #InstructionSet.PPC_fcmpu,      # Floating-Point Compare Unordered
    #InstructionSet.PPC_fctid,      # Floating-Point Convert to Integer Double Word
    #InstructionSet.PPC_fctidz,     # Floating-Point Convert to Integer Double Word with Round toward Zero
    #InstructionSet.PPC_fctiw,      # Floating-Point Convert to Integer Word
    #InstructionSet.PPC_fctiwz,     # Floating-Point Convert to Integer Word with Round toward Zero
    #InstructionSet.PPC_fdiv,       # Floating-Point Divide
    #InstructionSet.PPC_fdivs,      # Floating-Point Divide Single-Precision
    #InstructionSet.PPC_fmadd,      # Floating-Point Multiply-Add
    #InstructionSet.PPC_fmadds,     # Floating-Point Multiply-Add Single-Precision
    #InstructionSet.PPC_fmr,        # Floating-Point Move Register
    #InstructionSet.PPC_fmsub,      # Floating-Point Multiply-Subtract
    #InstructionSet.PPC_fmsubs,     # Floating-Point Multiply-Subtract (Single-Precision)
    #InstructionSet.PPC_fmul,       # Floating-Point Multiply
    #InstructionSet.PPC_fmuls,      # Floating-Point Multiply Single-Precision
    #InstructionSet.PPC_fnabs,      # Floating-Point Negative Absolute Value
    #InstructionSet.PPC_fneg,       # Floating-Point Negate
    #InstructionSet.PPC_fnmadd,     # Floating-Point Negative Multiply-Add
    #InstructionSet.PPC_fnmadds,    # Floating-Point Negative Multiply-Add Single-Precision
    #InstructionSet.PPC_fnmsub,     # Floating-Point Negative Multiply-Subtract
    #InstructionSet.PPC_fnmsubs,    # Floating-Point Negative Multiply-Subtract Single-Precision
    #InstructionSet.PPC_fres,       # Floating-Point Reciprocal Estimate Single-Precision
    #InstructionSet.PPC_frsp,       # Floating-Point Round to Single-Precision
    #InstructionSet.PPC_frsqrte,    # Floating-Point Reciprocal Square Root Estimate
    #InstructionSet.PPC_fsel,       # Floating-Point Select
    #InstructionSet.PPC_fsqrt,      # Floating-Point Square Root
    #InstructionSet.PPC_fsqrts,     # Floating-Point Square Root Single-Precision
    #InstructionSet.PPC_fsub,       # Floating-Point Subtract
    #InstructionSet.PPC_fsubs,      # Floating-Point Subtract Single-Precision
    #InstructionSet.PPC_icbi,       # Instruction Cache Block Invalidate
    #InstructionSet.PPC_isync,      # Instruction Synchronize
    #InstructionSet.PPC_lfd,        # Load Floating-Point Double-Precision
    #InstructionSet.PPC_lfdu,       # Load Floating-Point Double-Precision with Update
    #InstructionSet.PPC_lfdux,      # Load Floating-Point Double-Precision with Update Indexed
    #InstructionSet.PPC_lfdx,       # Load Floating-Point Double-Precision Indexed
    #InstructionSet.PPC_lfs,        # Load Floating-Point Single-Precision
    #InstructionSet.PPC_lfsu,       # Load Floating-Point Single-Precision with Update
    #InstructionSet.PPC_lfsux,      # Load Floating-Point Single-Precision with Update Indexed
    #InstructionSet.PPC_lfsx,       # Load Floating-Point Single-Precision Indexed
    #InstructionSet.PPC_rfi,        # Return from Interrupt
    #InstructionSet.PPC_rfid,       # Return from Interrupt Double Word
    #InstructionSet.PPC_sc,         # System Call
    #InstructionSet.PPC_slbia,      # SLB Invalidate All
    #InstructionSet.PPC_slbie,      # SLB Invalidate Entry
    #InstructionSet.PPC_stfd,       # Store Floating-Point Double-Precision
    #InstructionSet.PPC_stfdu,      # Store Floating-Point Double-Precision wiht Update
    #InstructionSet.PPC_stfdux,     # Store Floating-Point Double-Precision wiht Update Indexed
    #InstructionSet.PPC_stfdx,      # Store Floating-Point Double-Precision Indexed
    #InstructionSet.PPC_stfiwx,     # Store Floating-Point as Integer Word Indexed
    #InstructionSet.PPC_stfs,       # Store Floating-Point Single-Precision
    #InstructionSet.PPC_stfsu,      # Store Floating-Point Single-Precision with Update
    #InstructionSet.PPC_stfsux,     # Store Floating-Point Single-Precision with Update Indexed
    #InstructionSet.PPC_stfsx,      # Store Floating-Point Single-Precision Indexed
    #InstructionSet.PPC_sync,       # Synchronize
    #InstructionSet.PPC_td,         # Trap Double Word
    #InstructionSet.PPC_tdi,        # Trap Double Word Immediate
    #InstructionSet.PPC_tlbia,      # TLB Invalidate All
    #InstructionSet.PPC_tlbie,      # TLB Invalidate Entry
    #InstructionSet.PPC_tlbsync,    # TLB Synchronize
    #InstructionSet.PPC_tw,         # Trap Word
    #InstructionSet.PPC_twi,        # Trap Word Immediate

    #-------------

    InstructionSet.PPC_cmpwi,       # Compare Word Immediate
    InstructionSet.PPC_cmpw,        # Compare Word
    InstructionSet.PPC_cmplwi,      # Compare Logical Word Immediate
    InstructionSet.PPC_cmplw,       # Compare Logical Word
    InstructionSet.PPC_cmpdi,       # Compare Double Word Immediate
    InstructionSet.PPC_cmpd,        # Compare Double Word
    InstructionSet.PPC_cmpldi,      # Compare Logical Double Word Immediate
    InstructionSet.PPC_cmpld,       # Compare Logical Double Word

    #InstructionSet.PPC_trap,       # Trap Word Unconditionally
    #InstructionSet.PPC_trapd,      # Trap Double Word Unconditionally
    #InstructionSet.PPC_twlgt,      # Trap Word if Logically Greater Than
    #InstructionSet.PPC_twllt,      # Trap Word if Logically Less Than
    #InstructionSet.PPC_tweq,       # Trap Word if Equal
    #InstructionSet.PPC_twlge,      # Trap Word if Logically Greater Than or Equal
    #InstructionSet.PPC_twlle,      # Trap Word if Logically Less Than or Equal
    #InstructionSet.PPC_twgt,       # Trap Word if Greater Than
    #InstructionSet.PPC_twge,       # Trap Word if Greater Than or Equal
    #InstructionSet.PPC_twlt,       # Trap Word if Less Than
    #InstructionSet.PPC_twle,       # Trap Word if Less Than oe Equal
    #InstructionSet.PPC_twne,       # Trap Word if Not Equal
    #InstructionSet.PPC_twlgti,     # Trap Word Immediate if Logically Greater Than
    #InstructionSet.PPC_twllti,     # Trap Word Immediate if Logically Less Than
    #InstructionSet.PPC_tweqi,      # Trap Word Immediate if Equal
    #InstructionSet.PPC_twlgei,     # Trap Word Immediate if Logically Greater Than or Equal
    #InstructionSet.PPC_twllei,     # Trap Word Immediate if Logically Less Than or Equal
    #InstructionSet.PPC_twgti,      # Trap Word Immediate if Greater Than
    #InstructionSet.PPC_twgei,      # Trap Word Immediate if Greater Than or Equal
    #InstructionSet.PPC_twlti,      # Trap Word Immediate if Less Than
    #InstructionSet.PPC_twlei,      # Trap Word Immediate if Less Than oe Equal
    #InstructionSet.PPC_twnei,      # Trap Word Immediate if Not Equal
    #InstructionSet.PPC_tdlgt,      # Trap Double Word if Logically Greater Than
    #InstructionSet.PPC_tdllt,      # Trap Double Word if Logically Less Than
    #InstructionSet.PPC_tdeq,       # Trap Double Word if Equal
    #InstructionSet.PPC_tdlge,      # Trap Double Word if Logically Greater Than or Equal
    #InstructionSet.PPC_tdlle,      # Trap Double Word if Logically Less Than or Equal
    #InstructionSet.PPC_tdgt,       # Trap Double Word if Greater Than
    #InstructionSet.PPC_tdge,       # Trap Double Word if Greater Than or Equal
    #InstructionSet.PPC_tdlt,       # Trap Double Word if Less Than
    #InstructionSet.PPC_tdle,       # Trap Double Word if Less Than oe Equal
    #InstructionSet.PPC_tdne,       # Trap Double Word if Not Equal
    #InstructionSet.PPC_tdlgti,     # Trap Double Word Immediate if Logically Greater Than
    #InstructionSet.PPC_tdllti,     # Trap Double Word Immediate if Logically Less Than
    #InstructionSet.PPC_tdeqi,      # Trap Double Word Immediate if Equal
    #InstructionSet.PPC_tdlgei,     # Trap Double Word Immediate if Logically Greater Than or Equal
    #InstructionSet.PPC_tdllei,     # Trap Double Word Immediate if Logically Less Than or Equal
    #InstructionSet.PPC_tdgti,      # Trap Double Word Immediate if Greater Than
    #InstructionSet.PPC_tdgei,      # Trap Double Word Immediate if Greater Than or Equal
    #InstructionSet.PPC_tdlti,      # Trap Double Word Immediate if Less Than
    #InstructionSet.PPC_tdlei,      # Trap Double Word Immediate if Less Than oe Equal
    #InstructionSet.PPC_tdnei,      # Trap Double Word Immediate if Not Equal

    InstructionSet.PPC_crset,       # Condition Register Set
    InstructionSet.PPC_crnot,       # Condition Register NOT
    InstructionSet.PPC_crmove,      # Condition Register Move
    InstructionSet.PPC_crclr,       # Condition Register Clear

    InstructionSet.PPC_extlwi,      # Extract and Left Justify Immediate
    InstructionSet.PPC_extrwi,      # Extract and Right Justify Immediate
    InstructionSet.PPC_inslwi,      # Insert from Left Immediate
    InstructionSet.PPC_insrwi,      # Insert from Right Immediate
    InstructionSet.PPC_rotlwi,      # Rotate Left Immediate
    InstructionSet.PPC_rotrwi,      # Rotate Right Immediate
    InstructionSet.PPC_rotlw,       # Rotate Left
    InstructionSet.PPC_slwi,        # Shift Left Immediate
    InstructionSet.PPC_srwi,        # Shift Right Immediate
    InstructionSet.PPC_clrlwi,      # Clear Left Immediate
    InstructionSet.PPC_clrrwi,      # Clear Right Immediate
    InstructionSet.PPC_clrlslwi,    # Clear Left and Shift Left Immediate

    #
    #  PowerPC Embedded Controller Instructions
    #

    #InstructionSet.PPC_dccci,      # Data cache congruence class invalidate (p.438-439)
    #InstructionSet.PPC_dcread,     # Data cache read (p.440-441)
    #InstructionSet.PPC_icbt,       # Instruction cache block touch (p.450-451)
    #InstructionSet.PPC_iccci,      # Instruction cache congruence class invalidate (p.452-453)
    #InstructionSet.PPC_icread,     # Instruction cache read (p.454-455)
    #InstructionSet.PPC_mfdcr,      # Move from device control register (p.484-485)
    #InstructionSet.PPC_mtdcr,      # Move to device control register (p.491-492)
    #InstructionSet.PPC_rfci,       # Return from critical interrupt (p.507)
    #InstructionSet.PPC_tlbre,      # TLB read entry (p.548-549)
    #InstructionSet.PPC_tlbsx,      # TLB search indexed (p.550)
    #InstructionSet.PPC_tlbwe,      # TLB write entry (p.552-553)
    #InstructionSet.PPC_wrtee,      # Write external enable (p.560)
    #InstructionSet.PPC_wrteei,     # Write external enable immediate (p.561)

    #
    #  New PowerPC instructions
    #

    #InstructionSet.PPC_abs,        # Absolute
    #InstructionSet.PPC_clcs,       # Cache Lines Compute Size
    #InstructionSet.PPC_clf,        # Cache Line Flush
    #InstructionSet.PPC_cli,        # Cache Line Invalidate
    #InstructionSet.PPC_dclst,      # Data Cache Line Store
    #InstructionSet.PPC_div,        # Divide
    #InstructionSet.PPC_divs,       # Divide Short
    #InstructionSet.PPC_doz,        # Different Or Zero
    #InstructionSet.PPC_dozi,       # Different Or Zero Immediate
    #InstructionSet.PPC_frsqrtes,   # Floating Reciprocal Square Root Estimate Single
    #InstructionSet.PPC_hrfid,      # Hypervisor Return from Interrupt Doubleword
    #InstructionSet.PPC_lscbx,      # Load String And Compare Byte Indexed
    #InstructionSet.PPC_maskg,      # Mask Generate
    #InstructionSet.PPC_maskir,     # Mask Insert From Register
    #InstructionSet.PPC_mfsri,      # Move From Segment Register Indirect
    #InstructionSet.PPC_mul,        # Multiply
    #InstructionSet.PPC_nabs,       # Negative Absolute
    #InstructionSet.PPC_popcntb,    # Population Count Bytes
    #InstructionSet.PPC_rac,        # Real Address Compute
    #InstructionSet.PPC_rfsvc,      # Return From SVC
    #InstructionSet.PPC_rlmi,       # Rotate Left Then Mask Insert
    #InstructionSet.PPC_rrib,       # Rotate Right And Insert Bit
    #InstructionSet.PPC_slbmfee,    # SLB Move From Entry ESID
    #InstructionSet.PPC_slbmfev,    # SLB Move From Entry VSID
    #InstructionSet.PPC_slbmte,     # SLB Move To Entry
    #InstructionSet.PPC_sle,        # Shift Left Extended
    #InstructionSet.PPC_sleq,       # Shift Left Extended With MQ
    #InstructionSet.PPC_sliq,       # Shift Left Immediate With MQ
    #InstructionSet.PPC_slliq,      # Shift Left Long Immediate With MQ
    #InstructionSet.PPC_sllq,       # Shift Left Long With MQ
    #InstructionSet.PPC_slq,        # Shift Left With MQ
    #InstructionSet.PPC_sraiq,      # Shift Right Algebraic Immediate With MQ
    #InstructionSet.PPC_sraq,       # Shift Right Algebraic With MQ
    #InstructionSet.PPC_sre,        # Shift Right Extended
    #InstructionSet.PPC_srea,       # Shift Right Extended Algebraic
    #InstructionSet.PPC_sreq,       # Shift Right Extended With MQ
    #InstructionSet.PPC_sriq,       # Shift Right Immediate With MQ
    #InstructionSet.PPC_srliq,      # Shift Right Long Immediate With MQ
    #InstructionSet.PPC_srlq,       # Shift Right Long With MQ
    #InstructionSet.PPC_srq,        # Shift Right With MQ

    #
    #   New PowerPC instructions
    #

    #InstructionSet.PPC_mtocrf,     # Move To One Condition Register Field
    #InstructionSet.PPC_mfocrf,     # Move From One Condition Register Field
]

"""
Register    Status      Use
-----------------------------------------------------------------------------

General- Purpose
    GPR0        Volatile        Used in function prologs.
    GPR1        Dedicated       Stack Pointer.
    GPR2        Dedicated       Table of Contents (TOC) Pointer.
    GPR3        Volatile        First argument word; first word of function return value.
    GPR4        Volatile        Second argument word; second word function return value.
    GPR5        Volatile        Third argument word.
    GPR6        Volatile        Fourth argument word.
    GPR7        Volatile        Fifth argument word.
    GPR8        Volatile        Sixth argument word.
    GPR9        Volatile        Seventh argument word.
    GPR10       Volatile        Eighth argument word.
    GPR11       Volatile        Used in calls by pointer and as an environment pointer.
    GPR12       Volatile        Used for special exception handling and in glink code.
    GPR13:31    Non-volatile    Values are preserved across procedure calls.

Floating-Point
    FPR0        Volatile        Scratch register.
    FPR1        Volatile        First floating-point parameter; first floating-point scalar return value.
    FPR2        Volatile        Second floating-point parameter; second floating-point scalar return value.
    FPR3        Volatile        Third floating-point parameter; third floating-point scalar return value.
    FPR4        Volatile        Fourth floating-point parameter; fourth floating-point scalar return value.
    FPR5        Volatile        Fifth floating-point parameter.
    FPR6        Volatile        Sixth floating-point parameter.
    FPR7        Volatile        Seventh floating-point parameter.
    FPR8        Volatile        Eighth floating-point parameter.
    FPR9        Volatile        Ninth floating-point parameter.
    FPR10       Volatile        Tenth floating-point parameter.
    FPR11       Volatile        Eleventh floating-point parameter.
    FPR12       Volatile        Twelfth floating-point parameter.
    FPR13       Volatile        Thirteenth floating-point parameter.
    FPR14:31    Non-volatile    Values are preserved across procedure calls.

Special-Purpose
    LR          Volatile        Branch target address; procedure return address.
    CTR         Volatile        Branch target address; loop count value.
    XER         Volatile        Fixed point exception register.
    FPSCR       Volatile        Floating-point status and control register.

Condition
Register
    CR0, CR1    Volatile        Condition codes.
    CR2, CR3, CR4  Non-volatile Condition codes.
    CR5, CR6, CR7  Volatile     Condition codes. 
"""
