print "Hello, world"
import fnmatch
import scriptutil as SU
import os
import re

flist = SU.ffind('.', shellglobs=('*.py', '*.hpp'))
SU.printr(flist)

rootPath = './'
pattern = '*.py|*.hpp' 

for root, dirs, files in os.walk(rootPath):
  for filename in fnmatch.filter(files, pattern):
    '''print os.path.join(root, filename)'''
    new_name=os.path.join(root, filename)
    print new_name
