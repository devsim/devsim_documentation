
.. include:: macros.rst

.. _sec__solver:

*******************
Solver and numerics
*******************

Overview
========

|devsim| offers a range of simulation algorithms.

**DC**
The DC operating point analysis is useful for performing steady-state simulation for a different bias conditions.

**AC**
At each DC operating point, a small-signal AC analysis may be performed.  An AC source is provided through a circuit and the response is then simulated.  This is useful for both quasi-static capacitance simulation, as well as RF simulation.

**Noise/Sensitivity**
Noise analysis may be used to evaluate how internal noise sources are observed in the terminal currents of the device or circuit.  Using this method, it is also possible to simulate how the device response changes when device parameters are changed.

**Transient**
|devsim| is able to simulate the nonlinear transient behavior of devices, when the bias conditions change with time.


Solution methods
================

|devsim| uses Newton methods to solve the system of PDE's.  All of the analyses are performed using the :meth:`devsim.solve`.

DC analysis
-----------

A DC analysis is performed using the :meth:`devsim.solve`.

.. code-block:: python

  solve(type="dc", absolute_error=1.0e10, relative_error=1e-7 maximum_iterations=30)

AC analysis
-----------

An AC analysis is performed using the :meth:`devsim.solve`.  A circuit voltage source is required to set the AC source.

Noise and sensitivity analysis
------------------------------

An noise analysis is performed using the :meth:`devsim.solve` command.  A circuit node is specified in order to find its sensitivity to changes in the bulk quantities of each device.  If the circuit node is named ``V1.I``.  A noise simulation is performed using:

.. code-block:: python

  solve(type="noise", frequency=1e5, output_node="V1.I")

Noise and sensitivity analysis is performed using the :meth:`devsim.solve`.  If the equation begin solved is ``PotentialEquation``, the names of the scalar impedance field is then:

- ``V1.I_PotentialEquation_real``
- ``V1.I_PotentialEquation_imag``

and the vector impedance fields evaluated on the nodes are

- ``V1.I_PotentialEquation_real_gradx``
- ``V1.I_PotentialEquation_imag_gradx``
- ``V1.I_PotentialEquation_real_grady`` (2D and 3D)
- ``V1.I_PotentialEquation_imag_grady`` (2D and 3D)
- ``V1.I_PotentialEquation_real_gradz`` (3D only)
- ``V1.I_PotentialEquation_imag_gradz`` (3D only)

Transient analysis
------------------

Transient analysis is performed using the :meth:`devsim.solve`.  |devsim| supports time-integration of the device PDE's.  The three methods are supported are:

- BDF1
- TRBDF
- BDF2


Extended precision
==================

Platform dependence
-------------------

Extended precision is available on all binaries.  For |linux| ``x86_64``, this uses the 128-bit precision available with the ``GCC`` compilers.  On other platforms, ``x64``, ``arm64``, ``aarch64``, the ``cpp_bin_float_quad`` type is used from the |boost| libraries, and is similar to 128-bit precision.

How to control
--------------

The following new parameters are available:

- ``extended_solver``, extended precision matrix for Newton and linear solver
- ``extended_model``, extended precision model evaluation
- ``extended_equation``, extended precision equation assembly

Default geometric models, are also calculated with extended precision.

.. code-block:: python

  devsim.set_parameter(name = "extended_solver", value=True)
  devsim.set_parameter(name = "extended_model", value=True)
  devsim.set_parameter(name = "extended_equation", value=True)

Kahan summation in extended precision mode
------------------------------------------

The ``kahan3`` and ``kahan4`` functions use the Kahan summation algorithm for extended precision model evaluation.  With this change, better than 128-bit floating precision is available when extended precision is enabled.

.. code-block:: none

  devsim.set_parameter(name = "extended_model", value=True)

The ``testing/kahan_float128.py`` script demonstrates this.

Floating point exceptions
=========================

FPE checking during external solve
----------------------------------

