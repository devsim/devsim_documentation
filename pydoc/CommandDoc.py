import io
import commandCommon
import sys

import circuitCommands
import equationCommands
import geometryCommands
import materialCommands
import meshingCommands
import modelCommands
import solverCommands

#### TODO: handle OPTION for option list commands
#### replace expanded strings with macros wherever possible
# enforce use of option
Commands= (
    circuitCommands.Command,
    equationCommands.Command,
    geometryCommands.Command,
    materialCommands.Command,
    meshingCommands.Command,
    modelCommands.Command,
    solverCommands.Command,
)


## this string is printed in verbatim
#def printTexCommandString(ofh, command, print_verbatim=True):
#  if print_verbatim:
#    print >>ofh, r'\begin{verbatim}'
#  commandname = command["name"]
#  ret = "devsim."+commandname + " ("
#  parameters = command['parameters']
#  if len(parameters) == 0:
#    ret = ret + ")"
#  else:
#    for e, i in enumerate(parameters):
#      nstring=""
#      nstring=nstring + i[0] + "=" + i[3]
#      if e < len(parameters) - 1:
#        nstring = nstring + ", "
#
#      if e == len(command['parameters']) - 1:
#        nstring = nstring + ")"
#      if len(ret) + len(nstring) > 72:
#        print >>ofh, ret
#        ret = "    "
#      ret = ret + nstring
#  if ret:
#    print >>ofh, ret
#  if print_verbatim:
#    print >>ofh, r'\end{verbatim}'
#    
#def printTexCommandTable(ofh, command):
#  print >>ofh, r'\begin{commandTable}'
#  for i in command['parameters']:
#    paramname = TexEscape(i[0])
#    descstring = TexEscape(i[1])
#    required_string=''
#    if i[2] in (commandCommon.required, commandCommon.optional):
#      required_string=i[2]
#    default_string=''
#    if i[4]:
#      svalue=TexEscape(i[4])
#      if i[3] in (commandCommon.string, commandCommon.option):
#        svalue='"' + svalue + '"'
#      elif i[3] in (commandCommon.Float, commandCommon.integer):
#        pass
#      else:
#        raise RuntimeError("Unknown type: " + i[3])
#      default_string="(%s default)" % (svalue,)
#    print >>ofh, r'\specialoption{%s}{%s %s %s}' % (paramname, descstring, required_string, default_string)
#    if i[5]:
#      for j in i[5]:
#        print >>ofh, r'\textoption{%s}{%s}' % (TexEscape(j[0]), TexEscape(j[1]))
#  print >>ofh, r'\end{commandTable}'
#
#def camelCase(name):
#  index=0
#  ret = ""
#  while True:
#    nindex = name.find('_', index)
#    if nindex == -1:
#      if index == 0:
#        ret = name
#      else:
#        ret = ret + name[index].upper() +  name[index+1:]
#      break
#    else:
#      if index == 0:
#        ret = ret + name[index:nindex]
#      else:
#        ret = ret + name[index].upper() + name[index+1:nindex]
#      index = nindex + 1
#  return ret
#
#def TexEscape(name):
#  # this function is now more complicated to handle verbatim mode
#  if name.find(r'\begin{verbatim}') == -1:
#    return name.replace('_', '\_')
#  else:
#    out = ""
#    in_verbatim = False
#    for line in name.splitlines():
#      if in_verbatim:
#        if line.find(r'\end{verbatim}') > -1:
#          in_verbatim = False
#        out = out + line + '\n'
#      elif line.find(r'\begin{verbatim}') > -1:
#        in_verbatim = True
#        out = out + line + '\n'
#      else:
#        out = out + line.replace('_', '\_') + '\n'
#    return out
#
#def printTexCommand(ofh, sectionname, command):
#  for k in command.keys():
#    if k not in ("name", "description", "long_description", "parameters"):
#      raise RuntimeError("Unexpected key: " + k)
#  try:
#    commandname = command["name"].lower()
#    labelname = sectionname.lower() + "Commands:" + camelCase(commandname)
#    mydict = {
#      "sectionname" : sectionname,
#      "commandname" : commandname,
#      "esccommandname" : TexEscape(commandname),
#      "labelname" : labelname,
#    }
#    print >>ofh, '''
#  %%%%%%
#  %%%%%% %(commandname)s
#  %%%%%%
#  \commandSection{%(esccommandname)s\label{%(labelname)s}}\index{Commands!%(sectionname)s!%(esccommandname)s@\commandName{%(esccommandname)s}}\
#  ''' % mydict
#    print >>ofh, "\n\\noindent "+TexEscape(command["description"])
#    printTexCommandString(ofh, command)
#    printTexCommandTable(ofh, command)
#    if "long_description" in command:
#      print >>ofh, "\n" + r"~\\~\\" + TexEscape(command["long_description"])
#  except Exception as e:
#    raise RuntimeError("Error while processing commmand: " + commandname + "\n" + str(e))
#
#def printTexSection(ofh, command):
#  mydict = {
#    "sectionname" : command["name"],
#    "sectionlcname" : command["name"].lower(),
#    "sectiondescription" : command["description"],
#  }
#  #### Section Header
#  print >>ofh, '''\
#\section{%(sectionname)s commands\label{%(sectionlcname)sCommands}}\index{Commands!%(sectionname)s|(}
#%(sectiondescription)s\
#''' % (mydict)
#
#  for i in sorted(command["commands"], key=lambda x : x["name"]):
#    printTexCommand(ofh, mydict["sectionname"], i)
#
#  #### Section Footer
#  print >>ofh, '''\
#\index{Commands!%(sectionname)s|)}\
#''' % (mydict)

