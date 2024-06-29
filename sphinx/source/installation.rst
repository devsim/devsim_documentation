.. _sec__installation:



Supported platforms
===================

|devsim| is compiled and tested on the platforms in :numref:`installation__platforms`.

.. _installation__platforms:

.. csv-table:: Current platforms for |devsim|
  :header: "Platform", "Architecture", "OS Version"
  :widths: 10, 10, 20

  "|mswindows|", "x64", "|mswindowsten|"
  "|linux|", "x86_64, aarch64", "|rhelseven| (|centosseven| compatible)"
  "|macosx|", "x86_64, arm64", "|macosxmonterey|"

These are the minimum supported platforms, and also expected to work on newer versions of these operating systems.  If you require a version on a different software platform, please contact us :ref:`Contact`.

Install |python|
================


A |python| version of 3.7 or higher is needed to run |devsim|.  This requirement is often met by the default installations of the above systems.  In addition, it is possible to download other |python| versions online.  Popular distributions of |python| are listed in :numref:`python_distros`.

.. _python_distros:

.. csv-table:: |python| distributions
  :header: "Vendor", "Path", "Website"
  :widths: 10, 20, 40

  "Anaconda", "``$CONDA_PREFIX``", "https://www.anaconda.com"
  "Python.org", "``$VIRTUAL_ENV``", "https://python.org"


.. _sec__venv_install:

Create virtual environment
--------------------------

Creating a virtual environment is needed so |devsim| may necessary math libraries, as discussed in :ref:`sec_dllsearchpath`.  The |numpy| package is also recommended to ensure that needed math libraries are available.

|anaconda|
^^^^^^^^^^

Using the |conda| package manager in an |anaconda|, a virtual environment is created using.

.. code-block:: none

    conda create -n denv python numpy
    conda activate denv

where ``denv`` is the name of the environment.  If you are using a ``x64`` or ``x86_64`` based system, you may install the |intelmkl| with the Pardiso Solver.

.. code-block:: none

    conda install mkl


Using ``venv``
^^^^^^^^^^^^^^

For other |python| distributions, the requisite packages may be installed by using a ``venv`` based virtual environment.

.. code-block:: none

    python3 -mvenv denv
    source denv/bin/activate
    pip install numpy

where ``denv`` is the name of directory containing the environment.  If you are using a ``x64`` or ``x86_64`` based system, you may install the |intelmkl| with the Pardiso Solver.

.. code-block:: none

    pip install mkl

Install DEVSIM
==============

Install
-------

DEVSIM is available from `PyPI <https://pypi.org/project/devsim/>`_ using ``pip``.  To install this package for your platform:

.. code-block:: none

    pip install devsim

Please see the ``devsim_data/INSTALL.md`` file in the distribution for more information.  This files may be found in the prefix directory for your chosen environment listed in :numref:`python_distros`.


Test
----

To ensure a proper installation, please type the following at a |python| prompt.

.. code-block:: none

    >>> import devsim
    Searching DEVSIM_MATH_LIBS="libopenblas.dylib:liblapack.dylib:libblas.dylib"
    Loading "libopenblas.dylib": ALL BLAS/LAPACK LOADED
    Skipping liblapack.dylib
    Skipping libblas.dylib
    loading UMFPACK 5.1 as direct solver

Note that there will be an error if no math libraries are available.

.. code-block:: none

    >>> import devsim
    Searching DEVSIM_MATH_LIBS="libopenblas.so:liblapack.so:libblas.so"
    Loading "libopenblas.so": MISSING DLL
    Loading "liblapack.so": MISSING DLL
    Loading "libblas.so": MISSING DLL
    Error loading math libraries.  Please install a suitable BLAS/LAPACK library and set DEVSIM_MATH_LIBS.  Alternatively, install the Intel MKL.
    libblas.so: cannot open shared object file: No such file or directory
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/home/user/venv/lib/python3.8/site-packages/devsim/__init__.py", line 8, in <module>
        from .devsim_py3 import *
    RuntimeError: Issues initializing DEVSIM.


Running DEVSIM
--------------

See :ref:`ch__scripting` for instructions on how to invoke |devsim|.


Building from source
====================

Building from source is possible, and is useful when you want to extend the simulator, use compiler optimizations, or port to a new platform.  See the ``BUILD.md`` file in the project files for more information.

