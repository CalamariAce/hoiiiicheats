#!/usr/bin/env python
import re
import pdb
import os
import sys

#zeroPattern=re.compile('.000')
# outFile.write(zeroPattern.sub("", line))

def changeProvinceSingleLine(attribute, multiply, defaultAmount):
    if len(sys.argv) == 3:
        amount=defaultAmount
    elif len(sys.argv) == 4:
        amount=sys.argv[3]
    else:
        print "Usage: " + sys.argv[0] + " save.hoi3 NAT 10"
        sys.exit(2)

    output_file='outFile.hoi3'
    input_file=sys.argv[1]
    nation=sys.argv[2]
        
    text_file = open(input_file, "r")
    whole_thing = text_file.read()
    text_file.close()
    text_file = open(input_file, "r")
    outFile = open(output_file, 'w')
    
    match_nation_flag=False
    reached_end_of_provinces=False
    changes=False
    for idx, line in enumerate(text_file):
        if not reached_end_of_provinces:
            if re.match('\\A[0-9]*=',line):
                match_nation_flag=False
            elif re.match('\\AREB=',line):
                reached_end_of_provinces=True
            elif match_nation_flag:
                value = re.search('\t' + attribute,line)
                if value:
                    if multiply:
                        line = attribute + str(float(line[value.end():].rstrip()) * float(amount)) + '\n'
                    else:
                        line = attribute + amount + '\n'
                    changes=True
            elif re.search('\tcontroller="' + nation + '"',line):
                match_nation_flag=True
        outFile.write(line)
    
    text_file.close()
    outFile.close()
    if not changes:
        print 'Warning: no changes made'
        os.remove(output_file)
    else:
        os.remove(input_file)
        os.rename(output_file, input_file)
    print 'Finished making edits for', sys.argv[0]


def changeProvinceMultiLine(attribute, defaultAmount):
    if len(sys.argv) == 3:
        amount=defaultAmount
    elif len(sys.argv) == 4:
        amount=sys.argv[3]
    else:
        print "Usage: " + sys.argv[0] + " save.hoi3 NAT 10"
        sys.exit(2)

    output_file='outFile.hoi3'
    input_file=sys.argv[1]
    nation=sys.argv[2]
        
    text_file = open(input_file, "r")
    whole_thing = text_file.read()
    text_file.close()
    text_file = open(input_file, "r")
    outFile = open(output_file, 'w')
    
    match_nation_flag=False
    delay_write=False
    reached_end_of_provinces=False
    changes=False
    for idx, line in enumerate(text_file):
        if not reached_end_of_provinces:
            if re.match('\\A[0-9]*=',line):
                match_nation_flag=False
            elif re.match('\\AREB=',line):
                reached_end_of_provinces=True
            elif match_nation_flag:
                if re.search('\t' + attribute,line):
                    delay_write=True
                if delay_write:
                    if re.search('}',line):
                        delay_write=False
                        line=attribute + '{' + amount + ' ' + amount + '}\n'
                        changes=True
            elif re.search('\tcontroller="' + nation + '"',line):
                match_nation_flag=True
        if not delay_write:
            outFile.write(line)
    
    text_file.close()
    outFile.close()
    if not changes:
        print 'Warning: no changes made'
        os.remove(output_file)
    else:
        os.remove(input_file)
        os.rename(output_file, input_file)
    print 'Finished making edits for', sys.argv[0]

def changeProvinceProduction(attribute, defaultAmount):
    if len(sys.argv) == 3:
        amount=defaultAmount
    elif len(sys.argv) == 4:
        amount=sys.argv[3]
    else:
        print "Usage: " + sys.argv[0] + " save.hoi3 NAT 10"
        sys.exit(2)

    output_file='outFile.hoi3'
    input_file=sys.argv[1]
    nation=sys.argv[2]
        
    text_file = open(input_file, "r")
    whole_thing = text_file.read()
    text_file.close()
    text_file = open(input_file, "r")
    outFile = open(output_file, 'w')
    
    match_nation_flag=False
    reached_end_of_provinces=False
    changes=False
    producing=False
    for idx, line in enumerate(text_file):
        if not reached_end_of_provinces:
            if re.match('\\A[0-9]*=',line):
                match_nation_flag=False
                producing=False
            elif re.match('\\AREB=',line):
                reached_end_of_provinces=True
            elif match_nation_flag:
                if re.search('\t' + 'current_producing=',line):
                    producing=True
                elif producing:
                    value = re.search('\t' + attribute,line)
                    if value:
                        line = attribute + str(float(line[value.end():].rstrip()) * float(amount)) + '\n'
                        changes=True
            elif re.search('\tcontroller="' + nation + '"',line):
                match_nation_flag=True
        outFile.write(line)
    
    text_file.close()
    outFile.close()
    if not changes:
        print 'Warning: no changes made'
        os.remove(output_file)
    else:
        os.remove(input_file)
        os.rename(output_file, input_file)
    print 'Finished making edits for', sys.argv[0]


def changeNationSingleLine(attribute, multiply, defaultAmount):
    if len(sys.argv) == 3:
        amount=defaultAmount
    elif len(sys.argv) == 4:
        amount=sys.argv[3]
    else:
        print "Usage: " + sys.argv[0] + " save.hoi3 NAT 10"
        sys.exit(2)

    output_file='outFile.hoi3'
    input_file=sys.argv[1]
    nation=sys.argv[2]
    
    text_file = open(input_file, "r")
    whole_thing = text_file.read()
    text_file.close()
    text_file = open(input_file, "r")
    outFile = open(output_file, 'w')

    match_nation_flag=False
    reached_end=False
    entered_subelement=False
    changes=False
    for idx, line in enumerate(text_file):
        if not reached_end:
            if re.match('\\A' + nation + '=*',line):
                match_nation_flag=True
            elif match_nation_flag:
                if re.match('\\A[A-Z][A-Z][A-Z]=*',line):
                    reached_end=True
                value = re.search('\t' + attribute,line)
                if value:
                    if multiply:
                        line = attribute + str(float(line[value.end():].rstrip()) * float(amount)) + '\n'
                    else:
                        line = attribute + amount + '\n'
                    changes=True
        outFile.write(line)
    
    text_file.close()
    outFile.close()
    if not changes:
        print 'Warning: no changes made'
        os.remove(output_file)
    else:
        os.remove(input_file)
        os.rename(output_file, input_file)
    print 'Finished making edits for', sys.argv[0]
