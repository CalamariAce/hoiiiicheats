hoiiiicheats
============

Save game edit scripts for Hearts of Iron III: Their Finest Hour (hoi3, Hearts of Iron 3)

**May result in game save file corruption.  Use at your own risk.  You should make backup copies of any important save files before running these scripts on them.**

## Install/Setup

1. Install Python 2.x for your operating system using a package installer or [Download Page](https://www.python.org/downloads/)
2. Ensure that python is part of your operating system's path. For Windows, that's an option in the installer, but you'll have to reopen your console to see the effect
3. Download the python scripts provided in this repository [here](https://github.com/CalamariAce/hoiiiicheats/archive/master.zip) and extract
4. Open a command prompt (Start --> Run --> "cmd" on Windows) and "cd" to the script directory
5. Run any of the scripts on the desired save file as shown below. If you receive any error to the effect that the "python" binary cannot be found, then python is not in your Path and you should revisit step #2. You'll have to provide the save file names include paths.

## Scripts
Unless otherwise noted, scripts use the following syntax:

	syntax:  script path/to/save.hoi3 NAT [level]
	example: script path/to/save.hoi3 SOV 
	example: script path/to/save.hoi3 GER 10

### province resource production
Multiply resource production for all controlled provinces. Level parameter is a multiplier, default is 3.
	
| Script | Description |
| :--- | :--- |
| crude_oil  |
| energy_production  |
| metal_production  |
| rare_materials_production  |


### province improvement levels
Set improvement levels for all controlled provinces. Default level is 10.

| Script | Description |
| :--- | :--- |
| air_base  |
| anti_air  |
| coastal_fort  |
| industry  |
| infra  |
| land_fort  |
| naval_base  |
| radar_station  |

### other province details
Multiply other province details. Level parameter is a multiplier, default is 3.

| Script | Description |
| :--- | :--- |
| leadership  |
| manpower_production  |
| money  |
| supplies  |

### nation multiply value scripts
Multiply some value for a nation.

| Script | Description |
| :--- | :--- |
| fuel  |
| leader_experience  |
| manpower  |
| officers  |
| unit_experience  |


### nation set value scripts
Set some value for a nation.

| Script | Description |
| :--- | :--- |
| diplo_influence  |
| dissent  |
| national_unity  |
| neutrality  |
| organization  |
| spies  |
| war_exhaustion  |


### other
Other scripts. Syntax is script save.hoi3 unless noted otherwise
| Script | Description |
| :--- | :--- |
| infra_all 	| set all infrastructure in the world to 10. Syntax: script save.hoi3 |
| revolt_risk | set revolt risk to X. |
| alignment 	| set nations alignment to comintern, axis, allies, or neutral. Does not join or leave faction. |
| faction_battles  | grants 251 battles for air/naval/ground for veteran status |
| laws  | sets nation to best laws |
| military_construction  | completes all queued military constructions |
| strength  | put all units to full strength |
| takeOwnership  | take ownership of controlled provinces: Use: save.hoi3 controller oldOwner |
| theory_practical  | set theory and practical values on the tech screen |

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

