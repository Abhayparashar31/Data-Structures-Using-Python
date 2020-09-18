###############################
##### MAX #####################
###############################

# def max_val(arr):
#     maxVal = 0
#     for val in arr:
#         if val > maxVal:
#             maxVal=val
#     return maxVal

# '''
# [1,3,2]

# maxVal = 0
# 1>0   maxVal = 1
# 3>1 maxVal = 3
# 2>3 false maxVal = 3
# '''

# arr = list(int(num) for num in input("Enter the elements of the list\n").strip().split())



# print("Array:",arr)
# print("Max Value:",max_val(arr))




# '''
# for i in range(0,n):
#     arr[i]
# '''





















###############################
##### SECOND MAX ##############
###############################

### 1
# def max_val(arr):
#     arr.sort()
#     return arr[-2]

# '''
# [1,4,5,2,8]
# [1,2,4,5,8]
# 5 second max element
# '''

# arr = list(int(num) for num in input("Enter the elements of the list\n").strip().split())

# print("Array:",arr)
# print("Second Max Value:",max_val(arr))






### 2
# arr = list(int(num) for num in input("Enter the elements of the list\n").strip().split())
# print("Array:",arr)

# arr.remove(max(arr))
# print("Second Max Value:",max(arr))

# '''
# [1,5 4 ,2]
# 5
# [1,4,2]
#  4 
# '''