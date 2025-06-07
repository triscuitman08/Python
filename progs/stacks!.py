class Stack:
    def __init__(self):
        self.__stack_list = []


    def push(self, val):
        self.__stack_list.append(val)


    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val
    
    def contents(self):
        for num in self.__stack_list:
            result += num
        return result


stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())

stack2 = Stack()

stack2.push(3)
stack2.push(4)
stack2.push(5844)
print(stack2.contents())