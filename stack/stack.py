"""
[]
push 1
[1]
push 2
[1,2]

peek
2

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


















# #print(obj.is_empty())
# #print(obj.peek())
# obj.push(10)
# obj.push(20)
# obj.push(30)
# obj.push(40)
# print(obj.show_stack())
# obj.pop()
# # obj.pop()
# print(obj.show_stack())
# print(obj.is_empty())
# print(obj.peek())
# # print(obj.show_stack())






















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
