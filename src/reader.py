import sys
import os
import lexic
import syntax
import semantic

arg = sys.argv

if str(arg[1]) == '-c':
    extention = str(arg[2]).split('.')
    
    if(extention[1] == 'ws'):
        file_open = open(arg[2])
        lines = file_open.read().splitlines()
        count = 0
        print(semantic.analyzer(lines))
        #lexic.testTokens(lines)
          
    else:
        print('please compile a .ws file')
elif arg[1] == '-h':
        print('usage: python reader.py -c <filename>')
else:
    print('Wrong usage please use the -h argument')



