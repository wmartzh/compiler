
import re

operators = [
    "^[+]$",
    "^[-]$", 
    "^[*]$", 
    "^[/]$", 
    "^[>]$", 
    "^[<]$", 
    "^[<=]$", 
    "^[>=]$", 
    "^[==]$", 
    "^[!=]$", 
    "^[||]$", 
    "^[&]$", 
    "^[:]$", 
    #"^[;]$", 
    # r"^[]$", 
    # r"^[]$", 
    # r"^[]$", 
]
keywords = [
    "^int$", ## Integer
    "^str$", ## Stirng
    "^prt$", ## Print
    "^var$", ## var def
    "^//$",
    "^if$",
    "^else$",
    "^foreach$",
    "^function$",
    # r"[^ $]",
    # r"[^ $]",
    # r"[^ $]",
     ## coment
]
delimiters=[
    r"[)]", 
    r"[(]", 
    r"\"(.+?)", 
    r"(.+?)\"", 
    r"(.+?);", 
    r"(.+?)\{$", 
    r"^\{(.+?)$", 
    r"(.+?)/}$",     
    r"\}$",     
    r"^\((.+?)", 
    r"(.+?);$", 
]
indentifiers = [
    '[a-zA-Z0-9_]',
    '[0-9]'
]




## check lexic in values
def lexic_check(value):

    return analyzer(value)

def testTokens (lines):
   
   for line in lines:
       chars = line.split(' ')
       print(chars)
       for char in chars:
           result = analyzer(char);
           print(result)

## set if a value is a kw or tk and return the value
def analyzer(value):

    result =  checkTokens(value)
    
    if result is 'op':
        return {
            'type':'op',
            'value': value
            }
    elif result is 'kw':
        return {
            'type':'kw',
            'value': value
            }
    elif result is 'dlm':
        return {
            'type':'dlm',
            'value': value
            
            }
    elif result is 'id':
        return {
            'type':'id',
            'value': value
            }
    else:
        return {
            'type':'non',
            'value': 'non'
            }
  
## cheack if the value is a tk or kw
def checkTokens(value):
    if re.match(r'^\s*$',value):
        return 'blk'
    if re.match('[0-9]',value):
        return 'int'
     
    if re.match('[a-zA-Z0-9_]',value):
        return 'int'
     
    for op in operators:
        match = re.match(op,value)
        if match:
            return 'op'
       
    for kw in keywords:
        match = re.match(kw,value)
        if match :
            return 'kw'
      
            
    for dlm in delimiters:
        match = re.match(dlm,value)
        if match:
            return 'dlm'

    for Id in indentifiers:
        match = re.match(Id,value)
        if match:
            return 'id'
  

     


## check if is a string value
def isStringChar(value):
   long_string = re.findall(r'\"(.+?)\"',value)

   if long_string:
       return {'str_char':long_string}
   else:
       return None

#check if there are a paratesis statement
def isPrntsStatement(value):
   parentesis = re.findall(r'\((.*?)\)',value)
   if parentesis:
       return {'prnts':parentesis}
   else:
       return None


