#!/usr/bin/env python
import re
import pdb
import os
import sys
if len(sys.argv) != 2:
	print 'use: infra_all.py path/to/save.hoi3'
	sys.exit(2)

input_file=sys.argv[1]
text_file = open(input_file, "r")
whole_thing = text_file.read()
pattern=re.compile('infra=.+?}', re.MULTILINE|re.DOTALL)
new_file=pattern.sub("infra={10 10}",whole_thing)
outFile = open('outFile.hoi3', 'w')
outFile.write(new_file)