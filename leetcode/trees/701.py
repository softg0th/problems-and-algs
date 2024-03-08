from typing import Optional, List


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def __init__(self):
        self.root = None

    def insertion(self, root, val):
        if not root:
            return val
        elif val.val < root.val:
            root.left = self.insertion(root.left, val)
        elif val.val > root.val:
            root.right = self.insertion(root.right, val)
        return root

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not self.root:
            self.root = root
        val = TreeNode(val)
        ans = self.insertion(root, val)
        return ans

