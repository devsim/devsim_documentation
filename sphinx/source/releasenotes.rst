.. include:: macros.rst

.. _release_notes:

*************
Release notes
*************

Introduction
============

|devsim| download and installation instructions are located in :ref:`sec__installation`.  The following sections list bug fixes and enhancements over time.  Contact information is listed in :ref:`Contact`.
A file named ``CHANGES.md`` is now distributed with |devsim|, which can contain additional details concerning a new release.


Version 2.9.0
=============

Windows Python support
----------------------

The official ``python.org`` distribution is beter supported.  This is since the ``python.org`` distribution does not appear to ship the ``zlib.dll``.

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Based on a contribution by [@simbilod](https://github.com/simbilod) :meth:`devsim.write_devices` now supports reducing the file size of data files by allowing users to specify a callback function to reduce data usage.  In this example, only the ``NetDoping`` field is written to the Tecplot data file.

.. code-block:: none

    devsim.write_devices(
        file="mesh2d_reduced.tec",
        type="tecplot",
        include_test=lambda x: x in ("NetDoping",),
    )

FLOOPS data file output
^^^^^^^^^^^^^^^^^^^^^^^

The ``floops`` option for :meth:`devsim.write_devices` has been removed.


Platform support
----------------

Windows build issue
^^^^^^^^^^^^^^^^^^^

During testing, it was found the Visual Studio 2022 builds were failing a test related to threading.  This was found to be a problem with version ``17.10``, but not version ``17.9``.  This affects the build automation, but should not affect the binary releases.

Centos 7 end of life
^^^^^^^^^^^^^^^^^^^^

This is the last version to support Centos 7 before its end of life on June 30, 2024.  After this date we will be moving to the AlmaLinux 8 based ``manylinux_2_28``.


Previous releases
=================

For older release notes, please refer to the Version 2.8.1 manual located at `https://doi.org/10.5281/zenodo.12211919 <https://doi.org/10.5281/zenodo.12211919>`__.  The latest version is available from `https://doi.org/10.5281/zenodo.4583208 <https://doi.org/10.5281/zenodo.4583208>`__.
