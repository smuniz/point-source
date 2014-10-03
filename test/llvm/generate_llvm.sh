clang -cc1 -S -emit-llvm ../src/test0.c -o ./test0.ll
llc --x86-asm-syntax=intel test0.ll -o test0
