#!/usr/bin/env python
import re
import pdb
import os
import sys

global upgrade_type
global tech_increase_value

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
  
if len(sys.argv) > 3:
  ttype=sys.argv[3]
else:
  ttype='all'
#ttype = 'air'
#ttype = 'armor'
#ttype = 'sea'
#ttype = 'landing_craft'
#ttype = 'infantry'
#ttype = 'industry'
#ttype = 'secret'
#ttype = 'all'
#ttype = 'all_techs_under_research'

if len(sys.argv) > 4:
  tech_increase_value=int(sys.argv[4])
else:
  tech_increase_value=3
  
if len(sys.argv) > 5:
  upgrade_type=sys.argv[5]
else:
  upgrade_type='unrestricted'
#upgrade_type = 'unrestricted'
#upgrade_type = 'all_owned_techs'
  
if len(sys.argv) > 6:
  do_techtreeonly=sys.argv[6]
else:
  do_techtreeonly='True'

tech_dict = {
'single_engine_aircraft_design':1,
'twin_engine_aircraft_design':1,
'basic_aeroengine':1,
'basic_small_fueltank':1,
'basic_single_engine_airframe':1,
'basic_aircraft_machinegun':1,
'basic_medium_fueltank':1,
'basic_twin_engine_airframe':1,
'basic_bomb':1,
'multi_role_fighter_development':1,
'cas_development':1,
'nav_development':1,
'basic_four_engine_airframe':1,
'basic_strategic_bomber':1,
'aeroengine':12,
'small_fueltank':12,
'single_engine_airframe':12,
'single_engine_aircraft_armament':12,
'medium_fueltank':12,
'twin_engine_airframe':12,
'air_launched_torpedo':12,
'small_bomb':12,
'twin_engine_aircraft_armament':12,
'medium_bomb':12,
'large_fueltank':12,
'four_engine_airframe':12,
'strategic_bomber_armament':12,
'cargo_hold':12,
'large_bomb':12,
'advanced_aircraft_design':1,
'small_airsearch_radar':12,
'medium_airsearch_radar':12,
'large_airsearch_radar':12,
'small_navagation_radar':12,
'medium_navagation_radar':12,
'large_navagation_radar':12,
'drop_tanks':1,
'fighter_pilot_training':12,
'fighter_groundcrew_training':12,
'interception_tactics':12,
'fighter_ground_control':12,
'bomber_targerting_focus':12,
'fighter_targerting_focus':12,
'cas_pilot_training':12,
'cas_groundcrew_training':12,
'ground_attack_tactics':12,
'forward_air_control':12,
'battlefield_interdiction':12,
'tac_pilot_training':12,
'tac_groundcrew_training':12,
'interdiction_tactics':12,
'logistical_strike_tactics':12,
'installation_strike_tactics':12,
'airbase_strike_tactics':12,
'tactical_air_command':12,
'nav_pilot_training':12,
'nav_groundcrew_training':12,
'portstrike_tactics':12,
'navalstrike_tactics':12,
'naval_air_targeting':12,
'naval_tactics':12,
'heavy_bomber_pilot_training':12,
'heavy_bomber_groundcrew_training':12,
'strategic_bombardment_tactics':12,
'airborne_assault_tactics':12,
'strategic_air_command':12,
'aeronautic_engineering_research':12,
'lighttank_brigade':1,
'lighttank_gun':12,
'lighttank_engine':12,
'lighttank_armour':12,
'lighttank_reliability':12,
'tank_brigade':1,
'tank_gun':12,
'tank_engine':12,
'tank_armour':12,
'tank_reliability':12,
'heavy_tank_brigade':1,
'heavy_tank_gun':12,
'heavy_tank_engine':12,
'heavy_tank_armour':12,
'heavy_tank_reliability':12,
'armored_car_armour':12,
'armored_car_gun':12,
'SP_brigade':1,
'super_heavy_tank_brigade':1,
'super_heavy_tank_gun':12,
'super_heavy_tank_engine':12,
'super_heavy_tank_armour':12,
'super_heavy_tank_reliability':12,
'art_barrell_ammo':12,
'art_carriage_sights':12,
'at_barrell_sights':12,
'at_ammo_muzzel':12,
'aa_barrell_ammo':12,
'aa_carriage_sights':12,
'rocket_art':1,
'rocket_art_ammo':12,
'rocket_carriage_sights':12,
'mobile_warfare':12,
'elastic_defence':12,
'spearhead_doctrine':1,
'schwerpunkt':12,
'blitzkrieg':12,
'operational_level_command_structure':12,
'tactical_command_structure':12,
'delay_doctrine':12,
'integrated_support_doctrine':12,
'superior_firepower':1,
'mechanized_offensive':12,
'combined_arms_warfare':1,
'infantry_warfare':12,
'special_forces':12,
'central_planning':12,
'mass_assault':12,
'grand_battle_plan':1,
'assault_concentration':12,
'operational_level_organisation':12,
'large_front':12,
'guerilla_warfare':12,
'peoples_army':12,
'large_formations':1,
'human_wave':1,
'mechanicalengineering_research':12,
'automotive_research':12,
'artillery_research':12,
'mobile_research':12,
'fleet_auxiliary_carrier_doctrine':1,
'light_cruiser_escort_role':12,
'carrier_group_doctrine':12,
'light_cruiser_crew_training':12,
'carrier_crew_training':12,
'carrier_task_force':1,
'naval_underway_repleshment':12,
'radar_training':12,
'sea_lane_defence':1,
'destroyer_escort_role':12,
'battlefleet_concentration_doctrine':12,
'destroyer_crew_training':12,
'battleship_crew_training':12,
'commerce_defence':1,
'fire_control_system_training':12,
'commander_decision_making':12,
'fleet_auxiliary_submarine_doctrine':1,
'trade_interdiction_submarine_doctrine':12,
'cruiser_warfare':12,
'submarine_crew_training':12,
'cruiser_crew_training':12,
'unrestricted_submarine_warfare_doctrine':1,
'spotting':12,
'basing':12,
'destroyer_technology':1,
'destroyer_armament':12,
'destroyer_antiaircraft':12,
'destroyer_engine':12,
'destroyer_armour':12,
'lightcruiser_technology':1,
'lightcruiser_armament':12,
'lightcruiser_antiaircraft':12,
'lightcruiser_engine':12,
'lightcruiser_armour':12,
'smallwarship_radar':12,
'smallwarship_asw':12,
'heavycruiser_technology':1,
'heavycruiser_armament':12,
'heavycruiser_antiaircraft':12,
'heavycruiser_engine':12,
'heavycruiser_armour':12,
'battlecruiser_technology':1,
'battleship_technology':1,
'capitalship_armament':12,
'battlecruiser_antiaircraft':12,
'battlecruiser_engine':12,
'battlecruiser_armour':12,
'battleship_antiaircraft':12,
'battleship_engine':12,
'battleship_armour':12,
'super_heavy_battleship_technology':1,
'cag_development':1,
'escort_carrier_technology':1,
'carrier_technology':1,
'carrier_antiaircraft':12,
'carrier_engine':12,
'carrier_armour':12,
'carrier_hanger':12,
'largewarship_radar':12,
'submarine_technology':1,
'submarine_antiaircraft':12,
'submarine_engine':12,
'submarine_hull':12,
'submarine_torpedoes':12,
'submarine_sonar':12,
'submarine_airwarningequipment':12,
'naval_engineering_research':12,
'submarine_engineering_research':12,
'amphibious_invasion_craft':1,
'advanced_invasion_craft':1,
'amphibious_invasion_technology':12,
'amphibious_assault_units':12,
'chemical_engineering_research':12,
'electornicegineering_research':12,
'combat_medicine':12,
'first_aid':12,
'agriculture':12,
'industral_production':12,
'industral_efficiency':12,
'oil_to_coal_conversion':12,
'supply_production':12,
'heavy_aa_guns':12,
'electronic_mechanical_egineering':1,
'radio_technology':1,
'radio_detection_equipment':1,
'radio':1,
'radar':12,
'census_tabulation_machine':1,
'mechnical_computing_machine':12,
'electronic_computing_machine':12,
'decryption_machine':12,
'encryption_machine':12,
'construction_engineering':1,
'advanced_construction_engineering':1,
'oil_refinning':12,
'steel_production':12,
'raremetal_refinning_techniques':12,
'coal_processing_technologies':12,
'education':12,
'supply_transportation':12,
'supply_organisation':12,
'civil_defence':12,
'cavalry_smallarms':12,
'cavalry_support':12,
'cavalry_guns':12,
'cavalry_at':12,
'militia_smallarms':12,
'militia_support':12,
'militia_guns':12,
'militia_at':12,
'infantry_activation':1,
'smallarms_technology':12,
'infantry_support':12,
'infantry_guns':12,
'infantry_at':12,
'mountain_infantry':1,
'marine_infantry':1,
'paratrooper_infantry':1,
'night_goggles':1,
'engineer_brigade_activation':1,
'engineer_bridging_equipment':12,
'engineer_assault_equipment':12,
'imporved_police_brigade':12,
'mortorised_infantry':1,
'desert_warfare_equipment':1,
'jungle_warfare_equipment':1,
'mountain_warfare_equipment':1,
'artic_warfare_equipment':1,
'amphibious_warfare_equipment':1,
'airborne_warfare_equipment':1,
'militia_research':12,
'infantry_research':12,
'mechanised_infantry':1,
'jet_engine':12,
'rocket_interceptor_tech':1,
'jetengine_research':12,
'rocket_science_research':12,
'nuclear_physics_research':12,
'rocket_tests':1,
'rocket_engine':1,
'theorical_jet_engine':1,
'atomic_research':1,
'nuclear_research':1,
'isotope_seperation':1,
'civil_nuclear_research':12,
'strategic_rocket_development':1,
'flyingbomb_development':1,
'flyingrocket_development':1,
'strategicrocket_engine':12,
'strategicrocket_warhead':12,
'strategicrocket_structure':12,
'da_bomb':12,
'radar_guided_missile':1,
'radar_guided_bomb':1,
'electric_powered_torpedo':1,
'helecopters':1,
'medical_evacuation':1,
'pilot_rescue':1,
'sam':1,
'aam':1
}

