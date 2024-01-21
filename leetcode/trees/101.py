from typing import Optional, List


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def __init__(self):
        self.root = None

    def traversal(self, left, right):
        if not left and not right:
            return True

        if not left or not right:
            return False
        return (left.val == right.val and self.traversal(left.left, right.right) and
                    self.traversal(left.right, right.left))

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not self.root:
            self.root = root
        ans = self.traversal(root.left, root.right)
        return ans


balanced_tree = TreeNode(1, left=TreeNode(2, left=TreeNode(3), right=None),
                         right=TreeNode(2, left=TreeNode(3), right=None))
sol = Solution()
print(sol.isSymmetric(balanced_tree))
