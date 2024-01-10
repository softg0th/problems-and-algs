
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

    def removeNthFromEnd(self, node):
        head = self.head
        count = 0
        while head:
            count += 1
            head = head.next
        goal = count - node
        counter = 0
        head = self.head
        while head:
            if counter == goal:
                if self.head == head:
                    self.head = None
                if not head.next:
                    head.val = None
                    break
                head.next = head.next.next
                break
            counter += 1
            head = head.next
        output = self.printList()
        return output


sol = Solution()
sol.createList([1])
print(sol.removeNthFromEnd(1))