On ``arm64`` and ``aarch64`` platforms, the software does not check for floating point exceptions (FPEs) during usage of the direct solver.  During testing, it was discovered that FPEs were occuring during factorization for both the |superlu| and the |umfpack|.  Removing this check allows more of the tests to run through to completion.

Additional Information
----------------------

Please see :ref:`sec_fpe`.


Solver and math library selection
=================================

.. _sec__solver_selection:


Available libraries
-------------------

Intel Math Kernel Library
^^^^^^^^^^^^^^^^^^^^^^^^^

A specific version is not required when loading the |intelmkl|.  This method is the default for ``x64`` and ``x86_64`` systems.  Instructions for installing in a |python| virtual environment are given in :ref:`sec__venv_install`.

.. _sec__umfshim:

|umfpack| solver
^^^^^^^^^^^^^^^^

The |umfpack| solver is now available as a shared library distributed with the software.  It is licensed under the terms of the LGPL 2.1 and our version is hosted here:

`https://github.com/devsim/umfpack_lgpl <https://github.com/devsim/umfpack_lgpl>`__

Please note that this version uses a scheme to detect the BLAS/LAPACK libraries being used by |devsim|, as described in :ref:`sec_blaslapack_selection`.

In order to use this library, a shim script is provided to load |umfpack| and set it as the solver.  Please see this example:

.. code-block:: none

    python -mdevsim.umfpack.umfshim ssac_cap.py

Custom solver
^^^^^^^^^^^^^

Please see :ref:`sec_custom_direct_solver` for more information.

|superlu|
^^^^^^^^^

|superlu| is no longer available as a solver in the binary distributions of |devsim|.  It is available for custom applications, which would require a custom build of the software.


Automatic direct solver selection
---------------------------------

|umfpack| is the default when the |intelmkl| is not available, making this the default for the macOS arm64 platform.

The direct solver may be selected by using the ``direct_solver`` parameter.

.. code-block:: none

  devsim.set_parameter(name='direct_solver', value='mkl_pardiso')

All compatible platforms will search for the |intelmklpardiso|.  The default is ``mkl_pardiso`` when the |intelmkl| is loaded.  The ``umfshim`` described in :ref:`sec__umfshim` uses the ``custom`` option for this parameter to implement calls using the custom solver callback system described in :ref:`sec_custom_direct_solver`.


.. _sec_blaslapack_selection:

BLAS/LAPACK library selection
-----------------------------

Reference versions are available from https://netlib.org.  There are optimized versions available from other vendors.
It is possible to load alternative implementations of the BLAS/LAPACK used by the software.  The ``DEVSIM_MATH_LIBS`` environment variable may be used to set a ``:`` separated list of libraries.  These names may be based on relative or absolute paths.  The program will load the libraries in order, and stop when all of the necessary math symbols are supplied.  If symbols for the |intelmkl| are detected, then the Pardiso direct solver will be enabled.

|linux| example:

.. code-block:: none

  export DEVSIM_MATH_LIBS=libblas.so:liblapack.so

|macosx| example:

.. code-block:: none

  export DEVSIM_MATH_LIBS=libblas.dylib:liblapack.dylib

On Windows the ``DEVSIM_MATH_LIBS`` uses the ``;`` as the path separator, while macOS and Linux still use ``:``.

The math library search order is then:

* The math libraries listed in the ``DEVSIM_MATH_LIBS`` environment variable, with the appropriate separator.
* The Intel Math Kernel Library
* These dynamic libraries
  * OpenBLAS (e.g. libopenblas.so)
  * LAPACK (e.g. liblapack.so)
  * BLAS (e.g. libblas.so)


.. _sec_dllsearchpath:

Default math search path
------------------------

It is recommended to use the full path for all of the math solver libraries.
On macOS and Linux, the RPATH has been modified to look in places relative to the `devsim` module, instead of using ``CONDA_PREFIX`` or ``VIRTUAL_ENV``.