def printCppMultiline(ofh, csb):
    #s = CppEscape(csb.getvalue())
    #for l in s.splitlines():
    #    print(r'"%s\n"' % l, file=ofh) 
    ofh.write('R"(');
    ofh.write(csb.getvalue())
    ofh.write(')"');

def printCppCommand(ofh, sectionname, command):
    for k in list(command.keys()):
        if k not in ("name", "description", "long_description", "parameters"):
            raise RuntimeError("Unexpected key: " + k)
    try:
        commandname = command["name"].lower()

        print("\nstatic const char %s_doc[] =" % commandname, file=ofh)
        csb = io.StringIO()
        printPyCommand(csb, sectionname, command, False)
        printCppMultiline(ofh, csb)
        print(";", file=ofh)
    except Exception as e:
        #raise RuntimeError("Error while processing commmand: " + commandname + "\n" + str(e))
        raise

#def CppEscape(s):
#    return s.replace('\\', '').replace('"', '\\\"')

#def printCppCommandTable(ofh, command):
#  #print >>ofh, r'\begin{commandTable}'
#  print >>ofh
#  paramwidth=10
#  for i in command['parameters']:
#    paramname = CppEscape(i[0])
#    paramwidth=max(paramwidth, len(paramname))
#    
#  #paramwidth = max(10, max([len(CppEscape(i[0]) for i in command['parameters'])]))
#  for i in command['parameters']:
#    paramname = CppEscape(i[0])
#    descstring = CppEscape(i[1])
#    required_string=''
#    if i[2] in (commandCommon.required, commandCommon.optional):
#      required_string=i[2]
#    default_string=''
#    if i[4]:
#      svalue=CppEscape(i[4])
#      if i[3] in (commandCommon.string, commandCommon.option):
#        svalue=r'\"' + svalue + r'\"'
#      elif i[3] in (commandCommon.Float, commandCommon.integer):
#        pass
#      else:
#        raise RuntimeError("Unknown type: " + i[3])
#      default_string="(%s default)" % (svalue,)
#    print >>ofh, r'%s= %s %s %s' % (paramname.ljust(10), descstring, required_string, default_string)
#    if i[5]:
#      for j in i[5]:
#        print >>ofh, r'  %s %s' % (CppEscape(j[0]).ljust(15), CppEscape(j[1]))
#  #print >>ofh, r'\end{commandTable}'

def printCppDoc(ofh, command):
    mydict = {
        "sectionname" : command["name"],
      "sectionlcname" : command["name"].lower(),
      "sectiondescription" : command["description"],
    }
    for i in sorted(command["commands"], key=lambda x : x["name"]):
        printCppCommand(ofh, mydict["sectionname"], i)

def PyEscape(s):
    return s.replace('\\', '').replace('"', '\'')

def printPyCommandString(ofh, command):
    commandname = command["name"]
    ofh.write("devsim."+commandname + " (")
    ofh.write(", ".join([p[0] for p in command['parameters']]))
    ofh.write(")\n")

def printPyDescription(ofh, command):
    ofh.write("\n" + PyEscape(command["description"]) + "\n")

