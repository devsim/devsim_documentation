from commandCommon import *

Command = {
    "name" : "Solver",
  "description" : "Commands for simulation",
  "commands" : (
      {
          "name" : "get_contact_current",
          "description" : "Get current at the contact",
          "parameters" : (
              device_option_required,
              contact_option_required,
              ("equation", "Name of the contact equation from which we are retrieving the current", required, string, None, None),
          )
      },
      {
          "name" : "get_contact_charge",
          "description" : "Get charge at the contact",
          "parameters" : (
              device_option_required,
              contact_option_required,
              ("equation", "Name of the contact equation from which we are retrieving the charge", required, string, None, None),
          )
      },
      {
          "name" : "solve",
          "description" : "Call the solver.  A small-signal AC source is set with the circuit voltage source.",
          "parameters" : (
              ("type", "type of solve being performed", required, option, None, (
                  ("dc", "DC steady state simulation"),
                  ("ac", "Small-signal AC simulation"),
                  ("noise", "Small-signal AC simulation"),
                  ("transient_dc", "Perform DC steady state and keep calculate charge at initial time step"),
                  ("transient_bdf1", "Perform transient simulation using backward difference integration"),
                  ("transient_bdf2", "Perform transient simulation using backward difference integration"),
                  ("transient_tr", "Perform transient simulation using trapezoidal integration"),
              )
              ),
              ("solver_type", "Linear solver type", required, option, "direct", (
                  ("direct", "Use LU factorization"),
                  ("iterative", "Use iterative solver"),
              )
              ),
              ("absolute_error", "Required update norm in the solve", optional, Float, "0.0", None),
              ("relative_error", "Required relative update in the solve", optional, Float, "0.0", None),
              ("maximum_error", "Maximum absolute error before solve stops", optional, Float, "MAXDOUBLE", None),
              ("charge_error", "Relative error between projected and solved charge during transient simulation", optional, Float, "0.0", None),
              ("gamma", "Scaling factor for transient time step", optional, Float, "1.0", None),
              ("tdelta", "time step", optional, Float, "0.0", None),
              ("maximum_iterations", "Maximum number of iterations in the DC solve", optional, integer, "20", None),
              ("maximum_divergence", "Maximum number of diverging iterations during solve", optional, integer, "20", None),
              ("frequency", "Frequency for small-signal AC simulation", optional, Float, "0.0", None),
              ("output_node", "Output circuit node for noise simulation", optional, string, None, None),
              ("info", "Solve command return convergence information", optional, boolean, False, None),
          )
      },
      {
          "name" : "get_matrix_and_rhs",
          "description" : "Returns matrices and rhs vectors.",
          "parameters" : (
              ("format", "Option for returned matrix format.", required, option, None, (
                  ("csc", "Compressed Sparse Column Format"),
                  ("csr", "Compressed Sparse Row Format"),
                  ),
              ),
          )
      },
  )
}

