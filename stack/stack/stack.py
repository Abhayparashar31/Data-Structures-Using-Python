"""
[]
push 1
[1]
push 2
[1,2]
pop
[1]
pop
[]

push
pop
peek
"""
class Stack():
    def __init__(self):
        self.arr = []
    def push(self,item):
        self.arr.append(item)
    def pop(self,item):
        return self.arr.pop()
    def is_empty(self):
        return self.arr == []
    def peek(self):
        if not self.is_empty():
            return self.arr[-1]
    def show(self):
        return self.arr


obj = Stack()

obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)

print(obj.show())



















































# num = int(input("enter the number of commands"))
# for i in range(num):
#     command = input().split(" ")
#     if command[0]=='push':
#         obj.push(int(command[1]))
#         print(obj.show_stack())
#     elif command[0]=='pop':
#         obj.pop()
#         print(obj.show_stack())
#     elif command[0]=='peek':
#         print(obj.peek())
#     elif command[0]=='show':
#         print(obj.show_stack())
