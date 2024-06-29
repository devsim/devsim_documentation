import sys
import shutil

destfile = sys.argv[1]
oldfile = destfile + ".bak"

shutil.copy(destfile, oldfile)


opts =  {
          '-' : ('*', '*'),
          '~' : (None, '='),
          '^' : (None, '-'),
          '"' : (None, '^'),
        }

buffer = None
ifile = open(oldfile, 'r')
with open(destfile, 'w') as ofile:
    buffer = next(ifile).rstrip()
    for line in ifile:
        line = line.rstrip()
        if buffer is None:
            break
        elif (buffer == '' or (len(buffer) != len(line))) and (len(list(set(line))) != 1):
            print(buffer, file=ofile)
            buffer = line
        elif (len(list(set(line))) == 1) and (line[0] in opts):
            prefix, suffix = opts[line[0]]   
            if prefix is not None:
                print(prefix * len(buffer), file=ofile) 
            print(buffer, file=ofile)
            if suffix is not None:
                print(suffix * len(buffer), file=ofile) 
            buffer = next(ifile).rstrip()
        else:
            print(buffer, file=ofile)
            buffer = line
    if buffer is not None:
        print(buffer, file=ofile)
