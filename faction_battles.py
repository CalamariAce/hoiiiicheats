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
      land_battles_match = re.search('land_battles_fought=',line)
      air_battles_match = re.search('air_battles_fought=',line)
      naval_battles_match = re.search('naval_battles_fought=',line)
      if land_battles_match:
        line = 'land_battles_fought=251\n'
      elif air_battles_match:
        line = 'air_battles_fought=251\n'
      elif naval_battles_match:
        line = 'naval_battles_fought=251\n'
  if not delay_write:
    outFile.write(line)
text_file.close()
outFile.close()
os.rename('outFile.hoi3', input_file)
print 'Finished making edits for', sys.argv[0]