if ttype == "air":
  tech_list=[
'single_engine_aircraft_design',
'twin_engine_aircraft_design',
'basic_aeroengine',
'basic_small_fueltank',
'basic_single_engine_airframe',
'basic_aircraft_machinegun',
'basic_medium_fueltank',
'basic_twin_engine_airframe',
'basic_bomb',
'multi_role_fighter_development',
'cas_development',
'nav_development',
'basic_four_engine_airframe',
'basic_strategic_bomber',
'aeroengine',
'small_fueltank',
'single_engine_airframe',
'single_engine_aircraft_armament',
'medium_fueltank',
'twin_engine_airframe',
'air_launched_torpedo',
'small_bomb',
'twin_engine_aircraft_armament',
'medium_bomb',
'large_fueltank',
'four_engine_airframe',
'strategic_bomber_armament',
'cargo_hold',
'large_bomb',
'advanced_aircraft_design',
'small_airsearch_radar',
'medium_airsearch_radar',
'large_airsearch_radar',
'small_navagation_radar',
'medium_navagation_radar',
'large_navagation_radar',
'drop_tanks',
'fighter_pilot_training',
'fighter_groundcrew_training',
'interception_tactics',
'fighter_ground_control',
'bomber_targerting_focus',
'fighter_targerting_focus',
'cas_pilot_training',
'cas_groundcrew_training',
'ground_attack_tactics',
'forward_air_control',
'battlefield_interdiction',
'tac_pilot_training',
'tac_groundcrew_training',
'interdiction_tactics',
'logistical_strike_tactics',
'installation_strike_tactics',
'airbase_strike_tactics',
'tactical_air_command',
'nav_pilot_training',
'nav_groundcrew_training',
'portstrike_tactics',
'navalstrike_tactics',
'naval_air_targeting',
'naval_tactics',
'heavy_bomber_pilot_training',
'heavy_bomber_groundcrew_training',
'strategic_bombardment_tactics',
'airborne_assault_tactics',
'strategic_air_command',
'aeronautic_engineering_research'
  ]
