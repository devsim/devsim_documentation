.. include:: macros.txt

.. _ch__visualization:

Visualization
-------------

Introduction
~~~~~~~~~~~~

|devsim| is able to create files for visualization tools.  Information about acquiring these tools are presented in :ref:`thirdpartyavailability`.

Using Tecplot
~~~~~~~~~~~~~

The :meth:`ds.write_devices` is used to create an ASCII file suitable for use in |tecplot|.  Edge quantities are interpolated onto the node positions in the resulting structure.  Element edge quantities are interpolated onto the centers of each triangle or tetrahedron in the mesh.

.. code-block:: python

  write_devices(file="mos_2d_dd.dat", type="tecplot")

Using Postmini
~~~~~~~~~~~~~~

The :meth:`ds.write_devices` is used to create an ASCII file suitable for use in |postmini|.  Edge and element edge quantities are interpolated onto the node positions in the resulting structure.

.. code-block:: python

  write_devices(file="mos_2d_dd.flps", type="floops")

Using Paraview
~~~~~~~~~~~~~~

The :meth:`ds.write_devices` is used to create an ASCII file suitable for use in |paraview|.  Edge quantities are interpolated onto the node positions in the resulting structure.  Element edge quantities are interpolated onto the centers of each triangle or tetrahedron in the mesh.

.. code-block:: python

  write_devices(file="mos_2d_dd", type="vtk")

One ``vtu`` file per device region will be created, as well as a ``vtm`` file which may be used to load all of the device regions into |paraview|.

Using VisIt
~~~~~~~~~~~

|visit| supports reading the |tecplot| and |paraview| formats.  When using the ``vtk`` option on the :meth:`ds.write_devices`, a file with a ``visit`` filename extension is created to load the files created for |paraview|.

DEVSIM
~~~~~~

|devsim| has several commands for getting information on the mesh.  Those related to post processing are described in :ref:`ModelCommands` and :ref:`GeometryCommands`.

See :ref:`sec__devsimLoadSave` for information about loading and saving mesh information to a file.


