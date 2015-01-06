#!/bin/bash

gvim -O2 ./*.py \
    frontend/*.py \
    frontend/lir/*.py \
    frontend/generic_disasm/idapro/*.py \
    middleend/mir/*.py \
    middleend/*.py \
    cbackend/*.py \
    cbackend/hir/*.py
#gvim -O3 /home/topo/.wine/drive_c/Python26/Lib/site-packages/llvm/core.py /usr/src/llvm-py-0.5/test/*.py
