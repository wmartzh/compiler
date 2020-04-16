import sys
import os
import lexic
import syntax
import semantic
import parser

arg = sys.argv


if str(arg) == 'reader.py':
    print('Wrong usage please use the -h argument')
if str(arg[1]) == '-c':
    extention = str(arg[2]).split('.')
    
    if(extention[1] == 'ws'):
        file_open = open(arg[2])
        lines = file_open.read().splitlines()
        count = 0
        #parser.create_file(extention[0])
        print(parser.parse(lines,extention[0]))
       # print(lexic.testTokens(lines))
          
    else:
        print('please compile a .ws file')
elif arg[1] == '-h':

        print('============================================================')
        print( "                                           _ _           ");
        print( "                                          (_) |          ");
        print( " __      _____    ___ ___  _ __ ___  _ __  _| | ___ _ __ ");
        print( " \ \ /\ / / __| / __/ _ \| '_ \` _ \| '_ \| | |/ _ \ '__|");
        print( "  \ V  V /\__ \ | (_| (_) | | | | | | |_) | | |  __/ |   ");
        print( "   \_/\_/ |___/  \___\___/|_| |_| |_| .__/|_|_|\___|_|   ");
        print( "                                    | |                  ");
        print( "                                    |_|                  ");
        print(' ')
        print("By Wilian and Estiff ;)")
        print(' ')
        print(' ')
        print(' ')
        print('============================================================')
        print('Compile File: python reader.py -c <filename>')
        print(' ')
        print('========================================')

else:
    print('Wrong usage please use the -h argument')





