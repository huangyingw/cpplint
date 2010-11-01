print "Hello, world"
import os

def dirEntries(dir_name, subdir, *args):
  fileList = []
  if os.path.isfile(dirfile):
  elif os.path.isdir(dirfile) and subdir:
       print "Accessing directory:", dirfile
  fileList.extend(dirEntries(dirfile, subdir, *args))
  return fileList
