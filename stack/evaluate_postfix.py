
# Class to convert the expression 
class Stack():
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items==[]
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def show_stack(self):
        return self.items

obj = Stack()

	# The main function that converts given infix expression 
	# to postfix expression 
def evaluatePostfix(exp): 
    
    # Iterate over the expression for conversion 
    for i in exp: 
        
        # If the scanned character is an operand 
        # (number here) push it to the stack 
        if i.isdigit(): 
            obj.push(i) 

        # If the scanned character is an operator, 
        # pop two elements from stack and apply it. 
        else: 
            val1 = obj.pop() 
            val2 = obj.pop() 
            obj.push(str(eval(val2 + i + val1))) 

    return int(obj.pop()) 

'''
123+*8-

exp     val1 val2       val2 Operator val1         stack    
1                                                   [1]
2                                                   [1,2]
3                                                   [1,2,3]
+       3      2         2     +    3 =5            [1,5]
*       5      1         1     *    5               [5]
8                                                   [5,8]
-       8       5        5     -    8               [-3]


result = -3
'''

# Driver program to test above function 
exp = str(input("Enter the string\n"))
print ("postfix evaluation: "+ str(evaluatePostfix(exp))) 
# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
