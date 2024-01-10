from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.head = None

    def printList(self):
        node = self.head
        output = []
        while node:
            output.append(node.val)
            node = node.next
        return output

    def createList(self, nodes):
        for x in nodes:
            x = ListNode(x)
            if not self.head:
                self.head = x
                continue
            node = self.head
            while node.next:
                node = node.next
            node.next = x
    def reverseList(self):
        newHead = None
        head = self.head
        output = []
        while head:
            nextHead = head.next
            head.next = newHead
            newHead = head
            head = nextHead
            output.append(nextHead.val)
        print(output)

sol = Solution()
sol.createList([1, 2, 3, 4, 5])
sol.reverseList()