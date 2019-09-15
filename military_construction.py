#!/usr/bin/env python
import re
import pdb
import os
import sys
if len(sys.argv) > 1:
  input_file=sys.argv[1]
else:
  print 'Error: No .hoi3 save file was provided.'
  sys.exit(2)
if len(sys.argv) > 2:
  nation=sys.argv[2]
else:
  print 'Error: No capitalized 3-letter nation code was provided.'
  sys.exit(2)
text_file = open(input_file, "r")
whole_thing = text_file.read()
text_file.close()
text_file = open(input_file, "r")
outFile = open('outFile.hoi3', 'w')
match_nation_flag=False
delay_write=False
reached_end=False
entered_subelement=False
stored_duration=False
for idx, line in enumerate(text_file):
  if not reached_end:
    if re.match('[A-Z][A-Z][A-Z]=*',line) and match_nation_flag:
      reached_end=True
    if re.match(nation + '=*',line):
      match_nation_flag=True
    if match_nation_flag:
      if re.search('military_construction=',line) or re.search('building_construction=',line):
        entered_subelement=True
      reached_end = re.search('auto_maintain_convoy=',line)
      if entered_subelement:
        duration = re.search('duration=',line)
        if duration:
          stored_duration = line[duration.end():re.search('[0-9].[0-9]*',line[duration.end():]).end()+duration.end()]
          dur_idx = idx
        progress = re.search('progress=',line)
        if progress and idx == dur_idx + 1:
          line='progress=' + stored_duration + '\n'
  if not delay_write:
    outFile.write(line)
text_file.close()
outFile.close()
os.remove(input_file)
os.rename('outFile.hoi3', input_file)
print 'Finished making edits for', sys.argv[0]
