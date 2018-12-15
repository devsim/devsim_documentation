
.. include:: macros.txt

Release Notes
-------------

Introduction
~~~~~~~~~~~~

|devsim| download and installation instructions are located in :ref:`sec__installation`.  The following sections list bug fixes and enhancements over time.  Contact information is listed in :ref:`Contact`.

|release| (December 16, 2018)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Extended Precision
^^^^^^^^^^^^^^^^^^

The following new parameters are available:

- ``extended_solver``, extended precision matrix for Newton and linear Solver
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
|devsim| can now read meshes written from |geniusds|.  More information about |genius| is in :ref:`sec__geniusintro`.

|gmsh| **Mesh Import**
|devsim| reads version ``2.1`` and ``2.2`` meshes from |gmsh|.  Version ``2.0`` is no longer supported.  Please see :ref:`sec__gmshintro` for more information.

Math Functions
^^^^^^^^^^^^^^

The ``acosh``, ``asinh``, ``atanh``, are now available math functions.  Please see :numref:`symdiff__functions`.

Test directory structure
^^^^^^^^^^^^^^^^^^^^^^^^

Platform specific results are stored in a hierarchical fashion.

