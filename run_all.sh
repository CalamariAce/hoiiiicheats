#!/usr/bin/env bash

if [ -z "$1" ] || [ -z "$2" ]; then
  echo 'not enough argumets, exiting'
  echo 'need to supply file name and 3-letter nation string, in that order'
  exit 1
fi

/usr/bin/time -f '%e' ./air_base.py "$1" $2 10.000 #set all squares that have air base to this value
/usr/bin/time -f '%e' ./anti_air.py "$1" $2 10.000 #set all squares that have anti-air to this value
/usr/bin/time -f '%e' ./coastal_fort.py "$1" $2 10.000 #set all squares that haev coastal forts to this value
/usr/bin/time -f '%e' ./crude_oil.py "$1" $2 3 #crude production multiplier
/usr/bin/time -f '%e' ./diplo_influence.py "$1" $2 100 #set diplo influence to this amount
/usr/bin/time -f '%e' ./dissent.py "$1" $2 #sets dissent to zero
/usr/bin/time -f '%e' ./energy_production.py "$1" $2 7 #energy production multiplier
/usr/bin/time -f '%e' ./faction_battles.py "$1" $2 #grants 251 battles for air/naval/ground for veteran status
/usr/bin/time -f '%e' ./fuel.py "$1" $2 3 #fuel production multiplier
/usr/bin/time -f '%e' ./industry.py "$1" $2 10.000 #set all squares that have industry to this industry value
/usr/bin/time -f '%e' ./infra.py "$1" #sets all infra to 10.000
#/usr/bin/time -f '%e' ./infra_faction.py "$1" $2 10.000 #Faction specific infrasturcture change
/usr/bin/time -f '%e' ./land_fort.py "$1" $2 10.000 #set all squares that have land forts to this value
/usr/bin/time -f '%e' ./laws.py "$1" $2 #sets nation to best laws
/usr/bin/time -f '%e' ./leadership.py "$1" $2 3 #province leadership bonus multiplier
/usr/bin/time -f '%e' ./manpower_production.py "$1" $2 5 #manpower production multiplier
/usr/bin/time -f '%e' ./manpower.py "$1" $2 5 #multipliy current manpower stockpile by this maount
/usr/bin/time -f '%e' ./metal_production.py "$1" $2 7 #metal production multiplier
/usr/bin/time -f '%e' ./military_construction.py "$1" $2 #completes all queued military constructions for the faction
/usr/bin/time -f '%e' ./money.py "$1" $2 3 #current money multiplier
/usr/bin/time -f '%e' ./national_unity.py "$1" $2 99.999 #set national unity to this amount
/usr/bin/time -f '%e' ./naval_base.py "$1" $2 10.000 #set all squares that have naval bases to this value
/usr/bin/time -f '%e' ./neutrality.py "$1" $2 0.000 #set neutrality to this value
/usr/bin/time -f '%e' ./officers.py "$1" $2 5 #current officer multiplier
/usr/bin/time -f '%e' ./radar_station.py "$1" $2 10.000 #set all squares that have radar station to this value
/usr/bin/time -f '%e' ./rare_materials_production.py "$1" $2 10 #rare materials production multiplier
/usr/bin/time -f '%e' ./revolt_risk.py "$1" $2 #lowers the revolt risk to 0 for all controlled provinces
/usr/bin/time -f '%e' ./spies.py "$1" $2 150 #sets the number of free spies
/usr/bin/time -f '%e' ./supplies.py "$1" $2 3 #multiplies supply production and/or stockpile by this amount
/usr/bin/time -f '%e' ./theory_practical.py "$1" $2 99.000 #set theory and practical values on the tech screen to this value
/usr/bin/time -f '%e' ./war_exhaustion.py "$1" $2 #sets war exhaustion to 0 for this nation
/usr/bin/time -f '%e' ./organization.py "$1" $2 #make all units fully organized for this nation
/usr/bin/time -f '%e' ./strength.py "$1" $2 #put all units to full strength for this nation
/usr/bin/time -f '%e' ./unit_experience.py "$1" $2 1.5 #multiply all unit experience by this amount for this nation
/usr/bin/time -f '%e' ./leader_experience.py "$1" $2 1.5 #multiply all leader experience by this amount for this nation
/usr/bin/time -f '%e' ./rocket_test.py "$1" $2 10.000 #set all squares that have rocket test sites to this value
/usr/bin/time -f '%e' ./nuclear_reactor.py "$1" $2 10.000 #set all squares that have nuclear reactors to this value
#tech.py usage:
#./tech.py file_name nation ttype tech_increase_value upgrade_only_existing_tech do_techtreeonly
#where ttype can be one of the following: air, armor, sea, landing_craft, infantry, industry, secret, all, and all_techs_under_research
#and where tech_increase_value is the amount to increase the relevant techs by
#and where upgrade_only_existing_tech if set to 'all_owned_techs' will only upgrade tech already at a level of 1 or higher.  Default is 'unrestricted'.
#and where do_techtreeonly if set to True will only change techs in techtree.  If false, it will also applies the same tech updates to existing units, units under construction, and units waiting for deployment (Note - this takes a long time - several orders of magnitude longer than the others).
/usr/bin/time -f '%e' ./tech.py "$1" $2 all 2 unrestricted True

# Example #2 - increasing by 1 all techs currently being researched, and increase current deployed unit researches by the same amount.
#/usr/bin/time -f '%e' ./tech.py "$1" $2 all_techs_under_research 1 unrestricted False

# Example #3 - increasing by 1 all techs for which we have at least 1 point researched into
#/usr/bin/time -f '%e' ./tech.py "$1" $2 all 1 all_owned_techs True
