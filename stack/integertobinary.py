'''
Example : 90
90 % 2 = 0      45
45 % 2 = 1      22
22 % 2 = 0      11
11 % 2 = 1      5
5 % 2 = 1       2
2 % 2 = 0       1
        1
1011010
int('1011010',2)
'''


from stack import Stack
number = int(input("Enter an Integer"))

def div_by_2(number):
    s = Stack()
    while number > 0:
        rem = number % 2
        s.push(rem)
        number = number // 2

    bin_num = ''
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num
print(div_by_2(number))