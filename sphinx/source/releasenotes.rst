.. include:: macros.rst

.. _release_notes:

*************
Release notes
*************

Introduction
============

|devsim| download and installation instructions are located in :ref:`sec__installation`.  The following sections list bug fixes and enhancements over time.  Contact information is listed in :ref:`Contact`.
A file named ``CHANGES.md`` is now distributed with |devsim|, which can contain additional details concerning a new release.

Version 2.11.2
==============

Trusted Publishing
------------------

* [#170](https://github.com/devsim/devsim/issues/170) add trusted publishing to pypi

Python wheels are now published directly from GitHub Actions to PyPI.  This makes the released files more secure in the their handling.  Tools are available to verify the provenance.  More info is available from https://docs.pypi.org/trusted-publishers/.

Citing DEVSIM
-------------

* The ``CITATION.cff`` file contains citations for the simulator.  It also contains some additional references.

Resetting DEVSIM while using umfpack
------------------------------------

* [#169](https://github.com/devsim/devsim/issues/169) umfpack reload after ``devsim_reset``

When using the ``reset_devsim`` command to reset the simulator, the ``UMFPACK 5.1`` solver was not being reloaded.  The command is modified so that the solver will now continue to with the same ``BLAS`` library when ``devsim`` is first loaded.

Internally, the ``UMFPACK 5.1`` hook in devsim will no longer reload the ``BLAS`` library with each call to the ``solve`` command.  In addition, the math libraries used by ``devsim`` will only be loaded when the module is first imported.


pylance compatible docstrings
-----------------------------

* [#155](https://github.com/devsim/devsim/issues/155) pylance compatible docstrings

A ``__init__.pyi`` file is included in ``devsim`` to provide documentation in IDEs which cannot get them from the compiled shared libraries.  This file should be automatically detected and used within the IDE.  It is generated in the ``devsim/devsim_documenation`` project.

misc changes
------------

The ``symdiff`` manual and example files are no longer included in the distribution.  These files can be downloaded by installing ``symdiff`` via ``pip``.

An extra copy of the ``umfpack_lgpl`` dynamic library was being distributed in the ``macOS`` package and has been removed.



Version 2.11.1
==============

Math Library Support
--------------------

BLAS Symbol Naming
~~~~~~~~~~~~~~~~~~

* [#167](https://github.com/devsim/devsim/issues/167) Accept scipy-openblas32 as a BLAS/LAPACK provider

When ``DEVSIM_MATH_LIBS`` is set, a user may specify ``DEVSIM_BLAS_PREFIX`` and ``DEVSIM_BLAS_SUFFIX`` to math symbols not using the standard form.

.. code-block:: none

    import scipy_openblas32
    import os
    os.environ['DEVSIM_MATH_LIBS'] = os.path.join(scipy_openblas32.get_lib_dir(), 'libscipy_openblas.dylib')
    os.environ['DEVSIM_BLAS_PREFIX'] = 'scipy_'
    os.environ['DEVSIM_BLAS_SUFFIX'] = '_'
    import devsim

Please see ``testing/other_blas.py`` for an example using the ``scipy_openblas32`` package as an alternative to the default math packages on each system.  This example is fragile as the math package maintainers make no guarantess for a stable abi.

Thanks to [@benvial](https://github.com/benvial) for suggesting this feature.

Info strings with more math informaiton
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As part of this work, more information is returned via the ``info`` parameter:

.. code-block:: none

    >>> _ = [print(x) for x in devsim.get_parameter(name="info").items()]
    ('blas_symbol_prefix', 'scipy_')
    ('blas_symbol_suffix', '_')
    ('copyright', 'Copyright © 2009-2026 DEVSIM LLC')
    ('direct_solver', 'custom')
    ('extended_precision', True)
    ('license', 'Apache License, Version 2.0')
    ('math_libraries', ('/Users/user/git/venv/lib/python3.14/site-packages/scipy_openblas32/lib/libscipy_openblas.dylib',))
    ('version', '2.11.1')
    ('website', 'https://devsim.org')
    ('custom_solver', 'UMFPACK 5.1')

Platform Support
----------------

macOS Version
~~~~~~~~~~~~~

|macosxsequoia| is the minimum version supported for macOS.  This is due to the ending of vendor support for |macosxsonoma|.

Windows
~~~~~~~

Due to changes to the file location of shared libraries and include files in |anaconda| Python, the automated build has been updated.

Bugs
----

Helper function for model creation bug
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [#168](https://github.com/devsim/devsim/issues/168) ``model_create.EnsureEdgeFromNodeModelExists`` never creates the ``X@n0/X@n1`` edge models

Thanks to [@NooriDan](https://github.com/NooriDan) for reporting this issue.

Version 2.11.0
==============

Surface Normal Models
---------------------

* [#162](https://github.com/devsim/devsim/issues/162) surface normal models should point outward

The following node models now point outward for each node.  Previously, the sign was arbitrary.

* ``ContactNSurfaceNormal_x``
* ``ContactNSurfaceNormal_y``
* ``ContactNSurfaceNormal_z``
* ``NSurfaceNormal_x``
* ``NSurfaceNormal_y``
* ``NSurfaceNormal_z``

The only regression results affected were the saved values for the values at some nodes changed direction based on how they were averaged to the node.

GitHub Issues
-------------

* [#165](https://github.com/devsim/devsim/issues/165) Update c++20
* [#164](https://github.com/devsim/devsim/issues/164) use std array for basic shapes
* [#160](https://github.com/devsim/devsim/issues/160) Visual Studio 2026

Version 2.10.1
==============

UMFPACK Solver
--------------

Fixed issue with `UMFPACK` solver when the dynamic library is being unloaded at program termination.

Windows MKL
-----------

Fix issue [#159](https://github.com/devsim/devsim/issues/159) where users had to add ``Library\bin`` manually to the system path in order to load the Intel MKL when using a non Anaconda-based Python distribution.  The proper way to install the Intel MKL using ``pip`` is:

.. code-block:: none

  pip install mkl

Thanks to [@JoonatanAlanampa](https://github.com/JoonatanAlanampa) for helping to diagnose this issue.

Version 2.10.0
==============

Regression results
------------------

Due to the changes in this release, there are changes to the expected numerical results.  Please see :numref:`sec__regressions` for a listing of where the current results are stored.


Available platform builds
-------------------------

Build automation is now being done using GitHub Actions.   Please see :numref:`installation__platforms` for current OS support. This has lead to the following changes to the build:

macOS
~~~~~

Intel ``x86_64`` is no longer longer a supported on ``macOS``.  The minimum supported version is now |macosxsonoma|.

Windows
~~~~~~~

Now built on Windows 2025 server running the latest supported version of Visual Studio 2022 Enterprise.

Linux
~~~~~

Linux continues to be built on the ``manylinux_2_28`` docker image.  This is compatible with AlmaLinux 8 and is expected to be binary compatible with most current linux distributions for both ``x86_64`` and ``aarch64``.

Python Version
--------------

|pythonthreenine| is now the minimum supported version.  Please make sure you are using a newer version of Python when attempting to download from PyPi.  Python 3.9 is end of life on October 31, 2025, and we may switch to Python 3.10 as the minimum supported version after that.

Contact Normal Model
--------------------

Fix issue [#158](https://github.com/devsim/devsim/issues/158), Missing Contact Surface Normal

* ``ContactNSurfaceNormal_x``
* ``ContactNSurfaceNormal_y``
* ``ContactNSurfaceNormal_z``

are node models now listed in :numref:`models__node`.

Thanks to [@marc-flex](https://github.com/marc-flex) for providing a pull request for these missing models.

Documentation
-------------

A tasks note is added in ``HOWTO.md``, with some miscellaneous notes concerning building the software.

Version 2.9.1
=============

Internal code was refactored.  While it has been tested, please report any issues you may encounter.

Version 2.9.0
=============

Windows Python support
----------------------

The official ``python.org`` distribution is better supported.  This is since the ``python.org`` distribution does not appear to ship the ``zlib.dll``.

VTK writer
----------

[#151](https://github.com/devsim/devsim/issues/151)

Use ``zlib`` from Python module instead of Anaconda ``zlib.dll`` or the system ``zlib`` for other operating systems.  The compressed binary data written to the ``.vtu`` files should be numerically the same.

Clang build on Windows
----------------------

While the Windows version is still built with Visual Studio 2022, the build system now supports building with the Clang compilers.

Version 2.8.4
=============

Serialization of equation command
---------------------------------

Write ``variable_update`` when writing the :meth:`devsim.equation` command to the devsim file format.

Simulation Matrix
-----------------

Fix issue [#148](https://github.com/devsim/devsim/issues/148) segmentation fault in :meth:`devsim.get_matrix_and_rhs`.  Matrix and RHS now printed in ``testing/cap2.py``.

macOS Build
-----------

Fix issue [#149](https://github.com/devsim/devsim/issues/149) fix issue with macOS build scripts.

Version 2.8.3
=============

Linux support
-------------

Due to the |rhel-7| end of life on June 30, 2024, the minimum support level for Linux is now |rhel-8| using the |almalinux-8| based `manylinux_2_28 <https://github.com/pypa/manylinux?tab=readme-ov-file#manylinux_2_28-almalinux-8-based>`__.  Please see :ref:`sec__installation` for more information.

Clang format
------------

Add `.clang-format` file to provide assist automatic formatting for new source code.

Get equation command
--------------------

Fixed issue [#145](https://github.com/devsim/devsim/issues/145). `get_equation_command` now provides the `variable_update` option that was used.

Exception propagation
---------------------

Fixed issue where an internal C++ based exception, may not be caught properly on some platforms.

Version 2.8.2
=============

Documentation refactor
----------------------

The release notes section has been shortened to the most recent releases.  Important information from the release notes was placed in the appropriate sections of the manual.  The manual has also been reorganized.  The ``pdf`` formatting has been improved to reduce the number of empty pages.

For older release notes, please refer to the Version 2.8.1 manual located at `https://doi.org/10.5281/zenodo.12211919 <https://doi.org/10.5281/zenodo.12211919>`__.  The latest version is available from `https://doi.org/10.5281/zenodo.4583208 <https://doi.org/10.5281/zenodo.4583208>`__.

Version 2.8.1
=============

Help files
----------

Updated instructions.  Added additional documentation files.

.. list-table:: Added documentation files
   :header-rows: 1

   * - File
     - Purpose
   * - ``BUILD.md``
     - Building from source
   * - ``CODE_OF_CONDUCT.md``
     - Code of conduct
   * - ``TEST.md``
     - Testing instructions

Database command removal
------------------------

The material database has been removed.

* ``devsim.create_db``
* ``devsim.open_db``
* ``devsim.close_db``
* ``devsim.save_db``
* ``devsim.add_db_entry``
* ``devsim.get_db_entry``

This feature was only being used in the ``bioapp1`` examples, and those tests have been updated.  This also removes the binary dependence on SQLite.

Version 2.8.0
=============

|python| scripts
----------------

Based on a contribution by [@simbilod](https://github.com/simbilod), all of the |python| scripts have been reformatted.  The build system was also updated to enforce |python| script modifications are properly formatted when submitted to the project.

Data output
-----------

Reduction in data file sizes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Based on a contribution by [@simbilod](https://github.com/simbilod) :meth:`devsim.write_devices` now supports reducing the file size of data files by allowing users to specify a callback function to reduce data usage.  In this example, only the ``NetDoping`` field is written to the Tecplot data file.

.. code-block:: none

    devsim.write_devices(
        file="mesh2d_reduced.tec",
        type="tecplot",
        include_test=lambda x: x in ("NetDoping",),
    )

FLOOPS data file output
~~~~~~~~~~~~~~~~~~~~~~~

The ``floops`` option for :meth:`devsim.write_devices` has been removed.


Platform support
----------------

Windows build issue
~~~~~~~~~~~~~~~~~~~

During testing, it was found the Visual Studio 2022 builds were failing a test related to threading.  This was found to be a problem with version ``17.10``, but not version ``17.9``.  This affects the build automation, but should not affect the binary releases.

Centos 7 end of life
~~~~~~~~~~~~~~~~~~~~

This is the last version to support Centos 7 before its end of life on June 30, 2024.  After this date we will be moving to the AlmaLinux 8 based ``manylinux_2_28``.


Previous releases
=================

For older release notes, please refer to the Version 2.8.1 manual located at `https://doi.org/10.5281/zenodo.12211919 <https://doi.org/10.5281/zenodo.12211919>`__.  The latest version is available from `https://doi.org/10.5281/zenodo.4583208 <https://doi.org/10.5281/zenodo.4583208>`__.
