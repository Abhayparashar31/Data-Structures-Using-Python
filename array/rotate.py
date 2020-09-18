
'''
arr = [1,2,3,4,5]

rotated_arr = [5,1,2,3,4]

'''









##############################
##### ROTATE 1 TIME ##########
###############################
# def rotate(arr):
#     lst_element = arr[-1]
#     temp_arr = []
#     temp_arr.append(lst_element)
#     for ele in arr[:-1]:
#         temp_arr.append(ele)
#     return temp_arr

# '''
# []
# 5
# [5]
# [5,1,2,3,4]
# '''
# arr = [1,2,3,4,5]
# #arr = list(int(num) for num in input("Enter the elements of the list\n").strip().split())

# print("Original array:",arr)
# print("Rotated array:",rotate(arr))


















'''
arr = [1,2,3,4,5]
n = 3

[2,3,4,5,1]
[3,4,5,1,2]
[4,5,1,2,3]

rotated_arr = [4,5,1,2,3]

'''












###############################
##### ROTATE N TIMES ##########
###############################
def leftRotate(arr, n, k):  
    for i in range(k, k + n): 
        print(str(arr[i % n]),  
                   end = " ") 

'''
[1,2,3,4,5] 
3 , 8
arr[i%n]
arr[3%5] = 3    [4]
arr[4%5] = 4    [4,5]
arr[5%5] = 0    [4,5,1]
arr[6%5] = 1    [4,5,1,2]
arr[7%5] = 2    [4,5,1,2,3]
'''


arr = [1,2,3,4,5] 
n = len(arr) 
k = 3
leftRotate(arr, n, k) 
  