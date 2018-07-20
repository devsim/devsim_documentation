
.. _ch__circuits:

Circuits
--------

Circuit elements
~~~~~~~~~~~~~~~~

Circuit elements are manipulated using the commands in :ref:`CircuitCommands`.  Using the :meth:`ds.circuit_element` to add a circuit element will implicitly create the nodes being references.

A simple resistor divider with a voltage source would be specified as:

.. code-block:: python

  ds.circuit_element(name="V1", n1="1", n2="0", value=1.0)
  ds.circuit_element(name="R1", n1="1", n2="2", value=5.0)
  ds.circuit_element(name="R2", n1="2", n2="0", value=5.0)

Circuit nodes are created automatically when referred to by these commands.  Voltage sources create an additional circuit node of the form ``V1.I`` to account for the current flowing through it.

Connecting devices
~~~~~~~~~~~~~~~~~~

For devices to contribute current to an external circuit, the :meth:`ds.contact_equation` should use the ``circuitnode`` option to specify the circuit node in which to integrate its current.  This option does not create a node in the circuit.  No circuit boundary condition for the contact equation will exist if the circuit node does not actually exist in the circuit.  The :meth:`ds.circuit_node_alias` may be used to associate the name specified on the contact equation to an existing circuit node on the circuit.

The circuit node names may be used in any model expression on the regions and interfaces.  However, the simulator will only take derivatives with respect to circuit nodes names on models used to compose the contact equation.

