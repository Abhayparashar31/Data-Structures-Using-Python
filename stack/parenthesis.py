"""
Example :
(), {} , (({[]}))   <- Balanced
{{} , ()) , ((()))) , }}  <- Unbalanced


(    -> [(]

)  ->   []

"""
from stack import Stack

def is_match(p1,p2):
    if  p1 == '(' and p2 == ')':
        return True
    if p1 == '[' and p2 == ']':
        return True
    if  p1 == '{' and p2 == '}':
        return True
    else :
        return False
def check_paren_balanced(paren_string):
    s = Stack()
    is_balance = True
    index = 0

    while index < len(paren_string) and is_balance:
        paren = paren_string[index]
        if paren in '({[':
            s.push(paren)
        else :
            if s.is_empty():
                is_balance = False
            else :
                top = s.pop()
                if not is_match(top,paren):
                    is_balance = False
        index +=1

    if s.is_empty and is_balance :
        return  True
    else :
        return  False


string = str(input("Enter the set of parenthesis :\n"))
print(check_paren_balanced(string))