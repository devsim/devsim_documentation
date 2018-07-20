.. include:: macros.txt

.. _ch__modelparameters:

Model Parameters
----------------

Parameters can be set using the commands in :ref:`MaterialCommands`.  There are two complementary formalisms for doing this.

Parameters
~~~~~~~~~~

Parameters are set globally, on devices, or on regions of a device.  The models on each device region are automatically updated whenever parameters change.

.. code-block:: python

  ds.set_parameter(device="device", region="region",
    name="ThermalVoltage", value=0.0259)

Material database entries
~~~~~~~~~~~~~~~~~~~~~~~~~

Alternatively, parameters may be set based on material types.  A database file is used for getting values on the regions of the device.

.. code-block:: python

  ds.create_db(filename="foodb")
  ds.add_db_entry(material="global", parameter="q", value=1.60217646e-19,
    unit="coul", description="Electron Charge")
  ds.add_db_entry(material="Si", parameter="one",
    value=1, unit="", description="")
  ds.close_db

When a database entry is not available for a specific material, the parameter will be looked up on the ``global`` material entry.

Discussion
~~~~~~~~~~

Both parameters and material database entries may be used in model expressions.  Parameters have precedence in this situation.  If a parameter is not found, then |devsim| will also look for a circuit node by the name used in the model expression.


