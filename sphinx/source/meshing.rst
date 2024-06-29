.. include:: macros.rst

.. _ch__meshing:

*******
Meshing
*******

1D mesher
=========

|devsim| has an internal 1D mesher and the proper sequence of commands follow in this example.

.. code-block:: python

  devsim.create_1d_mesh(mesh="cap")
  devsim.add_1d_mesh_line(mesh="cap", pos=0, ps=0.1, tag="top")
  devsim.add_1d_mesh_line(mesh="cap", pos=0.5, ps=0.1, tag="mid")
  devsim.add_1d_mesh_line(mesh="cap", pos=1, ps=0.1, tag="bot")
  devsim.add_1d_contact(mesh="cap", name="top", tag="top", material="metal")
  devsim.add_1d_contact(mesh="cap", name="bot", tag="bot", material="metal")
  devsim.add_1d_interface(mesh="cap", name="MySiOx", tag="mid")
  devsim.add_1d_region(mesh="cap", material="Si", region="MySiRegion",
    tag1="top", tag2="mid")
  devsim.add_1d_region(mesh="cap", material="Ox", region="MyOxRegion",
    tag1="mid", tag2="bot")
  devsim.finalize_mesh(mesh="cap")
  devsim.create_device(mesh="cap", device="device")

The :meth:`devsim.create_1d_mesh` is first used to initialize the specification of a new mesh by the name specified with the ``command`` option. The :meth:`devsim.add_1d_mesh_line` is used to specify the end points of the 1D structure, as well as the location of points where the spacing changes.  The ``command`` is used to create reference labels used for specifying the contacts, interfaces and regions.

The :meth:`devsim.add_1d_contact`, :meth:`devsim.add_1d_interface` and :meth:`devsim.add_1d_region` are used to specify the contacts, interfaces and regions for the device.

Once the meshing commands have been completed, the :meth:`devsim.finalize_mesh` is called to create a mesh structure and then :meth:`devsim.create_device` is used to create a device using the mesh.

2D mesher
=========

Similar to the 1D mesher, the 2D mesher uses a sequence of non-terminating mesh lines are specified in both the x and y directions to specify a mesh structure.  As opposed to using tags, the regions are specified using :meth:`devsim.add_2d_region` as box coordinates on the mesh coordinates.  The contacts and interfaces are specified using boxes, however it is best to ensure the the interfaces and contacts encompass only one line of points.

.. code-block:: python

  devsim.create_2d_mesh(mesh="cap")
  devsim.add_2d_mesh_line(mesh="cap", dir="y", pos=-0.001, ps=0.001)
  devsim.add_2d_mesh_line(mesh="cap", dir="x", pos=xmin, ps=0.1)
  devsim.add_2d_mesh_line(mesh="cap", dir="x", pos=xmax, ps=0.1)
  devsim.add_2d_mesh_line(mesh="cap", dir="y", pos=ymin, ps=0.1)
  devsim.add_2d_mesh_line(mesh="cap", dir="y", pos=ymax, ps=0.1)
  devsim.add_2d_mesh_line(mesh="cap", dir="y", pos=+1.001, ps=0.001)
  devsim.add_2d_region(mesh="cap", material="gas", region="gas1", yl=-.001, yh=0.0)
  devsim.add_2d_region(mesh="cap", material="gas", region="gas2", yl=1.0, yh=1.001)
  devsim.add_2d_region(mesh="cap", material="Oxide", region="r0", xl=xmin, xh=xmax,
    yl=ymid1, yh=ymin)
  devsim.add_2d_region(mesh="cap", material="Silicon", region="r1", xl=xmin, xh=xmax,
    yl=ymid2, yh=ymid1)
  devsim.add_2d_region(mesh="cap", material="Silicon", region="r2", xl=xmin, xh=xmax,
    yl=ymid2, yh=ymax)

  devsim.add_2d_interface(mesh="cap", name="i0", region0="r0", region1="r1")
  devsim.add_2d_interface(mesh="cap", name="i1", region0="r1", region1="r2",
    xl=0, xh=1, yl=ymid2, yh=ymid2, bloat=1.0e-10)
  devsim.add_2d_contact(mesh="cap", name="top", region="r0", yl=ymin, yh=ymin,
    bloat=1.0e-10, material="metal")
  devsim.add_2d_contact(mesh="cap", name="bot", region="r2", yl=ymax, yh=ymax,
    bloat=1.0e-10, material="metal")
  devsim.finalize_mesh(mesh="cap")
  devsim.create_device(mesh="cap", device="device")

