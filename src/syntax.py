import re
import lexic
## Store the structures of statements
statements =[
    ## kw id : () ;
    "^[(a-zA-Z)(a-zA-Z0-9_):;]$"
]

def oneLineBlocks(line):
    long_string = re.findall(r'\"(.+?)\"',line)
    parentesis = re.findall(r'\((.*?)\)',line)
    

    if long_string:
        return {'str_structure':long_string}
    if parentesis:
        return {'prts_structure':parentesis}



def analyzer(line,statement,previous_statement,line_count):
    #
    
    resul =''
    serror = structure_analyzer(line,statement, previous_statement ,line_count)  
    #print(serror)
    if serror:
        if serror['syntax'] is 'error':
            resul = serror
        elif serror ['syntax'] is 'ok':
            resul = serror

    return resul
  

    
 
      
 

def lineAnalyzer(line):
    
    ##Check if there are a assignment
    if re.findall(r'^\s*$',line):
        return 'blank'
    elif re.findall(r'^(.+?):(.+?);$',line):
        return 'statement'
   ## cheack when there an incomplete statement
    elif re.findall(r'^(.+?):(.+?)$',line):
        return 'incomplete_statement'

    ##start block wth kw before
    elif re.findall(r'^if(.+?)((.+?))\{$',line):
        return 'if_statement'
    
    elif re.findall(r'\}$',line):
        return 'block_end'

    ##Check if there are a comment
    elif re.findall(r'^#(.+?)',line):
        return 'comment'
    ## Print Line
    elif re.findall(r'^prt((.+?))\;$',line):
        return 'print'
    
    elif re.findall(r'(.*?);$',line):
        return 'unknow_expression'
 
   
    ##check the empty lines
    elif re.findall('',line):
        return 'empty_line'
   
def lineError(previous_line, actual_line,line_count ):
    
    if actual_line is 'statement' or 'call':
           if previous_line is 'incomplete_statement'  :
                return {'error': True , 'message':'Syntax Error at  line '+ str( line_count)}
   
   


def structure_analyzer(line, statement,previous_statement,line_count):
    chars = line.split(' ')
    prev_token =None
    #check line

    lerror = lineError(previous_statement, statement, line_count)
    if lerror != None:
        
        if lerror['error'] is True:
              return {'syntax' : 'error', 'message':'definition error at line '+ str(line_count)}

    for char in chars:

        token = lexic.analyzer(char)
        print(token)
        if statement is 'statement':
            if prev_token : 
                               
                if prev_token['type'] is 'id' and token['type'] is 'op':
                       
                    prev_token = token     
                    if token['value'] == ':':
                       return {'syntax' : 'ok'}
                    else:
                       return {'syntax' : 'error', 'message':'definition error at line '+ str(line_count)}
                
                elif prev_token['type'] is 'kw' and token['type'] is 'id':
                    prev_token = token     
                                
                elif prev_token['type'] is 'id' and token['type'] is 'id':
                    prev_token = token     
                    return {'syntax' : 'error','message':'definition error at line '+ str(line_count)}

                elif prev_token['type'] is 'kw' and token['type'] is 'kw':
                    prev_token = token     
                    return {'syntax' : 'error','message':'definition error at line '+ str(line_count)}
                
                elif prev_token['type'] is 'op' and token['type'] is 'id' or 'dlm':
                    
                    if prev_token['value'] == ':':
                       prev_token = token    
                       return {'syntax' : 'ok'}
                    else:
                       return {'syntax' : 'error', 'message':'definition error at line '+ str(line_count)}
                
            else:
                prev_token = token
                   
                   
        elif statement is 'if_statement':
            return {'syntax' : 'ok'}

        elif statement is 'block_end':
            return {'syntax' : 'ok'}
            
       

        elif statement is 'comment':
            return {'syntax' : 'ok'}

        elif statement is 'empty_line':
            return {'syntax' : 'ok'}

        elif statement is 'print':
            return {'syntax' : 'ok'}

         
        elif statement is 'unknow_expression':
            return {'syntax' : 'error','message':'Unknow expression at line '+ str(line_count)}
    
            

       










    
    
    



   


