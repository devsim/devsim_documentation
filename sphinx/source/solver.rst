
.. include:: macros.txt

.. _sec__solver:

Solver
------

Solver
~~~~~~

|devsim| uses Newton methods to solve the system of PDE's.  All of the analyses are performed using the :meth:`ds.solve`.

DC analysis
~~~~~~~~~~~

A DC analysis is performed using the :meth:`ds.solve`.

.. code-block:: python

  solve(type="dc", absolute_error=1.0e10, relative_error=1e-7 maximum_iterations=30)

AC analysis
~~~~~~~~~~~

An AC analysis is performed using the :meth:`ds.solve`.  A circuit voltage source is required to set the AC source.

Noise/Sensitivity analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~

An noise analysis is performed using the :meth:`ds.solve` command.  A circuit node is specified in order to find its sensitivity to changes in the bulk quantities of each device.  If the circuit node is named ``V1.I``.  A noise simulation is performed using:

.. code-block:: python

  solve(type="noise", frequency=1e5, output_node="V1.I")

Noise and sensitivity analysis is performed using the :meth:`ds.solve`.  If the equation begin solved is ``PotentialEquation``, the names of the scalar impedance field is then:

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
~~~~~~~~~~~~~~~~~~

Transient analysis is performed using the :meth:`ds.solve`.  |devsim| supports time-integration of the device PDE's.  The three methods are supported are:

- BDF1
- TRBDF
- BDF2

