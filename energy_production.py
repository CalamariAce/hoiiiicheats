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
  multiplier=float(sys.argv[3])
else:
  multiplier=7
text_file = open(input_file, "r")
whole_thing = text_file.read()
text_file.close()
text_file = open(input_file, "r")
outFile = open('outFile.hoi3', 'w')
match_nation_flag=False
delay_write=False
reached_end_of_provinces=False
entered_subelement=False
for idx, line in enumerate(text_file):
  if re.match('REB=',line):
    reached_end_of_provinces=True
  if not reached_end_of_provinces:
    if re.match('[0-9]*=',line):
      match_nation_flag=False
    if re.search('controller="' + nation + '"',line):
      match_nation_flag=True
    if match_nation_flag:
      if re.search('current_producing=',line):
        entered_subelement=True
      if entered_subelement:
        if re.search( '\W}', line):
          entered_subelement=False
        energy_match = re.search('energy=',line)
        if energy_match:
          line='energy=' + str(float(line[energy_match.end():re.search('[0-9].[0-9]*',line[energy_match.end():]).end()+energy_match.end()]) * multiplier) + '\n'
  if not delay_write:
    outFile.write(line)
text_file.close()
outFile.close()
os.rename('outFile.hoi3', input_file)
print 'Finished making edits for', sys.argv[0]
