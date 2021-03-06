#!/bin/bash
PAPER_TOPDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)"
rm -rf ${PAPER_TOPDIR}/build/*
mkdir -p ${PAPER_TOPDIR}/build
cd ${PAPER_TOPDIR}/build
cmake ..
cd ..
make -C build

echo "Your PDF awaits under $(pwd)/build"
