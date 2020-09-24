'''
Algorithm :

1. Scan the infix expression from left to right.
2. If the scanned character is an operand, output it.
3. Else,
    .3.1 If the precedence of the scanned operator is greater than the precedence of the operator in the stack(or the stack is empty or the stack contains a ‘(‘ ), push it.
    .3.2 Else, Pop all the operators from the stack which are greater than or equal to in precedence than that of the scanned operator. After doing that Push the scanned operator to the stack. (If you encounter parenthesis while popping then stop there and push the scanned operator in the stack.)
4. If the scanned character is an ‘(‘, push it to the stack.
5. If the scanned character is an ‘)’, pop the stack and and output it until a ‘(‘ is encountered, and discard both the parenthesis.
6. Repeat steps 2-6 until infix expression is scanned.
7. Print the output
8. Pop and output from the stack until it is not empty.


infix = (a+b)+c

infix       stack       output
(              (
a                       a
+              +        
b              (+        ab
)                       ab+
+               +       ab+
c               +         c
                +        ab+c+   
            
postfix = ab+c+  
'''


















OPERATORS = set(['+', '-', '*', '/', '(', ')', '^'])  # set of operators
PRIORITY = {'+':1, '-':1, '*':2, '/':2, '^':3} # dictionary having priorities 
def infix_to_postfix(expression): #input expression
    stack = [] # initially stack empty
    output = '' # initially output empty
    for ch in expression:
        if ch not in OPERATORS:  # if an operand then put it directly in postfix expression
            output+= ch
        elif ch == '(' :  # else operators should be put in stack

            stack.append('(')
        elif ch==')':
            while stack and stack[-1]!= '(':
                output+=stack.pop()
            stack.pop()
        else:
            # lesser priority can't be on top on higher or equal priority    
            # so pop and put in output   
            while stack and stack[-1]!='(' and PRIORITY[ch]<=PRIORITY[stack[-1]]:
                output+=stack.pop()
            stack.append(ch)
    while stack:
        output+=stack.pop()
    return output
expression = input('Enter infix expression')
print('infix expression: ',expression)
print('postfix expression: ',infix_to_postfix(expression))

