from commandCommon import *

Command = {
    "name" : "Geometry",
  "description" : "Commands for getting information about the device structure.",
  "commands" : (
      {
          "name" : "get_device_list",
          "description" : "Gets a list of devices on the simulation.",
          "parameters" : (
          )
      },
      {
          "name" : "get_region_list",
          "description" : "Gets a list of regions on a device, contact, or interface.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("contact", "If specified, gets the name of the region belonging to this contact on the device", optional, string, None, None),
              ("interface", "If specified, gets the name of the regions belonging to this interface on the device", optional, string, None, None),
          )
      },
      {
          "name" : "get_interface_list",
          "description" : "Gets a list of interfaces on a device.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
          )
      },
      {
          "name" : "get_contact_list",
          "description" : "Gets a list of contacts on a device.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
          )
      },
      {
          "name" : "get_element_node_list",
          "description" : "Gets a list of nodes for each element on a device, region, contact, or interface.",
          "parameters" : (
              ("device", device_option_text, required, string, None, None),
              ("region", region_option_text, required, string, None, None),
              ("contact", "If specified, gets the element nodes for the contact on the specified region", optional, string, None, None),
              ("interface", "If specified, gets the element nodes for the interface on the specified region", optional, string, None, None),
              ("reorder", "If specified, reorders the element nodes in a manner compatible in meshing software", optional, boolean, False, None),
          )
      },
  )
}

