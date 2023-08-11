class Queue:
    def __init__(self, queue):
        self.__queue = queue

    def push(self, value):
        self.__queue.append(value)

    def pop(self):
        self.__queue.pop(0)

    def clear(self):
        for element in range(len(self.__queue)):
            self.__queue.pop(0)

    def view(self):
        print(self.__queue)


q = Queue([])
q.push(5)
q.push(3)
q.push(4)
q.push(8)
q.push(9)
q.view()
q.pop()
q.pop()
q.view()
q.clear()
q.view()
