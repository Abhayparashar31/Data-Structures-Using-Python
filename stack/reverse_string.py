"""
String : Python
reversed string : nohtyp


python

[p,y,t,h,o,n]

""+n = n
"n"+o = no

'nohtyp'

"""

from stack import Stack

def reverse_strings(string):
    s = Stack()
    for i in range(len(string)):
        s.push(string[i])
    reverse_string = ""
    while not s.is_empty():
        reverse_string += s.pop()
    return reverse_string


string = str(input("Enter a string : "))
print(reverse_strings(string))