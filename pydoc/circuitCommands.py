from commandCommon import *

Command={
    "name" : "Circuit",
  "description" : "Commands are for adding circuit elements to the simulation.",
  "commands" : (
      {
          "name" : "add_circuit_node",
          "description" : "Adds a circuit node for use in circuit or multi-device simulation",
          "parameters" : (
              ("name", name_option("circuit node", "created"), required, string, None, None),
              ("value", "initial value", optional, Float, "0.0", None),
              ("variable_update", "update type for circuit variable", optional, option, "default", (
                  ("default",  "Variable can be positive or negative"),
                  ("log_damp", "Variable update is damped"),
                  ("positive", "Solution update results in positive quantity"),
              )
              ),
          )
      },
    {
        "name" : "circuit_alter",
          "description" : "Alter the value of a circuit element parameter",
          "parameters" : (
              ("name", name_option("circuit node", "created"), required, string, None, None),
              ("param", "parameter being modified", optional, string, "value", None),
              ("value", "value for the parameter", required, Float, None, None),

          )
      },
    {
        "name" : "circuit_element",
          "description" : "Adds a circuit element external to the devices",
          "parameters" : (
              ("name", name_option("circuit element", 'created.  A prefix of "V" is for voltage source, "I" for current source, "R" for resistor, "L" for inductor, and "C" for capacitor.'), required, string, None, None),
              ("value", "value for the default parameter of the circuit element", optional, Float, "0.0", None),
              ("n1", "circuit node", required, string, None, None),
              ("n2", "circuit node", required, string, None, None),
              ("acreal", "real part of AC source for voltage", optional, Float, "0.0", None),
              ("acimag", "imag part of AC source for voltage", optional, Float, "0.0", None),
          )
      },
    {
        "name" : "circuit_node_alias",
          "description" : "Create an alias for a circuit node",
          "parameters" : (
              ("node", "circuit node being aliased", required, string, None, None),
              ("alias", "alias for the circuit node", required, string, None, None),
          ),
      },
    {
        "name" : "get_circuit_equation_number",
          "description" : "Returns the row number correspond to circuit node in a region.  Values are only valid when during the course of a solve.",
          "parameters" : (
              ("node", "circuit node", required, string, None, None),
          ),
      },
    {
        "name" : "get_circuit_node_list",
          "description" : "Gets the list of the nodes in the circuit.",
          "parameters" : (
          ),
      },
    {
        "name" : "get_circuit_node_value",
          "description" : "Gets the value of a circuit node for a given solution type.",
          "parameters" : (
              ("solution", 'name of the solution. "dcop" is the name for the DC solution', optional, string, "dcop", None),
              ("node", "circuit node of interest", required, string, None, None),
          ),
      },
    {
        "name" : "get_circuit_solution_list",
          "description" : "Gets the list of available circuit solutions.",
          "parameters" : (
          ),
      },
    {
        "name" : "set_circuit_node_value",
          "description" : "Sets the value of a circuit node for a given solution type.",
          "parameters" : (
              ("solution", 'name of the solution. "dcop" is the name for the DC solution', optional, string, "dcop", None),
              ("node", "circuit node of interest", required, string, None, None),
              ("value", "new value", optional, Float, "0.0", None),
          ),
      },
  )
}

