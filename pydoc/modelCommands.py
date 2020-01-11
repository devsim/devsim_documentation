from commandCommon import *

Command = {
    "name" : "Model",
  "description" : "Commands for defining and evaluating models",
  "commands" : (
      {
          "name" : "contact_edge_model",
          "description" : "Create an edge model evaluated at a contact",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("contact", contact_option_text, required, string, None, None),
              ("name", name_option("contact edge model", "created"), required, string, None, None),
              ("equation", equation_option("contact edge model being created"), required, string, None, None),
              ("display_type", "Option for output display in graphical viewer", optional, option, "vector", (
                  ("nodisplay", "Data on edge will not be displayed"),
                  ("scalar", "Data on edge is a scalar quantity"),
                  ("vector", "Data on edge is a vector quantity"),
              )
              ),
          )
      },
      {
          "name" : "contact_node_model",
          "description" : "Create an node model evaluated at a contact",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("contact", contact_option_text, required, string, None, None),
              ("name", name_option("contact node model", "created"), required, string, None, None),
              ("equation", equation_option("contact node model being created"), required, string, None, None),
              ("display_type", "Option for output display in graphical viewer", optional, option, "scalar", (
                  ("nodisplay", "Data on edge will not be displayed"),
                  ("scalar", "Data on edge is a scalar quantity"),
              )
              )
          ),
      },

      {
          "name" : "cylindrical_edge_couple",
          "description" : "This command creates the ``EdgeCouple`` model for 2D cylindrical simulation",
          "long_description" : r'''
This model is only available in 2D.  The created variables are

- ``ElementCylindricalEdgeCouple`` (Element Edge Model)
- ``CylindricalEdgeCouple`` (Edge Model)

The :meth:`devsim.set_parameter` must be used to set

- ``raxis_variable``, the variable (``x`` or ``y``) which is the radial axis variable in the cylindrical coordinate system
- ``raxis_zero``, the location of the z axis for the radial axis variable
''',
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
          )
      },
      {
          "name" : "cylindrical_node_volume",
          "description" : "This command creates the ``NodeVolume`` model for 2D cylindrical simulation",
          "long_description" : r'''
This model is only available in 2D.  The created variables are

- ``ElementCylindricalNodeVolume@en0`` (Element Edge Model)
- ``ElementCylindricalNodeVolume@en1`` (Element Edge Model)
- ``CylindricalEdgeNodeVolume@n0`` (Edge Model)
- ``CylindricalEdgeNodeVolume@n1`` (Edge Model)
- ``CylindricalNodeVolume`` (Node Model)

The ``ElementCylindricalNodeVolume@en0`` and ``ElementCylindricalNodeVolume@en1`` represent the node volume at each end of the element edge.

The :meth:`devsim.set_parameter` must be used to set

- ``raxis_variable``, the variable (``x`` or ``y``) which is the radial axis variable in the cylindrical coordinate system
- ``raxis_zero``, the location of the z axis for the radial axis variable

''',
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
          )
      },
      {
          "name" : "cylindrical_surface_area",
          "description" : "This command creates the ``SurfaceArea`` model for 2D cylindrical simulation",
          "long_description" : r'''
This model is only available in 2D.  The created variables are

- ``CylindricalSurfaceArea`` (Node Model)

and is the cylindrical surface area along each contact and interface node in the device region.

The :meth:`devsim.set_parameter` must be used to set

- ``raxis_variable``, the variable (``x`` or ``y``) which is the radial axis variable in the cylindrical coordinate system
- ``raxis_zero``, the location of the z axis for the radial axis variable

''',
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
          )

      },
      {
          "name" : "delete_edge_model",
          "description" : "Deletes an edge model from a region",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("name", name_option("edge model", "deleted"), required, string, None, None),
          )
      },
      {
          "name" : "delete_interface_model",
          "description" : "Deletes an interface model from an interface",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("interface", interface_option_text, required, string, None, None),
              ("name", name_option("interface model", "deleted"), required, string, None, None),
          )
      },

      {
          "name" : "delete_node_model",
          "description" : "Deletes a node model from a region",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("name", name_option("node model", "deleted"), required, string, None, None),
          )
      },
      {
          "name" : "delete_element_model",
          "description" : "Deletes a element model from a region",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("name", name_option("node model", "deleted"), required, string, None, None),
          )
      },
      {
          "name" : "edge_average_model",
          "description" : "Creates an edge model based on the node model values", 
          "long_description" : r'''
For a node model, creates 2 edge models referring to the node model value at both ends of the edge.  For example, to calculate electric field:

..

  devsim.edge_average_model(device=device, region=region, node_model="Potential", edge_model="ElecticField", average_type="negative_gradient")

and the derivatives ``ElectricField:Potential@n0`` and ``ElectricField:Potential@n1`` are then created from

..

  devsim.edge_average_model(device=device, region=region, node_model="Potential", edge_model="ElecticField", average_type="negative_gradient", derivative="Potential")
''',
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("node_model", "The node model from which we are creating the edge model.  If ``derivative`` is specified, the edge model is created from ``nodeModel:derivativeModel``", required, string, None, None),
              ("edge_model", "The edge model name being created.  If ``derivative`` is specified, the edge models created are ``edgeModel:derivativeModel@n0`` ``edgeModel:derivativeModel@n1``, which are the derivatives with respect to the derivative model on each side of the edge", required, string, None, None),
              ("derivative", "The node model of the variable for which the derivative is being taken.  The node model ``nodeModel:derivativeModel`` is used to create the resulting edge models.", optional, string, None, None),
              ("average_type", "The node models on both sides of the edge are averaged together to create one of the following types of averages.", optional, string, "arithmetic", (
                  ("arithmetic", "The edge model is the average of the node model on both sides"),
                  ("geometric", "The edge model is the square root of the product of the node model evaluated on each side"),
                  ("gradient", "The edge model is the gradient along the edge with respect to the distance between the two nodes."),
                  ("negative_gradient", "The edge model is the negative of the gradient along the edge"),
              )
              ),
          )
      },
      {
          "name" : "edge_from_node_model",
          "description" : "For a node model, creates an 2 edge models referring to the node model value at both ends of the edge.",
          "long_description" : r'''
For example, to calculate electric field:

..

  devsim.edge_from_node_model(device=device, region=region, node_model="Potential")

''',
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("node_model", "The node model from which we are creating the edge model", required, string, None, None),
          )
      },
      {
          "name" : "edge_model",
          "description" : "Creates an edge model based on an equation",
          "long_description" : r'''
The ``vector`` option uses an averaging scheme for the edge values projected in the direction of each edge.  For a given model, ``model``, the generated components in the visualization files is:

- ``model_x_onNode``
- ``model_y_onNode``
- ``model_z_onNode`` (3D)

This averaging scheme does not produce accurate results, and it is recommended to use the :meth:`devsim.element_from_edge_model` to create components better suited for visualization.  See :ref:`ch__visualization` for more information about creating data files for external visualization programs.
''',
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("name", name_option("edge model", "created"), required, string, None, None),
              ("equation", equation_option("edge model being created"), required, string, None, None),
              ("display_type", "Option for output display in graphical viewer", optional, string, "scalar", (
                  ("nodisplay", "Data on edge will not be displayed"),
                  ("scalar", "Data on edge is a scalar quantity"),
                  ("vector", "Data on edge is a vector quantity (deprecated)"),
              )
              ),
          )
      },
      {
          "name" : "element_model",
          "description" : "Create a model evaluated on element edges.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("name", name_option("element edge model", "created"), required, string, None, None),
              ("equation", equation_option("element edge model being created"), required, string, None, None),
              ("display_type", "Option for output display in graphical viewer", optional, string, "scalar", (
                  ("nodisplay", "Data on edge will not be displayed"),
                  ("scalar", "Data on edge is a scalar quantity"),
              )
              ),
          )
      },
      {
          "name" : "element_from_edge_model",
          "description" : "Creates element edge models from an edge model",
          "long_description" : r'''
For an edge model ``emodel``, creates an element models referring to the directional components on each edge of the element:

- ``emodel_x``
- ``emodel_y``

If the ``derivative`` ``variable`` option is specified, the ``emodel@n0`` and ``emodel@n1`` are used to create:

- ``emodel_x:variable@en0``
- ``emodel_y:variable@en0``
- ``emodel_x:variable@en1``
- ``emodel_y:variable@en1``
- ``emodel_x:variable@en2``
- ``emodel_y:variable@en2``

in 2D for each node on a triangular element. and 

- ``emodel_x:variable@en0``
- ``emodel_y:variable@en0``
- ``emodel_z:variable@en0``
- ``emodel_x:variable@en1``
- ``emodel_y:variable@en1``
- ``emodel_z:variable@en1``
- ``emodel_x:variable@en2``
- ``emodel_y:variable@en2``
- ``emodel_z:variable@en2``
- ``emodel_x:variable@en3``
- ``emodel_y:variable@en3``
- ``emodel_z:variable@en3``

in 3D for each node on a tetrahedral element.

The suffix ``en0`` refers to the first node on the edge of the element and ``en1`` refers to the second node.  ``en2`` and ``en3`` specifies the derivatives with respect the variable at the nodes opposite the edges on the element being considered.
''',
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("edge_model", "The edge model from which we are creating the element model", required, string, None, None),
              ("derivative", "The variable we are taking with respect to edge_model", optional, string, None, None),
          )
      },
      {
          "name" : "element_from_node_model",
          "description" : "Creates element edge models from a node model",
          "long_description" : r'''
This command creates an element edge model from a node model so that each corner of the element is represented.  A node model, ``nmodel``, would be be accessible as 

- ``nmodel@en0``
- ``nmodel@en1``
- ``nmodel@en2``
- ``nmodel@en3`` (3D)

where ``en0``, and ``en1`` refers to the nodes on the element's edge.  In 2D, ``en2`` refers to the node on the triangle node opposite the edge.  In 3D, ``en2`` and ``en3`` refers to the nodes on the nodes off the element edge on the tetrahedral element.
''',
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("node_model", "The node model from which we are creating the edge model", required, string, None, None),
          )
      },
      {
          "name" : "get_edge_model_list",
          "description" : "Returns a list of the edge models on the device region",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
          )
      },
      {
          "name" : "get_edge_model_values",
          "description" : "Get the edge model values calculated at each edge.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("name", name_option("edge model values", "returned as a list"), required, string, None, None),
          )
      },
      {
          "name" : "get_element_model_list",
          "description" : "Returns a list of the element edge models on the device region",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
          )
      },
      {
          "name" : "get_element_model_values",
          "description" : "Get element model values at each element edge",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("name", name_option("element edge model values", "returned as a list"), required, string, None, None),
          )
      },
      {
          "name" : "get_interface_model_list",
          "description" : "Returns a list of the interface models on the interface",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("interface", interface_option_text, required, string, None, None),
          )
      },
      {
          "name" : "get_interface_model_values",
          "description" : "Gets interface model values evaluated at each interface node.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("interface", interface_option_text, required, string, None, None),
              ("name", name_option("interface model values", "returned as a list"), required, string, None, None),
          )
      },
      {
          "name" : "get_node_model_list",
          "description" : "Returns a list of the node models on the device region",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
          )
      },
      {
          "name" : "get_node_model_values",
          "description" : "Get node model values evaluated at each node in a region.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("name", name_option("node model values", "returned as a list"), required, string, None, None),
          )
      },
      {
          "name" : "interface_model",
          "description" : "Create an interface model from an equation.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("interface", interface_option_text, required, string, None, None),
              ("equation", equation_option("interface node model being created"), required, string, None, None),
          )
      },
      {
          "name" : "interface_normal_model",
          "description" : "Creates edge models whose components are based on direction and distance to an interface",
          "long_description" : r'''
This model creates the following edge models:

- ``iname_distance``
- ``iname_normal_x`` (2D and 3D)
- ``iname_normal_y`` (2D and 3D)
- ``iname_normal_z`` (3D only)

where ``iname`` is the name of the interface.  The normals are of the closest node on the interface.  The sign is toward the interface.
''',
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("interface", interface_option_text, required, string, None, None),
          )
      },
      {
          "name" : "node_model",
          "description" : "Create a node model from an equation.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("name", name_option("node model", "created"), required, string, None, None),
              ("equation", equation_option("node model being created"), required, string, None, None),
              ("display_type", "Option for output display in graphical viewer", optional, string, "scalar", (
                  ("nodisplay", "Data on node will not be displayed"),
                  ("scalar", "Data on node is a scalar quantity"),
              )
              ),
          )
      },
      {
          "name" : "node_solution",
          "description" : "Create node model whose values are set.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("name", name_option("solution", "created"), required, string, None, None),
          )
      },
      {
          "name" : "edge_solution",
          "description" : "Create node model whose values are set.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("name", name_option("solution", "created"), required, string, None, None),
          )
      },
      {
          "name" : "element_solution",
          "description" : "Create node model whose values are set.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("name", name_option("solution", "created"), required, string, None, None),
          )
      },
      {
          "name" : "print_node_values",
          "description" : "Print node values for debugging.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("name", name_option("node model values", "printed to the screen"), required, string, None, None),
          )
      },
      {
          "name" : "print_edge_values",
          "description" : "Print edge values for debugging.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("name", name_option("edge model values", "printed to the screen"), required, string, None, None),
          )
      },
      {
          "name" : "print_element_values",
          "description" : "Print element values for debugging.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("name", name_option("element edge model values", "printed to the screen"), required, string, None, None),
          )
      },
      {
          "name" : "register_function",
          "description" : "This command is used to register a new Python procedure for evaluation by SYMDIFF.",
          "parameters" : (
              ("name", "Name of the function", required, string, None, None),
              ("nargs", "Number of arguments to the function", required, string, None, None),
              ("procedure", "The procedure to be called", required, string, None, None),
          )
      },
      {
          "name" : "set_node_value",
          "description" : "A uniform value is used if index is not specified.  Note that equation based node models will lose this value if their equation is recalculated.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("name", name_option("node model", "whose value is being set"), required, string, None, None),
              ("index", "Index of node being set", required, integer, None, None),
              ("value", "Value of node being set", required, Float, None, None),
          )
      },
      {
          "name" : "set_node_values",
          "description" : "Set node model values from another node model, or a list of values.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("name", name_option("node model", "initialized"), required, string, None, None),
              ("init_from", "Node model we are using to initialize the node solution", optional, string, None, None),
              ("values", "List of values for each node in the region.", optional, List, None, None),
          )
      },
      {
          "name" : "set_edge_values",
          "description" : "Set edge model values from another edge model, or a list of values.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("name", name_option("edge model", "initialized"), required, string, None, None),
              ("init_from", "Node model we are using to initialize the edge solution", optional, string, None, None),
              ("values", "List of values for each edge in the region.", optional, List, None, None),
          )
      },
      {
          "name" : "set_element_values",
          "description" : "Set element model values from another element model, or a list of values.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("name", name_option("element model", "initialized"), required, string, None, None),
              ("init_from", "Node model we are using to initialize the element solution", optional, string, None, None),
              ("values", "List of values for each element in the region.", optional, List, None, None),
          )
      },
      {
          "name" : "symdiff",
          "description" : "This command returns an expression.  All strings are treated as independent variables.  It is primarily used for defining new functions to the parser.",
          "parameters" : (
              ("expr", "Expression to send to SYMDIFF", required, string, None, None),
          )
      },
      {
          "name" : "vector_element_model",
          "description" : "Create vector components from an element edge model",
          "long_description" : r'''
This command creates element edge models from an element model which represent the vector components on the element edge.  An element model, ``emodel``, would then have

- ``emodel_x``
- ``emodel_y``
- ``emodel_z`` (3D only)

The primary use of these components are for visualization.
''',
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("element_model", "The element model for which we are calculating the vector compoenents", required, string, None, None),
          )
      },
      {
          "name" : "vector_gradient",
          "description" : "Creates the vector gradient for noise analysis",
          "long_description" : r'''
Used for noise analysis.  The ``avoidzero`` option is important for noise analysis, since a node model value of zero is not physical for some contact and interface boundary conditions.  For a given node model, ``model``, a node model is created in each direction:

- ``model_gradx`` (1D)
- ``model_grady`` (2D and 3D)
- ``model_gradz`` (3D)

It is important not to use these models for simulation, since DEVSIM, does not have a way of evaluating the derivatives of these models.  The models can be used for integrating the impedance field, and other postprocessing.  The :meth:`devsim.element_from_edge_model` command can be used to create gradients for use in a simulation.
''',
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("node_model", "The node model from which we are creating the edge model", required, string, None, None),
              ("calc_type", "The node model from which we are creating the edge model", optional, string, "default", (
                  ("default", "Consider all nodes for calculating the gradient field"),
                  ("avoidzero", "Do not take gradient at nodes where the node_model is zero"),
              ),
              ),
          )
      },
      {
          "name" : "debug_triangle_models",
          "description" : "Debugging command used in the development of DEVSIM and used in regressions.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
          )
      },
  )
}

