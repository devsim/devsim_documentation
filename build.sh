#!/bin/bash
set -e

BASEDIR=${PWD}
PYDIR=${BASEDIR}/pydoc
SPHINXDIR=${BASEDIR}/sphinx
SPHINXSOURCE=${SPHINXDIR}/source
SPHINXBUILD=${SPHINXDIR}/build
PKGDIR=${BASEDIR}/doc
export PYTHONPATH=${PYDIR}
echo ${PYTHONPATH}

cd ${PYDIR}
echo "Generating Python Documentation"
python CommandDoc.py

cp -av CommandReference.rst ${SPHINXSOURCE}

cd ${SPHINXDIR}
make html
make latexpdf

rm -rf ${PKGDIR}
mkdir -p ${PKGDIR}
cp -vR  ${SPHINXBUILD}/html ${PKGDIR}
cp -v ${SPHINXBUILD}/latex/devsim.pdf ${PKGDIR}
cp -v ${PYDIR}/DevsimDoc.cc ${PKGDIR}

