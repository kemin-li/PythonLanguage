# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 2017
Convert statement: print ***, in python 2.x file to 
    print(***) in python 3.x
Usage:
conver2to3(inFilename), for verification purpose
    for all lines in inFilename contain print ***,
    first print out original statement print ***,
    then print statement modified to print (***)
conver2to3(inFilename, outFilename)
    Read lines from inFilename, then output to outFilename with
    print *** replaced to print(***)
Not being extensive tested, please use with caution.
@author: K Li
"""

import re
import sys

def convert2to3(inFile, outFile = None):
    pattern = re.compile(r'(.*print\s+)([^\(;#].*)([;#]*.*)')
    #pattern = re.compile(r'(\s*print\s+)([^(;#]*)([;#]*.*)')
    if(outFile):
        with open(inFile,'r') as src, open(outFile, 'w') as dest:
            for line in src.readlines():
                matched = re.search(pattern,line)
                if matched: # find print xxx, replaced with print(xxx)
                    a = matched.groups()
                    replaced = a[0]+'('+a[1].strip()+')'+a[2]+'\n'
                    dest.write(replaced)
                    print('new print statement is %s'%replaced)
                else: # not a print xxx statement, write original line
                    dest.write(line)
    else: # output lines that contain print and also replacement with print()
        with open(inFile,'r') as src:
            dest = sys.stdout
            for line in src.readlines():
                matched = re.search(pattern, line)
                if matched:
                    a = matched.groups()
                    print('Converting -------')
                    print(line, end='')
                    print(a[0]+'(',a[1].strip()+')',a[2]+'\n',end='')
            