def printPyParameters(ofh, command):
    if not command["parameters"]:
        return
    ofh.write('''
Parameters
----------
''')
    # TODO handle strings in quotes
    # escape params
    # put all default values for optional
    # put descriptions
    # put long descriptions
    for param in command["parameters"]:
        ofh.write(param[0] + " : ")
        if param[3] != commandCommon.option and param[5] != None:
            raise RuntimeError('Set option for "%s" "%s"' % (command["name"], param[0],))
        if param[3] == commandCommon.option:
            default_value = None
            if param[2] == commandCommon.optional:
                default_value = param[4]
                if not param[4]:
                    raise RuntimeError("ISSUE")
            options = [p[0] for p in param[5] if p[0] != default_value]
            if default_value:
                options[:0] = (default_value,)
            options = ["'" + p + "'" for p in options]
            ofh.write('{' + ", ".join(options) + "}")
            if not default_value:
                ofh.write(' required')
            #pass
            #if param[2] == commandCommon.optional:
            #  ofh.write(""
            #if param[2] == commandCommon.required:
            #  raise RuntimeError("2")
            #else:
            #  raise RuntimeError("3")
        else:
            ofh.write(commandCommon.pymap[param[3]])
            if param[2] == commandCommon.optional:
                ofh.write(', optional')
        ofh.write('\n')
        ofh.write('   ' + PyEscape(param[1]))
        if param[2] == commandCommon.optional and param[3] != commandCommon.option:
            pt = param[3]
            pv = param[4]
            if pv is not None:
                dv = None
                if not pt:
                    raise RuntimeError("ISSUE 2 " + str(param))
                if pt == commandCommon.string:
                    dv = "'" + pv + "'"
                elif pt in (commandCommon.Float, commandCommon.integer):
                    dv = pv
                elif pt == commandCommon.boolean:
                    dv = str(pv)
                else:
                    raise RuntimeError("missing type " + str(param))
                ofh.write(" (default %s)" % dv)

        ofh.write('\n')
        #if param[2] == commandCommon.required:
        #  pass
        #elif param[2] == commandCommon.optional:
        #  pass
        #else:
        #  raise RuntimeError("Issue! " + str(param))

# Follow guide from https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
# TODO return values
def printPyCommand(ofh, sectionname, command, print_def):
    for k in list(command.keys()):
        if k not in ("name", "description", "long_description", "parameters"):
            raise RuntimeError("Unexpected key: " + k)
    try:
        commandname = command["name"].lower()
        if print_def:
            mydict = {
                "commandname" : commandname,
            }
            ofh.write("\ndef %(commandname)s (**kwargs):\n" % mydict)
        csb = io.StringIO()
        if print_def:
            csb.write("'''\n")
        printPyCommandString(csb, command)
        printPyDescription(csb, command)
        printPyParameters(csb, command)
        if "long_description" in command:
            csb.write('''
Notes
-----
''')
            for line in command['long_description'].splitlines():
                csb.write(line + "\n")
        if print_def:
            csb.write("'''\n")
            csb.write("pass\n")
        for line in csb.getvalue().splitlines():
            if line:
                ofh.write("    " + line)
            ofh.write("\n")
    except Exception as e:
        #raise RuntimeError("Error while processing commmand: " + commandname + "\n" + str(e))
        raise

def printPyDoc(ofh, command):
    mydict = {
        "sectionname" : command["name"],
      "sectionlcname" : command["name"].lower(),
      "sectiondescription" : command["description"],
    }
    for i in sorted(command["commands"], key=lambda x : x["name"]):
        printPyCommand(ofh, mydict["sectionname"], i, print_def=True)

#for command in Commands:
#  filename=command["name"].lower() + "Commands.tex"
#  with open(filename, "w") as ofh:
#    printTexSection(ofh, command)

filename="DevsimDoc.cc"
with open(filename, "w") as ofh:
    for command in Commands:
        printCppDoc(ofh, command)

filename="devsim.py"
with open(filename, "w") as ofh:
    for command in Commands:
        printPyDoc(ofh, command)

filename="CommandReference.rst"
with open(filename, "w") as ofh:
    ofh.write('''
*****************
Command Reference
*****************
''')
    ofh.write('''
.. automodule:: devsim
   :no-members:
''')

    for command in Commands:
        mydict = {
            "sectionname" : command["name"],
          "sectionlcname" : command["name"].lower(),
          "sectiondescription" : command["description"],
        }


    for command in Commands:
        refname = '\n.. _' + command["name"] + "Commands:"
        ofh.write(refname + '\n\n')
        head = command["name"] + " commands"
        head = head + '\n' + '=' * len(head) + '\n\n'
        ofh.write(head)
        ofh.write(command["description"] + "\n\n")
        # https://stackoverflow.com/questions/61374995/sphinx-with-autodoc-duplicate-object-description-warning-when-grouping-members
        methods = [i['name'] for i in sorted(command["commands"], key=lambda x : x["name"])]
        #methods = ', '.join([i['name'] for i in sorted(command["commands"], key=lambda x : x["name"])])
        #print methods
        ofh.write('''
.. currentmodule:: devsim
''')
        for method in methods:
            ofh.write(".. autofunction:: %s\n" % (method,))
        ofh.write('\n\n')



