
.. include:: macros.txt

Release Notes
-------------

Introduction
~~~~~~~~~~~~

|devsim| download and installation instructions are located in :ref:`sec__installation`.  The following sections list bug fixes and enhancements over time.  Contact information is listed in :ref:`Contact`.

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

Elements written to the ``tecplot`` format in 2d and 3d have node orderings compatible with the element connectivity in visualization formats.  Specifying the ``reorder=True`` option in :meth:`get_element_node_list` will result in node ordering compatible with meshing and visualization software.


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

On Linux, the releases are now on |centosseven|, as |centossix| has reached its end of life on November 30, 2020.

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

