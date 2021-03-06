import re
import lexic
import syntax




def analyzer(line,statement,previous_statement,line_count):
 
    syntax_error = syntax.analyzer(line,statement,previous_statement,line_count)
  
    if syntax_error:
        if syntax_error['syntax'] is 'ok':
           ##statement = syntax.lineAnalyzer(line)
            blank = re.findall(r'^\s*$',line)

            if  blank is not None:
                return meaning_analyzer(line)
             
        else:  
            return syntax_error
  
               


def meaning_analyzer(line):
   

    lineAnalyzed = syntax.lineAnalyzer(line)
   
    chars = line.split()
    #print(lineAnalyzed)
    mean_line = {}
    lineOperation ={}
    ids  = {}   
    count= 0
    if lineAnalyzed != None:
        if lineAnalyzed is 'statement'or 'call':
            for char in chars:
                token = lexic.analyzer(char)
                if token['type'] is 'op':
                    if token['value'] is ':':
                        
                         lineOperation.update({
                             count:{
                                'operator':token['value'],
                                'expression':'assigment'
                             }
                             
                         })
                         count = count +1
                    elif token['value'] is '+':
                         lineOperation.update({
                             count:{
                                'operator':token['value'],
                                'expression':'sum'
                             }
                             
                         })
                         count = count +1
                    elif token['value'] is '*':
                         lineOperation.update({
                             count :{
                                'operator':token['value'],
                                'expression':'mult'
                             }
                             
                         })
                         count = count +1
                elif token['type'] is 'id':
                    ids.update({'id_refer':token['value']})

        if lineAnalyzed is 'print':
            text = re.findall(r'\(\"(.*?)\"\)',line)
               
            ids.update({'str_print':str(text)})
            lineOperation.update({
                             count :{
                                'operator':'prt',
                                'expression':'print'
                             }
                             
                         })
            
     
        if lineAnalyzed is 'assigment':
            for char in chars:
                token = lexic.analyzer(char)
                if token['type'] is 'int':
                    if token['value'] is ':':
                        ids.update({'int_value':str(text)})
                        
                       
     

    mean_line = {
        'actions':lineOperation,
        'ids':ids,
    }
    return mean_line
             
                    

                
    



     
