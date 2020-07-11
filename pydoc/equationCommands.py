from commandCommon import *

Command={
    "name" : "Equation",
  "description" : "Commands for manipulating equations on contacts, interface, and regions",
  "commands" : (
      {
          "name" : "contact_equation",
          "description" : "Create a contact equation on a device",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("contact", contact_option_text, required, string, None, None),
              ("name", name_option("contact equation", "created"), required, string, None, None),
              ("variable_name", "The variable name is used to determine the bulk equation we are replacing at this contact (deprecated)", optional, string, None, None),
              ("circuit_node", "Name of the circuit we integrate the flux into", optional, string, None, None),
              ("edge_charge_model", "Name of the edge model used to determine the charge at this contact", optional, string, None, None),
              ("edge_current_model", "Name of the edge model used to determine the current flowing out of this contact", optional, string, None, None),
              ("edge_model", "Name of the edge model being integrated at each edge at this contact", optional, string, None, None),
              ("element_charge_model", "Name of the element edge model used to determine the charge at this contact", optional, string, None, None),
              ("element_current_model", "Name of the element edge model used to determine the current flowing out of this contact", optional, string, None, None),
              ("element_model", "Name of the element edge model being integrated at each edge at this contact", optional, string, None, None),
              ("node_charge_model", "Name of the node model used to determine the charge at this contact", optional, string, None, None),
              ("node_current_model", "Name of the node model used to determine the current flowing out of this contact", optional, string, None, None),
              ("node_model", "Name of the node_model being integrated at each node at this contact", optional, string, None, None),
          )
      },
      {
          "name" : "custom_equation",
          "description" : "Custom equation assembly.  See :ref:`models__customequation` for a description of how the function should be structured.",
          "parameters" : (
              ("name", name_option("custom equation", "created"), required, string, None, None),
              ("procedure", "The procedure to be called", required, string, None, None),
          )
      },
      {
          "name" : "equation",
          "description" : "Specify an equation to solve on a device",
          "long_description" : r'''
The integration variables can be changed in 2D for cylindrical coordinate systems by setting the appropriate parameters as described in :ref:`sec__cylindrical`.

In order to set the node volumes for integration of the ``edge_volume_model``, it is possible to do something like this:

..
  devsim.edge_model(device="device", region="region", name="EdgeNodeVolume", equation="0.5*SurfaceArea*EdgeLength")
  devsim.set_parameter(name="edge_node0_volume_model", value="EdgeNodeVolume")
  devsim.set_parameter(name="edge_node1_volume_model", value="EdgeNodeVolume")

''',
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("name", name_option("equation", "created"), required, string, None, None),
              ("variable_name", "Name of the node_solution being solved", required, string, None, None),
              ("node_model", "Name of the node_model being integrated at each node in the device volume", optional, string, None, None),
              ("edge_model", "Name of the edge model being integrated over each edge in the device volume", optional, string, None, None),
              ("edge_volume_model", "Name of the edge model being integrated over the volume of each edge in the device volume", optional, string, None, None),
              ("time_node_model", "Name of the time dependent node_model being integrated at each node in the device volume", optional, string, None, None),
              ("element_model", "Name of the element_model being integrated over each edge in the device volume", optional, string, None, None),
              ("volume_model", "Name of the element_model being integrated over the volume of each edge in the device volume", optional, string, None, None),
              ("variable_update", "update type for circuit variable", optional, option, "default", (
                  ("default", "Variable can be positive or negative"),
                  ("log_damp", "Variable update is damped"),
                  ("positive", "Solution update results in positive quantity"),
              )
              ),
          )
      },
      {
          "name" : "delete_contact_equation",
          "description" : "This command deletes an equation from a contact.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("contact", contact_option_text, required, string, None, None),
              ("name", name_option("contact equation", "deleted"), required, string, None, None),
          )
      },
      {
          "name" : "delete_interface_equation",
          "description" : "This command deletes an equation from an interface.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("interface", interface_option_text, required, string, None, None),
              ("name", name_option("interface equation", "deleted"), required, string, None, None),
          )
      },
      {
          "name" : "delete_equation",
          "description" : "This command deletes an equation from a region.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("name", name_option("equation", "deleted"), required, string, None, None),
          )
      },
      {
          "name" : "get_contact_equation_command",
          "description" : "This command gets the options used when creating this contact equation.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("contact", contact_option_text, required, string, None, None),
              ("name", name_option("contact equation", "command options returned"), required, string, None, None),
          )
      },
      {
          "name" : "get_interface_equation_command",
          "description" : "This command gets the options used when creating this interface equation.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("interface", interface_option_text, required, string, None, None),
              ("name", name_option("interface equation", "command options returned"), required, string, None, None),
          )
      },
      {
          "name" : "get_equation_command",
          "description" : "This command gets the options used when creating this equation.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("name", name_option("equation", "command options returned"), required, string, None, None),
          )
      },
      {
          "name" : "get_contact_equation_list",
          "description" : "This command gets a list of equations on the specified contact.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("contact", contact_option_text, required, string, None, None),
          )
      },
      {
          "name" : "get_interface_equation_list",
          "description" : "This command gets a list of equations on the specified interface.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("interface", interface_option_text, required, string, None, None),
          )
      },
      {
          "name" : "get_equation_list",
          "description" : "This command gets a list of equations on the specified region.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
          )
      },
      {
          "name" : "get_equation_numbers",
          "description" : "Returns a list of the equation numbers corresponding to each node in a region.  Values are only valid when during the course of a solve.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("equation", "Name of the equation", optional, string, None, None),
              ("variable", "Name of the variable", optional, string, None, None),
          )
      },
      {
          "name" : "interface_equation",
          "description" : "Command to specify an equation at an interface",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("interface", interface_option_text, required, string, None, None),
              ("name", name_option("interface equation", "created"), required, string, None, None),
              ("name0", name_option("equation coupling in region 0", "created"), optional, string, "name", None),
              ("name1", name_option("equation coupling in region 1", "created"), optional, string, "name", None),
              ("variable_name", "The variable name is used to determine the bulk equation we are coupling this interface to (deprecated)", optional, string, None, None),
              ("interface_model", "When specified, the bulk equations on both sides of the interface are integrated together.  This model is then used to specify how nodal quantities on both sides of the interface are balanced", required, string, None, None),
              ("type", "Specifies the type of boundary condition", required, option, None, (
                  ("continuous", r"Equations of the same name in the two regions are added.  The ``interface_model`` is an additional equation is created to specify how quantities across the interface are solved"),
                  ("fluxterm", r"The ``interface_model`` is added to the bulk equation in the first region, and subtracted from the second"),
                  ("hybrid", r"Flux in the second region is added to the flux in the first region.  The ``interface_model`` is subtracted from the net flux in the second region"),
              )
              )
          )
      },
  ),
}



