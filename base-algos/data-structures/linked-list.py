class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        val = Node(value)
        if not self.head:
            self.head = val
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = val

    def pop(self):
        node = self.head
        if node is None:
            return
        while node.next.next:
            node = node.next
        node.next = None

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

    def clear(self):
        self.head = None

    def show(self):
        members = []
        node = self.head
        while node:
            members.append(node.data)
            node = node.next
        return members


ll = LinkedList()
ll.append(1)
ll.append('a')
ll.append('b')
print(ll.show())
print(ll.value(1))
ll.pop()
print(ll.show())
ll.clear()
print(ll.show())
