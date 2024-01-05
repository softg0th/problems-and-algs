class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


class Dequeue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, data):
        value = Node(data)
        if not self.head:
            self.head = value
            self.tail = value
            return

        value.next = self.head
        self.head.previous = value
        self.head = value

    def push_tail(self, data):
        value = Node(data)
        if not self.head:
            self.head = value
            self.tail = value
            return
        value.previous = self.tail
        self.tail.next = value
        self.tail = value

    def pop_head(self):
        if self.head.next:
            node = self.head.next
            self.head.next.previous = None
            self.head = node
            return
        self.head = None
        self.tail = None

    def pop_tail(self):
        if self.tail.previous:
            node = self.tail.previous
            self.tail.previous.next = None
            self.tail = node
            return
        self.head = None
        self.tail = None

    def view(self):
        output = []
        if self.head:
            node = self.head
            while node:
                output.append(node.data)
                node = node.next
        return output

    def clear(self):
        self.head = None
        self.tail = None

    def size(self):
        counter = 0
        if self.head:
            node = self.head
            while node:
                counter += 1
                node = node.next
        return counter


dq = Dequeue()
dq.push_tail(1)
dq.push_tail(2)
dq.push_tail(5)
dq.push_head(0)
dq.pop_head()
dq.pop_head()
