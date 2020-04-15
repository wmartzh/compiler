import os
import re
import lexic
import syntax
import semantic


states={
        'id': None,
        'kw':None,
        'value': None,
        'prev_value':None,
    }
def parse(lines,file_name):
    
    previous_line = None
    previous_statement = ''
    line_count=1
    path = os.path.basename("/py_files")
    fileopen = open(path+'/'+file_name+'.py','a')
    
    for line in lines:
        statement = syntax.lineAnalyzer(line)
        #print(line.split(' '))
        smtic = semantic.analyzer(line,statement,previous_statement,line_count)
        print(smtic)

        if smtic:
            
            Ids = smtic['ids']
            for Id in Ids:
                if Id is 'str_print':
                    text = Ids['str_print']
                    ##fileopen.write("print("+text+")")
    
   
   
    previous_statement = statement
    line_count=line_count + 1
    print('')


def printer(value):
    print(value)

def sum(value1 , value2):
    return value1 + value2




def create_file(file_name):
    path = os.path.basename("/py_files")
    access_rights = 0o755
    try:
        os.mkdir(path, access_rights)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)

        file= open(path +'/'+ file_name+'.py',"w+")

          