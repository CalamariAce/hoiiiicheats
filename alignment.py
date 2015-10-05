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
  faction=sys.argv[3]
else:
  faction='comintern'
if faction == 'comintern':
  xval = '-200.000'
  yval = '200.000'
elif faction == 'allies':
  xval = '0.000'
  yval = '-146.000'
elif faction == 'axis':
  xval = '200.000'
  yval = '200.000'
else:
  print "Do not recognize the faction you specified: " + faction
  print "Faction must be `comintern`, `allies`, or `axis`"
  sys.exit(1)
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
    if re.match('[A-Z][A-Z][A-Z]=*',line) and match_nation_flag and nation != 'all':
      reached_end=True
    if re.match(nation + '=*',line):
      match_nation_flag=True
    if match_nation_flag or nation == 'all':
      if re.search('position=',line):
        delay_write=True
      if delay_write:
        if re.search('}',line):
          delay_write=False
          line='position={x=' + xval + ' y=' + yval + '}\n'
  if not delay_write:
    outFile.write(line)
text_file.close()
outFile.close()
os.rename('outFile.hoi3', input_file)
print 'Finished making edits for', sys.argv[0]
