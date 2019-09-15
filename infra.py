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
#infra=re.findall('infra=.+?}', whole_thing, re.DOTALL)
#pdb.set_trace()
#s = p.sub(infra, s)
#s = re.sub(infra, 's', 'z')
#new_file=re.sub('infra=.+?}', 'infra={10.000 10.000}', whole_thing, re.DOTALL)
pattern=re.compile('infra=.+?}', re.MULTILINE|re.DOTALL)
new_file=pattern.sub("infra={10.000 10.000}",whole_thing)
outFile = open('outFile.hoi3', 'w')
outFile.write(new_file)
text_file.close()
outFile.close()
os.remove(input_file)
os.rename('outFile.hoi3', input_file)
print 'Finished making edits for', sys.argv[0]
