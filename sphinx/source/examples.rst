.. include:: macros.txt

.. _ch__examples:

Example Overview
----------------

In the following chapters, examples are presented for the use of |devsim| to solve some simulation problems.
Examples are also located in the |devsim| distribution and their location is mentioned in :ref:`installation__directories`.

The following example directories are contained in the distribution.

capacitance
~~~~~~~~~~~
These are 1D and 2D capacitor simulations, using the internal mesher.  A description of these examples is presented in :ref:`ch__capacitance`.

diode
~~~~~

This is a collection of 1D, 2D, and 3D diode structures using the internal mesher, as well as |gmsh|.  These examples are discussed in :ref:`ch__diode`.

bioapp1
~~~~~~~

This is a biosensor application.

.. _examples__geniusdir:

genius
~~~~~~

This directory has examples importing meshes from |geniusds|.

vector_potential
~~~~~~~~~~~~~~~~

This is a 2D magnetic field simulation solving for the magnetic potential.  The simulation script is ``vector_potential/twowire.py``  A simulation result for two wires conducting current is shown in :numref:`twowireresult`.


.. _twowireresult:

.. figure:: twowire.*
    :align: center

    Simulation result for solving for the magnetic potential and field.  The coloring is by the Z component of the magnetic potential, and the stream traces are for components of magnetic field.

mobility
~~~~~~~~
This is an advanced example using electric field dependendent mobility models.

