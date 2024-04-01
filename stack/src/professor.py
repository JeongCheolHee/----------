from Liststack import *

def checkstring(string):
    stack = liststack()
    i = 0
    for i in range(len(string)):
        if(string[i] == '$'): break
        stack.push(string[i])
    
    for j in range(i+1, len(string)):
        if(stack.isEmpty()): return False
        if(stack.pop() != string[j]): return False
        
    if (stack.isEmpty()) : return True
    else: return False
    
rv = checkstring("abc$cba")
print(rv)




def paranBalance(s:str):
    stack = liststack()
    for i in range(len(s)):
        if s[i] == '(':
            stack.push(s[i])
        elif s[i]  == ')':
            if stack.isEmpty():
                return False
            stack.pop()
    return stack.isEmpty()


print(paranBalance("(A+B)+d"))
            
