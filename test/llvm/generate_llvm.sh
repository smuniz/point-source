#!/bin/sh

PATH=/opt/clang+llvm-3.3-Ubuntu-13.04-x86_64-linux-gnu/bin/:$PATH clang -cc1 -S -emit-llvm ../src/test1.c -o ./test1.ll
#PATH=/opt/clang+llvm-3.3-Ubuntu-13.04-x86_64-linux-gnu/bin/:$PATH llc --x86-asm-syntax=intel test1.ll -o test1
PATH=/opt/clang+llvm-3.3-Ubuntu-13.04-x86_64-linux-gnu/bin/:$PATH llc --march=ppc32 test1.ll -o test1.S

PATH=/opt/clang+llvm-3.3-Ubuntu-13.04-x86_64-linux-gnu/bin/:$PATH llc -march=cpp test82.ll
