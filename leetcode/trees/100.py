from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traversal(self, node1, node2):
        if node1 is None and node2 is None:
            return True

        if (not node1 and node2) or (not node2 and node1):
            raise ValueError
        if node1.val != node2.val:
            raise ValueError

        if node1.left and node2.left:
            if node1.left.val == node2.left.val:
                self.traversal(node1.left, node2.left)
            else:
                raise ValueError
        if (node1.left and not node2.left) or (not node1.left and node2.left):
            raise ValueError
        if node1.right and node2.right:
            if node1.right.val == node2.right.val:
                self.traversal(node1.right, node2.right)
            else:
                raise ValueError
        if (node1.right and not node2.right) or (not node1.right and node2.right):
            raise ValueError
        return True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        try:
            ans = self.traversal(p, q)
        except ValueError:
            ans = False
        return ans


balanced_tree = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
balanced_tree_2 = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
sol = Solution()

print(sol.isSameTree(balanced_tree, balanced_tree_2))