In the current implementation of the software, it is necessary to create a region on both sides of the contact in order to create a contact using :meth:`devsim.add_2d_contact` or an interface using :meth:`devsim.add_2d_interface`.

Once the meshing commands have been completed, the :meth:`devsim.finalize_mesh` is called to create a mesh structure and then :meth:`devsim.create_device` is used to create a device using the mesh.

.. _sec__externalmesher:

Using an external mesher
========================

.. _sec__gmshintro:

Gmsh
----

The |gmsh| meshing software (see :ref:`gmshAvailability`) can be used to create a 1D, 2D, or 3D mesh suitable for use in |devsim|.  |devsim| supports reading version ``2.2`` meshes from |gmsh|.  In order to write this format, it is necessary to specify the mesh format when writing out a mesh file.  From the `gmsh` command line, use the ``-format msh2`` option.

When creating the mesh file using the software, use physical group names to map the difference entities in the resulting mesh file to a group name.  


In this example, a MOS structure is read in:

.. code-block:: python

  devsim.create_gmsh_mesh(file="gmsh_mos2d.msh", mesh="mos2d")
  devsim.add_gmsh_region(mesh="mos2d" gmsh_name="bulk", region="bulk",
    material="Silicon")
  devsim.add_gmsh_region(mesh="mos2d" gmsh_name="oxide", region="oxide",
    material="Silicon")
  devsim.add_gmsh_region(mesh="mos2d" gmsh_name="gate", region="gate",
    material="Silicon")
  devsim.add_gmsh_contact(mesh="mos2d" gmsh_name="drain_contact", region="bulk",
      name="drain", material="metal")
  devsim.add_gmsh_contact(mesh="mos2d" gmsh_name="source_contact", region="bulk",
      name="source", material="metal")
  devsim.add_gmsh_contact(mesh="mos2d" gmsh_name="body_contact", region="bulk",
      name="body", material="metal")
  devsim.add_gmsh_contact(mesh="mos2d" gmsh_name="gate_contact", region="gate",
      name="gate", material="metal")
  devsim.add_gmsh_interface(mesh="mos2d" gmsh_name="gate_oxide_interface",
    region0="gate", region1="oxide", name="gate_oxide")
  devsim.add_gmsh_interface(mesh="mos2d" gmsh_name="bulk_oxide_interface",
    region0="bulk", region1="oxide", name="bulk_oxide")
  devsim.finalize_mesh(mesh="mos2d")
  devsim.create_device(mesh="mos2d", device="mos2d")


Once the meshing commands have been completed, the :meth:`devsim.finalize_mesh` is called to create a mesh structure and then :meth:`devsim.create_device` is used to create a device using the mesh.

.. _sec__customMeshLoad:

Custom mesh loading using scripting
-----------------------------------

It is also possible to arbitrarily load a mesh from a |python| using the :meth:`devsim.create_gmsh_mesh`.  This is explained in the ``Notes`` section of the command.  In addition, please see the ``testing/pythonmesh1d`` script for a simple demonstration script.
These meshes may only contain points, lines, triangles, and tetrahedra.  Hybrid meshes or uniform meshes containing other elements are not supported at this time.

.. _sec__devsimLoadSave:

Loading and saving results
==========================

The :meth:`devsim.write_devices` is used to create an ASCII file suitable for saving data for restarting the simulation later.  The ``devsim`` format encodes structural information, as well as the commands necessary for generating the models and equations used in the simulation.  The ``devsim_data`` format is used for storing numerical information for use in other programs for analysis.
The :meth:`devsim.load_devices` is then used to reload the device data for restarting the simulation.

Mesh processing
===============

See :ref:`ch__examples` for examples involving mesh processing.

Notes
=====

Contacts
--------

Contact material
^^^^^^^^^^^^^^^^

Contacts requires a material setting (e.g. ``metal``).  This is for informational purposes.  Contact models still look up parameter values based on the region they are located.


Create contacts from interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :meth:`devsim.create_contact_from_interface` may be used to create a contact at the location of an interface.  This is useful when contact boundary conditions are needed for a region connected to the interface.

Device and mesh deletion commands
---------------------------------

The :meth:`devsim.delete_device` command makes it possible to delete devices so they will no longer be solved in the simulation.  Any parameters set on the device are also removed from the system.

The :meth:`devsim.delete_mesh` command makes it possible to delete meshes.  Once a mesh has been deleted, it is no longer possible to create devices from it using the :meth:`devsim.create_device` command.


Periodic boundary conditions
----------------------------

The :meth:`devsim.create_interface_from_nodes` command makes it possible to create an interface with non coincident nodes.  This enables the use of periodic boundary conditions.


