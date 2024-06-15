
.. include:: macros.txt

.. _release_notes:

Release Notes
-------------

Introduction
~~~~~~~~~~~~

|devsim| download and installation instructions are located in :ref:`sec__installation`.  The following sections list bug fixes and enhancements over time.  Contact information is listed in :ref:`Contact`.
A file named ``CHANGES.md`` is now distributed with |devsim|, which can contain additional details concerning a new release.

Version 2.8.1
~~~~~~~~~~~~~

The material database has been removed.

* ``devsim.create_db``
* ``devsim.open_db``
* ``devsim.close_db``
* ``devsim.save_db``
* ``devsim.add_db_entry``
* ``devsim.get_db_entry``

This feature was not used in any example or well documented.

Version 2.8.0
~~~~~~~~~~~~~

Python Scripts
^^^^^^^^^^^^^^

Based on a contribution by [@simbilod](https://github.com/simbilod), all of the Python scripts have been reformatted.  The build system was also updated to enforce Python script modifications are properly formatted when submitted to the project.

Data Output
^^^^^^^^^^^

Reduction in Data file sizes
""""""""""""""""""""""""""""

Based on a contribution by [@simbilod](https://github.com/simbilod) :meth:`devsim.write_devices` now supports reducing the file size of data files by allowing users to specify a callback function to reduce data usage.  In this example, only the ``NetDoping`` field is written to the Tecplot data file.

.. code-block:: none

    devsim.write_devices(
        file="mesh2d_reduced.tec",
        type="tecplot",
        include_test=lambda x: x in ("NetDoping",),
    )

FLOOPS Data File Output
"""""""""""""""""""""""

The ``floops`` option for :meth:`devsim.write_devices` has been removed.


Platform Support
^^^^^^^^^^^^^^^^

Windows Build Issue
"""""""""""""""""""

During testing, it was found the Visual Studio 2022 builds were failing a test related to threading.  This was found to be a problem with version ``17.10``, but not version ``17.9``.  This affects the build automation, but should not affect the binary releases.

Centos 7 End of Life
""""""""""""""""""""

This is the last version to support Centos 7 before its end of life on June 30, 2024.  After this date we will be moving to the AlmaLinux 8 based ``manylinux_2_28``.

Version 2.7.3
~~~~~~~~~~~~~

Fixed issue [#133](https://github.com/devsim/devsim/issues/133) identified by [@yh-kwok](https://github.com/yh-kwok).

Version 2.7.2
~~~~~~~~~~~~~

* macOS package is now Universal.  Both ``x86_64`` and ``arm64`` will use ``clang`` compiler and macOS 12.0 is now the minimum supported version.
* Update Boost version to 1.82
* Improvements to extended precision complex numbers implementation to work with newer compilers.
* Script to build for ``manylinux_2_28`` (Centos 8)
* Build Linux aarch64 from macOS system with docker

Version 2.7.1
~~~~~~~~~~~~~

* Support for Linux aarch64, which can be run on Amazon AWS 64 bit instances.
* Better implicit float conversions in parameters.

Version 2.7.0
~~~~~~~~~~~~~

Error Handling
^^^^^^^^^^^^^^

More helpful exception information returned to Python if the error is considered fatal.  This can be used to decide if the simulation can be restarted.  Note that if this occurs during a solve, it is necessary for the user to restore the previous circuit and device solutions if a restart is desired.  In addition, model evaluation is reset so that no false cyclic dependencies are reported after an error.

In this example code below, the previously ``DEVSIM FATAL`` error string will now provide the context that a floating point exception occurred and be handled in Python.

.. code-block:: none

    try:
        self.solve()
    except error as msg:
        m = str(msg)
        if 'Convergence failure' in m:
            self.set_vapp(last_bias)
        elif'floating point exception' in m:
            self.set_vapp(last_bias)
            self.restore_callback(self.is_circuit)
        else:
            raise


Version 2.6.5
~~~~~~~~~~~~~

Bugs
^^^^
Fixed issue [#123](https://github.com/devsim/devsim/issues/123) identified by [@gluek](https://github.com/gluek) This resulted in bad results on Windows and macOS in calculation of 3d mesh areas and volumes.

Version 2.6.4
~~~~~~~~~~~~~

SuperLU
^^^^^^^

Use ``MMD_ATA`` preconditioner for SuperLU builds.

Android
^^^^^^^

Android builds use special implementations for the Bernoulli function to prevent overflow.

Examples
^^^^^^^^

``testing/pythonmesh1d.py`` demonstrates how to get mesh information using :meth:`devsim.get_element_node_list`.

``examples/diode/tran_diode.py`` demonstrates transient diode simulation.

Version 2.6.3
~~~~~~~~~~~~~

Allow Python threading during long solve operations.

Version 2.6.2
~~~~~~~~~~~~~

* :meth:`devsim.delete_circuit`
* :meth:`devsim.get_mesh_list`

Version 2.6.1
~~~~~~~~~~~~~

Bugs
^^^^

Fix issue [#116](https://github.com/devsim/devsim/issues/116) where the contact current was being calculated incorrectly in transient mode.



Version 2.6.0
~~~~~~~~~~~~~

Symbolic Factorization Reuse
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Intel MKL solver will now use reuse the symbolic factorization, if the simulation matrix sparse matrix pattern has not changed after the second nonlinear solver iteration.  This reduces simulation time, but can result in numerical differences in the simulation result.  Setting the environment variable, ``DEVSIM_NEW_SYMBOLIC``, will do a new symbolic factorization for each iteration.

This behavior may be controlled by using this option in the :meth:`devsim.solve` command

.. code-block:: none

    solve(symbolic_iteration_limit = -1)

where setting the value to ``-1`` will create a new symbolic factorization for all nonlinear iterations.  Setting the value to a number greater than ``0`` will mark all iterations afterwards for reusing the previous symbolic factorization.

Reset Simulator
^^^^^^^^^^^^^^^

The :meth:`devsim.reset_devsim` command will clear all simulator data, so that a program restart is not necessary.

Build Infrastructure
^^^^^^^^^^^^^^^^^^^^

LAPACK is Optional
""""""""""""""""""

When LAPACK functions are not available, it is now possible to use Eigen instead.  BLAS is still required.  It is up to the direct solver being used to determine necessary LAPACK functions.

Self Contained Build
""""""""""""""""""""

The build infrastructure is being updated to support a small application build on different systems.

SuperLU Solver
""""""""""""""

For self contained builds, some commands are removed and SuperLU is the only available solver.

Citing DEVSIM
^^^^^^^^^^^^^

``CITATION.md`` has been updated with recent articles written about the simulator.

Documentation
^^^^^^^^^^^^^

Fix documentation issue in :ref:`sec__diode1d` where the length of the 1D diode was incorrect.

Fix issue where ``surface_area_model`` was missing from :ref:`parameters__behavior`.

Added table of environment variables controlling program behavior in :ref:`parameters__environment`.

Version 2.5.0
~~~~~~~~~~~~~

UMFPACK 5.1 is the new default when the Intel MKL is not available, making this the default for the macOS arm64 platform.

SuperLU is removed and no longer available as a solver.

Regression scripts were passing when there were numerical differences in the data diff comparison.  This is now corrected and the regression results have been updated on all platforms.

For those building the software, the ``EXPLICIT_MATH_LOAD`` CMAKE option has been removed, so that the software is not directly linked to any math library.

The license text for the Apache 2.0 license has been replaced with the SPDX format of the license string.  This ensures that the text can be used in a consistent manner across all source files.

Version 2.4.0
~~~~~~~~~~~~~

Determine Loaded Math Libraries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To determine the loaded math libraries, use

.. code-block:: none

    devsim.get_parameter(name='info')['math_libraries']

UMFPACK 5.1 Solver
^^^^^^^^^^^^^^^^^^

The ``UMFPACK`` 5.1 solver is now available as a shared library distributed with the software.  It is licensed under the terms of the LGPL 2.1 and our version is hosted here:

[https://github.com/devsim/umfpack_lgpl](https://github.com/devsim/umfpack_lgpl)

Please note that this version uses a scheme to provide the needed math library functions when the library is loaded.

In order to use this library, a shim script is provided to load UMFPACK and set it as the solver.  Please see this example:

.. code-block:: none

    python -mdevsim.umfpack.umfshim ssac_cap.py

Direct Solver Callback
^^^^^^^^^^^^^^^^^^^^^^

It is now possible to setup call a custom direct solver.  The direct solver is called from Python and the callback is implemented by setting these parameters:

.. code-block:: none

    devsim.set_parameter(name="direct_solver", value="custom")
    devsim.set_parameter(name="solver_callback", value=local_solver_callback)

Where the first parameter enables the use of the second parameter to set a callback function.  Please see the ``testing/umfpack_shim.py`` for a sample implementation using UMFPACK 5.1.

Apple M1
^^^^^^^^

On this platform, the software does not check for floating point exceptions (FPEs) during usage of the direct solver.  During testing, it was discovered that FPEs were occuring during factorization for both the ``SuperLU`` and the ``UMFPACK``.  Removing this check allows more of the tests to run through to completion.

Bugs
^^^^

Fix issue [#104](https://github.com/devsim/devsim/issues/104) where the 2D MOSFET example was not fully connected across region interfaces.

.. code-block:: none

    testing/mos_2d.py
    testing/mos_2d_restart.py
    testing/mos_2d_restart2.py

This was resulting in an FPE during testing on macOS M1.

Version 2.3.8
~~~~~~~~~~~~~

Bugs
^^^^

[@ryan3141](https://github.com/ryan3141) fixed an issue where math functions added with :meth:`devsim.register_function` were not available in extended precision model evaluation.  The ``testing/testfunc_extended.py`` test is added to validate the fix.

Update NOTICE with the license files from the various dependencies.

Version 2.3.7
~~~~~~~~~~~~~

Apple M1 Support
^^^^^^^^^^^^^^^^

Intel MKL Pardiso not available, so using system BLAS/LAPACK or openblas by default.  In addition, SuperLU, is used instead of the MKL Pardiso.  This results in some test failures, based on the use of a different solver, and not the OS architecture.

Extended precision is enabled.

Enabled by running pip install.

The regression results are in this newly created repo:

* [devsim_tests_macos_arm64](https://github.com/devsim/devsim_tests_macos_arm64)


Python Notebook Example With 3D Visualization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A plotting example using ``pyvista`` is presented in ``examples/plotting/visualization.ipynb``.  This example was provided by [@simbilod](https://github.com/simbilod).

Bugs
^^^^

When instantiating a mesh from Gmsh, contact and interface related errors to dimensionality have an improved error message.


Version 2.3.6
~~~~~~~~~~~~~

On Windows the ``DEVSIM_MATH_LIBS`` now uses the ``;`` as the path separator, while macOS and Linux still use ``:``.

The math library search order is then:

* The math libraries listed in the ``DEVSIM_MATH_LIBS`` environment variable, with the appropriate separator.
* The Intel Math Kernel Library
* These dynamic libraries
  * OpenBLAS (e.g. libopenblas.so)
  * LAPACK (e.g. liblapack.so)
  * BLAS (e.g. libblas.so)

All platforms will search for the Intel MKL by trying several version numbers.  When the Intel MKL is not available, the direct solver will switch from Intel MKL Pardiso to SuperLU.

On macOS and Linux, the RPATH has been modified to look in places relative to the `devsim` module, instead of using ``CONDA_PREFIX`` or ``VIRTUAL_ENV``.

* ``macOS`` : ``@loader_path;@loader_path/../lib;@loader_path/../../../../lib;@executable_path/../lib``
* ``Linux`` : ``$ORIGIN:$ORIGIN/../lib:$ORIGIN/../../../../lib``



Release 2.3.1
~~~~~~~~~~~~~

Python PIP Package
^^^^^^^^^^^^^^^^^^

DEVSIM is now available via ``pip`` for macOS, Linux, and Microsoft Windows.  To install this package for your platform:

.. code-block:: none

    pip install devsim

Please see the ``INSTALL.md`` file in the distribution for more information.  These files may be found in the ``$CONDA_PREFIX/devsim_data`` directory of your |Anaconda| environment.  If you are using ``venv``, it may be found in the ``$VIRTUAL_ENV/devsim_data`` of your virtual environment.


Remove Windows MSYS Build
^^^^^^^^^^^^^^^^^^^^^^^^^

The ``msys`` build is removed as an available binary package.  Windows is still supported through the use of the Visual C++ compiler build.

Build Notes
^^^^^^^^^^^

The compiler for the Linux build are now upgraded to ``devtoolset-10`` and is now built on ``manylinux2014``.

Boost is now added as a submodule, instead of using system libraries or Anaconda Python versions.  The Linux build no longer requires Anaconda Python.

Release 2.2.0
~~~~~~~~~~~~~

Device and mesh deletion commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :meth:`devsim.delete_device` command makes it possible to delete devices so they will no longer be solved in the simulation.  Any parameters set on the device are also removed from the system.

The :meth:`devsim.delete_mesh` command makes it possible to delete meshes.  Once a mesh has been deleted, it is no longer possible to create devices from it using the :meth:`devsim.create_device` command.


Extended Precision
^^^^^^^^^^^^^^^^^^

Extended precision is now available on Windows builds using the Visual Studio Compiler.  Note that this precision is not as accurate as the float128 type used on other systems.

Direct Solver
^^^^^^^^^^^^^

SuperLU has been updated from version 4.3 to version 5.3.  It is the solver used when the Intel MKL is not available.

Code Quality
^^^^^^^^^^^^

Fixed defects found in Coverity scanning.

Release 2.1.0
~~~~~~~~~~~~~

Explicit math library loading
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since the Intel Math Kernel Library started versioning the names of their dynamic link libraries, it has been difficult to maintain a proper Anaconda Python environment when the version has been updated.  With this release, it is possible to use any recent version of the Intel MKL.  In addition, the user is able to load alternative BLAS/LAPACK math libraries.

Intel MKL
"""""""""

From DEVSIM Version 2.1.0 onward, a specific version is not required when loading the Intel MKL.  If the Intel MKL is not found, the import of the ``devsim`` module will fail, and an error message will be printed.  This method is the default, and should work when using an Anaconda Python environment with the ``mkl`` package installed.

When using a different Python distribution, or having an installation in a different place, it is possible to specify the location by modifying the ``LD_LIBRARY_PATH`` environment variable on |linux|, or using ``DYLD_LIBRARY_PATH`` on |macosx|.  The explicit path may be set to the MKL math libraries may be set using the method in the next section.

Loading other math libraries
""""""""""""""""""""""""""""

It is possible to load alternative implementations of the BLAS/LAPACK used by the software.  The ``DEVSIM_MATH_LIBS`` environment variable may be used to set a ``:`` separated list of libraries.  These names may be based on relative or absolute paths.  The program will load the libraries in order, and stop when all of the necessary math symbols are supplied.  If symbols for the Intel MKL are detected, then the Pardiso direct solver will be enabled.

|linux| example:

.. code-block:: none

  export DEVSIM_MATH_LIBS=libblas.so:liblapack.so

|macosx| example:

.. code-block:: none

  export DEVSIM_MATH_LIBS=libblas.dylib:liblapack.dylib

Direct solver selection
^^^^^^^^^^^^^^^^^^^^^^^

The direct solver may be selected by using the ``direct_solver`` parameter.

.. code-block:: none

  devsim.set_parameter(name='direct_solver', value='mkl_pardiso')

The following options are available:

- ``mkl_pardiso`` Intel MKL Pardiso
- ``superlu`` SuperLU 4.3

The default is ``mkl_pardiso`` when the Intel MKL is loaded.  Otherwise, the default will switch to ``superlu``.

Kahan summation in extended precision mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``kahan3`` and ``kahan4`` functions are now using the Kahan summation algorithm for extended precision model evaluation.  Previously, this algorithm was replaced with 128-bit floating point addition and subtraction in releases that support extended precision mode.  With this change, better than 128-bit floating precision is available when extended precision is enabled.

.. code-block:: none

  devsim.set_parameter(name = "extended_model", value=True)

The ``testing/kahan_float128.py`` test has been added.

Visual Studio 2022
^^^^^^^^^^^^^^^^^^

The Microsoft Windows ``win64`` release version is now built using the Visual Studio 2022 compiler.  For users needing extended precision on the Windows platform, the ``msys`` build is recommended.


Release 2.0.1
~~~~~~~~~~~~~

Update documentation files
^^^^^^^^^^^^^^^^^^^^^^^^^^

The following files were updated in the text documentation distributed with the software.

* ``CONTRIBUTING.md``
* ``INSTALL.md``
* ``README.md``

This was done to create a version to coincide with this paper in the Journal of Open Source Software.

  Sanchez, J. E., (2022). DEVSIM: A TCAD Semiconductor Device Simulator. Journal of Open Source Software, 7(70), 3898, `https://doi.org/10.21105/joss.03898 <https://doi.org/10.21105/joss.03898>`__.

Update MKL Version
^^^^^^^^^^^^^^^^^^

The release version of this software is build against version 2 of the Intel MKL, which corresponds to the latest version of Anaconda Python.

Release 2.0.0
~~~~~~~~~~~~~

New Major Version
^^^^^^^^^^^^^^^^^

Based on the change in the sections :ref:`sec__contact_and_interface_equation_2_0_0` and :ref:`sec__transient_fixes_2_0_0`.  The major version of the software has been updated to 2.  Existing scripts may need to be updated for this change.

.. _sec__contact_and_interface_equation_2_0_0:

Contact and Interface Equation Commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The previously deprecated ``variable_name`` option is no longer accepted by the :meth:`devsim.contact_equation` and :meth:`devsim.interface_equation` commands.  This has been updated in the documentation.


Documentation
^^^^^^^^^^^^^

Manual
""""""

* Fixed unit in description for example in :ref:`sec__cap1d`.
* Added DOI to referenced papers and updated bibliography style in biblography.
* Added reference to :ref:`sec__models` with additional information about element assembly.
* Updated :ref:`sec__models` and :ref:`sec__cap1d` to remove ``variable_name`` option from :meth:`devsim.contact_equation` and :meth:`devsim.interface_equation`.


Documentation Files
"""""""""""""""""""

Some out of date files (e.g. RELEASE, INSTALL, . . .) have been removed.  The ``README.md`` has been updated and the ``INSTALL.md`` has been added.


Python Packages
^^^^^^^^^^^^^^^

The ``rampbias`` function in the ``devsim.python_packages.ramp`` module has been fixed to properly reduce the bias when there is a convergence failure.

|python| 2.7 specific instructions in :ref:`ch__scripting` has been removed.

Solver
^^^^^^


.. _sec__transient_fixes_2_0_0:

Transient Simulation
""""""""""""""""""""

* Fixed bug with ``transient_tr`` (trapezoidal) time integration method in the :meth:`devsim.solve` command where the wrong sign was used to integrate previous time steps.
* Fixed bug in the charge error calculation, which calculates the simulation result with that a forward difference projection.
* Added ``testing/transient_rc.py`` test which compares simulation with analytic result for RC circuit.
* Added :meth:`devsim.set_initial_condition` to set initial transient condition as alternative to using the ``transient_dc`` option to the :meth:`devsim.solve` command.  Suitable options for this command may be provided from the :meth:`get_matrix_and_rhs` command.


Convergence Tests
"""""""""""""""""

The ``maximum_error`` and ``maximum_divergence`` options where added to the :meth:`devsim.solve` command.  If the absolute error of any iteration goes above ``maximum_error``, the simulation stops with a convergence failure.  The ``maximum_divergence`` is the maximum number of iterations that the simulator error may increase before stopping.

Verbosity
"""""""""

During the :meth:`devsim.solve`, circuit node and circuit solution information is no longer printed to the screen for the default verbosity level.  In addition, the number of equations per device and region is no longer displayed at the start of the first iteration.


Intel Math Kernel Library
"""""""""""""""""""""""""

The Intel Math Kernel Library now uses versioned library names.  Binary releases are now updated against the latest versioned dll names from MKL available in the Anaconda Python distribution.


SuperLU
"""""""

The code now supports newer versions of ``SuperLU``.  The release version is still using SuperLU 4.3 for the iterative solution method, and the Intel MKL Pardiso for the direct solve method.

Simulation Matrix
"""""""""""""""""

The :meth:`devsim.get_matrix_and_rhs` command was not properly accepting the ``format`` parameter, and was always returning the same type.


Add Interface supporting Periodic Boundary Conditions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :meth:`devsim.create_interface_from_nodes` command makes it possible to create an interface with non coincident nodes.  This enables the use of periodic boundary conditions.

Build Scripts
^^^^^^^^^^^^^

The build scripts have been updated on all platforms to be less dependent on specific Python 3 versions.

An updated Fedora build script has been added.  It uses the system installed ``SuperLU`` as the direct solver.

Release 1.6.0
~~~~~~~~~~~~~

Array Type Input and Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^

In most circumstances, the software now returns numerical data using the Python ``array`` class.  This is more efficient than using standard lists, as it encapsulates a contiguous block of memory.  More information about this class can be found at `https://docs.python.org/3/library/array.html <https://docs.python.org/3/library/array.html>`__.  The representation can be easily converted to lists and ``numpy`` arrays for efficient manipulation.

When accepting user input involving lists of homogenous data, such as :meth:`devsim.set_node_values` the user may enter data using either a list, string of bytes, or the ``array`` class.  It may also be used to input ``numpy`` arrays or any other class with a ``tobytes`` method.

Get Matrix and RHS for External Use
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :meth:`devsim.get_matrix_and_rhs` command has been added to assemble the static and dynamic matrices, as well as their right hand sides, based on the current state of the device being simulated.  The ``format`` option is used to specify the sparse matrix format, which may be either in the compressed column or compressed row formats, ``csc`` or ``csr``.

Maximum Divergence Count
^^^^^^^^^^^^^^^^^^^^^^^^

If the Newton iteration errors keep increasing for 20 iterations in a row, then the simulator stops.  This limit was previously 5.  This gives a chance for a solution to be found, when there is a poor initial guess.

Mesh Visualization Element Orientation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Elements written to the ``tecplot`` format in 2d and 3d have node orderings compatible with the element connectivity in visualization formats.  Specifying the ``reorder=True`` option in :meth:`devsim.get_element_node_list` will result in node ordering compatible with meshing and visualization software.


Figure annotation
^^^^^^^^^^^^^^^^^

:numref:`edgecell` has been updated, showing the ``EdgeNodeVolume``.


Citation
^^^^^^^^

The :ref:`sec__citation` section has been added with information on how to cite the manual and the simulator.

Documentation License
^^^^^^^^^^^^^^^^^^^^^

The license terms have been changed in :ref:`sec__documentationlicense` so that derivative works are allowed.


Online Forum
^^^^^^^^^^^^

The online forum for discussion about the software has moved to |devsimforum|. This has been updated in :ref:`Contact`.


Release 1.5.1
~~~~~~~~~~~~~~

.. _sec__installation_script:

Installation Script
^^^^^^^^^^^^^^^^^^^

A new installation script is in the base directory of the package.
It provides instructions of completing the installation to the ``python`` environment without having to set the ``PYTHONPATH`` environment variable.
It notifies the user of missing components to finish the installation within an ``Anaconda`` or ``Miniconda`` environment.


To use the script, use the following command inside of the ``devsim`` directory.

.. code-block:: none

    python install.py

The install script will write a file named ``lib/setup.py``, which can be used to complete the installation using ``pip``.  The script provides instructions for the installation and deinstallation of ``devsim``.

.. code-block:: none

    INFO: Writing setup.py
    INFO:
    INFO: Please type the following command to install devsim:
    INFO: pip install -e lib
    INFO:
    INFO: To remove the file, type:
    INFO: pip uninstall devsim

Math Functions Table
^^^^^^^^^^^^^^^^^^^^
The list of available math functions, :numref:`symdiff__functions`, has been reformatted, and parts have been split into the tables referenced in the next few sections.

Error Functions
^^^^^^^^^^^^^^^

The following inverse functions and their derivatives are now available in the model interpreter, and also listed in :numref:`error__functions`.

- ``erf_inv`` Inverse Error Function
- ``erfc_inv`` Inverse Complimentary Error Function
- ``derf_invdx`` Derivative of Inverse Error Function
- ``derfc_invdx`` Derivative of Complimentary Inverse Error Function

Fermi Integral
^^^^^^^^^^^^^^

The Joyce-Dixon approximation :cite:`joycedixon` for the Fermi integral and its inverse are now calculated with extended floating point precision, when extended precision is enabled.  These functions are now listed in :numref:`fermi__functions`.

- ``Fermi`` Fermi integral
- ``dFermidx`` Derivative of Fermi integral
- ``InvFermi`` Inverse Fermi integral
- ``dInvFermidx`` Derivative of inverse Fermi Integral

The following examples are available:

- ``testing/Fermi1.py`` Fermi integral
- ``testing/Fermi1_float128.py`` Fermi integral in extended floating point precision

Gauss-Fermi Integral
^^^^^^^^^^^^^^^^^^^^

The Gauss-Fermi Integral, using Paasch's equations :cite:`paasch:2010` are now available, and are listed in :numref:`gaussfermi__functions`..

- ``gfi`` Gauss-Fermi Integral
- ``dgfidx`` Derivative of Gauss-Fermi Integral
- ``igfi`` Inverse Gauss-Fermi Integral
- ``digfidx`` Derivative of Inverse Gauss-Fermi Integral

Each of these functions take two arguments, ``zeta`` and ``s``.  The derivatives with respect to the first argument are provided.

The following examples are available:

- ``testing/GaussFermi.py`` Gauss-Fermi integral
- ``testing/GaussFermi.py`` Gauss-Fermi integral with extended floating point precision



Release 1.5.0
~~~~~~~~~~~~~~

The :meth:`devsim.custom_equation` command has been modified to require a third return value.  This boolean value denotes whether the matrix entries should be row permutated or not.  For the bulk equations this value should be ``True``.  For interface and contact boundary conditions, this value should be ``False``.  More information is available in :ref:`models__customequation`.

It is now possible to replace an existing ``custom_equation``.

The file ``examples/diode/diode_1d_custom.py`` demonstrates custom matrix assembly and can be directly compared to ``examples/diode/diode_1d.py``.

The ``EdgeNodeVolume`` model is now available for the volume contained by an edge and is referenced in :ref:`models__edgemodel`.

The :meth:`devsim.equation` command has removed support for the ``volume_model`` option.  It has been replaced with:

- ``volume_node0_model``
- ``volume_node1_model``

This makes it possible to better integrate nodal quantities on the volumes of element edges.  For example, a field dependent generation-recombination rate can be volume integrated separately for each node of an element edge.


The :meth:`devsim.contact_equation` now supports the following options:

- ``edge_volume_model``
- ``volume_node0_model``
- ``volume_node1_model``

This makes it possible to integrate edge and element edge quantities with respect to the volume on nodes of the edge at the contact.  This is similar to :meth:`devsim.equation`, described in :ref:`sec__06072015`.


The integration parameters for ``edge_volume_model`` are set with

- ``edge_node0_volume_model`` (default ``EdgeNodeVolume`` :ref:`models__edgemodel` )
- ``edge_node1_volume_model`` (default ``EdgeNodeVolume``)

and for ``volume_model`` with:

- ``element_node0_volume_model`` (default ``ElementNodeVolume`` :ref:`models__elementedge`)
- ``element_node1_volume_model`` (default ``ElementNodeVolume``)

These parameters are applicable to both :meth:`devsim.equation` :meth:`devsim.contact_equation`.


Release 1.4.14
~~~~~~~~~~~~~~

Platforms
^^^^^^^^^

Windows 32 bit is no longer supported.  Binary releases of the ``Visual Studio 2019`` ``MSYS2/Mingw-w64`` 64-bit builds are still available online for |mswindowsten|.

On |linux|, the releases are now on |centosseven|, as |centossix| has reached its end of life on November 30, 2020.

Please see :ref:`sec__supportedplatforms` for more information.

For future development, |cplusplusseventeen| is now the recommended C++ compiler standard.

Release 1.4.13
~~~~~~~~~~~~~~

The node indexes with the maximum error for each equation will be printed when ``debug_level`` is ``verbose``.

.. code-block:: none

  devsim.set_parameter(name="debug_level", value="verbose")

These are printed as ``RelErrorNode`` and ``AbsErrorNode``:

.. code-block:: none

    Region: "gate"	RelError: 5.21531e-14	AbsError: 4.91520e+04
      Equation: "ElectronContinuityEquation"	RelError: 4.91520e-16	AbsError: 4.91520e+04
	RelErrorNode: 129	AbsErrorNode: 129

This information is also returned when using the ``info=True`` option on the :meth:`devsim.solve` command for each equation on each region of a device.

If the ``info`` flag is set to ``True`` on the ``solve`` command, the iteration information will be returned, and an exception for convergence will no longer be thrown.  It is the responsibility of the caller to test the result of the ``solve`` command to see if the simulation converged.  Other types of exceptions, such as floating point errors, will still result in a Python exception that needs to be caught.



Release 1.4.12
~~~~~~~~~~~~~~

Element assembly for calculation of current and charges from the device into the circuit equation are fixed.  These tests are added:

- ``testing/cap_2d_edge.py``
- ``testing/cap_2d_element.py``
- ``testing/cap_3d_edge.py``
- ``testing/cap_3d_element.py``

The ``edge`` variant is using standard edge based assembly, and the ``element`` variant is using element-based assembly.

Release 1.4.11
~~~~~~~~~~~~~~

The :meth:`devsim.element_pair_from_edge_model` command is available to calculate element edge components averaged onto each node of the element edge.  This makes it possible to create an edge weighting scheme different from those used in :meth:`devsim.element_from_edge_model`.  The examples ``examples/diode/laux2d.py`` (2D) and ``examples/diode/laux3d.py`` (3D) compare the built-in implementations of these commands with equivalent implementations written in |python|

Fixed issue where command option names where not always shown in the documentation.

The platform specific notes now clarify that any version of Python 3 (3.6 or higher) is supported.

- ``linux.txt``
- ``windows.txt``
- ``macos.txt``

Release 1.4.10
~~~~~~~~~~~~~~

Fixed crash when evaluating element edge model in 3D.

Fixed potential error using :meth:`devsim.delete_node_model` and similar deletion commands.

Release 1.4.9
~~~~~~~~~~~~~

Support for loading mesh files containing element edge data.

Release 1.4.8
~~~~~~~~~~~~~

In transient mode, the convergence test was flawed so that the ``charge_error`` was the only convergence check required for convergence.  The software now ensures all convergence criteria are met.

Release 1.4.7
~~~~~~~~~~~~~

Models
^^^^^^

In the simple physics models, the sign for time-derivative terms was wrong for the electron and hole continuity equations.  This affects small-signal and noise simulations.  The example at ``examples/diode/ssac_diode.py`` was updated to reflect the change.

Platforms
^^^^^^^^^

Fix build script issue for |macosx| on Travis CI, updated the compiler to ``g++-9``.

Update |centossix| build from ``devtoolset-6`` to ``devtoolset-8``.


Release 1.4.6
~~~~~~~~~~~~~

Version Information
^^^^^^^^^^^^^^^^^^^

Parameter ``info`` can be queried for getting version information.  The file ``testing/info.py`` contains an example.

.. code-block:: none

  python info.py
  {'copyright': 'Copyright © 2009-2020 DEVSIM LLC', 'direct_solver': 'mkl_pardiso', 'extended_precision': True, 'license': 'Apache License, Version 2.0', 'version': '1.4.6', 'website': 'https://devsim.org'}

Extended Precision
^^^^^^^^^^^^^^^^^^

The example ``examples/diode/gmsh_diode3d_float128.py`` provides an example where extended precision is enabled.

Python Formatting
^^^^^^^^^^^^^^^^^

The |python| scripts in the ``examples`` and ``testing`` directories have been reformatted to be more consistent with language standards.

Platforms
^^^^^^^^^

|mswindowsten| is supported and is now compiled using Microsoft Visual Studio 2019.

|mswindowsseven| is no longer supported, as Microsoft has dropped support as of January 14, 2020.

External Meshing
^^^^^^^^^^^^^^^^

Support for reading meshes from |geniusds| has been completely removed from |devsim|.


Release 1.4.5
~~~~~~~~~~~~~

An |msys| build is available for 64-bit |mswindows|.  This build, labeled ``devsim_msys_v1.4.5``, enables the use of the 128-bit floating point precision already available on the |macosx| and |linux| platforms.

Release 1.4.4
~~~~~~~~~~~~~

Bug Fixes
^^^^^^^^^

An intermittent crash on |mswindowsten| was occuring at the end of the program.  It is now fixed.

Documentation
^^^^^^^^^^^^^

A file named ``CHANGES.md`` is now distributed with |devsim|, detailing changes to the program.

Internal changes
^^^^^^^^^^^^^^^^
- Regression system script refactored to Python
- Refactored threading code using |cpluspluseleven| function
- Refactored timing functions for verbose mode using |cpluspluseleven| functions
- Refactored FPE detection code to |cpluspluseleven| standard


Release 1.4.3
~~~~~~~~~~~~~

Fix failures with the following commands:

- :meth:`devsim.delete_edge_model`
- :meth:`devsim.delete_element_model`
- :meth:`devsim.delete_interface_model`
- :meth:`devsim.delete_node_model`

Release 1.4.2
~~~~~~~~~~~~~

In this release there are the following improvements.

* Errors due to floating point exceptions and failed matrix factorization are not fatal.
* The |macosx| release fixes runtime issues with |macosxhighsierra|.
* The provided binary releases utilize more libraries from |anaconda|.

Release 1.4.1
~~~~~~~~~~~~~

Math Functions
^^^^^^^^^^^^^^

The ``cosh``, ``sinh``, ``tanh``, are now available math functions.  Please see :numref:`symdiff__functions`.  In addition, all of the functions in the table, except for Fermi and inverse Fermi functions, are evaluate in extended precision mode.  This mode may be enabled using the parameters discussed in :ref:`release_extended`.

Element Model Memory Leak
^^^^^^^^^^^^^^^^^^^^^^^^^

A large memory leak was occurring during the evaluation of element edge models created with :meth:`devsim.element_from_edge_model`.  It is now fixed and memory usage is now stable when these models are evaluated.

|pythonthree| API Memory Leak
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A small memory leak could occur when :py:mod:`devsim` functions where called, or when data was returned.  These reference counting issues are now fixed.



Release 1.4.0
~~~~~~~~~~~~~

The :meth:`devsim.custom_equation` and :meth:`devsim.register_function` commands take |python| functions, instead of the a string with the function name.

The following commands are available to store data on edges and element edges:

- :meth:`devsim.edge_solution`
- :meth:`devsim.set_edge_values`
- :meth:`devsim.element_solution`
- :meth:`devsim.set_element_values`


Release 1.3.0
~~~~~~~~~~~~~

|pythonthree| Examples
^^^^^^^^^^^^^^^^^^^^^^

All of the |tcl| regression tests in the ``testing`` directory have been converted to |pythonthree|.  These tests serve as examples for features that were previously only tested using |tcl| scripting.

|tcl| Support Deprecated
^^^^^^^^^^^^^^^^^^^^^^^^

|tcl| support is deprecated and will be removed in a future release of the software.

Binary Releases
^^^^^^^^^^^^^^^

Scripting Languages
"""""""""""""""""""

|pythonthree| is now the only scripting language in the releases available from:

|devsimgithubrelease|

Math Library
""""""""""""

The |mswindows| version now uses |intelmklpardiso| for direct matrix factorization.  Both |linux| and |macosx| have been using |intelmklpardiso| since :ref:`release_11012015`.  Binary releases for all operating systems use BLAS/LAPACK routines from |intelmkl|.


Release 1.2.0
~~~~~~~~~~~~~

|devsim| releases have better support for |pythonthree|.  Using the stable ABI, the software is able to run newer |pythonthree| releases, without rebuilding the software.

Support for |pythontwoseven| has been removed.

The banner has been removed when the |devsim| module is imported.

The ``symdiff`` python module is now part of the |devsim| release.  This module has additional features not available using the :meth:`devsim.symdiff` command from |devsim|.  By first setting the ``PYTHONPATH`` variable to the ``lib`` directory in the |devsim| distribution, ``symdiff`` is loaded by using

.. code-block:: python

  import symdiff

Documentation is available in the ``doc`` directory of this distribution.  Examples are available in the ``examples/symdiff`` directory.

Release 1.1.0
~~~~~~~~~~~~~

The Bernoulli function, :math:`B(x)`,

.. math::

  B \left( x \right) = \frac{x}{\mathrm{e}^x - 1}

and its derivative,

.. math::
  dBdx \left( x \right) = \frac{\mathrm{e}^x - 1 - x \mathrm{e}^x}{\left(\mathrm{e}^x - 1\right)^2}

have been refactored.  They are used to calculate electron and hole current densities using the Scharfetter-Gummel method :cite:`sgieeeted1969`.

The Bernoulli function has numerical issues when :math:`x` approaches ``0`` and requires special evaluation.  In this release, |devsim|, takes advantage of |cpluspluseleven| math library functions for evaluating the denominator.

In addition, these functions are evaluated with extended precision, when this mode is enabled in the simulator.  This mode is described in :ref:`release_extended` and controlling parameters are in :ref:`parameters__behavior`.

Users should expect that simulation results should change in the number of solver iterations and small differences in simulation results.  This and other functions are listed in :ref:`symdiff__functions`.

Release 1.0.0
~~~~~~~~~~~~~

Documentation
^^^^^^^^^^^^^

The formatting of the PDF and online documentation has been improved.  Also significant changes have been made to the way |devsim| is called from |python|.

Version
^^^^^^^

Due to the numerous changes in the |python| API, the version number has been updated to having a major revision of ``1``.  We adopt the semantic version numbering presented at https://semver.org.  The version number can be accessed through the |python| interface using the ``devsim.__version__`` variable.

Operating Systems
^^^^^^^^^^^^^^^^^

The |mswindows| 32-bit operating system is now supported in addition to the platforms listed in :ref:`sec__supportedplatforms`.

Python Support
^^^^^^^^^^^^^^

|devsim| is now loaded as a shared library from any compatible Python interpreter.  Previously, |devsim| binaries contained an embedded Python interpreter.  The following versions of Python are supported in this release

- 2.7
- 3.6
- 3.7 

By first setting the ``PYTHONPATH`` variable to the ``lib`` directory in the |devsim| distribution, ``devsim`` is loaded by using

.. code-block:: python

  import devsim

from |python|.  Previous releases of devsim used the ``ds`` module, the manual will be updated to reflect the change in module name.

Many of the examples in the distribution rely on the ``python_packages`` module, which is available by using:

.. code-block:: python

  import devsim.python_packages

The default version of |python| for use in scripts is |pythonthreeseven|. Scripts written for earlier versions of |pythonthree| should work.  |pythontwoseven| is deprecated for future development.


|anaconda| |pythonthreeseven| is the recommended distribution and is available from https://continuum.io.  The |intelmkl| is required for the official |devsim| releases.  These may be installed in |anaconda| using the following command:

.. code-block:: none

  conda install mkl

On the |mswindows| platform, the following packages should also be installed:

.. code-block:: none

  conda install sqlite zlib

Some of the examples and tests also use ``numpy``, which is available using:

.. code-block:: none

  conda install numpy

Please see :ref:`ch__scripting` and :ref:`sec__installation` for more information.

GMSH Support
^^^^^^^^^^^^

|gmsh| has announced a new version of their mesh format ``4.0``.  |devsim| currently supports the previous version, ``2.2``.  To load a file from |gmsh|, it is now necessary to either:

* Save the file in the ``2.2`` format from |gmsh|
* Parse the ``4.0`` file, and then use :ref:`sec__customMeshLoad`

A future release of |devsim| will provide this capability.

CGNS Support
^^^^^^^^^^^^

Support for loading |cgns| files is deprecated, and is no longer part of the official releases.  Please see :ref:`sec__externalmesher` for more information about importing meshes from other tools.

July 20, 2018
~~~~~~~~~~~~~

Documentation
^^^^^^^^^^^^^

The documentation has a new license, which is described in :ref:`sec__copyright`.  The source files are now available for download from: https://github.com/devsim/devsim_documentation.

Python 3 Support
^^^^^^^^^^^^^^^^

Python 3 executable, ``devsim_py3`` is now supplied in addition to standard Python 2 executable, ``devsim``.

Element Information
^^^^^^^^^^^^^^^^^^^

The :meth:`devsim.get_element_node_list` retrieves a list of nodes for every element on a ``region``, ``contact``, or ``interface``.

Interface Boundary Condition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``type=hybrid`` option is now available for the :meth:`devsim.interface_equation` command.  Please see :ref:`sec__interface_equation_assembly` for information about boundary conditions.

Interace Equation Coupling
^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``name0``, and ``name1`` options are now available for the :meth:`devsim.interface_equation` command.  They make it possible to couple dissimilar equation names across regions.

Interface and Contact Surface Area
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Contact surface area is no longer included in ``SurfaceArea`` node model.  It is now placed in ``ContactSurfaceArea``.  These are listed in :numref:`models__node`.

Bug Fixes
^^^^^^^^^

- The :meth:`devsim.interface_equation` command is fixed for ``type=fluxterm`` boundary conditions on the interface.
- The :meth:`devsim.get_material`, and :meth:`devsim.set_material` handle the ``contact`` option.
- Interface equation assembly skips nodes when an interface node is shared with a contact.

.. _release_extended:

Extended Precision
^^^^^^^^^^^^^^^^^^

The following new parameters are available:

- ``extended_solver``, extended precision matrix for Newton and linear solver
- ``extended_model``, extended precision model evaluation
- ``extended_equation``, extended precision equation assembly

When compiled with 128-bit extended precision support, these options enable calculations to be performed with higher precision.  Default geometric models, are also calculated with extended precision.

.. code-block:: python

  devsim.set_parameter(name = "extended_solver", value=True)
  devsim.set_parameter(name = "extended_model", value=True)
  devsim.set_parameter(name = "extended_equation", value=True)

Currently, the |linux| and gcc-based |macosx| versions have extended precision support.

May 15, 2017
~~~~~~~~~~~~

Platforms
^^^^^^^^^

- The |ubuntuxenial| platform is now supported.
- The |ubuntuprecise|, |centosfive| (|redhatfive| compatible) platforms are no longer supported.  These platforms are no longer supported by their vendors.
- |macosx| compiled with ``flat_namespace`` to allow substitution of dynamically linked libraries.
- |mswindowsseven|  is compiled using Microsoft Visual Studio 2017.

Binary Releases
^^^^^^^^^^^^^^^

- Releases available from |devsimgithubrelease|.
- |centossix| released is linked against the |intelmkl|.
- |mswindowsseven| release is linked against the |intelmkl|
- |macosx| can optionally use the |intelmkl|.
- |Anaconda| |pythontwoseven| is the recommended distribution.
- Please see release notes for more information.

Bug Fixes
^^^^^^^^^

* 3D element edge derivatives were not being evaluated correctly
* 3D equation model evaluation for element edge models

Enhancements
^^^^^^^^^^^^

- Build scripts are provided to build on various platforms.
- |devsim| mesh format stores elements, instead of just nodes, for contact and interfaces
- The :meth:`devsim.create_gmsh_mesh` command can be used to create a device from a provided list of elements.

Example Availability
^^^^^^^^^^^^^^^^^^^^

- BJT simulation example available from https://github.com/devsim/devsim_bjt_example.

February 6, 2016
~~~~~~~~~~~~~~~~

|devsim| is now covered by the Apache License, Version 2.0 :cite:`apache2`.  Please see the ``NOTICE`` and ``LICENSE`` file for more information.

November 24, 2015
~~~~~~~~~~~~~~~~~

Python Help
^^^^^^^^^^^

The |python| interpreter now has documentation for each command, derived from the documentation in the manual.  For example, help for the :meth:`devsim.solve` can be found using:

.. code-block:: python

  help("devsim.solve")

Manual Updates
^^^^^^^^^^^^^^

The manual has been updated so that commands are easier to find in the index.  Every command now has a short description.  Cross references have been fixed.  The date has been added to the front page.


.. _release_11012015:

November 1, 2015
~~~~~~~~~~~~~~~~

Convergence Info
^^^^^^^^^^^^^^^^

The :meth:`devsim.solve` now supports the ``info`` option.  The solve command will then return convergence information.

Python Interpreter Changes
^^^^^^^^^^^^^^^^^^^^^^^^^^

The way |devsim| commands are loaded into the ``devsim`` module has been changed.  It is now possible to see the full list of |devsim| commands by typing

.. code-block:: python

  help('devsim')

in the |python| interpreter.

Platform Improvements and Binary Availability
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Many improvements have been made in the way binaries are generated for the |linux|, |macosx|, and |mswindows| platforms.

For |linux| (see ``linux.txt``):

- Create |centosfive|, (|rhelfive| compatible) build
- Build uses |intelmkl| math libraries (community edition)
- Build uses any compatible |pythontwoseven|, including |anaconda|
- Build compatible with newer |linux| distributions.

For |macosx|  (see ``macos.txt``):

- Uses the system |pythontwoseven| on |macosxyosemite|
- Provide instructions to use |anaconda| |python|

For |mswindows| (see ``windows.txt``):

- Uses any compatible |pythontwoseven|, including |anaconda|
- Build uses |intelmklce|

Binary releases are available for these platforms at |devsimorg|.

September 6, 2015
~~~~~~~~~~~~~~~~~

The :meth:`devsim.set_node_values` takes a new option, ``values``.  It is a list containing values to set for all of the nodes in a region.

The following new commands have been added:

- :meth:`devsim.get_equation_list`
- :meth:`devsim.get_contact_equation_list`
- :meth:`devsim.get_interface_equation_list`
- :meth:`devsim.delete_equation`
- :meth:`devsim.delete_contact_equation`
- :meth:`devsim.delete_interface_equation`
- :meth:`devsim.get_equation_command`
- :meth:`devsim.get_contact_equation_command`
- :meth:`devsim.get_interface_equation_command`

August 10, 2015
~~~~~~~~~~~~~~~

The :meth:`devsim.create_contact_from_interface` may be used to create a contact at the location of an interface.  This is useful when contact boundary conditions are needed for a region connected to the interface.

July 16, 2015
~~~~~~~~~~~~~

The :meth:`devsim.set_node_value` was not properly setting the value.  This issue is now resolved.

.. _sec__06072015:

June 7, 2015
~~~~~~~~~~~~

The :meth:`devsim.equation` now suppports the ``edge_volume_model``.  This makes it possible to integrate edge quantities properly so that it is integrated with respect to the volume on nodes of the edge.  To set the node volumes for integration, it is necessary to define a model for the node volumes on both nodes of the edge.  For example:

.. code-block:: python

  devsim.edge_model(device="device", region="region", name="EdgeNodeVolume",
    equation="0.5*EdgeCouple*EdgeLength")
  set_parameter(name="edge_node0_volume_model", value="EdgeNodeVolume")
  set_parameter(name="edge_node1_volume_model", value="EdgeNodeVolume")

For the cylindrical coordinate system in 2D, please see :ref:`sec__cylindrical`.

|macosxyosemite| is now supported.  Regression results in the source distribution are for a 2014 Macbook Pro i7 running this operating system.

October 4, 2014
~~~~~~~~~~~~~~~

Platform Availability
^^^^^^^^^^^^^^^^^^^^^

The software is now supported on the |mswindows|.  Please see :ref:`sec__supportedplatforms` for more information.

December 25, 2013
~~~~~~~~~~~~~~~~~

Binary Availability
^^^^^^^^^^^^^^^^^^^

Binary versions of the |devsim| software are available for download from |devsimsourceforge|.  Current versions available are for

- |macosxyosemite|
- |rhelsix|
- |ubuntuprecise|

Please see :ref:`sec__installation` for more information.

Platforms
^^^^^^^^^

|macosxyosemite| is now supported.  Support for 32 bit is no longer supported on this platform, since the operating system is only released as 64 bit.

Regression data will no longer be maintained in the source code repository for 32 bit versions of |ubuntuprecise| and |rhelsix|.  Building and running on these platforms will still be supported.

Source code improvements
^^^^^^^^^^^^^^^^^^^^^^^^

The source code has been improved to compile on |macosxyosemite| and to comply with |cpluspluseleven| language standards.  Some of the structure of the project has been reorganized.  These changes to the infrastructure will help to keep the program maintainable and useable into the future.

September 8, 2013
~~~~~~~~~~~~~~~~~

Convergence
^^^^^^^^^^^

If the simulation is diverging for 5 or more iterations, the simulation stops.

Bernoulli Function Derivative Evaluation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``dBdx`` math function has been improved to reduce overflow.

Default Edge Model
^^^^^^^^^^^^^^^^^^

The ``edge_index`` is now a default edge models created on a region :numref:`models__edge`.

August 14, 2013
~~~~~~~~~~~~~~~

|symdiff| functions
^^^^^^^^^^^^^^^^^^^

The ``vec_max`` and ``vec_min`` functions have been added to the |symdiff| parser (:numref:`symdiff__functions`).  The ``vec_sum`` function replaces ``sum``.

Default Node Models
^^^^^^^^^^^^^^^^^^^

The ``coordinate_index`` and ``node_index`` are now part of the default node models created on a region (:numref:`models__node`}).

Set Node Value
^^^^^^^^^^^^^^

It is now possible to use the :meth:`devsim.set_node_value` to set a uniform value or indexed value on a node model.

Fix Edge Average Model
^^^^^^^^^^^^^^^^^^^^^^

Fixed issue with :meth:`devsim.edge_average_model` during serialization to the |devsim| format.

July 29, 2013
~~~~~~~~~~~~~

|devsim| is open source
^^^^^^^^^^^^^^^^^^^^^^^

|devsim| is now an open source project and is available from |devsimgithub|.  License information may be found in :ref:`devsim__license`.  If you would like to participate in this project or need support, please contact us using the information in :ref:`Contact`.
Installation instructions may be found in :ref:`sec__installation`.

Build
^^^^^

The |tcl| interpreter version of |devsim| is now called ``devsim_tcl``, and is located in ``/src/main/`` of the build directory.  Please see the ``INSTALL`` file for more information.

Contact Material
^^^^^^^^^^^^^^^^

Contacts now require a material setting (e.g. ``metal``).  This is for informational purposes.  Contact models still look up parameter values based on the region they are located.

External Meshing
^^^^^^^^^^^^^^^^

Please see :ref:`sec__externalmesher` for more information about importing meshes from other tools.

|genius| **Mesh Import**
|devsim| can now read meshes written from |geniusds|.  *Support is no longer available in recent versions releases*.

|gmsh| **Mesh Import**
|devsim| reads version ``2.1`` and ``2.2`` meshes from |gmsh|.  Version ``2.0`` is no longer supported.  Please see :ref:`sec__gmshintro` for more information.

Math Functions
^^^^^^^^^^^^^^

The ``acosh``, ``asinh``, ``atanh``, are now available math functions.  Please see :numref:`symdiff__functions`.

Test directory structure
^^^^^^^^^^^^^^^^^^^^^^^^

Platform specific results are stored in a hierarchical fashion.

