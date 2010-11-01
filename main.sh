#! /bin/bash

find . \( -name \.svn -o -name \.git -o -name \.hg \) -prune -o \( -name \*\.c -o -name \*\.cc -o -name \*\.cpp -o -name \*\.hpp -o -name \*\.h \) | while read ss; do
  if [ `./cpplint.py $ss` -ne 0 ]; then
    echo $ss has style error
  fi
done

