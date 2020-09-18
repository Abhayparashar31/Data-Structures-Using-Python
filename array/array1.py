'''
1 : Insertion
2 : Deletion
3 : Update
4 : Traverse
5 : search
e : exit


Insertion
    Front
    End
    Location

Deletion 
    Removing a value

Update 
    Updating a value

Traverse
    Showing the array / Printing array

Search 
    search for an element in the array


'''













def choices(choice):
    if choice==1 : ##Insertion
        command = str(input('''
        1. At the start of an array
        2. At the end
        3. At a particular position  
        '''))
        if command == '3':
            pos = int(input("Enter the position"))
            ### 7 9
            if pos > len(arr):
                print("Position error")
            else:
                val = int(input("Enter the value"))
                arr.insert(pos,val)
                print(arr)

        elif command == '1':
            val = int(input("Enter the value"))
            arr.insert(0,val)
            print(arr)
        else:
            val = int(input("Enter the value"))
            arr.append(val)
            print(arr)
    elif choice==4:
        print(arr)


    elif choice==2:
        val = int(input("Enter the value to be delete"))
        arr.remove(val)
        print(arr)


    elif choice==3:
        pos = int(input("enter the position"))
        if pos > len(arr):
            print("Position error")
        else:
            val = int(input("Enter the value"))
            arr[pos]=val
            print(arr)
    
    
    elif choice==5:
        val = int(input("Enter the value to be search"))
        if arr.count(val) > 0 :
            print(f"{val} found in List ",arr.index(val))
    
if __name__ == "__main__":
    arr = []
    while True:
        print("Enter your choice:")
        choice = str(input('''
        1 : Insertion
        2 : Deletion
        3 : Update
        4 : Traverse
        5 : search
        e : exit
        '''))
        if choice=='e':
            break
        else:
            choices(int(choice))