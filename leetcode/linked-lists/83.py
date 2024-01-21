from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = set()
        current = head

        while current.next:
            if not nodes:
                nodes.add(current.val)
            if not current.next.val in nodes:
                nodes.add(current.next.val)
            else:
                current.next = current.next.next
        return head


sol = Solution()
print(sol.deleteDuplicates(ListNode(1, ListNode(2, ListNode(2)))))
