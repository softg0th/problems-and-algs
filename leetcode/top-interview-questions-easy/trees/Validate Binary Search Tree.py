from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.tag = None
        self.right = False
        self.left = False
        self.root = None

    def compare(self, root):
        if not self.tag:
            self.tag = root
            self.root = root
            self.left = True

            if root.left:
                if root.left.val >= root.val:
                    return False
            if root.right:
                if root.right.val <= root.val:
                    return False

        elif self.left:
            if root.left:
                if root.left.val >= self.tag.val:
                    return False
            if root.right:
                if root.right.val >= self.tag.val:
                    return False
        elif self.right:
            if root.left:
                if root.left.val <= self.root.val or root.left.val >= self.tag.val:
                    return False
            if root.right:
                if root.right.val <= self.root.val or root.right.val <= self.tag.val:
                    return False
        if root.right is None or root.left is None:
            self.tag = root
        return True

    def dfs(self, root):
        if not root:
            return True
        if not root.left and not root.right:
            self.left = False
            self.right = True
            return True

        flag = self.compare(root)
        if not flag:
            return False

        return self.dfs(root.left) and self.dfs(root.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = self.dfs(root)
        return ans


toor = TreeNode(3)
toor.left = TreeNode(1)
toor.right = TreeNode(5)
toor.left.left = TreeNode(0)
toor.left.right = TreeNode(2)
toor.right.left = TreeNode(4)
toor.right.right = TreeNode(6)
sol = Solution()
print(sol.isValidBST(toor))

'''
root = TreeNode(0)
root.left = TreeNode(-1)
print(sol.isValidBST(root))
'''
