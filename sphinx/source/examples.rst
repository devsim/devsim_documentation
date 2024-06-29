.. include:: macros.rst

.. _ch__examples:

********
Examples
********


Included examples
=================

The following example directories are contained in the distribution.  Some of them are described in :ref:`ch__examples_short`.

.. list-table:: Examples Distributed with |devsim|
   :header-rows: 1
   :widths: 30 70

   * - Directory
     - Description
   * - ``capacitance``
     - These are 1D and 2D capacitor simulations, using the internal mesher.  A description of these examples is presented in :ref:`ch__capacitance`.
   * - ``diode``
     - This is a collection of 1D, 2D, and 3D diode structures using the internal mesher, as well as |gmsh|.  These examples are discussed in :ref:`ch__diode`.
   * - ``bioapp1``
     - This is a biosensor application.
   * - ``vector_potential``
     - This is a 2D magnetic field simulation solving for the magnetic potential.  The simulation script is ``vector_potential/twowire.py``  A simulation result for two wires conducting current is shown in :numref:`twowireresult`.
   * - ``mobility``
     - This is an advanced example using electric field dependendent mobility models.
   * - ``plotting``
     - Example using a |python| notebook.  There is 3D visualization using ``pyvista``.

.. _twowireresult:

.. figure:: twowire.*
    :align: center

    Simulation result for solving for the magnetic potential and field.  The coloring is by the Z component of the magnetic potential, and the stream traces are for components of magnetic field.

Test scripts
============

The scripts in the ``testing`` and ``examples`` directories are used for the regression tests whose platform dependent results are kept in the repositories listed in :ref:`sec__regressions`.

Some of them demonstrate the use  of different features of the simulator.

* Extended precision

   ``examples/diode/gmsh_diode3d_float128.py``

* Version and Solver Information

   Parameter ``info`` can be queried for getting version information.  The file ``testing/info.py`` contains an example.

* Small signal simulation

   ``examples/diode/ssac_diode.py``

* Custom Matrix Assembly

   ``examples/diode/diode_1d_custom.py`` demonstrates custom matrix assembly and can be directly compared to ``examples/diode/diode_1d.py``.

* Custom External Meshing

   ``testing/pythonmesh1d.py`` demonstrates how to create a mesh via script, and how to get mesh information using :meth:`devsim.get_element_node_list`.

* Transient Simulation

   * ``examples/diode/tran_diode.py`` demonstrates transient diode simulation.

   * ``testing/transient_rc.py`` test which compares simulation with analytic result for RC circuit.

* Fermi and Gauss-Fermi Statistics

   * ``testing/Fermi1.py`` Fermi integral
   * ``testing/Fermi1_float128.py`` Fermi integral in extended floating point precision
   * ``testing/GaussFermi.py`` Gauss-Fermi integral
   * ``testing/GaussFermi.py`` Gauss-Fermi integral with extended floating point precision


Related projects
================


Source code
-----------

* `devsim <https://github.com/devsim/devsim>`__

   The simulator

* `devsim_documentation <https://github.com/devsim/devsim_documentation>`__

   Documentation for the project

* `umfpack_lgpl <https://github.com/devsim/umfpack_lgpl>`__

   Fork of |umfpack|

Examples
--------

* `devsim_bjt_example <https://github.com/devsim/devsim_bjt_example>`__

    BJT Example.

* `devsim_3dmos <https://github.com/devsim/devsim_3dmos>`__

    Simulation files use in publication.  Processes mesh generated with ``Cubit``.

* `devsim_misc <https://github.com/devsim/devsim_misc>`__

    Miscellaneous Documentation Files.  Contains mesh refinement scripts and |gmsh| processing.

* `devsim_density_gradient <https://github.com/devsim/devsim_density_gradient>`__

    Density Gradient Simulation

.. _sec__regressions:

Regression results
------------------

* `devsim_tests_linux_aarch64 <https://github.com/devsim/devsim_tests_linux_aarch64>`__

    Linux ``arm64``

* `devsim_tests_linux_x86_64 <https://github.com/devsim/devsim_tests_linux_x86_64>`__

    Linux ``x86_64``

* `devsim_tests_macos_arm64 <https://github.com/devsim/devsim_tests_macos_arm64>`__

    macOS ``arm64``

* `devsim_tests_win64 <https://github.com/devsim/devsim_tests_win64>`__

    Windows ``x64``

Mobile app
==========

- https://tcadapp


.. _sec__thirdparty:

Third party libraries
=====================

- `Eigen <https://gitlab.com/libeigen/eigen.git>`__
- `Boost multiprecision <https://github.com/boostorg/multiprecision>`__
- `Boost math <https://github.com/boostorg/math>`__
- `|superlu| <https://github.com/xiaoyeli/superlu>`__

