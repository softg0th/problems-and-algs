from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.root = None

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        left = root.right
        right = root.left
        root.left = self.invertTree(left)
        root.right = self.invertTree(right)
        return root


nodes = TreeNode(2, TreeNode(1), TreeNode(3))
sol = Solution()
print(sol.invertTree(nodes))
