def isDelimiter(ch):
    if (ch == ';' or ch == '+' or ch == '-' or ch == '*' or
        ch == '/' or ch == ',' or ch == ';' or ch == '>' or
        ch == '<' or ch == '=' or ch == '(' or ch == ')' or
        ch == '[' or ch == ']' or ch == '{' or ch == '}'):
        return True
    else:
        return False

def isOperator(ch):
    if (ch == '+' or ch == '-' or ch == '*' or
        ch == '/' or ch == '>' or ch == '<' or
        ch == '='):
        return True
    else:
        return False
        
def isKeyword(str):
    if (str == "if" or str == "else"  or str == "while" 
        or str == "do" or str == "break" or str == "int" 
        or str == "float" or str == "return"  or str == "char"
        or str == "main" or str == "print"):
        return True
    else:
        return False
        
def isInteger(str):
    if len == 0:
        return False
    for i in range(len(str)):
        if (str[i] != '0' and str[i] != '1' and str[i] != '2'
            and str[i] != '3' and str[i] != '4' and str[i] != '5'
            and str[i] != '6' and str[i] != '7' and str[i] != '8'
            and str[i] != '9' or (str[i] == '-' and i > 0)):
            return False
    else:
        return True
      
def validIdentifier(str):
    if (isInteger(str[0]) == True or isDelimiter(str[0]) == True or isOperator(str[0]) == True ):
        return False
    else:
        return True
        
def isRealNumber (str):
    hasDecimal = False
 
    if len == 0:
        return False
    for i in range(len(str)):
        if (str[i] != '0' and str[i] != '1' and str[i] != '2'
            and str[i] != '3' and str[i] != '4' and str[i] != '5'
            and str[i] != '6' and str[i] != '7' and str[i] != '8'
            and str[i] != '9' and str[i] != '.' or
            (str[i] == '-' and i > 0)):
            return False
        if str[i] == '.':
            hasDecimal = True
    else:
        return hasDecimal
        
def parse(str):
    for elem in str:
        list = ""
        list = list + elem
        if isKeyword(list) == True:
            print("IS A KEYWORD ", list)

        elif isDelimiter(list) == True:
            print("IS A DELIMITER ", list)
        
        elif isOperator(list) == True:
            print("IS A OPERATOR ", list)
    
        elif isInteger(list) == True:
            print("IS AN INTEGER", list)
    
        elif isRealNumber(list) == True:
            print("IS A REAL NUMBER", list)
    
        elif validIdentifier(list) == True:
            print("IS A IDENTIFIER ", list)
            
file = open("test.txt", "r")

for line in file:
    x = line.split(" ")
    parse(x) 
file = open("test.txt", "r")
tokentable={"identifier" : 0, "number" : 1, "int" : 2, "}" : 3, "(" : 4, ")" : 5, "{" : 6, ";" : 7, "=": 8, "+": 9, "print" : 10}
identifiertable={}
numerictable={}
new={}
k=0
ok=0
for line in file:
    if ok:
        break
    x=line.split(" ")
    for elem in x:
        list = ""
        list = list + elem
        if isDelimiter(list)==True or isKeyword(list)==True or isOperator(list)==True:
            new[list]=[tokentable[list],-1]
        elif validIdentifier(list)==True:
            if list not in identifiertable.keys():
                identifiertable[list]=k
                k=k+1
            new[list]=[0,identifiertable[list]]
        elif isInteger(list)==True or isRealNumber(list)==True:
            if list not in numerictable.keys():
                numerictable[list]=k
                k=k+1
            new[list]=[1,numerictable[list]]
print(new)
