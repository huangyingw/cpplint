print "Hello, world"
import fnmatch
import os

rootPath = './'
pattern = '*.py' # Can include any UNIX shell-style wildcards

for root, dirs, files in os.walk(rootPath):
  for filename in fnmatch.filter(files, pattern):
    print os.path.join(root, filename)
