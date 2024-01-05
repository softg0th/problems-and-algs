class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def validate(self):
        if self.head is None:
            return False
        return True

    def append(self, value):
        val = Node(value)
        if not self.head:
            self.head = val
            self.tail = val
            return
        node = self.tail
        node.next = val
        val.previous = node
        self.tail = val

    def pop(self):
        if self.validate():
            node = self.head
            if self.head == self.tail:
                self.head = None
                self.tail = None
                return
            while node.next.next:
                node = node.next
            node.next = None
        return

    def pop_first(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        if self.validate():
            node = self.head
            if node.next:
                self.head = node.next
                node.next.previous = None

    def remove(self, index):
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        if self.validate():
            counter = 0
            node = self.head
            if not node.next:
                self.pop()
                return
            if counter == index:
                self.pop_first()
                return
            while counter < index:
                if not node.next:
                    self.pop()
                    return
                node = node.next
                counter += 1
            node.previous.next = node.next
            node.next.previous = node.previous

    def value(self, index):
        if self.head is None:
            return
        counter = 0
        if counter == index:
            return self.head
        node = self.head
        while counter < index:
            if not node.next:
                return
            node = node.next
            counter += 1
        return node.data

    def show(self):
        members = []
        node = self.head
        while node:
            members.append(node.data)
            node = node.next
        return members
