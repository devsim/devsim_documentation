Introduction
============

|devsim| is a technology computer-aided design (TCAD) software for semiconductor device simulation.  While geared toward this application, it may be used where the control volume approach is appropriate for solving systems of partial-differential equations (PDE's) on a static mesh.
After introducing |devsim|, the rest of the manual discusses the key components of the system, and instructions for their use.


The primary goal of |devsim| is to give the user as much flexibility and control as possible.  In this regard, few models are coded into the program binary.  They are implemented in human-readable scripts that can be modified if necessary.

|devsim| has a scripting language interface (:ref:`ch__scripting`).  This provides control structures and language syntax in a consistent and intuitive manner.
The user is provided an environment where they can implement new models on their own.  This is without requiring extensive vendor support or use of compiled programming languages.

|symdiff| (:ref:`ch__symdiff`) is the symbolic expression parser used to allow the formulation of device equations in terms of models and parameters.  Using symbolic differentiation, the required partial derivatives can be generated, or provided by the user.  |devsim| then assembles these equations over the mesh.

Getting help
============

Please see :ref:`Contact` for project contact information.  The most responsive method is to contact the online forum at `https://forum.devsim.org <https://forum.devsim.org>`_.  Additional information, with links to documentation is available at `https://devsim.org <https://devsim.org>`_.  Additional documentation files released with the simulator are presented at `https://pypi.org/project/devsim/ <https://pypi.org/project/devsim/>`_.




