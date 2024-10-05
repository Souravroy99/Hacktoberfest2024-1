class RedBlackTree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
            self.colour = 'R'
            self.parent = None

    def __init__(self):
        self.root = None
        self.ll = False
        self.rr = False
        self.lr = False
        self.rl = False

    def rotateLeft(self, node):
        x = node.right
        y = x.left
        x.left = node
        node.right = y
        node.parent = x
        if y is not None:
            y.parent = node
        return x

    def rotateRight(self, node):
        x = node.left
        y = x.right
        x.right = node
        node.left = y
        node.parent = x
        if y is not None:
            y.parent = node
        return x

    def insertHelp(self, root, data):
        f = False

        if root is None:
            return self.Node(data)
        elif data < root.data:
            root.left = self.insertHelp(root.left, data)
            root.left.parent = root
            if root != self.root:
                if root.colour == 'R' and root.left.colour == 'R':
                    f = True
        else:
            root.right = self.insertHelp(root.right, data)
            root.right.parent = root
            if root != self.root:
                if root.colour == 'R' and root.right.colour == 'R':
                    f = True

        if self.ll:
            root = self.rotateLeft(root)
            root.colour = 'B'
            root.left.colour = 'R'
            self.ll = False
        elif self.rr:
            root = self.rotateRight(root)
            root.colour = 'B'
            root.right.colour = 'R'
            self.rr = False
        elif self.rl:
            root.right = self.rotateRight(root.right)
            root.right.parent = root
            root = self.rotateLeft(root)
            root.colour = 'B'
            root.left.colour = 'R'
            self.rl = False
        elif self.lr:
            root.left = self.rotateLeft(root.left)
            root.left.parent = root
            root = self.rotateRight(root)
            root.colour = 'B'
            root.right.colour = 'R'
            self.lr = False

        if f:
            if root.parent.right == root:
                if root.parent.left is None or root.parent.left.colour == 'B':
                    if root.left is not None and root.left.colour == 'R':
                        self.rl = True
                    elif root.right is not None and root.right.colour == 'R':
                        self.ll = True
                else:
                    root.parent.left.colour = 'B'
                    root.colour = 'B'
                    if root.parent != self.root:
                        root.parent.colour = 'R'
            else:
                if root.parent.right is None or root.parent.right.colour == 'B':
                    if root.left is not None and root.left.colour == 'R':
                        self.rr = True
                    elif root.right is not None and root.right.colour == 'R':
                        self.lr = True
                else:
                    root.parent.right.colour = 'B'
                    root.colour = 'B'
                    if root.parent != self.root:
                        root.parent.colour = 'R'
            f = False
        return root

    def inorderTraversalHelper(self, node):
        if node is not None:
            self.inorderTraversalHelper(node.left)
            print(node.data, end=" ")
            self.inorderTraversalHelper(node.right)

    def printTreeHelper(self, root, space):
        if root is not None:
            space += 10
            self.printTreeHelper(root.right, space)
            print("\n" + " " * (space - 10) + str(root.data))
            self.printTreeHelper(root.left, space)

    def insert(self, data):
        if self.root is None:
            self.root = self.Node(data)
            self.root.colour = 'B'
        else:
            self.root = self.insertHelp(self.root, data)

    def inorderTraversal(self):
        self.inorderTraversalHelper(self.root)

    def printTree(self):
        self.printTreeHelper(self.root, 0)


t = RedBlackTree()
arr = [1, 4, 6, 3, 5, 7, 8, 2, 9]
for i in range(9):
    t.insert(arr[i])
    print()
    t.inorderTraversal()
t.printTree()
