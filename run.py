import os, sys, types, re, fnmatch, itertools
import scriptutil as SU
import cpplint as cl 

flist = SU.ffind('.', shellglobs=('*.h', '*.cc'))
if type(flist) == types.DictType:
  for f in sorted(flist.keys()):
    sys.stdout.write("%s\n%s\n" % (flist[f],f))
else:
    sys.argv = flist
    execfile('cpplint.py')
