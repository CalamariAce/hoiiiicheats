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
global amount
if len(sys.argv) > 3:
  amount=str(sys.argv[3])
else:
  amount='99.000'
text_file = open(input_file, "r")
whole_thing = text_file.read()
text_file.close()
text_file = open(input_file, "r")
outFile = open('outFile.hoi3', 'w')
match_nation_flag=False
delay_write=False
reached_end=False
entered_subelement=False
def yays(search_pattern,line):
  if re.search(search_pattern,line):
    return search_pattern + amount + '\n'
  else:
    return False
for idx, line in enumerate(text_file):
  if not reached_end:
    if re.match('[A-Z][A-Z][A-Z]=*',line) and match_nation_flag:
      reached_end=True
    if re.match(nation + '=*',line):
      match_nation_flag=True
    if match_nation_flag:
      result=yays('infantry_theory=',line)
      if result: line = result
      result=yays('militia_theory=',line)
      if result: line = result
      result=yays('mobile_theory=',line)
      if result: line = result
      result=yays('artillery_theory=',line)
      if result: line = result
      result=yays('rocket_science=',line)
      if result: line = result
      result=yays('submarine_engineering=',line)
      if result: line = result
      result=yays('electornicegineering_theory=',line)
      if result: line = result
      result=yays('aeronautic_engineering=',line)
      if result: line = result
      result=yays('automotive_theory=',line)
      if result: line = result
      result=yays('spearhead_theory=',line)
      if result: line = result
      result=yays('superior_firepower_theory=',line)
      if result: line = result
      result=yays('grand_battleplan_theory=',line)
      if result: line = result
      result=yays('human_wave_theory=',line)
      if result: line = result
      result=yays('base_strike_doctrine=',line)
      if result: line = result
      result=yays('fleet_in_being_doctrine=',line)
      if result: line = result
      result=yays('sealane_interdiction_doctrine=',line)
      if result: line = result
      result=yays('fighter_focus=',line)
      if result: line = result
      result=yays('cas_focus=',line)
      if result: line = result
      result=yays('tac_focus=',line)
      if result: line = result
      result=yays('nav_focus=',line)
      if result: line = result
      result=yays('strategic_air_focus=',line)
      if result: line = result
      result=yays('mechanicalengineering_theory=',line)
      if result: line = result
      result=yays('chemical_engineering=',line)
      if result: line = result
      result=yays('jetengine_theory=',line)
      if result: line = result
      result=yays('nuclear_physics=',line)
      if result: line = result
      result=yays('infantry_practical=',line)
      if result: line = result
      result=yays('militia_practical=',line)
      if result: line = result
      result=yays('mobile_practical=',line)
      if result: line = result
      result=yays('artillery_practical=',line)
      if result: line = result
      result=yays('rocket_practical=',line)
      if result: line = result
      result=yays('naval_engineering=',line)
      if result: line = result
      result=yays('destroyer_practical=',line)
      if result: line = result
      result=yays('cruiser_practical=',line)
      if result: line = result
      result=yays('capitalship_practical=',line)
      if result: line = result
      result=yays('carrier_practical=',line)
      if result: line = result
      result=yays('submarine_practical=',line)
      if result: line = result
      result=yays('electornicegineering_practical=',line)
      if result: line = result
      result=yays('armour_practical=',line)
      if result: line = result
      result=yays('single_engine_aircraft_practical=',line)
      if result: line = result
      result=yays('twin_engine_aircraft_practical=',line)
      if result: line = result
      result=yays('four_engine_aircraft_practical=',line)
      if result: line = result
      result=yays('land_doctrine_practical=',line)
      if result: line = result
      result=yays('naval_doctrine_practical=',line)
      if result: line = result
      result=yays('air_doctrine_practical=',line)
      if result: line = result
      result=yays('jetengine_practical=',line)
      if result: line = result
      result=yays('nuclear_bomb=',line)
      if result: line = result
      result=yays('transport_practical=',line)
      if result: line = result
      result=yays('construction_practical=',line)
      if result: line = result
  if not delay_write:
    outFile.write(line)
text_file.close()
outFile.close()
os.rename('outFile.hoi3', input_file)
print 'Finished making edits for', sys.argv[0]
