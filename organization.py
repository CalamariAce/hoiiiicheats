#!/usr/bin/env python
import re
import pdb
import os
import sys
if len(sys.argv) > 1:
  input_file=sys.argv[1]
else:
  input_file='soviet_losing_japan_ally.hoi3'
if len(sys.argv) > 2:
  nation=sys.argv[2]
else:
  nation='SOV'
if len(sys.argv) > 3:
  value=sys.argv[3]
else:
  value='222.222'
text_file = open(input_file, "r")
whole_thing = text_file.read()
text_file.close()
text_file = open(input_file, "r")
outFile = open('outFile.hoi3', 'w')
match_nation_flag=False
delay_write=False
reached_end=False
entered_subelement=False
for idx, line in enumerate(text_file):
  if not reached_end:
    if re.match('[A-Z][A-Z][A-Z]=*',line) and match_nation_flag:
      reached_end=True
    if re.match(nation + '=*',line):
      match_nation_flag=True
    if match_nation_flag:
      organisation = re.search('organisation=[0-9]',line)
      if organisation:
        line='organisation=' + value + '\n'
  if not delay_write:
    outFile.write(line)
text_file.close()
outFile.close()
os.rename('outFile.hoi3', input_file)
print 'Finished making edits for', sys.argv[0]
