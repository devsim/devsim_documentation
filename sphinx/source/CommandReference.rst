
Command Reference
-----------------

.. automodule:: devsim
   :no-members:

.. _CircuitCommands:

Circuit Commands
~~~~~~~~~~~~~~~~

Commands are for adding circuit elements to the simulation.


.. currentmodule:: devsim
.. autofunction:: add_circuit_node
.. autofunction:: circuit_alter
.. autofunction:: circuit_element
.. autofunction:: circuit_node_alias
.. autofunction:: get_circuit_equation_number
.. autofunction:: get_circuit_node_list
.. autofunction:: get_circuit_node_value
.. autofunction:: get_circuit_solution_list
.. autofunction:: set_circuit_node_value



.. _EquationCommands:

Equation Commands
~~~~~~~~~~~~~~~~~

Commands for manipulating equations on contacts, interface, and regions


.. currentmodule:: devsim
.. autofunction:: contact_equation
.. autofunction:: custom_equation
.. autofunction:: delete_contact_equation
.. autofunction:: delete_equation
.. autofunction:: delete_interface_equation
.. autofunction:: equation
.. autofunction:: get_contact_equation_command
.. autofunction:: get_contact_equation_list
.. autofunction:: get_equation_command
.. autofunction:: get_equation_list
.. autofunction:: get_equation_numbers
.. autofunction:: get_interface_equation_command
.. autofunction:: get_interface_equation_list
.. autofunction:: interface_equation



.. _GeometryCommands:

Geometry Commands
~~~~~~~~~~~~~~~~~

Commands for getting information about the device structure.


.. currentmodule:: devsim
.. autofunction:: get_contact_list
.. autofunction:: get_device_list
.. autofunction:: get_element_node_list
.. autofunction:: get_interface_list
.. autofunction:: get_region_list



.. _MaterialCommands:

Material Commands
~~~~~~~~~~~~~~~~~

Commands for manipulating parameters and material properties


.. currentmodule:: devsim
.. autofunction:: add_db_entry
.. autofunction:: close_db
.. autofunction:: create_db
.. autofunction:: get_db_entry
.. autofunction:: get_dimension
.. autofunction:: get_material
.. autofunction:: get_parameter
.. autofunction:: get_parameter_list
.. autofunction:: open_db
.. autofunction:: save_db
.. autofunction:: set_material
.. autofunction:: set_parameter



.. _MeshingCommands:

Meshing Commands
~~~~~~~~~~~~~~~~

Commands for reading and writing meshes


.. currentmodule:: devsim
.. autofunction:: add_1d_contact
.. autofunction:: add_1d_interface
.. autofunction:: add_1d_mesh_line
.. autofunction:: add_1d_region
.. autofunction:: add_2d_contact
.. autofunction:: add_2d_interface
.. autofunction:: add_2d_mesh_line
.. autofunction:: add_2d_region
.. autofunction:: add_gmsh_contact
.. autofunction:: add_gmsh_interface
.. autofunction:: add_gmsh_region
.. autofunction:: create_1d_mesh
.. autofunction:: create_2d_mesh
.. autofunction:: create_contact_from_interface
.. autofunction:: create_device
.. autofunction:: create_gmsh_mesh
.. autofunction:: finalize_mesh
.. autofunction:: load_devices
.. autofunction:: write_devices



.. _ModelCommands:

Model Commands
~~~~~~~~~~~~~~

Commands for defining and evaluating models


.. currentmodule:: devsim
.. autofunction:: contact_edge_model
.. autofunction:: contact_node_model
.. autofunction:: cylindrical_edge_couple
.. autofunction:: cylindrical_node_volume
.. autofunction:: cylindrical_surface_area
.. autofunction:: debug_triangle_models
.. autofunction:: delete_edge_model
.. autofunction:: delete_element_model
.. autofunction:: delete_interface_model
.. autofunction:: delete_node_model
.. autofunction:: edge_average_model
.. autofunction:: edge_from_node_model
.. autofunction:: edge_model
.. autofunction:: edge_solution
.. autofunction:: element_from_edge_model
.. autofunction:: element_from_node_model
.. autofunction:: element_model
.. autofunction:: element_pair_from_edge_model
.. autofunction:: element_solution
.. autofunction:: get_edge_model_list
.. autofunction:: get_edge_model_values
.. autofunction:: get_element_model_list
.. autofunction:: get_element_model_values
.. autofunction:: get_interface_model_list
.. autofunction:: get_interface_model_values
.. autofunction:: get_node_model_list
.. autofunction:: get_node_model_values
.. autofunction:: interface_model
.. autofunction:: interface_normal_model
.. autofunction:: node_model
.. autofunction:: node_solution
.. autofunction:: print_edge_values
.. autofunction:: print_element_values
.. autofunction:: print_node_values
.. autofunction:: register_function
.. autofunction:: set_edge_values
.. autofunction:: set_element_values
.. autofunction:: set_node_value
.. autofunction:: set_node_values
.. autofunction:: symdiff
.. autofunction:: vector_element_model
.. autofunction:: vector_gradient



.. _SolverCommands:

Solver Commands
~~~~~~~~~~~~~~~

Commands for simulation


.. currentmodule:: devsim
.. autofunction:: get_contact_charge
.. autofunction:: get_contact_current
.. autofunction:: get_matrix_and_rhs
.. autofunction:: solve