elif ttype == "armor":
  tech_list=[
'lighttank_brigade',
'lighttank_gun',
'lighttank_engine',
'lighttank_armour',
'lighttank_reliability',
'tank_brigade',
'tank_gun',
'tank_engine',
'tank_armour',
'tank_reliability',
'heavy_tank_brigade',
'heavy_tank_gun',
'heavy_tank_engine',
'heavy_tank_armour',
'heavy_tank_reliability',
'armored_car_armour',
'armored_car_gun',
'SP_brigade',
'super_heavy_tank_brigade',
'super_heavy_tank_gun',
'super_heavy_tank_engine',
'super_heavy_tank_armour',
'super_heavy_tank_reliability',
'art_barrell_ammo',
'art_carriage_sights',
'at_barrell_sights',
'at_ammo_muzzel',
'aa_barrell_ammo',
'aa_carriage_sights',
'rocket_art',
'rocket_art_ammo',
'rocket_carriage_sights',
'mobile_warfare',
'elastic_defence',
'spearhead_doctrine',
'schwerpunkt',
'blitzkrieg',
'operational_level_command_structure',
'tactical_command_structure',
'delay_doctrine',
'integrated_support_doctrine',
'superior_firepower',
'mechanized_offensive',
'combined_arms_warfare',
'infantry_warfare',
'special_forces',
'central_planning',
'mass_assault',
'grand_battle_plan',
'assault_concentration',
'operational_level_organisation',
'large_front',
'guerilla_warfare',
'peoples_army',
'large_formations',
'human_wave',
'mechanicalengineering_research',
'automotive_research',
'artillery_research',
'mobile_research'
  ]
