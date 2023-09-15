#!/usr/bin/env bash
scriptdir=$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")
export BUILDDIR=${BUILDDIR:-_build}
mkdir -p ${BUILDDIR}
echo BUILDDIR
(
    cd ${BUILDDIR}
    robot "$@" ${scriptdir}/robot
)
