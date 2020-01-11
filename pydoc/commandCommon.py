device_option_text="The selected device"
region_option_text="The selected region"
contact_option_text= "Contact on which to apply this command"
interface_option_text= "Interface on which to apply this command"
optional="(optional)"
required="(required)"
string="STRING"
boolean="BOOL"
option="OPTION"
Float="FLOAT"
List="LIST"
integer="INTEGER"
anytype="ANY"

pymap = {
    string : "str",
  Float  : "Float",
  integer : "int",
  anytype : "any",
  List : "list",
  boolean : "bool",
}

xl_option = ("xl", "x position for corner of bounding box", optional, Float, "-MAXDOUBLE", None)
xh_option = ("xh", "x position for corner of bounding box", optional, Float, "+MAXDOUBLE", None)
yl_option = ("yl", "y position for corner of bounding box", optional, Float, "-MAXDOUBLE", None)
yh_option = ("yh", "y position for corner of bounding box", optional, Float, "+MAXDOUBLE", None)
bloat_option = ("bloat", "Extend bounding box by this amount when search for mesh to include in region", optional, Float, "1e-10", None)

def name_option(thing, verb):
    return "Name of the " + thing + " being " + verb

def equation_option(what):
    return "Equation used to describe the " + what

device_option_required = ("device", device_option_text, required, string, None, None)
device_option_optional = ("device", device_option_text, optional, string, None, None)
contact_option_required = ("contact", contact_option_text, required, string, None, None)
contact_option_optional = ("contact", contact_option_text, optional, string, None, None)
interface_option_required = ("interface", interface_option_text, required, string, None, None)
interface_option_optional = ("interface", interface_option_text, optional, string, None, None)
region_option_required = ("region", region_option_text, required, string, None, None)
region_option_optional = ("region", region_option_text, optional, string, None, None)

