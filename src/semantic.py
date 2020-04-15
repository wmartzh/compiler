import re
import lexic
import syntax




def analyzer(lines):
   
    previous_line = None
    previous_statement = ''
    line_count=1

    for line in lines:
        statement = syntax.lineAnalyzer(line)
        syntax_error = syntax.analyzer(line,statement,previous_statement,line_count)
      
        if syntax_error:
            if syntax_error['syntax'] is 'ok':
               ##statement = syntax.lineAnalyzer(line)
                blank = re.findall(r'^\s*$',line)

                if  blank is not None:
                    return meaning_analyzer(line)
                 
            else:  
                return syntax_error
            
        previous_statement = statement
        line_count=line_count + 1
               


def meaning_analyzer(line):
   

    lineAnalyzed = syntax.lineAnalyzer(line)
   
    chars = line.split()

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
        
     

    mean_line = {
        'actions':lineOperation,
        'ids':ids,
    }
    return mean_line
             
                    

                
    



     
