from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return left+1 if left > right else right+1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = self.dfs(root)
        return ans

# root = [3,9,20,null,null,15,7]


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7) # Testing the maxDepth function solution = Solution() result = solution.maxDepth(root) print(result)
sol = Solution()
print(sol.maxDepth(root))
