class TreeObj:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None


    def append(self, data):
        value = TreeObj(data)
        if not self.root:
            self.root = value
            return

        if not self.root.left and data < self.root.data:
            self.root.left = value
            return

        if not self.root.right and data > self.root.data:
            self.root.right = value
            return

        if value.data < self.root.data:
            while self.root.left:
                if self.root
