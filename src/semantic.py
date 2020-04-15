import re
import lexic
import syntax

integers =[]
strings = []



def analyzer(lines):
    syntax_error = syntax.analyzer(lines)

    if syntax_error['syntax'] is 'ok':
       previous_line = None
       for line in lines:
           ##statement = syntax.lineAnalyzer(line)
           print (meaning_analyzer(line))
           
         
    else:
       if syntax_error != None:
           return syntax_error
       


def meaning_analyzer(line):
   

    lineAnalyzed = syntax.lineAnalyzer(line)
   
    chars = line.split()

    mean_line = {}
    lineOperation ={}
    ids  = {}   
    count= 0
    if lineAnalyzed is 'statement' or 'call':
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
        'action':lineOperation,
        'ids':ids,
    }
    return mean_line
             
                    

                
    



     
