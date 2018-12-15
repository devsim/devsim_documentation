.. include:: macros.txt

.. _ch__modelparameters:

Parameters
----------

Parameters can be set using the commands in :ref:`MaterialCommands`.  There are two complementary formalisms for doing this.

Parameters
~~~~~~~~~~


Parameters are set globally, on devices, or on regions of a device.  The models on each device region are automatically updated whenever parameters change.

.. code-block:: python

  devsim.set_parameter(device="device", region="region",
    name="ThermalVoltage", value=0.0259)


They may also be used to control program behavior, as listed in :numref:`parameters__behavior`:

.. TODO: break up into multiple tables

.. _parameters__behavior:

.. csv-table:: Parameters controlling program behavior.
  :header: "Parameter", "Description"
  :widths: 20, 20

  "``debug_level``", "``info``, ``verbose`` :numref:`python__verbosity`"
  "``threads_available``", "``value=1``, :numref:`python__parallelization`"
  "``threads_task_size``", "``value=?``, :numref:`python__parallelization`"
  "``node_volume_model``", ":numref:`sec__cylindrical`"
  "``edge_couple_model``", ":numref:`sec__cylindrical`"
  "``edge_node0_volume_model``", ":numref:`sec__cylindrical`"
  "``edge_node1_volume_model``", ":numref:`sec__cylindrical`"
  "``element_edge_couple_model``", ":numref:`sec__cylindrical`"
  "``element_node0_volume_model``", ":numref:`sec__cylindrical`"
  "``element_node1_volume_model``", ":numref:`sec__cylindrical`"
  "``extended_solver``", "``value=False`` Extended precision matrix and RHS assembly and error evaluations.  Linear solver and circuit assembly is still double precision``"
  "``extended_model``",  "``value=False`` Extended precision model evaluation"
  "``extended_equation``", "``value=False`` Extended precision equation evaluation"


Material database entries
~~~~~~~~~~~~~~~~~~~~~~~~~

Alternatively, parameters may be set based on material types.  A database file is used for getting values on the regions of the device.

.. code-block:: python

  devsim.create_db(filename="foodb")
  devsim.add_db_entry(material="global", parameter="q", value=1.60217646e-19,
    unit="coul", description="Electron Charge")
  devsim.add_db_entry(material="Si", parameter="one",
    value=1, unit="", description="")
  devsim.close_db

When a database entry is not available for a specific material, the parameter will be looked up on the ``global`` material entry.

Discussion
~~~~~~~~~~

Both parameters and material database entries may be used in model expressions.  Parameters have precedence in this situation.  If a parameter is not found, then |devsim| will also look for a circuit node by the name used in the model expression.


