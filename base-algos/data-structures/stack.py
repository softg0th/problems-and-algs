class Stack:
    def __init__(self, stack):
        self.__stack = stack

    def push(self, value):
        self.__stack.append(value)

    def pop(self):
        self.__stack.pop()

    def clear(self):
        for element in range(len(self.__stack)):
            self.__stack.pop()

    def view(self):
        print(self.__stack)


s = Stack([1])
s.push(5)
s.push(3)
s.push(4)
s.push(8)
s.push(9)
s.view()
s.pop()
s.pop()
s.view()
s.clear()
s.view()