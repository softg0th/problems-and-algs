class ListNode:
    def __init__(self, x=None):
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

    def mergeSortedLists(self, list1, list2):
        head = ListNode()
        headNext = head
        l1 = len(list1)
        l2 = len(list2)

        i = 0
        j = 0

        if l1 == 0:
            head = ListNode()
            for i in list2:
                head.val = i
                head = head.next
        elif l2 == 0:
            head = ListNode()
            for j in list1:
                head.val = j
                head = head.next

        else:
            while i != l1 and j != l2:
                if not head:
                    if list1[i] >= list2[j]:
                        head = ListNode(list2[j])
                        j += 1
                    else:
                        headNext.next = ListNode(list1[i])
                        headNext = headNext.next
                        i += 1
                else:
                    if j == l2 and i != l1:
                        headNext.next = ListNode(list1[i])
                        headNext = headNext.next
                        i += 1
                    elif i == l1 and j != l2:
                        headNext.next = ListNode(list2[j])
                        headNext = headNext.next
                        j += 1
                    else:
                        if list1[i] >= list2[j]:
                            headNext.next = ListNode(list2[j])
                            headNext = headNext.next
                            j += 1
                        else:
                            headNext.next = ListNode(list1[i])
                            headNext = headNext.next
                            i += 1
            return head




sol = Solution()
print(sol.mergeSortedLists([2], []))
