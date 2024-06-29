.. _thirdpartyavailability:

Install external software tools
===============================


Meshing
-------

.. _gmshAvailability:

Gmsh
^^^^

|gmsh| :cite:`Gmsh:2009` is available from https://gmsh.info.  |devsim| is able to import triangular or tetrahedral meshes from this application.  More information is in :ref:`sec__gmshintro`.

Other meshers
^^^^^^^^^^^^^

It is also possible to import other mesh formats by writing a converter in |python|, as described in :ref:`sec__customMeshLoad`.

Visualization
-------------

See :ref:`sec__visualizationsoftware` for a listing of available meshing tools, which are known to work with |devsim|.

Math libraries
--------------

BLAS and LAPACK
^^^^^^^^^^^^^^^

These are the basic linear algebra routines used in |devsim| and their selection is described in :ref:`sec_blaslapack_selection`.

|intelmklpardiso|
^^^^^^^^^^^^^^^^^

This library may be installed and selected using the instructions in :ref:`sec__solver_selection`.

