#!/usr/bin/env python
import re
import pdb
import os
import sys
if len(sys.argv) > 1:
  input_file=sys.argv[1]
else:
  input_file = 'soviet_losing_japan_ally.hoi3'
if len(sys.argv) > 2:
  nation=sys.argv[2]
else:
  print 'Error: No capitalized 3-letter nation code was provided.'
  sys.exit(2)
text_file = open(input_file, "r")
whole_thing = text_file.read()
pattern=re.compile('infra=.+?}', re.MULTILINE|re.DOTALL)
new_file=pattern.sub("infra={10 10}",whole_thing)
outFile = open('outFile.hoi3', 'w')
outFile.write(new_file)