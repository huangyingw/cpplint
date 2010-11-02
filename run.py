import os, sys, types, re, fnmatch, itertools
import scriptutil as SU
import cpplint as cl 

flist = SU.ffind('.', shellglobs=('*.h', '*.hpp', '*.cc'))
if type(flist) == types.DictType:
  for f in sorted(flist.keys()):
    sys.stdout.write("%s\n%s\n" % (flist[f],f))
else:
  for f in sorted(flist):
    ''' sys.stdout.write("%s\n" % f)''' 
    file_name=f
    cl.main(f)
    '''execfile('cpplint.py')'''
    print file_name 


'''
rootPath = './'
pattern = '*.hpp' 

for root, dirs, files in os.walk(rootPath):
  for filename in fnmatch.filter(files, pattern):
    new_name=os.path.join(root, filename)
    print new_name
'''
