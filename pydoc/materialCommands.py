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
  )
}