elif ttype == "sea":
  tech_list = [
'fleet_auxiliary_carrier_doctrine',
'light_cruiser_escort_role',
'carrier_group_doctrine',
'light_cruiser_crew_training',
'carrier_crew_training',
'carrier_task_force',
'naval_underway_repleshment',
'radar_training',
'sea_lane_defence',
'destroyer_escort_role',
'battlefleet_concentration_doctrine',
'destroyer_crew_training',
'battleship_crew_training',
'commerce_defence',
'fire_control_system_training',
'commander_decision_making',
'fleet_auxiliary_submarine_doctrine',
'trade_interdiction_submarine_doctrine',
'cruiser_warfare',
'submarine_crew_training',
'cruiser_crew_training',
'unrestricted_submarine_warfare_doctrine',
'spotting',
'basing',
'destroyer_technology',
'destroyer_armament',
'destroyer_antiaircraft',
'destroyer_engine',
'destroyer_armour',
'lightcruiser_technology',
'lightcruiser_armament',
'lightcruiser_antiaircraft',
'lightcruiser_engine',
'lightcruiser_armour',
'smallwarship_radar',
'smallwarship_asw',
'heavycruiser_technology',
'heavycruiser_armament',
'heavycruiser_antiaircraft',
'heavycruiser_engine',
'heavycruiser_armour',
'battlecruiser_technology',
'battleship_technology',
'capitalship_armament',
'battlecruiser_antiaircraft',
'battlecruiser_engine',
'battlecruiser_armour',
'battleship_antiaircraft',
'battleship_engine',
'battleship_armour',
'super_heavy_battleship_technology',
'cag_development',
'escort_carrier_technology',
'carrier_technology',
'carrier_antiaircraft',
'carrier_engine',
'carrier_armour',
'carrier_hanger',
'largewarship_radar',
'submarine_technology',
'submarine_antiaircraft',
'submarine_engine',
'submarine_hull',
'submarine_torpedoes',
'submarine_sonar',
'submarine_airwarningequipment',
'naval_engineering_research',
'submarine_engineering_research'
  ]
elif ttype == "landing_craft":
  tech_list = [
'amphibious_invasion_craft',
'advanced_invasion_craft',
'amphibious_invasion_technology',
'amphibious_assault_units'
  ]
elif ttype == "industry":
  tech_list = [
'chemical_engineering_research',
'electornicegineering_research',
'combat_medicine',
'first_aid',
'agriculture',
'industral_production',
'industral_efficiency',
'oil_to_coal_conversion',
'supply_production',
'heavy_aa_guns',
'electronic_mechanical_egineering',
'radio_technology',
'radio_detection_equipment',
'radio',
'radar',
'census_tabulation_machine',
'mechnical_computing_machine',
'electronic_computing_machine',
'decryption_machine',
'encryption_machine',
'construction_engineering',
'advanced_construction_engineering',
'oil_refinning',
'steel_production',
'raremetal_refinning_techniques',
'coal_processing_technologies',
'education',
'supply_transportation',
'supply_organisation',
'civil_defence'
  ]
