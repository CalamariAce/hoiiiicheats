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
  nation='all'
if len(sys.argv) > 3:
  nation2=sys.argv[3]
else:
  nation2='ENG'
if len(sys.argv) > 4:
  threat=str(sys.argv[4])
else:
  threat='999.999'
text_file = open(input_file, "r")
whole_thing = text_file.read()
text_file.close()
text_file = open(input_file, "r")
outFile = open('outFile.hoi3', 'w')
match_nation_flag=False
delay_write=False
reached_end=False
entered_subelement=False
match_nation2=False
for idx, line in enumerate(text_file):
  if not reached_end:
    if re.match('[A-Z][A-Z][A-Z]=*',line) and match_nation_flag and nation != 'all':
      reached_end=True
    if re.match(nation + '=*',line):
      match_nation_flag=True
    if match_nation_flag or nation == 'all':
      if re.search(nation2 + '=.*',line) and not re.match(nation2 + '=.*',line):
        match_nation2=True
      if match_nation2 and re.search('threat=[0-9]',line) and not re.search('highest_threat=',line):
        match_nation2=False
        match_nation_flag=False
        line='threat=' + threat + '\n'
      if re.search('ministers=',line):
        match_nation2=False
  if not delay_write:
    outFile.write(line)
text_file.close()
outFile.close()
os.rename('outFile.hoi3', input_file)
print 'Finished making edits for', sys.argv[0]
