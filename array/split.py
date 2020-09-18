'''
arr = [12,10,5,6,52,36]
pos = 2


5
[12,10] +  [5,6,52,36]  = [5,6,52,36,12,10]

[5,6,52,36,12,10]



'''









def split(arr,pos):
    print(arr[pos:])
    print(arr[:pos])
    arr = arr[pos:] + arr[:pos]
    return arr 


# arr = list(int(num) for num in input("Enter the elements of the list\n").strip().split())
arr = [12, 10, 5, 6, 52, 36]
pos = 2
print(arr)
print("Splitted array : ",split(arr,pos))