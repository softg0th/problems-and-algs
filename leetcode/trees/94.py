from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.arr = []

    def traversal(self, node):
        if node is None:
            return []
        if node.left:
            self.traversal(node.left)
        self.arr.append(node.val)
        if node.right:
            self.traversal(node.right)
        return self.arr

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.arr = self.traversal(root)
        return self.arr

'''
# Тест 1: Пустое дерево
empty_tree = None
result_empty_tree = Solution().inorderTraversal(empty_tree)
print(result_empty_tree)  # Ожидаемый вывод: []

# Тест 2: Дерево с одним узлом
single_node_tree = TreeNode(5)
result_single_node_tree = Solution().inorderTraversal(single_node_tree)
print(result_single_node_tree)  # Ожидаемый вывод: [5]
'''
'''
# Тест 3: Балансированное дерево
balanced_tree = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
result_balanced_tree = Solution().inorderTraversal(balanced_tree)
print(result_balanced_tree)  # Ожидаемый вывод: [2, 1, 3]
'''
# Тест 4: Дерево с несколькими узлами
complex_tree = TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)), right=TreeNode(3))
result_complex_tree = Solution().inorderTraversal(complex_tree)
print(result_complex_tree)  # Ожидаемый вывод: [4, 2, 5, 1, 3]
