#!/usr/bin/env python
import re
import pdb
import os
import sys

if len(sys.argv) != 4:
    print "Usage: " + sys.argv[0] + " save.hoi3 USA CAN --- USA takes ownership of captured CAN provinces"
    sys.exit(2)

output_file = 'outFile.hoi3'
input_file  = sys.argv[1]
controller  = sys.argv[2]
owner       = sys.argv[3]

text = '\towner="$"\n\tcontroller="' + controller + '"'
oldText = re.sub('$', owner, text)
newText = re.sub('$', controller, text)

pattern     = re.compile(oldText)
text_file   = open(input_file, "r")
newSave     = pattern.sub(newText, text_file.read())
text_file.close()

outFile=open('outFile.hoi3', 'w')
outFile.write(newSave)
outFile.close()

os.remove(input_file)
os.rename(output_file, input_file)