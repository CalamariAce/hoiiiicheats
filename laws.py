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
for idx, line in enumerate(text_file):
  if not reached_end:
    if re.match('[A-Z][A-Z][A-Z]=*',line) and match_nation_flag:
      reached_end=True
    if re.match(nation + '=*',line):
      match_nation_flag=True
    if match_nation_flag:
      civil_law = re.search('civil_law=',line)
      conscription_law = re.search('conscription_law=',line)
      economic_law = re.search('economic_law=',line)
      education_investment_law = re.search('education_investment_law=',line)
      industrial_policy_laws = re.search('industrial_policy_laws=',line)
      press_laws = re.search('press_laws=',line)
      training_laws = re.search('training_laws=',line)
      if civil_law:
        line = 'civil_law=totalitarian_system\n'
      elif conscription_law:
        line = 'conscription_law=service_by_requirement\n'
      elif economic_law:
        line = 'economic_law=total_economic_mobilisation\n'
      elif education_investment_law:
        line = 'education_investment_law=big_education_investment\n'
      elif industrial_policy_laws:
        line = 'industrial_policy_laws=heavy_industry_emphasis\n'
      elif press_laws:
        line = 'press_laws=propaganda_press\n'
      elif training_laws:
        line = 'training_laws=specialist_training\n'
  if not delay_write:
    outFile.write(line)
text_file.close()
outFile.close()
os.remove(input_file)
os.rename('outFile.hoi3', input_file)
print 'Finished making edits for', sys.argv[0]
