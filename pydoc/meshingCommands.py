from commandCommon import *

Command = {
  "name" : "Meshing",
  "description" : "Commands for reading and writing meshes",
  "commands" : (

{
"name" : "create_gmsh_mesh",
"description" : "Create a mesh to import a Gmsh mesh",
"parameters" : (
("mesh", "name of the mesh being generated", required, string, None, None),
("file", "name of the Gmsh mesh file being read into DEVSIM", optional, string, None, None),
("coordinates", "List of coordinate positions on mesh.", optional, List, None, None),
("elements", "List of elements on the mesh.", optional, List, None, None),
("physical_names", "List of names for each contact, interface, and region on mesh.", optional, List, None, None),
),
"long_description" : r'''
This file will import a Gmsh format mesh from a file.  Alternatively, the mesh structure may be passed in as as arguments:

``coordinates`` is a float list of positions in the mesh.  Each coordinate adds an x, y, and z position so that the coordinate list length is 3 times the number of coordinates.

``physical_names`` is a list of contact, interface, and region names.  It is referenced by index by the ``elements`` list. 

``elements`` is a list of elements.  Each element adds

* Element Type (float)

  - 0 node
  - 1 edge 
  - 2 triangle
  - 3 tetrahedron

* Physical Index

  - This indexes into the ``physical_names`` list.

* Nodes

  - Each node of the element indexes into the coordinates list.

''',
},
{
"name" : "add_gmsh_contact",
"description" : "Create a mesh to import a Gmsh mesh",
"parameters" : (
("gmsh_name", "physical group name in the Gmsh file", required, string, None, None),
("material", "material for the contact being created", required, string, None, None),
("mesh", "name of the mesh being generated", required, string, None, None),
("name", "name of the contact begin created", required, string, None, None),
("region", "region that the contact is attached to", required, string, None, None),
)
},
{
"name" : "add_gmsh_interface",
"description" : "Create an interface for an imported Gmsh mesh",
"parameters" : (
("gmsh_name", "physical group name in the Gmsh file", required, string, None, None),
("mesh", "name of the mesh being generated", required, string, None, None),
("name", "name of the interface begin created", required, string, None, None),
("region0", "first region that the interface is attached to", required, string, None, None),
("region1", "second region that the interface is attached to", required, string, None, None),
)
},
{
"name" : "add_gmsh_region",
"description" : "Create a region for an imported Gmsh mesh",
"parameters" : (
("gmsh_name", "physical group name in the Gmsh file", required, string, None, None),
("mesh", "name of the mesh being generated", required, string, None, None),
("region", "name of the region begin created", required, string, None, None),
("material", "material for the region being created", required, string, None, None),
)
},
{
"name" : "create_1d_mesh",
"description" : "Create a mesh to create a 1D device",
"parameters" : (
("mesh", "name of the 1D mesh being created", required, string, None, None),
)
},
{
"name" : "finalize_mesh",
"description" : "Finalize a mesh so no additional mesh specifications can be added and devices can be created.",
"parameters" : (
("mesh", "Mesh to finalize", required, string, None, None),
)
},
{
"name" : "add_1d_mesh_line",
"description" : "Add a mesh line to a 1D mesh",
"parameters" : (
("mesh", "Mesh to add the line to", required, string, None, None),
("tag", "Text label for the position", optional, string, None, None),
("pos", "Position for the mesh point", required, string, None, None),
("ns", "Spacing from this point in the negative direction", optional, Float, "ps value" , None),
("ps", "Spacing from this point in the positive direction", required, Float, None, None),
)
},
{
"name" : "add_1d_interface",
"description" : "Add an interface to a 1D mesh",
"parameters" : (
("mesh", "Mesh to add the interface to", required, string, None, None),
("tag", "Text label for the position to add the interface", required, string, None, None),
("name", "Name for the interface being created", required, string, None, None),
)
},
{
"name" : "add_1d_contact",
"description" : "Add a contact to a 1D mesh",
"parameters" : (
("material", "material for the contact being created", required, string, None, None),
("mesh", "Mesh to add the contact to", required, string, None, None),
("name", "Name for the contact being created", required, string, None, None),
("tag", "Text label for the position to add the contact", required, string, None, None),
)
},
{
"name" : "add_1d_region",
"description" : "Add a region to a 1D mesh",
"parameters" : (
("mesh", "Mesh to add the line to", required, string, None, None),
("tag1", "Text label for the position bounding the region being added", required, string, None, None),
("tag2", "Text label for the position bounding the region being added", required, string, None, None),
("region", "Name for the region being created", required, string, None, None),
("material", "Material for the region being created", required, string, None, None),
)
},
{
"name" : "create_2d_mesh",
"description" : "Create a mesh to create a 2D device",
"parameters" : (
("mesh", "name of the 2D mesh being created", required, string, None, None),
)
},
{
"name" : "add_2d_mesh_line",
"description" : "Add a mesh line to a 2D mesh",
"parameters" : (
("mesh", "Mesh to add the line to", required, string, None, None),
("pos", "Position for the mesh point", required, string, None, None),
("ns", "Spacing from this point in the negative direction", required, Float, "ps value", None),
("ps", "Spacing from this point in the positive direction", required, Float, None, None),
)
},
{
"name" : "add_2d_region",
"description" : "Add a region to a 2D mesh",
"parameters" : (
("mesh", "Mesh to add the region to", required, string, None, None),
("region", "Name for the region being created", required, string, None, None),
("material", "Material for the region being created", required, string, None, None),
xl_option,
xh_option,
yl_option,
yh_option,
bloat_option,
)
},
{
"name" : "add_2d_interface",
"description" : "Add an interface to a 2D mesh",
"parameters" : (
("mesh", "Mesh to add the interface to", required, string, None, None),
("name", "Name for the interface being created", required, string, None, None),
("region0", "Name of the region included in the interface", required, string, None, None),
("region1", "Name of the region included in the interface", required, string, None, None),
xl_option,
xh_option,
yl_option,
yh_option,
bloat_option,
)
},
{
"name" : "add_2d_contact",
"description" : "Add an interface to a 2D mesh",
"parameters" : (
("name", "Name for the contact being created", required, string, None, None),
("material", "material for the contact being created", required, string, None, None),
("mesh", "Mesh to add the contact to", required, string, None, None),
("region", "Name of the region included in the contact", required, string, None, None),
xl_option,
xh_option,
yl_option,
yh_option,
bloat_option,
)
},
{
"name" : "create_device",
"description" : "Create a device from a mesh",
"parameters" : (
("mesh", "name of the mesh being used to create a device", required, string, None, None),
("device", "name of the device being created", required, string, None, None),
)
},
{
"name" : "load_devices",
"description" : r"Load devices from a DEVSIM file",
"parameters" : (
("file", "name of the file to load the meshes from", required, string, None, None),
)
},
{
"name" : "write_devices",
"description" : "Write a device to a file for visualization or restart",
"parameters" : (
("file", "name of the file to write the meshes to", required, string, None, None),
("device", "name of the device to write", optional, string, None, None),
("type", "format to use", optional, option, "devsim", (
("devsim", r"DEVSIM format"),
("devsim_data", r"DEVSIM output format with numerical data for all models"),
("floops", r"Floops format (for visualization in Postmini)"),
("tecplot", r"Tecplot format (for visualization in Tecplot)"),
("vtk", r"VTK format (for visualization in Paraview and VisIt)"),
)
),
)
},
{
"name" : "create_contact_from_interface",
"description" : "Creates a contact on a device from an existing interface",
"parameters" : (
("device", device_option_text, required, string, None, None),
("region", region_option_text, required, string, None, None),
("interface", interface_option_text, required, string, None, None),
("material", "material for the contact being created", required, string, None, None),
("name", "name of the contact begin created", required, string, None, None),
)
},

)
}

