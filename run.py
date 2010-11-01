print "Hello, world"
import os, sys, types, re, fnmatch, itertools
import scriptutil as SU

flist = SU.ffind('.', shellglobs=('*.h', '*.hpp', '*.cc'))
if type(flist) == types.DictType:
  for f in sorted(flist.keys()):
    sys.stdout.write("%s\n%s\n" % (flist[f],f))
else:
  for f in sorted(flist):
    sys.stdout.write("%s\n" % f)
    sys.argv = [0,f] 
    execfile('cpplint.py')
    '''print sys.argv'''


'''
rootPath = './'
pattern = '*.hpp' 

for root, dirs, files in os.walk(rootPath):
  for filename in fnmatch.filter(files, pattern):
    new_name=os.path.join(root, filename)
    print new_name
'''
