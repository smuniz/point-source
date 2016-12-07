#
# Copyright (c) 2014 Sebastian Muniz
# 
# This code is part of point source decompiler
#

import idaapi


class InstructionSet(object):
    PPC_add = idaapi.PPC_add        # Add
    PPC_addc = idaapi.PPC_addc          # Add Carrying
    PPC_adde = idaapi.PPC_adde          # Add Extended
    PPC_addi = idaapi.PPC_addi          # Add Immediate
    PPC_addic = idaapi.PPC_addic        # Add Immediate Carrying
    PPC_addis = idaapi.PPC_addis        # Add Immediate Shifted
    PPC_addme = idaapi.PPC_addme        # Add to Minus One Extended
    PPC_addze = idaapi.PPC_addze        # Add to Zero Extended
    PPC_and = idaapi.PPC_and        # AND
    PPC_andc = idaapi.PPC_andc          # AND with Complement
    PPC_andi = idaapi.PPC_andi          # AND Immediate
    PPC_andis = idaapi.PPC_andis        # AND Immediate Shifted

    PPC_cmpwi = idaapi.PPC_cmpwi        # Compare Word Immediate
    PPC_cmpw = idaapi.PPC_cmpw      # Compare Word
    PPC_cmplwi = idaapi.PPC_cmplwi      # Compare Logical Word Immediate
    PPC_cmplw = idaapi.PPC_cmplw        # Compare Logical Word
    PPC_cmpdi = idaapi.PPC_cmpdi        # Compare Double Word Immediate
    PPC_cmpd = idaapi.PPC_cmpd      # Compare Double Word
    PPC_cmpldi = idaapi.PPC_cmpldi      # Compare Logical Double Word Immediate
    PPC_cmpld = idaapi.PPC_cmpld        # Compare Logical Double Word

    PPC_cmp = idaapi.PPC_cmp        # Compare
    PPC_cmpi = idaapi.PPC_cmpi      # Compare Immediate
    PPC_cmpl = idaapi.PPC_cmpl      # Compare Logical
    PPC_cmpli = idaapi.PPC_cmpli        # Compare Logical Immediate

    PPC_divd = idaapi.PPC_divd          # Divide Double Word
    PPC_divdu = idaapi.PPC_divdu        # Divide Double Word Unsigned
    PPC_divw = idaapi.PPC_divw          # Divide Word
    PPC_divwu = idaapi.PPC_divwu        # Divide Word Unsigned
    PPC_lbz = idaapi.PPC_lbz        # Load Byte and Zero
    PPC_lbzu = idaapi.PPC_lbzu          # Load Byte and Zero with Update
    PPC_lbzux = idaapi.PPC_lbzux        # Load Byte and Zero with Update Indexed
    PPC_lbzx = idaapi.PPC_lbzx          # Load Byte and Zero Indexed
    PPC_ld = idaapi.PPC_ld          # Load Double Word
    PPC_ldarx = idaapi.PPC_ldarx        # Load Double Word and Reserve Indexed
    PPC_ldu = idaapi.PPC_ldu        # Load Double Word with Update
    PPC_ldux = idaapi.PPC_ldux      # Load Double Word with Update Indexed
    PPC_ldx = idaapi.PPC_ldx        # Load Double Word Indexed
    PPC_lha = idaapi.PPC_lha        # Load Half Word Algebraic
    PPC_lhau = idaapi.PPC_lhau      # Load Half Word Algebraic with Update
    PPC_lhaux = idaapi.PPC_lhaux        # Load Half Word Algebraic with Update Indexed
    PPC_lhax = idaapi.PPC_lhax      # Load Half Word Algebraic Indexed
    PPC_lhbrx = idaapi.PPC_lhbrx        # Load Half Word Byte-reverse Indexed
    PPC_lhz = idaapi.PPC_lhz        # Load Half Word and Zero
    PPC_lhzu = idaapi.PPC_lhzu      # Load Half Word and Zero with Update
    PPC_lhzux = idaapi.PPC_lhzux        # Load Half Word and Zero with Update Indexed
    PPC_lhzx = idaapi.PPC_lhzx      # Load Half Word and Zero Indexed
    PPC_lmw = idaapi.PPC_lmw        # Load Multiple Word
    PPC_lswi = idaapi.PPC_lswi      # Load String Word Immediate
    PPC_lswx = idaapi.PPC_lswx      # Load String Word Indexed
    PPC_lwa = idaapi.PPC_lwa        # Load Word Algebraic
    PPC_lwarx = idaapi.PPC_lwarx        # Load Word and Reserve Indexed
    PPC_lwaux = idaapi.PPC_lwaux        # Load Word Algebraic with Update Indexed
    PPC_lwax = idaapi.PPC_lwax      # Load Word Algebraic Indexed
    PPC_lwbrx = idaapi.PPC_lwbrx        # Load Word Byte-Reverse Indexed
    PPC_lwz = idaapi.PPC_lwz        # Load Word and Zero
    PPC_lwzu = idaapi.PPC_lwzu      # Load Word and Zero with Update
    PPC_lwzux = idaapi.PPC_lwzux        # Load Word and Zero with Update Indexed
    PPC_lwzx = idaapi.PPC_lwzx      # Load Word and Zero Indexed
    PPC_mcrf = idaapi.PPC_mcrf      # Move Condition register Field
    PPC_mcrfs = idaapi.PPC_mcrfs        # Move to Condition Register from FPSCR
    PPC_mcrxr = idaapi.PPC_mcrxr        # Move to Condition Register from XER
    PPC_mfcr = idaapi.PPC_mfcr      # Move from Condition Register
    PPC_mffs = idaapi.PPC_mffs      # Move from FPSCR
    PPC_mfmsr = idaapi.PPC_mfmsr        # Move from Machine State Register
    PPC_mfspr = idaapi.PPC_mfspr        # Move from Special Purpose Register
    PPC_mfsr = idaapi.PPC_mfsr      # Move from Segment Register
    PPC_mfsrin = idaapi.PPC_mfsrin      # Move from Segment Register Indexed
    PPC_mftb = idaapi.PPC_mftb      # Move from Time Base
    PPC_mtcrf = idaapi.PPC_mtcrf        # Move to Condition Register Fields
    PPC_mtfsb0 = idaapi.PPC_mtfsb0      # Move to FPSCR Bit 0
    PPC_mtfsb1 = idaapi.PPC_mtfsb1      # Move to FPSCR Bit 1
    PPC_mtfsf = idaapi.PPC_mtfsf        # Move to FPSCR Fields
    PPC_mtfsfi = idaapi.PPC_mtfsfi      # Move to FPSCR Field Immediate
    PPC_mtmsr = idaapi.PPC_mtmsr        # Move to Machine State Register
    PPC_mtmsrd = idaapi.PPC_mtmsrd      # Move to Machine State Register Double Word
    PPC_mtspr = idaapi.PPC_mtspr        # Move to Special Purpose Register
    PPC_mtsr = idaapi.PPC_mtsr      # Move to Segment Register
    PPC_mtsrd = idaapi.PPC_mtsrd        # Move to Segment Register Double Word
    PPC_mtsrdin = idaapi.PPC_mtsrdin        # Move to Segment Register Indirect Double
    PPC_mtsrin = idaapi.PPC_mtsrin      # Move to Segment Register Indirect
    PPC_mulhd = idaapi.PPC_mulhd        # Multiply High Double Word
    PPC_mulhdu = idaapi.PPC_mulhdu      # Multiply High Double Word Unsigned
    PPC_mulhw = idaapi.PPC_mulhw        # Multiply High Word
    PPC_mulhwu = idaapi.PPC_mulhwu      # Multiply High Word Unsigned
    PPC_mulld = idaapi.PPC_mulld        # Multiply Low Double Word
    PPC_mulli = idaapi.PPC_mulli        # Multiply Low Immediate
    PPC_mullw = idaapi.PPC_mullw        # Multiply Low
    PPC_nand = idaapi.PPC_nand      # NAND (not AND)
    PPC_neg = idaapi.PPC_neg        # Negate
    PPC_nor = idaapi.PPC_nor        # NOR (not OR)
    PPC_or = idaapi.PPC_or      # OR
    PPC_orc = idaapi.PPC_orc        # OR with Complement
    PPC_ori = idaapi.PPC_ori        # OR Immediate
    PPC_oris = idaapi.PPC_oris      # OR Immediate Shifted
    PPC_rldcl = idaapi.PPC_rldcl        # Rotate Left Double Word then Clear Left
    PPC_rldcr = idaapi.PPC_rldcr        # Rotate Left Double Word then Clear Right
    PPC_rldic = idaapi.PPC_rldic        # Rotate Left Double Word Immediate then Clear
    PPC_rldicl = idaapi.PPC_rldicl      # Rotate Left Double Word Immediate then Clear Left
    PPC_rldicr = idaapi.PPC_rldicr      # Rotate Left Double Word Immediate then Clear Right
    PPC_rldimi = idaapi.PPC_rldimi      # Rotate Left Double Word Immediate then Mask Insert
    PPC_rlwimi = idaapi.PPC_rlwimi      # Rotate Left Word Immediate then Mask Insert
    PPC_rlwinm = idaapi.PPC_rlwinm      # Rotate Left Word Immediate then AND with Mask
    PPC_rlwnm = idaapi.PPC_rlwnm        # Rotate Left Word then AND with Mask
    PPC_sld = idaapi.PPC_sld        # Shift Left Double Word
    PPC_slw = idaapi.PPC_slw        # Shift Left Word
    PPC_srad = idaapi.PPC_srad      # Shift Right Algebraic Double Word
    PPC_sradi = idaapi.PPC_sradi        # Shift Right Algebraic Double Word Immediate
    PPC_sraw = idaapi.PPC_sraw      # Shift Right Algebraic Word
    PPC_srawi = idaapi.PPC_srawi        # Shift Right Algebraic Word Immediate
    PPC_srd = idaapi.PPC_srd        # Shift Right Double Word
    PPC_srw = idaapi.PPC_srw        # Shift Right Word
    PPC_stb = idaapi.PPC_stb        # Store Byte
    PPC_stbu = idaapi.PPC_stbu      # Store Byte with Update
    PPC_stbux = idaapi.PPC_stbux        # Store Byte with Update Indexed
    PPC_stbx = idaapi.PPC_stbx      # Store Byte Indexed
    PPC_std = idaapi.PPC_std        # Store Double Word
    PPC_stdcx = idaapi.PPC_stdcx        # Store Double Word Conditional Indexed
    PPC_stdu = idaapi.PPC_stdu      # Store Double Word with Update
    PPC_stdux = idaapi.PPC_stdux        # Store Double Word with Update Indexed
    PPC_stdx = idaapi.PPC_stdx      # Store Double Word Indexed
    PPC_sth = idaapi.PPC_sth        # Store Half Word
    PPC_sthbrx = idaapi.PPC_sthbrx      # Store Half Word Byte-Reverse Indexed
    PPC_sthu = idaapi.PPC_sthu      # Store Half Word with Update
    PPC_sthux = idaapi.PPC_sthux        # Store Half Word with Update Indexed
    PPC_sthx = idaapi.PPC_sthx      # Store Half Word Indexed
    PPC_stmw = idaapi.PPC_stmw      # Store Multiple Word
    PPC_stswi = idaapi.PPC_stswi        # Store String Word Immediate
    PPC_stswx = idaapi.PPC_stswx        # Store String Word Indexed
    PPC_stw = idaapi.PPC_stw        # Store Word
    PPC_stwbrx = idaapi.PPC_stwbrx      # Store Word Byte-Reverse Indexed
    PPC_stwcx = idaapi.PPC_stwcx        # Store Word Conditional Indexed
    PPC_stwu = idaapi.PPC_stwu      # Store Word with Update
    PPC_stwux = idaapi.PPC_stwux        # Store Word with Update Indexed
    PPC_stwx = idaapi.PPC_stwx      # Store Word Indexed
    PPC_subf = idaapi.PPC_subf      # Subtract from
    PPC_subfc = idaapi.PPC_subfc        # Subtract from Carrying
    PPC_subfe = idaapi.PPC_subfe        # Subtract from Extended
    PPC_subfic = idaapi.PPC_subfic      # Subtract from Immediate Carrying
    PPC_subfme = idaapi.PPC_subfme      # Subtract from Minus One Extended
    PPC_subfze = idaapi.PPC_subfze      # Subtract from Zero Extended
    PPC_xor = idaapi.PPC_xor        # XOR
    PPC_xori = idaapi.PPC_xori      # XOR Immediate
    PPC_xoris = idaapi.PPC_xoris        # XOR Immediate Shifted

    PPC_nop = idaapi.PPC_nop        # No Operation
    PPC_not = idaapi.PPC_not        # Complement Register
    PPC_mr = idaapi.PPC_mr      # Move Register

    PPC_subi = idaapi.PPC_subi      # Subtract Immediate
    PPC_subic = idaapi.PPC_subic        # Subtract Immediate Carrying
    PPC_subis = idaapi.PPC_subis        # Subtract Immediate Shifted
    PPC_li = idaapi.PPC_li      # Load Immediate
    PPC_lis = idaapi.PPC_lis        # Load Immediate Shifted

    PPC_mtxer = idaapi.PPC_mtxer        # Move to integer unit exception register
    PPC_mtlr = idaapi.PPC_mtlr      # Move to link register
    PPC_mtctr = idaapi.PPC_mtctr        # Move to count register
    PPC_mtdsisr = idaapi.PPC_mtdsisr        # Move to DAE/source instruction service register
    PPC_mtdar = idaapi.PPC_mtdar        # Move to data address register
    PPC_mtdec = idaapi.PPC_mtdec        # Move to decrementer register
    PPC_mtsrr0 = idaapi.PPC_mtsrr0      # Move to status save/restore register 0
    PPC_mtsrr1 = idaapi.PPC_mtsrr1      # Move to status save/restore register 1
    PPC_mtsprg0 = idaapi.PPC_mtsprg0        # Move to general special purpose register 0
    PPC_mtsprg1 = idaapi.PPC_mtsprg1        # Move to general special purpose register 1
    PPC_mtsprg2 = idaapi.PPC_mtsprg2        # Move to general special purpose register 2
    PPC_mtsprg3 = idaapi.PPC_mtsprg3        # Move to general special purpose register 3
    PPC_mttbl = idaapi.PPC_mttbl        # Move to time base register (lower)
    PPC_mttbu = idaapi.PPC_mttbu        # Move to time base register (upper)
    PPC_mfxer = idaapi.PPC_mfxer        # Move from integer unit exception register
    PPC_mflr = idaapi.PPC_mflr      # Move from link register
    PPC_mfctr = idaapi.PPC_mfctr        # Move from count register
    PPC_mfdsisr = idaapi.PPC_mfdsisr        # Move from DAE/source instruction service register
    PPC_mfdar = idaapi.PPC_mfdar        # Move from data address register
    PPC_mfdec = idaapi.PPC_mfdec        # Move from decrementer register
    PPC_mfsrr0 = idaapi.PPC_mfsrr0      # Move from status save/restore register 0
    PPC_mfsrr1 = idaapi.PPC_mfsrr1      # Move from status save/restore register 1
    PPC_mfsprg0 = idaapi.PPC_mfsprg0        # Move from general special purpose register 0
    PPC_mfsprg1 = idaapi.PPC_mfsprg1        # Move from general special purpose register 1
    PPC_mfsprg2 = idaapi.PPC_mfsprg2        # Move from general special purpose register 2
    PPC_mfsprg3 = idaapi.PPC_mfsprg3        # Move from general special purpose register 3
    PPC_mftbl = idaapi.PPC_mftbl        # Move from time base register (lower)
    PPC_mftbu = idaapi.PPC_mftbu        # Move from time base register (upper)
    PPC_mfpvr = idaapi.PPC_mfpvr        # Move from processor version register

    # UNCONDITIONAL_BRANCH_TYPES
    PPC_b = idaapi.PPC_b        # Branch
    PPC_balways = idaapi.PPC_balways        # Branch unconditionally

    # CONDITIONAL_BRANCH_TYPES
    PPC_bc = idaapi.PPC_bc      # Branch Conditional
    PPC_bcctr = idaapi.PPC_bcctr        # Branch Conditional to Count Register
    PPC_bclr = idaapi.PPC_bclr      # Branch Conditional to Link Register

    # suffixes:
    #      lr      - goto lr
    #      ctr     - goto ctr
    #      l       - update lr
    #      a       - absolute

    PPC_bt = idaapi.PPC_bt      # Branch if true
    PPC_bf = idaapi.PPC_bf      # Branch if false
    PPC_bdnz = idaapi.PPC_bdnz      # CTR--; branch if CTR non-zero
    PPC_bdnzt = idaapi.PPC_bdnzt        # CTR--; branch if CTR non-zero and condition is true
    PPC_bdnzf = idaapi.PPC_bdnzf        # CTR--; branch if CTR non-zero and condition is false
    PPC_bdz = idaapi.PPC_bdz        # CTR--; branch if CTR zero
    PPC_bdzt = idaapi.PPC_bdzt      # CTR--; branch if CTR zero and condition is true
    PPC_bdzf = idaapi.PPC_bdzf      # CTR--; branch if CTR zero and condition is false

    PPC_blt = idaapi.PPC_blt        # Branch if less than
    PPC_ble = idaapi.PPC_ble        # Branch if less than or equal
    PPC_beq = idaapi.PPC_beq        # Branch if equal
    PPC_bge = idaapi.PPC_bge        # Branch if greater than or equal
    PPC_bgt = idaapi.PPC_bgt        # Branch if greater than
    PPC_bne = idaapi.PPC_bne        # Branch if not equal
    PPC_bso = idaapi.PPC_bso        # Branch if summary overflow
    PPC_bns = idaapi.PPC_bns        # Branch if not summary overflow

    # UNIMPLEMENTED_TYPES

    PPC_cntlzd = idaapi.PPC_cntlzd      # Count Leading Zeros Double Word
    PPC_cntlzw = idaapi.PPC_cntlzw      # Count Leading Zeros Word
    PPC_crand = idaapi.PPC_crand        # Condition Register AND
    PPC_crandc = idaapi.PPC_crandc      # Condition Register AND with Complement
    PPC_creqv = idaapi.PPC_creqv        # Condition Register Equivalent
    PPC_crnand = idaapi.PPC_crnand      # Condition Register NAND
    PPC_crnor = idaapi.PPC_crnor        # Condition Register NOR
    PPC_cror = idaapi.PPC_cror      # Condiiton Register OR
    PPC_crorc = idaapi.PPC_crorc        # Condition Register OR with Comlement
    PPC_crxor = idaapi.PPC_crxor        # Condition Register XOR
    #PPC_dcba = idaapi.PPC_dcba         #
    #PPC_dcbf = idaapi.PPC_dcbf         # Data Cache Block Flush
    #PPC_dcbi = idaapi.PPC_dcbi         # Data Cache Block Invalidate
    #PPC_dcbst = idaapi.PPC_dcbst       # Data Cache Block Store
    #PPC_dcbt = idaapi.PPC_dcbt         # Data Cache Block Touch
    #PPC_dcbtst = idaapi.PPC_dcbtst         # Data Cache Block Touch for Store
    #PPC_dcbz = idaapi.PPC_dcbz         # Data Cache Block Set to Zero
    PPC_eciwx = idaapi.PPC_eciwx        # External Control In Word Indexed
    PPC_ecowx = idaapi.PPC_ecowx        # External Control Out Word Indexed
    PPC_eieio = idaapi.PPC_eieio        # Enforce In-Order Execution of I/O
    PPC_eqv = idaapi.PPC_eqv        # Equivalent
    PPC_extsb = idaapi.PPC_extsb        # Extend Sign Byte
    PPC_extsh = idaapi.PPC_extsh        # Extend Sign Half Word
    PPC_extsw = idaapi.PPC_extsw        # Extend Sign Word
    #PPC_fabs = idaapi.PPC_fabs         # Floating-Point Absolute Value
    #PPC_fadd = idaapi.PPC_fadd         # Floating-Point Add
    #PPC_fadds = idaapi.PPC_fadds       # Floating-Point Add (Single-Precision)
    #PPC_fcfid = idaapi.PPC_fcfid       # Floating-Point Convert from Integer Double Word
    #PPC_fcmpo = idaapi.PPC_fcmpo       # Floating-Point Compare Ordered
    #PPC_fcmpu = idaapi.PPC_fcmpu       # Floating-Point Compare Unordered
    #PPC_fctid = idaapi.PPC_fctid       # Floating-Point Convert to Integer Double Word
    #PPC_fctidz = idaapi.PPC_fctidz         # Floating-Point Convert to Integer Double Word with Round toward Zero
    #PPC_fctiw = idaapi.PPC_fctiw       # Floating-Point Convert to Integer Word
    #PPC_fctiwz = idaapi.PPC_fctiwz         # Floating-Point Convert to Integer Word with Round toward Zero
    #PPC_fdiv = idaapi.PPC_fdiv         # Floating-Point Divide
    #PPC_fdivs = idaapi.PPC_fdivs       # Floating-Point Divide Single-Precision
    #PPC_fmadd = idaapi.PPC_fmadd       # Floating-Point Multiply-Add
    #PPC_fmadds = idaapi.PPC_fmadds         # Floating-Point Multiply-Add Single-Precision
    #PPC_fmr = idaapi.PPC_fmr       # Floating-Point Move Register
    #PPC_fmsub = idaapi.PPC_fmsub       # Floating-Point Multiply-Subtract
    #PPC_fmsubs = idaapi.PPC_fmsubs         # Floating-Point Multiply-Subtract (Single-Precision)
    #PPC_fmul = idaapi.PPC_fmul         # Floating-Point Multiply
    #PPC_fmuls = idaapi.PPC_fmuls       # Floating-Point Multiply Single-Precision
    #PPC_fnabs = idaapi.PPC_fnabs       # Floating-Point Negative Absolute Value
    #PPC_fneg = idaapi.PPC_fneg         # Floating-Point Negate
    #PPC_fnmadd = idaapi.PPC_fnmadd         # Floating-Point Negative Multiply-Add
    #PPC_fnmadds = idaapi.PPC_fnmadds       # Floating-Point Negative Multiply-Add Single-Precision
    #PPC_fnmsub = idaapi.PPC_fnmsub         # Floating-Point Negative Multiply-Subtract
    #PPC_fnmsubs = idaapi.PPC_fnmsubs       # Floating-Point Negative Multiply-Subtract Single-Precision
    #PPC_fres = idaapi.PPC_fres         # Floating-Point Reciprocal Estimate Single-Precision
    #PPC_frsp = idaapi.PPC_frsp         # Floating-Point Round to Single-Precision
    #PPC_frsqrte = idaapi.PPC_frsqrte       # Floating-Point Reciprocal Square Root Estimate
    #PPC_fsel = idaapi.PPC_fsel         # Floating-Point Select
    #PPC_fsqrt = idaapi.PPC_fsqrt       # Floating-Point Square Root
    #PPC_fsqrts = idaapi.PPC_fsqrts         # Floating-Point Square Root Single-Precision
    #PPC_fsub = idaapi.PPC_fsub         # Floating-Point Subtract
    #PPC_fsubs = idaapi.PPC_fsubs       # Floating-Point Subtract Single-Precision
    #PPC_icbi = idaapi.PPC_icbi         # Instruction Cache Block Invalidate
    #PPC_isync = idaapi.PPC_isync       # Instruction Synchronize
    #PPC_lfd = idaapi.PPC_lfd       # Load Floating-Point Double-Precision
    #PPC_lfdu = idaapi.PPC_lfdu         # Load Floating-Point Double-Precision with Update
    #PPC_lfdux = idaapi.PPC_lfdux       # Load Floating-Point Double-Precision with Update Indexed
    #PPC_lfdx = idaapi.PPC_lfdx         # Load Floating-Point Double-Precision Indexed
    #PPC_lfs = idaapi.PPC_lfs       # Load Floating-Point Single-Precision
    #PPC_lfsu = idaapi.PPC_lfsu         # Load Floating-Point Single-Precision with Update
    #PPC_lfsux = idaapi.PPC_lfsux       # Load Floating-Point Single-Precision with Update Indexed
    #PPC_lfsx = idaapi.PPC_lfsx         # Load Floating-Point Single-Precision Indexed
    #PPC_rfi = idaapi.PPC_rfi       # Return from Interrupt
    #PPC_rfid = idaapi.PPC_rfid         # Return from Interrupt Double Word
    #PPC_sc = idaapi.PPC_sc         # System Call
    #PPC_slbia = idaapi.PPC_slbia       # SLB Invalidate All
    #PPC_slbie = idaapi.PPC_slbie       # SLB Invalidate Entry
    #PPC_stfd = idaapi.PPC_stfd         # Store Floating-Point Double-Precision
    #PPC_stfdu = idaapi.PPC_stfdu       # Store Floating-Point Double-Precision wiht Update
    #PPC_stfdux = idaapi.PPC_stfdux         # Store Floating-Point Double-Precision wiht Update Indexed
    #PPC_stfdx = idaapi.PPC_stfdx       # Store Floating-Point Double-Precision Indexed
    #PPC_stfiwx = idaapi.PPC_stfiwx         # Store Floating-Point as Integer Word Indexed
    #PPC_stfs = idaapi.PPC_stfs         # Store Floating-Point Single-Precision
    #PPC_stfsu = idaapi.PPC_stfsu       # Store Floating-Point Single-Precision with Update
    #PPC_stfsux = idaapi.PPC_stfsux         # Store Floating-Point Single-Precision with Update Indexed
    #PPC_stfsx = idaapi.PPC_stfsx       # Store Floating-Point Single-Precision Indexed
    #PPC_sync = idaapi.PPC_sync         # Synchronize
    #PPC_td = idaapi.PPC_td         # Trap Double Word
    #PPC_tdi = idaapi.PPC_tdi       # Trap Double Word Immediate
    #PPC_tlbia = idaapi.PPC_tlbia       # TLB Invalidate All
    #PPC_tlbie = idaapi.PPC_tlbie       # TLB Invalidate Entry
    #PPC_tlbsync = idaapi.PPC_tlbsync       # TLB Synchronize
    #PPC_tw = idaapi.PPC_tw         # Trap Word
    #PPC_twi = idaapi.PPC_twi       # Trap Word Immediate

    #-------------

    #PPC_trap = idaapi.PPC_trap         # Trap Word Unconditionally
    #PPC_trapd = idaapi.PPC_trapd       # Trap Double Word Unconditionally
    #PPC_twlgt = idaapi.PPC_twlgt       # Trap Word if Logically Greater Than
    #PPC_twllt = idaapi.PPC_twllt       # Trap Word if Logically Less Than
    #PPC_tweq = idaapi.PPC_tweq         # Trap Word if Equal
    #PPC_twlge = idaapi.PPC_twlge       # Trap Word if Logically Greater Than or Equal
    #PPC_twlle = idaapi.PPC_twlle       # Trap Word if Logically Less Than or Equal
    #PPC_twgt = idaapi.PPC_twgt         # Trap Word if Greater Than
    #PPC_twge = idaapi.PPC_twge         # Trap Word if Greater Than or Equal
    #PPC_twlt = idaapi.PPC_twlt         # Trap Word if Less Than
    #PPC_twle = idaapi.PPC_twle         # Trap Word if Less Than oe Equal
    #PPC_twne = idaapi.PPC_twne         # Trap Word if Not Equal
    #PPC_twlgti = idaapi.PPC_twlgti         # Trap Word Immediate if Logically Greater Than
    #PPC_twllti = idaapi.PPC_twllti         # Trap Word Immediate if Logically Less Than
    #PPC_tweqi = idaapi.PPC_tweqi       # Trap Word Immediate if Equal
    #PPC_twlgei = idaapi.PPC_twlgei         # Trap Word Immediate if Logically Greater Than or Equal
    #PPC_twllei = idaapi.PPC_twllei         # Trap Word Immediate if Logically Less Than or Equal
    #PPC_twgti = idaapi.PPC_twgti       # Trap Word Immediate if Greater Than
    #PPC_twgei = idaapi.PPC_twgei       # Trap Word Immediate if Greater Than or Equal
    #PPC_twlti = idaapi.PPC_twlti       # Trap Word Immediate if Less Than
    #PPC_twlei = idaapi.PPC_twlei       # Trap Word Immediate if Less Than oe Equal
    #PPC_twnei = idaapi.PPC_twnei       # Trap Word Immediate if Not Equal
    #PPC_tdlgt = idaapi.PPC_tdlgt       # Trap Double Word if Logically Greater Than
    #PPC_tdllt = idaapi.PPC_tdllt       # Trap Double Word if Logically Less Than
    #PPC_tdeq = idaapi.PPC_tdeq         # Trap Double Word if Equal
    #PPC_tdlge = idaapi.PPC_tdlge       # Trap Double Word if Logically Greater Than or Equal
    #PPC_tdlle = idaapi.PPC_tdlle       # Trap Double Word if Logically Less Than or Equal
    #PPC_tdgt = idaapi.PPC_tdgt         # Trap Double Word if Greater Than
    #PPC_tdge = idaapi.PPC_tdge         # Trap Double Word if Greater Than or Equal
    #PPC_tdlt = idaapi.PPC_tdlt         # Trap Double Word if Less Than
    #PPC_tdle = idaapi.PPC_tdle         # Trap Double Word if Less Than oe Equal
    #PPC_tdne = idaapi.PPC_tdne         # Trap Double Word if Not Equal
    #PPC_tdlgti = idaapi.PPC_tdlgti         # Trap Double Word Immediate if Logically Greater Than
    #PPC_tdllti = idaapi.PPC_tdllti         # Trap Double Word Immediate if Logically Less Than
    #PPC_tdeqi = idaapi.PPC_tdeqi       # Trap Double Word Immediate if Equal
    #PPC_tdlgei = idaapi.PPC_tdlgei         # Trap Double Word Immediate if Logically Greater Than or Equal
    #PPC_tdllei = idaapi.PPC_tdllei         # Trap Double Word Immediate if Logically Less Than or Equal
    #PPC_tdgti = idaapi.PPC_tdgti       # Trap Double Word Immediate if Greater Than
    #PPC_tdgei = idaapi.PPC_tdgei       # Trap Double Word Immediate if Greater Than or Equal
    #PPC_tdlti = idaapi.PPC_tdlti       # Trap Double Word Immediate if Less Than
    #PPC_tdlei = idaapi.PPC_tdlei       # Trap Double Word Immediate if Less Than oe Equal
    #PPC_tdnei = idaapi.PPC_tdnei       # Trap Double Word Immediate if Not Equal

    PPC_crset = idaapi.PPC_crset        # Condition Register Set
    PPC_crnot = idaapi.PPC_crnot        # Condition Register NOT
    PPC_crmove = idaapi.PPC_crmove      # Condition Register Move
    PPC_crclr = idaapi.PPC_crclr        # Condition Register Clear

    PPC_extlwi = idaapi.PPC_extlwi      # Extract and Left Justify Immediate
    PPC_extrwi = idaapi.PPC_extrwi      # Extract and Right Justify Immediate
    PPC_inslwi = idaapi.PPC_inslwi      # Insert from Left Immediate
    PPC_insrwi = idaapi.PPC_insrwi      # Insert from Right Immediate
    PPC_rotlwi = idaapi.PPC_rotlwi      # Rotate Left Immediate
    PPC_rotrwi = idaapi.PPC_rotrwi      # Rotate Right Immediate
    PPC_rotlw = idaapi.PPC_rotlw        # Rotate Left
    PPC_slwi = idaapi.PPC_slwi      # Shift Left Immediate
    PPC_srwi = idaapi.PPC_srwi      # Shift Right Immediate
    PPC_clrlwi = idaapi.PPC_clrlwi      # Clear Left Immediate
    PPC_clrrwi = idaapi.PPC_clrrwi      # Clear Right Immediate
    PPC_clrlslwi = idaapi.PPC_clrlslwi      # Clear Left and Shift Left Immediate

    #
    #  PowerPC Embedded Controller Instructions
    #

    #PPC_dccci = idaapi.PPC_dccci       # Data cache congruence class invalidate (p.438-439)
    #PPC_dcread = idaapi.PPC_dcread         # Data cache read (p.440-441)
    #PPC_icbt = idaapi.PPC_icbt         # Instruction cache block touch (p.450-451)
    #PPC_iccci = idaapi.PPC_iccci       # Instruction cache congruence class invalidate (p.452-453)
    #PPC_icread = idaapi.PPC_icread         # Instruction cache read (p.454-455)
    #PPC_mfdcr = idaapi.PPC_mfdcr       # Move from device control register (p.484-485)
    #PPC_mtdcr = idaapi.PPC_mtdcr       # Move to device control register (p.491-492)
    #PPC_rfci = idaapi.PPC_rfci         # Return from critical interrupt (p.507)
    #PPC_tlbre = idaapi.PPC_tlbre       # TLB read entry (p.548-549)
    #PPC_tlbsx = idaapi.PPC_tlbsx       # TLB search indexed (p.550)
    #PPC_tlbwe = idaapi.PPC_tlbwe       # TLB write entry (p.552-553)
    #PPC_wrtee = idaapi.PPC_wrtee       # Write external enable (p.560)
    #PPC_wrteei = idaapi.PPC_wrteei         # Write external enable immediate (p.561)

    #
    #  New PowerPC instructions
    #

    #PPC_abs = idaapi.PPC_abs       # Absolute
    #PPC_clcs = idaapi.PPC_clcs         # Cache Lines Compute Size
    #PPC_clf = idaapi.PPC_clf       # Cache Line Flush
    #PPC_cli = idaapi.PPC_cli       # Cache Line Invalidate
    #PPC_dclst = idaapi.PPC_dclst       # Data Cache Line Store
    #PPC_div = idaapi.PPC_div       # Divide
    #PPC_divs = idaapi.PPC_divs         # Divide Short
    #PPC_doz = idaapi.PPC_doz       # Different Or Zero
    #PPC_dozi = idaapi.PPC_dozi         # Different Or Zero Immediate
    #PPC_frsqrtes = idaapi.PPC_frsqrtes         # Floating Reciprocal Square Root Estimate Single
    #PPC_hrfid = idaapi.PPC_hrfid       # Hypervisor Return from Interrupt Doubleword
    #PPC_lscbx = idaapi.PPC_lscbx       # Load String And Compare Byte Indexed
    #PPC_maskg = idaapi.PPC_maskg       # Mask Generate
    #PPC_maskir = idaapi.PPC_maskir         # Mask Insert From Register
    #PPC_mfsri = idaapi.PPC_mfsri       # Move From Segment Register Indirect
    #PPC_mul = idaapi.PPC_mul       # Multiply
    #PPC_nabs = idaapi.PPC_nabs         # Negative Absolute
    #PPC_popcntb = idaapi.PPC_popcntb       # Population Count Bytes
    #PPC_rac = idaapi.PPC_rac       # Real Address Compute
    #PPC_rfsvc = idaapi.PPC_rfsvc       # Return From SVC
    #PPC_rlmi = idaapi.PPC_rlmi         # Rotate Left Then Mask Insert
    #PPC_rrib = idaapi.PPC_rrib         # Rotate Right And Insert Bit
    #PPC_slbmfee = idaapi.PPC_slbmfee       # SLB Move From Entry ESID
    #PPC_slbmfev = idaapi.PPC_slbmfev       # SLB Move From Entry VSID
    #PPC_slbmte = idaapi.PPC_slbmte         # SLB Move To Entry
    #PPC_sle = idaapi.PPC_sle       # Shift Left Extended
    #PPC_sleq = idaapi.PPC_sleq         # Shift Left Extended With MQ
    #PPC_sliq = idaapi.PPC_sliq         # Shift Left Immediate With MQ
    #PPC_slliq = idaapi.PPC_slliq       # Shift Left Long Immediate With MQ
    #PPC_sllq = idaapi.PPC_sllq         # Shift Left Long With MQ
    #PPC_slq = idaapi.PPC_slq       # Shift Left With MQ
    #PPC_sraiq = idaapi.PPC_sraiq       # Shift Right Algebraic Immediate With MQ
    #PPC_sraq = idaapi.PPC_sraq         # Shift Right Algebraic With MQ
    #PPC_sre = idaapi.PPC_sre       # Shift Right Extended
    #PPC_srea = idaapi.PPC_srea         # Shift Right Extended Algebraic
    #PPC_sreq = idaapi.PPC_sreq         # Shift Right Extended With MQ
    #PPC_sriq = idaapi.PPC_sriq         # Shift Right Immediate With MQ
    #PPC_srliq = idaapi.PPC_srliq       # Shift Right Long Immediate With MQ
    #PPC_srlq = idaapi.PPC_srlq         # Shift Right Long With MQ
    #PPC_srq = idaapi.PPC_srq       # Shift Right With MQ

    #
    #   New PowerPC instructions
    #

    #PPC_mtocrf = idaapi.PPC_mtocrf         # Move To One Condition Register Field
    #PPC_mfocrf = idaapi.PPC_mfocrf         # Move From One Condition Register Field

    GPR0 = 0
    GPR1 = 1
    SP   = GPR1
    GPR2 = 2
    TOC  = GPR2
    GPR3 = 3
    GPR4 = 4
    GPR5 = 5
    GPR6 = 6
    GPR7 = 7
    GPR8 = 8
    GPR9 = 9
    GPR10 = 10
    GPR11 = 11
    GPR12 = 12 
    GPR13 = 13
    GPR14 = 14
    GPR15 = 15
    GPR16 = 16
    GPR17 = 17
    GPR18 = 18
    GPR19 = 19
    GPR20 = 20
    GPR21 = 21
    GPR22 = 22
    GPR23 = 23
    GPR24 = 24
    GPR25 = 25
    GPR26 = 26
    GPR27 = 27
    GPR28 = 28
    GPR29 = 29
    GPR30 = 30
    GPR31 = 31

    TOTAL_GPR = 32      # Number of general purpose registers.

    GPR_NAMES = {
        GPR0 : "r0",
        GPR1 : "r1",
        SP   : "sp",
        GPR2 : "r2",
        TOC  : "TOC",
        GPR3 : "r3",
        GPR4 : "r4",
        GPR5 : "r5",
        GPR6 : "r6",
        GPR7 : "r7",
        GPR8 : "r8",
        GPR9 : "r9",
        GPR10 : "r10",
        GPR11 : "r11",
        GPR12 : "r12", 
        GPR13 : "r13",
        GPR14 : "r14",
        GPR15 : "r15",
        GPR16 : "r16",
        GPR17 : "r17",
        GPR18 : "r18",
        GPR19 : "r19",
        GPR20 : "r20",
        GPR21 : "r21",
        GPR22 : "r22",
        GPR23 : "r23",
        GPR24 : "r24",
        GPR25 : "r25",
        GPR26 : "r26",
        GPR27 : "r27",
        GPR28 : "r28",
        GPR29 : "r29",
        GPR30 : "r30",
        GPR31 : "r31",
    }

    def reg_name(self, reg):
        """Return the name of the specified register."""
        return self.GPR_NAMES.get(reg, None)

    #
    # Special purpose registers in PowerPC
    #
    SPR       = idaapi.o_idpspec0     # Special purpose register
    TWOFPR    = idaapi.o_idpspec1     # Two FPPR_s
    SHMBME    = idaapi.o_idpspec2     # SH & MB & ME
    CRF       = idaapi.o_idpspec3     # crfield      x.reg
    CRB       = idaapi.o_idpspec4     # crbit        x.reg
    DCR       = idaapi.o_idpspec5     # Device control register

    SPR_NAMES = {
        SPR       : "spr",
        TWOFPR    : "twofpr",
        SHMBME    : "shmbme",
        CRF       : "crf",
        CRB       : "crb",
        DCR       : "dcr",
    }

    ARGUMENT_REGISTERS = [GPR3, GPR4, GPR5, GPR6, GPR7, GPR8, GPR9, GPR10]

    RETURN_REGISTERS = [GPR3, GPR4]

    VOLATILE_REGISTERS = ARGUMENT_REGISTERS + [GPR11, GPR12]

    #
    #  Helper methods
    #

    def is_branch(self, inst_type):
        """Indicate if the specified instruction is some kind of branch
        instruction.

        """
        return inst_type in CONDITIONAL_BRANCH_TYPES or \
            inst_type in UNCONDITIONAL_BRANCH_TYPES

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

    InstructionSet.PPC_cmpwi,       # Compare Word Immediate
    InstructionSet.PPC_cmpw,        # Compare Word
    InstructionSet.PPC_cmplwi,      # Compare Logical Word Immediate
    InstructionSet.PPC_cmplw,       # Compare Logical Word
    InstructionSet.PPC_cmpdi,       # Compare Double Word Immediate
    InstructionSet.PPC_cmpd,        # Compare Double Word
    InstructionSet.PPC_cmpldi,      # Compare Logical Double Word Immediate
    InstructionSet.PPC_cmpld,       # Compare Logical Double Word

    InstructionSet.PPC_cmp,         # Compare
    InstructionSet.PPC_cmpi,        # Compare Immediate
    InstructionSet.PPC_cmpl,        # Compare Logical
    InstructionSet.PPC_cmpli,       # Compare Logical Immediate

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
    InstructionSet.PPC_mftbl,       # Move from time base register (lower)
    InstructionSet.PPC_mftbu,       # Move from time base register (upper)
    InstructionSet.PPC_mfpvr,       # Move from processor version register
]

UNCONDITIONAL_BRANCH_TYPES = [
    InstructionSet.PPC_b,           # Branch
    InstructionSet.PPC_balways,     # Branch unconditionally
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
http://www-01.ibm.com/support/knowledgecenter/ssw_aix_53/com.ibm.aix.aixassem/doc/alangref/linkage_convent.htm%23a108f065c

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

