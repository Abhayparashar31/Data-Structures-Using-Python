'''
typecode
b	Represents signed integer of size 1 byte/td>
B	Represents unsigned integer of size 1 byte
c	Represents character of size 1 byte
i	Represents signed integer of size 2 bytes
I	Represents unsigned integer of size 2 bytes
f	Represents floating point of size 4 bytes
d	Represents floating point of size 8 bytes

Array Operations :

1 : Insertion
2 : Deletion
3 : Update
4 : Traverse
5 : Search
'''

from array import *
arr = array('i',[])

def choices(choice):
    if choice=='1':
        
        num = int(input("Enter the value:\n"))
        arr.append(num)
        print(arr)
    elif choice == '2':
        num = int(input("Enter the value:\n"))
        arr.remove(num)
        print(arr)
    elif choice=='3':
        pos = int(input("Enter the pos\n"))
        num = int(input("Enter the value:\n"))
        arr[pos]=num
        print(arr)
    elif choice =='4':
        print(arr)
    elif choice=='5':
        num = int(input("Enter the value:\n"))
        if arr.count(num)>0:
            print(f"fount at index {arr.index(num)}")
        else :
            print("NUmber is not found")
    else :
        print("Invalid\n")


while True:
    print("ENter the choice:")
    choice = str(input('''
    1 : Insertion
    2 : Deletion
    3 : Update
    4 : Traverse
    5 : Search
    e : exit
    '''))

    if choice == 'e':
        break
    else :
        choices(choice)
