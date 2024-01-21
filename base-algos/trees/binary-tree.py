class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def __find(self, node, parent, value):
        if node is None:
            return None, parent

        if value == node.data:
            return node, parent

        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent

    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj

        s, p = self.__find(self.root, None, obj.data)

        if obj.data < s.data:
                s.left = obj
        else:
            s.right = obj

        return obj

    def show_tree(self, node):
        if node is None:
            return

        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)


v = [2, 1]

t = Tree()

for x in v:
    t.append(Node(x))

t.show_tree(t.root)
