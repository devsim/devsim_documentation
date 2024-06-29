.. include:: macros.rst

.. _ch__modelparameters:

**********
Parameters
**********


Parameters
==========


Parameters are set globally, on devices, or on regions of a device.  The models on each device region are automatically updated whenever parameters change.

.. code-block:: python

  devsim.set_parameter(device="device", region="region",
    name="ThermalVoltage", value=0.0259)


They may also be used to control program behavior, as listed in :ref:`parameters__behavior`:

.. _parameters__behavior:

.. csv-table:: Parameters controlling program behavior
  :header: "Parameter", "Description"
  :widths: 20, 20

  "``debug_level``", "``info``, ``verbose`` :ref:`python__verbosity`"
  "``edge_couple_model``", ":ref:`sec__cylindrical`"
  "``edge_node0_volume_model``", ":ref:`sec__cylindrical`"
  "``edge_node1_volume_model``", ":ref:`sec__cylindrical`"
  "``element_edge_couple_model``", ":ref:`sec__cylindrical`"
  "``element_node0_volume_model``", ":ref:`sec__cylindrical`"
  "``element_node1_volume_model``", ":ref:`sec__cylindrical`"
  "``extended_equation``", "``value=False`` Extended precision equation evaluation"
  "``extended_model``",  "``value=False`` Extended precision model evaluation"
  "``extended_solver``", "``value=False`` Extended precision matrix and RHS assembly and error evaluations.  Linear solver and circuit assembly is still double precision``"
  "``info``", ":ref:`sec_infoparam`"
  "``node_volume_model``", ":ref:`sec__cylindrical`"
  "``solver_callback``", ":ref:`sec_custom_direct_solver`"
  "``surface_area_model``", "Model for integration of flux and hybrid interfaces."
  "``threads_available``", "``value=1``, :ref:`python__parallelization`"
  "``threads_task_size``", "``value=?``, :ref:`python__parallelization`"

Environment variables
=====================

Environment variables to control program behavior are listed in :ref:`parameters__environment`:.  Please consult :ref:`release_notes`: for the most up to information concerning their usage.

.. _parameters__environment:

.. csv-table:: Environment controlling program behavior
  :header: "Environment Variable", "Description"
  :widths: 20, 20

  "``DEVSIM_MATH_LIBS``", "List of BLAS/LAPACK libraries to load instead of system defaults"
  "``DEVSIM_NEW_SYMBOLIC``", "When set, do a new symbolic matrix factorization during direct solve iterations, :ref:`sec_new_symbolic`"
  "``CONDA_PREFIX``", "For Anaconda |python| installations, this is the location of the ``devsim_data`` directory."
  "``VIRTUAL_ENV``", "For ``pip``-based |python| installations, this is the location of the ``devsim_data`` directory."

Notes
=====

Parameters may be used in model expressions.  If a parameter is not found, then |devsim| will also look for a circuit node by the name used in the model expression.


