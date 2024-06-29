.. include:: macros.rst

.. _ch__visualization:

*********************************
Visualization and post processing
*********************************

Introduction
============

|devsim| is able to create files for visualization tools.  Information about acquiring these tools are presented in :ref:`thirdpartyavailability`.


.. _sec__visualizationsoftware:

Visualization software
======================

Overview
--------

The tools in :numref:`table__visualizationtools` can read the file Tecplot and VTK Formats.


.. _table__visualizationtools:

.. list-table:: Open source visualization tools
   :header-rows: 1
   :widths: 40 60

   * - |paraview|
     - visualization tool available at https://paraview.org.
   * - |visit|
     - visualization tool available from https://visit-dav.github.io/visit-website/


Using |paraview|
----------------

The :meth:`devsim.write_devices` is used to create an ASCII file suitable for use in |paraview|.  Edge quantities are interpolated onto the node positions in the resulting structure.  Element edge quantities are interpolated onto the centers of each triangle or tetrahedron in the mesh.

.. code-block:: python

  write_devices(file="mos_2d_dd", type="vtk")

One ``vtu`` file per device region will be created, as well as a ``vtm`` file which may be used to load all of the device regions into |paraview|.

Using |visit|
-------------

|visit| supports reading the |tecplot| and |paraview| formats.  When using the ``vtk`` option on the :meth:`devsim.write_devices`, a file with a ``visit`` filename extension is created to load the files created for |paraview|.


Reducing file sizes
===================

Based on a contribution by [@simbilod](https://github.com/simbilod) :meth:`devsim.write_devices` now supports reducing the file size of data files by allowing users to specify a callback function to reduce data usage.  In this example, only the ``NetDoping`` field is written to the Tecplot data file.

.. code-block:: none

    devsim.write_devices(
        file="mesh2d_reduced.tec",
        type="tecplot",
        include_test=lambda x: x in ("NetDoping",),
    )


Post processing
===============

|devsim| has several commands for getting information on the mesh.  Those related to post processing are described in :ref:`ModelCommands` and :ref:`GeometryCommands`.

See :ref:`sec__devsimLoadSave` for information about loading and saving mesh information to a file.


Index information
-----------------


The ``coordinate_index`` and ``node_index`` are default node models created on a region (:numref:`models__node`}).
The ``edge_index`` is a default edge models created on a region :numref:`models__edge`.

Element node list
-----------------

The :meth:`devsim.get_element_node_list` retrieves a list of nodes for every element on a ``region``, ``contact``, or ``interface``.

