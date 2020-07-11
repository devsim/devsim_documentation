from commandCommon import *

Command = {
    "name" : "Material",
  "description" : "Commands for manipulating parameters and material properties",
  "commands" : (
      {
          "name" : "get_dimension",
          "description" : "Get the dimension of the device",
          "parameters" : (
              device_option_optional,
          )
      },
      {
          "name" : "get_parameter",
          "description" : "Get a parameter on a region, device, or globally.",
          "long_description" : r'''
Note that the ``device`` and ``region`` options are optional.  If the region is not specified, the parameter is retrieved for the entire device.  If the device is not specified, the parameter is retrieved for all devices.  If the parameter is not found on the region, it is retrieved on the device.  If it is not found on the device, it is retrieved over all devices.
''',
          "parameters" : (
              device_option_optional,
              region_option_optional,
              ("name", name_option("parameter name", "retrieved"), required, string, None, None),
          )
      },
      {
          "name" : "get_parameter_list",
          "description" : "Get list of parameter names on region, device, or globally",
          "long_description" : r'''
Note that the ``device`` and ``region`` options are optional.  If the region is not specified, the parameter is retrieved for the entire device.  If the device is not specified, the parameter is retrieved for all devices.  Unlike the :meth:`devsim.getParameter`, parameter names on the the device are not retrieved if they do not exist on the region.  Similarly, the parameter names over all devices are not retrieved if they do not exist on the device.
''',
          "parameters" : (
              device_option_optional,
              region_option_optional,
          )
      },
      {
          "name" : "set_parameter",
          "description" : "Set a parameter on region, device, or globally",
          "long_description" : r'''
Note that the device and region options are optional.  If the region is not specified, the parameter is set for the entire device.  If the device is not specified, the parameter is set for all devices.
''',
          "parameters" : (
              device_option_optional,
              region_option_optional,
              ("name", name_option("parameter name", "retrieved"), required, string, None, None),
              ("value", "value to set for the parameter", required, anytype, None, None),
          )
      },
      {
          "name" : "get_material",
          "description" : "Returns the material for the specified region",
          "parameters" : (
              device_option_optional,
              region_option_optional,
              contact_option_optional,
          )
      },
      {
          "name" : "set_material",
          "description" : "Sets the new material for a region",
          "parameters" : (
              device_option_optional,
              region_option_optional,
              contact_option_optional,
              ("material", "New material name", required, string, None, None),
          )
      },
      {
          "name" : "create_db",
          "description" : "Create a database to store material properties",
          "parameters" : (
              ("filename", "filename to create for the db", required, string, None, None),
          )
      },
      {
          "name" : "open_db",
          "description" : "Open a database storing material properties",
          "parameters" : (
              ("filename", "filename to create for the db", required, string, None, None),
              ("permissions", "permissions on the db", optional, option, "readonly", (
                  ("readwrite", "Open file for reading and writing"),
                  ("readonly", "Open file for read only"),
              )
              ),
          )
      },
      {
          "name" : "close_db",
          "description" : "Closes the database so that its entries are no longer available",
          "parameters" : (),
      },
      {
          "name" : "save_db",
          "description" : "Saves any new or modified db entries to the database file",
          "parameters" : (),
      },
      {
          "name" : "add_db_entry",
          "description" : "Adds an entry to the database",
          "long_description" : r'''
The :meth:`devsim.save_db` command is used to commit these added entries permanently to the database.
''',
          "parameters" : (
              ("material", "Material name requested. ``global`` refers to all regions whose material does not have the parameter name specified", required, string, None, None),
              ("parameter", "Parameter name", required, string, None, None),
              ("value", "Value assigned for the parameter", required, string, None, None),
              ("unit", "String describing the units for this parameter name", required, string, None, None),
              ("description", "Description of the parameter for this material type.", required, string, None, None),
          )
      },
      {
          "name" : "get_db_entry",
          "description" : "This command returns a list containing the value, unit, and description for the requested material db entry",
          "parameters" : (
              ("material", "Material name", required, string, None, None),
              ("parameter", "Parameter name", required, string, None, None),
          )
      }
  )
}


