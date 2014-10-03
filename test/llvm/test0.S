	.file	"test0.ll"
	.text
	.globl	test0
	.align	2
	.type	test0,@function
test0:                                  # @test0
# BB#0:
	li 3, 291                       # <MCInst #352 LI
                                        #  <MCOperand Reg:83>
                                        #  <MCOperand Imm:291>>
	blr                             # <MCInst #128 BLR
                                        #  <MCOperand Reg:78>
                                        #  <MCOperand Reg:112>
                                        #  <MCOperand Reg:83>>
.Ltmp0:
	.size	test0, .Ltmp0-test0


