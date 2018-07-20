
Command Reference
-----------------

.. _CircuitCommands:

Circuit Commands
~~~~~~~~~~~~~~~~

Commands are for adding circuit elements to the simulation.


.. automodule:: ds
   :members: add_circuit_node, circuit_alter, circuit_element, circuit_node_alias, get_circuit_equation_number, get_circuit_node_list, get_circuit_node_value, get_circuit_solution_list, set_circuit_node_value


.. _EquationCommands:

Equation Commands
~~~~~~~~~~~~~~~~~

Commands for manipulating equations on contacts, interface, and regions


.. automodule:: ds
   :members: contact_equation, custom_equation, delete_contact_equation, delete_equation, delete_interface_equation, equation, get_contact_equation_command, get_contact_equation_list, get_equation_command, get_equation_list, get_equation_numbers, get_interface_equation_command, get_interface_equation_list, interface_equation


.. _GeometryCommands:

Geometry Commands
~~~~~~~~~~~~~~~~~

Commands for getting information about the device structure.


.. automodule:: ds
   :members: get_contact_list, get_device_list, get_element_node_list, get_interface_list, get_region_list


.. _MaterialCommands:

Material Commands
~~~~~~~~~~~~~~~~~

Commands for manipulating parameters and material properties


.. automodule:: ds
   :members: add_db_entry, close_db, create_db, get_db_entry, get_dimension, get_material, get_parameter, get_parameter_list, open_db, save_db, set_material, set_parameter


.. _MeshingCommands:

Meshing Commands
~~~~~~~~~~~~~~~~

Commands for reading and writing meshes


.. automodule:: ds
   :members: add_1d_contact, add_1d_interface, add_1d_mesh_line, add_1d_region, add_2d_contact, add_2d_interface, add_2d_mesh_line, add_2d_region, add_genius_contact, add_genius_interface, add_genius_region, add_gmsh_contact, add_gmsh_interface, add_gmsh_region, create_1d_mesh, create_2d_mesh, create_contact_from_interface, create_device, create_genius_mesh, create_gmsh_mesh, finalize_mesh, load_devices, write_devices


.. _ModelCommands:

Model Commands
~~~~~~~~~~~~~~

Commands for defining and evaluating models


.. automodule:: ds
   :members: contact_edge_model, contact_node_model, cylindrical_edge_couple, cylindrical_node_volume, cylindrical_surface_area, debug_triangle_models, delete_edge_model, delete_element_model, delete_interface_model, delete_node_model, edge_average_model, edge_from_node_model, edge_model, element_from_edge_model, element_from_node_model, element_model, get_edge_model_list, get_edge_model_values, get_element_model_list, get_element_model_values, get_interface_model_list, get_interface_model_values, get_node_model_list, get_node_model_values, interface_model, interface_normal_model, node_model, node_solution, print_edge_values, print_element_values, print_node_values, register_function, set_node_value, set_node_values, symdiff, vector_element_model, vector_gradient


.. _SolverCommands:

Solver Commands
~~~~~~~~~~~~~~~

Commands for simulation


.. automodule:: ds
   :members: get_contact_charge, get_contact_current, solve

