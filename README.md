hoiiiicheats
============

Cheats for Hearts of Iron III: Their Finest Hour

**May result in game save file corruption.  Use at your own risk.  You should make backup copies of any important save files before running these scripts on them.**

## Install/Setup

1. Install Python 2.x for your operating system, e.g.: [Python 2.7.16 Win 64](https://www.python.org/ftp/python/2.7.16/python-2.7.16.amd64.msi) | [Python 2.7.16 Win 32](https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi)
2. Ensure that python is part of your operating system's path. Google search `windows python path` and follow the featured snippets `Add Python to the Windows Path` and `Is Python in your PATH ?`. It may be necessary to restart your operating system session before you will see any changes take effect.
3. Download the python scripts provided in this repository [here](https://github.com/CalamariAce/hoiiiicheats/archive/master.zip)
4. Extract the zip file downloaded in step #3 into the directory where your hoi3 save files are located. The .py files should be in the same directory as the .hoi3 files. If they are not, relocate the .py files to the same directory as the .hoi3 files.
5. Open a command prompt (Start --> Run --> "cmd" on Windows) and "cd" to the hoi3 save directory.
6. Run any of the scripts on the desired save file as shown below. If you receive any error to the effect that the "python" binary cannot be found, then python is not in your Path and you should revisit step #2.

## Usage examples

<pre><code>
# General script call format:
./script.py "HOI3-save-file-name.hoi3" "3-letter-nation-code" "parameter(s)"

# Examples for modifying myGame.hoi3 for soviets (SOV)
./air_base.py myGame.hoi3 "SOV" 10.000 #set all squares that have air base to this value
./anti_air.py "myGame.hoi3" "SOV" 10.000 #set all squares that have anti-air to this value
./coastal_fort.py "myGame.hoi3" "SOV" 10.000 #set all squares that haev coastal forts to this value
./crude_oil.py "myGame.hoi3" "SOV" 3 #crude production multiplier
./diplo_influence.py "myGame.hoi3" "SOV" 100 #set diplo influence to this amount
./dissent.py "myGame.hoi3" "SOV" #sets dissent to zero
./energy_production.py "myGame.hoi3" "SOV" 7 #energy production multiplier
./faction_battles.py "myGame.hoi3" "SOV" #grants 251 battles for air/naval/ground for veteran status
./fuel.py "myGame.hoi3" "SOV" 3 #fuel production multiplier
./industry.py "myGame.hoi3" "SOV" 10.000 #set all squares that have industry to this industry value
./infra.py "myGame.hoi3" #sets all infra to 10.000
./infra_faction.py "myGame.hoi3" "SOV" 10.000 #Faction specific infrasturcture change
./land_fort.py "myGame.hoi3" "SOV" 10.000 #set all squares that have land forts to this value
./laws.py "myGame.hoi3" "SOV" #sets nation to best laws
./leadership.py "myGame.hoi3" "SOV" 3 #province leadership bonus multiplier
./manpower_production.py "myGame.hoi3" "SOV" 5 #manpower production multiplier
./manpower.py "myGame.hoi3" "SOV" 5 #multipliy current manpower stockpile by this maount
./metal_production.py "myGame.hoi3" "SOV" 7 #metal production multiplier
./military_construction.py "myGame.hoi3" "SOV" #completes all queued military constructions for the faction
./money.py "myGame.hoi3" "SOV" 3 #current money multiplier
./national_unity.py "myGame.hoi3" "SOV" 99.999 #set national unity to this amount
./naval_base.py "myGame.hoi3" "SOV" 10.000 #set all squares that have naval bases to this value
./neutrality.py "myGame.hoi3" "SOV" 0.000 #set neutrality to this value
./officers.py "myGame.hoi3" "SOV" 5 #current officer multiplier
./radar_station.py "myGame.hoi3" "SOV" 10.000 #set all squares that have radar station to this value
./rare_materials_production.py "myGame.hoi3" "SOV" 10 #rare materials production multiplier
./revolt_risk.py "myGame.hoi3" "SOV" #lowers the revolt risk to 0 for all controlled provinces
./spies.py "myGame.hoi3" "SOV" 150 #sets the number of free spies
./supplies.py "myGame.hoi3" "SOV" 3 #multiplies supply production and/or stockpile by this amount
./theory_practical.py "myGame.hoi3" "SOV" 99.000 #set theory and practical values on the tech screen to this value
./war_exhaustion.py "myGame.hoi3" "SOV" #sets war exhaustion to 0 for this nation
./organization.py "myGame.hoi3" "SOV" #make all units fully organized for this nation
./strength.py "myGame.hoi3" "SOV" #put all units to full strength for this nation
./unit_experience.py "myGame.hoi3" "SOV" 1.5 #multiply all unit experience by this amount for this nation
./leader_experience.py "myGame.hoi3" "SOV" 1.5 #multiply all leader experience by this amount for this nation

#tech.py usage:
#./tech.py file_name nation ttype tech_increase_value upgrade_only_existing_tech do_techtreeonly
#where ttype can be one of the following: air, armor, sea, landing_craft, infantry, industry, secret, all, and all_techs_under_research
#and where tech_increase_value is the amount to increase the relevant techs by
#and where upgrade_only_existing_tech if set to 'all_owned_techs' will only upgrade tech already at a level of 1 or higher.  Default is 'unrestricted'.
#and where do_techtreeonly if set to True will only change techs in techtree.  If false, it will also applies the same tech updates to existing units, units under construction, and units waiting for deployment (Note - this takes a long time - several orders of magnitude longer than the others).
./tech.py "myGame.hoi3" "SOV" all 2 unrestricted True

# Example #2 - increasing by 1 all techs currently being researched, and increase current deployed unit researches by the same amount.
./tech.py "myGame.hoi3" "SOV" all_techs_under_research 1 unrestricted False

# Example #3 - increasing by 1 all techs for which we have at least 1 point researched into
./tech.py "myGame.hoi3" "SOV" all 1 all_owned_techs True

#alignment.py usage:
./alignment.py "myGame.hoi3" "USA" comintern #set alignment for this nation to `comintern` faction so that you can try to invite this nation to your faction.  Other acceptable values are `allies` and `axis`.  Substitute the keyword `all` for the nation string to change alignment of all nations.

#threat.py usage:
./threat.py "myGame.hoi3" "USA" ENG 999.999 #set threat level of england to 999.999 for this nation.  Substitute the keyword `all` for the (first) nation string to set the threat level of england for all nations at once.  Useful in combination with alignment.py to be able to invite nations to your faction.
</code></pre>

## Where do I find country codes?

Pasted from / credit given to [here](https://forum.paradoxplaza.com/forum/index.php?threads/a-list-of-countries-tags.476342/)

<pre><code>
# Special countries...
REB 	= "countries/Rebels.txt"

# The Important Majors!
GER	= "countries/Germany.txt"
ENG	= "countries/United Kingdom.txt"
SOV	= "countries/Soviet Union.txt"
USA	= "countries/USA.txt"
JAP	= "countries/Japan.txt"
FRA	= "countries/France.txt"
ITA	= "countries/Italy.txt"


# Northern Europe
DEN	= "countries/Denmark.txt"
ICL	= "countries/Iceland.txt"
EST	= "countries/Estonia.txt"
FIN	= "countries/Finland.txt"
LAT	= "countries/Latvia.txt"
LIT	= "countries/Lithuania.txt"
NOR	= "countries/Norway.txt"
SWE	= "countries/Sweden.txt"


# Western Europe
BEL	= "countries/Belgium.txt"
HOL	= "countries/Netherlands.txt"
IRE	= "countries/Ireland.txt"
LUX	= "countries/Luxemburg.txt"
VIC	= "countries/Vichy France.txt"


# Central Europe
AUS	= "countries/Austria.txt"
CZE	= "countries/Czechoslovakia.txt"
CRO	= "countries/Croatia.txt"
DDR	= "countries/DDR.txt"
DFR	= "countries/FRG.txt"
HUN	= "countries/Hungary.txt"
POL	= "countries/Poland.txt"
ROM	= "countries/Romania.txt"
SLO	= "countries/Slovakia.txt"
SCH	= "countries/Switzerland.txt"


# Southern Europe
POR	= "countries/Portugal.txt"
RSI	= "countries/Italian Social Republic.txt"
SPA	= "countries/Nationalist Spain.txt"
SPR	= "countries/Republican Spain.txt"


# Southeast Europe
ALB	= "countries/Albania.txt"
BUL	= "countries/Bulgaria.txt"
GRE	= "countries/Greece.txt"
YUG	= "countries/Yugoslavia.txt"



# Western Asia
AFG	= "countries/Afghanistan.txt"
IRQ	= "countries/Iraq.txt"
ISR	= "countries/Israel.txt"
JOR	= "countries/Jordan.txt"
LEB	= "countries/Lebanon.txt"
OMN	= "countries/Oman.txt"
PAL	= "countries/Palestine.txt"
PER	= "countries/Persia.txt"
SAU	= "countries/Saudi Arabia.txt"
SYR	= "countries/Syria.txt"
TUR	= "countries/Turkey.txt"
YEM	= "countries/Yemen.txt"




# Southern Asia
BHU	= "countries/Bhutan.txt"
IND	= "countries/India.txt"
NEP	= "countries/Nepal.txt"
PAK	= "countries/Pakistan.txt"


# Eastern Asia
CGX	= "countries/Guangxi Clique.txt"
CHC	= "countries/Communist China.txt"
CHI	= "countries/Nationalist China.txt"
CSX	= "countries/Shanxi.txt"
CXB	= "countries/Xibei San Ma.txt"
CYN	= "countries/Yunnan.txt"
KOR	= "countries/Korea.txt"
MAN	= "countries/Manchukuo.txt"
MEN	= "countries/Mengkukuo.txt"
MON	= "countries/Mongolia.txt"
PRK	= "countries/People's Republic of Korea.txt"
SIK	= "countries/Sinkiang.txt"
TAN	= "countries/Tannu Tuva.txt"
TIB	= "countries/Tibet.txt"


# Southeastern Asia
IDC	= "countries/Indochina.txt"
INO	= "countries/Indonesia.txt"
PHI	= "countries/Philippines.txt"
SIA	= "countries/Siam.txt"


# Africa
EGY	= "countries/Egypt.txt"
LIB	= "countries/Liberia.txt"
ETH	= "countries/Ethiopia.txt"
SAF	= "countries/South Africa.txt"


# Australasia
AST	= "countries/Australia.txt"
NZL	= "countries/New Zealand.txt"

# Northern America
CAN	= "countries/Canada.txt"
CUB	= "countries/Cuba.txt"
COS	= "countries/Costa Rica.txt"
DOM	= "countries/Dominican Republic.txt"
GUA	= "countries/Guatemala.txt"
HAI	= "countries/Haiti.txt"
HON	= "countries/Honduras.txt"
MEX	= "countries/Mexico.txt"
NIC	= "countries/Nicaragua.txt"
PAN	= "countries/Panama.txt"
SAL	= "countries/El Salvador.txt"


# Southern America
ARG	= "countries/Argentina.txt"
BOL	= "countries/Bolivia.txt"
BRA	= "countries/Brazil.txt"
CHL	= "countries/Chile.txt"
COL	= "countries/Colombia.txt"
ECU	= "countries/Ecuador.txt"
GUY	= "countries/Guyana.txt"
PAR	= "countries/Paraguay.txt"
PRU	= "countries/Peru.txt"
URU	= "countries/Uruguay.txt"
VEN	= "countries/Venezuela.txt"
</code></pre>

