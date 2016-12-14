#!/bin/bash
_base=".."
_dfiles="${_base}/src/*.c"


mkdir x86_64
cd x86_64

for f in $_dfiles
do
    x86_64-linux-gnu-gcc "${f}" -c
done

#cd ../
#mkdir x86
#cd x86
#
#for f in $_dfiles
#do
#    x86-linux-gnu-gcc "${f}" -c
#done

cd ../
mkdir aarch64-linux-gnu
cd aarch64-linux-gnu

for f in $_dfiles
do
    aarch64-linux-gnu-gcc "${f}" -c
done

cd ../
mkdir arm-linux-gnueabi
cd arm-linux-gnueabi

for f in $_dfiles
do
    arm-linux-gnueabi-gcc "${f}" -c
done

cd ../
mkdir mips-linux-gnu
cd mips-linux-gnu

for f in $_dfiles
do
    mips-linux-gnu-gcc "${f}" -c
done

cd ../
mkdir powerpc-linux-gnu
cd powerpc-linux-gnu

for f in $_dfiles
do
    powerpc-linux-gnu-gcc "${f}" -c
done

