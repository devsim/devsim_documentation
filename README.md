# devsim_documentation

[![Build Status](https://travis-ci.org/devsim/devsim_documentation.svg?branch=master)](https://travis-ci.org/devsim/devsim_documentation)

## Introduction

This is the future location for the DEVSIM Manual and related documentation.  It is currently hosted in pdf and html formats here. https://devsim.net

## Contributing

If you are interested in helping improve the documentation for DEVSIM.  Please contact us in our forum.

https://forum.devsim.org

## Building

Build steps starting with a Python virtual environment in your path.

```
# create environment
python3 -mvenv venv

# activate
source venv/bin/activate

# install sphinx documentation packages

source preinstall.sh

# build html and pdf documentation

bash build.sh
```

The doc directory contains the pdf, html, and c++ file.

## Adding a new command

When adding a new command in ``devsim`` you should place the Python documentation in the `pydoc` directory of this project in the appropriate file.  The `build.sh` script will then create the doc strings for the pdf and html documentation.  A ``DevsimDoc.cc`` is also generated and needs to be placed in the ``src/pythonapi`` directory of your source repository.
