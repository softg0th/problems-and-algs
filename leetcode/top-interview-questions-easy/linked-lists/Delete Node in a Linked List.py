
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

    def deleteNode(self, node):
        head = self.head
        while head.next.val != node:
            head = head.next
        head.next = head.next.next
        output = self.printList()
        return output



sol = Solution()
sol.createList([4,5,1,9])
print(sol.deleteNode(1))