elif ttype == "infantry":
  tech_list = [
'cavalry_smallarms',
'cavalry_support',
'cavalry_guns',
'cavalry_at',
'militia_smallarms',
'militia_support',
'militia_guns',
'militia_at',
'infantry_activation',
'smallarms_technology',
'infantry_support',
'infantry_guns',
'infantry_at',
'mountain_infantry',
'marine_infantry',
'paratrooper_infantry',
'night_goggles',
'engineer_brigade_activation',
'engineer_bridging_equipment',
'engineer_assault_equipment',
'imporved_police_brigade',
'mortorised_infantry',
'desert_warfare_equipment',
'jungle_warfare_equipment',
'mountain_warfare_equipment',
'artic_warfare_equipment',
'amphibious_warfare_equipment',
'airborne_warfare_equipment',
'militia_research',
'infantry_research',
'mechanised_infantry'
  ]
elif ttype == "secret":
  tech_list = [
'jet_engine',
'rocket_interceptor_tech',
'jetengine_research',
'rocket_science_research',
'nuclear_physics_research',
'rocket_tests',
'rocket_engine',
'theorical_jet_engine',
'atomic_research',
'nuclear_research',
'isotope_seperation',
'civil_nuclear_research',
'strategic_rocket_development',
'flyingbomb_development',
'flyingrocket_development',
'strategicrocket_engine',
'strategicrocket_warhead',
'strategicrocket_structure',
'da_bomb',
'radar_guided_missile',
'radar_guided_bomb',
'electric_powered_torpedo',
'helecopters',
'medical_evacuation',
'pilot_rescue',
'sam',
'aam'
  ]
elif ttype == "all_techs_under_research":
  tech_list = []
elif ttype == "all":
  tech_list = tech_dict.keys()
else:
  print 'Invalid selection of ' + ttype + '; exiting'
  sys.exit()

global entered_subelement
entered_troop_subelement = False
text_file = open(input_file, "r")
whole_thing = text_file.read()
text_file.close()
text_file = open(input_file, "r")
text_file2 = open(input_file, "r")
outFile = open('outFile.hoi3', 'w')
match_nation_flag=False
delay_write=False
reached_end=False
entered_subelement=False
def yays(search_pattern,line,maxx=12):
  match_obj = re.search( '\W' + search_pattern + '={',line)
  if match_obj:
    orig_t_value = int(line[match_obj.end():re.search('[0-9]+',line[match_obj.end():]).end()+match_obj.end()])
    t_value = orig_t_value + tech_increase_value
    if t_value > maxx:
      t_value = maxx
    if orig_t_value is 0 and upgrade_type == 'all_owned_techs':
      return False
    if entered_troop_subelement:
      return search_pattern + '={' + str(t_value) + ' 0.000}\n'
    else:
      return search_pattern + '={' + str(t_value) + ' 0.00000 0.000}\n'
  else:
    return False

if ttype == 'all_techs_under_research':
  for idx, line in enumerate(text_file2):
    if not reached_end:
      if re.match('[A-Z][A-Z][A-Z]=*',line) and match_nation_flag:
        reached_end=True
      if re.match(nation + '=*',line):
        match_nation_flag=True
      if match_nation_flag:
        if re.search('\Wtechnology=',line):
          entered_subelement=True
        if entered_subelement:
          if re.search( 'war_exhaustion', line):
            entered_subelement=False
            reached_end=True
        if entered_subelement and re.search('\Wresearch=',line):
          match_obj = re.search('\Wresearch=',line)
          tech_list.append(line[match_obj.end():].lstrip().rstrip())

text_file2.close()
reached_end=False
match_nation_flag=False
entered_subelement=False
for idx, line in enumerate(text_file):
  if not reached_end:
    if re.match('[A-Z][A-Z][A-Z]=*',line) and match_nation_flag:
      reached_end=True
    if re.match(nation + '=*',line):
      match_nation_flag=True
    if match_nation_flag:
      if re.search('\Wtechnology=',line):
        entered_subelement=True
      if re.search('\Wname',line):
        entered_troop_subelement=True
      if entered_subelement or entered_troop_subelement:
        if re.search( '\W}', line):
          entered_subelement=False
          entered_troop_subelement=False
          if do_techtreeonly == 'True':
            reached_end=True
      if ( entered_subelement or entered_troop_subelement ) and re.search('{',line) and re.search('}',line):
        for tech in tech_list:
          result=yays(tech,line,tech_dict.get(tech))
          if result: line = result
  if not delay_write:
    outFile.write(line)
text_file.close()
outFile.close()
os.remove(input_file)
os.rename('outFile.hoi3', input_file)
print 'Finished making edits for', sys.argv[0]
