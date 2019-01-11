#!/bin/bash
set -e
conda create --yes --name devsim_doc python=3
source activate devsim_doc
conda install --yes sphinx sphinx_rtd_theme numpydoc
pip install sphinxcontrib-bibtex
