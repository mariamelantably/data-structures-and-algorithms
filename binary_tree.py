class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is not None:
                    self.left.insert(data)
                else:
                    self.left = Tree(data)
            elif data > self.data:
                if self.right is not None:
                    self.right.insert(data)
                else:
                    self.right = Tree(data)
            else:
                return
        
    def preorder_traversal(self):
        print(self.data, end = " ")
        if self.left is not None:
            self.left.preorder_traversal()
        if self.right is not None:
            self.right.preorder_traversal()

    def inorder_traversal(self):
        if self.left is not None:
            self.left.inorder_traversal()
        print(self.data, end = " ")
        if self.right is not None:
            self.right.inorder_traversal()

    def postorder_traversal(self):
        if self.left is not None:
            self.left.postorder_traversal()
        if self.right is not None:
            self.right.postorder_traversal()
        print(self.data, end = " ")    

print("=================================")
print("=== Loading tree with numbers ===")
tree = Tree(50)
tree.insert(30)
tree.insert(20)
tree.insert(40)
tree.insert(10)
tree.insert(80)
tree.insert(100)
tree.insert(60)
tree.insert(70)
tree.insert(90)
print("\n === In-order traversal of tree ===")
tree.inorder_traversal()
print("\n === Pre-order traversal of tree ===")
tree.preorder_traversal()
print("\n === Post-order traversal of tree ===")
tree.postorder_traversal()