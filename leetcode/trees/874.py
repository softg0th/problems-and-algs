from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.leaf_first = []
        self.leaf_second = []
        self.switch = True

    def dfs(self, root):
        if not root:
            self.switch = False
        if root:
            print(root.val, self.switch)
            self.dfs(root.left)
            if not root.left and not root.right:
                if self.switch:
                    self.leaf_first.append(root.val)
                else:
                    self.leaf_second.append(root.val)
            self.dfs(root.right)
        if self.switch:
            return self.leaf_first
        else:
            return self.leaf_second

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        data = self.dfs(root1)
        dt = self.dfs(root2)
        print(dt, data)


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)

tree2 = TreeNode(4)
tree.left = TreeNode(5)
tree.right = TreeNode(6)

sol = Solution()
print(sol.leafSimilar(tree, tree2))