* ``macOS`` : ``@loader_path;@loader_path/../lib;@loader_path/../../../../lib;@executable_path/../lib``
* ``Linux`` : ``$ORIGIN:$ORIGIN/../lib:$ORIGIN/../../../../lib``



.. _sec_infoparam:

Determine loaded math libraries
-------------------------------

To determine the loaded math libraries, use

.. code-block:: none

    devsim.get_parameter(name='info')['math_libraries']

.. _sec_custom_direct_solver:

Custom direct solver
====================

It is call a custom direct solver.  The direct solver is called from |python| and the callback is implemented by setting these parameters:

parameter table

.. code-block:: none

    devsim.set_parameter(name="direct_solver", value="custom")
    devsim.set_parameter(name="solver_callback", value=local_solver_callback)

Where the first parameter enables the use of the second parameter to set a callback function.  Please see the ``testing/umfpack_shim.py`` for a sample implementation using |umfpack|.


Diagnostics
===========

Problem node identification
---------------------------

The node indexes with the maximum error for each equation will be printed when ``debug_level`` is ``verbose``.

.. code-block:: none

  devsim.set_parameter(name="debug_level", value="verbose")

These are printed as ``RelErrorNode`` and ``AbsErrorNode``:

.. code-block:: none

    Region: "gate"	RelError: 5.21531e-14	AbsError: 4.91520e+04
      Equation: "ElectronContinuityEquation"	RelError: 4.91520e-16	AbsError: 4.91520e+04
	RelErrorNode: 129	AbsErrorNode: 129

This information is also returned when using the ``info=True`` option on the :meth:`devsim.solve` command for each equation on each region of a device.

If the ``info`` flag is set to ``True`` on the ``solve`` command, the iteration information will be returned, and an exception for convergence will no longer be thrown.  It is the responsibility of the caller to test the result of the ``solve`` command to see if the simulation converged.  Other types of exceptions, such as floating point errors, will still result in a |python| exception that needs to be caught.


Convergence information
-----------------------

The :meth:`devsim.solve` now supports the ``info`` option.  The solve command will then return convergence information.


.. _sec_new_symbolic:

Symbolic factorization reuse
============================

The |intelmkl| solver will now use reuse the symbolic factorization, if the simulation matrix sparse matrix pattern has not changed after the second nonlinear solver iteration.  This reduces simulation time, but can result in numerical differences in the simulation result.  Setting the environment variable, ``DEVSIM_NEW_SYMBOLIC``, will do a new symbolic factorization for each iteration.

This behavior may be controlled by using this option in the :meth:`devsim.solve` command

.. code-block:: none

    solve(symbolic_iteration_limit = -1)

where setting the value to ``-1`` will create a new symbolic factorization for all nonlinear iterations.  Setting the value to a number greater than ``0`` will mark all iterations afterwards for reusing the previous symbolic factorization.

Notes
=====

Convergence tests
-----------------

The ``maximum_error`` and ``maximum_divergence`` options were added to the :meth:`devsim.solve` command.  If the absolute error of any iteration goes above ``maximum_error``, the simulation stops with a convergence failure.  The ``maximum_divergence`` is the maximum number of iterations that the simulator error may increase before stopping.

Simulation matrix
-----------------

The :meth:`devsim.get_matrix_and_rhs` command was not properly accepting the ``format`` parameter, and was always returning the same type.


Get matrix and rhs for external use
-----------------------------------

The :meth:`devsim.get_matrix_and_rhs` command has been added to assemble the static and dynamic matrices, as well as their right hand sides, based on the current state of the device being simulated.  The ``format`` option is used to specify the sparse matrix format, which may be either in the compressed column or compressed row formats, ``csc`` or ``csr``.

Transient analysis
------------------

:meth:`devsim.set_initial_condition` to set initial transient condition as alternative to using the ``transient_dc`` option to the :meth:`devsim.solve` command.  Suitable options for this command may be provided from the :meth:`get_matrix_and_rhs` command.



