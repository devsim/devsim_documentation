
.. include:: macros.txt

Introduction
------------

Overview
~~~~~~~~

|devsim| is a technology computer-aided design (TCAD) software for semiconductor device simulation.  While geared toward this application, it may be used where the control volume approach is appropriate for solving systems of partial-differential equations (PDE's) on a static mesh.
After introducing |devsim|, the rest of the manual discusses the key components of the system, and instructions for their use.

  |devsim| is available from |devsimorg|.  The source code is available under the terms of the Apache License Version 2.0 :cite:`apache2`. Examples are released under the Apache License Version 2.0 :cite:`apache2`.  Contributions to this project are welcome in the form of bug reporting, documentation, modeling, and feature implementation.

Goals
~~~~~

The primary goal of |devsim| is to give the user as much flexibility and control as possible.  In this regard, few models are coded into the program binary.  They are implemented in human-readable scripts that can be modified if necessary.

|devsim| has a scripting language interface (:ref:`ch__scripting`).  This provides control structures and language syntax in a consistent and intuitive manner.
The user is provided an environment where they can implement new models on their own.  This is without requiring extensive vendor support or use of compiled programming languages.

|symdiff| (:ref:`ch__symdiff`) is the symbolic expression parser used to allow the formulation of device equations in terms of models and parameters.  Using symbolic differentiation, the required partial derivatives can be generated, or provided by the user.  |devsim| then assembles these equations over the mesh.


Structures
~~~~~~~~~~

**Devices**
A ``device`` refers to a discrete structure being simulated.  It is composed of the following types of objects.

**Regions**
A ``region`` defines a portion of the device of a specific material.  Each region has its own system of equations being solved.

**Interfaces**
An ``interface`` connects two regions together.  At the interfaces, equations are specified to account for how the flux in each device region crosses the region boundary.

**Contacts**
A ``contact`` specifies the boundary conditions required for device simulation.  It also specifies how terminal currents are are integrated into an external circuit.

Equation assembly
~~~~~~~~~~~~~~~~~

Equation assembly of models is discussed in :ref:`sec__models`.

Parameters
~~~~~~~~~~

Parameters may be specified globally, or for a specific device or region.  Alternatively, parameters may be based on the material type of the regions.  Usage is discussed in :ref:`ch__modelparameters`.

Circuits
~~~~~~~~

Circuit boundary conditions allow multi-device simulation.  They are also required for setting sources and their response for AC and noise analysis.  Circuit elements, such as voltage sources, current sources, resistors, capacitors, and inductors may be specified.  This is further discussed in :ref:`ch__circuits`.

Meshing
~~~~~~~

Meshing is discussed in :ref:`ch__meshing`.

Analysis
~~~~~~~~

|devsim| offers a range of simulation algorithms.  They are discussed in more detail in :ref:`sec__solver`.

**DC**
The DC operating point analysis is useful for performing steady-state simulation for a different bias conditions.

**AC**
At each DC operating point, a small-signal AC analysis may be performed.  An AC source is provided through a circuit and the response is then simulated.  This is useful for both quasi-static capacitance simulation, as well as RF simulation.

**Noise/Sensitivity**
Noise analysis may be used to evaluate how internal noise sources are observed in the terminal currents of the device or circuit.  Using this method, it is also possible to simulate how the device response changes when device parameters are changed.

**Transient**
|devsim| is able to simulate the nonlinear transient behavior of devices, when the bias conditions change with time.

Scripting interface
~~~~~~~~~~~~~~~~~~~

The scripting interface to |devsim| is discussed in :ref:`ch__scripting`.


Expression parser
~~~~~~~~~~~~~~~~~

The expression parser is discussed in :ref:`ch__symdiff`.


Visualization and postprocessing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Visualization is discussed in :ref:`ch__visualization`.

Installation
~~~~~~~~~~~~

Installation is discussed in :ref:`sec__installation`.

Additional information
~~~~~~~~~~~~~~~~~~~~~~

Additional information is discussed in :ref:`ch__additional`.

Examples
~~~~~~~~

Examples are discussed in the remaining chapters beginning with :ref:`ch__examples`.

