class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        # Langkah 1
        new = Node(data)

        #Langkah 2
        if self.root is None:
            # Jika ya
            self.root = new
            return
        
        #Langkah 3
        P = self.root
        Q = self.root
        
        #Langkah 4
        while Q is not None and new.data != P.data:
            #Langkah 5
            P = Q

            if new.data < P.data:
                Q = P.left
            else:
                Q = P.right
        
        #Langkah 7
        if new.data == P.data:
            #Jika iya
            print("Datanya Duplikat")
        
        #Langkah 8
        if new.data < P.data:
            #Jika iya
            P.left = new
        #Jika tidak
        else:
            P.right = new

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_root(self,data):
        self.root = Node(data)
    
    def insert_left(self, pr_node, data):
        if pr_node.left is None:
            pr_node.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = pr_node.left
            pr_node.left = new_node
    
    def insert_right(self, pr_node, data):
        if pr_node.right is None:
            pr_node.right = Node(data)
        else:
            new_node = Node(data)
            new_node.right = pr_node.right
            pr_node.right = new_node

def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")

tree = BinaryTree()

tree.insert_root('F')
tree.insert_left(tree.root, "B")
tree.insert_right(tree.root, "G")
tree.insert_left(tree.root.left, "A")
tree.insert_right(tree.root.left, "D")
tree.insert_left(tree.root.left.right, "C")
tree.insert_right(tree.root.left.right, "E")
tree.insert_right(tree.root.right, "I")
tree.insert_left(tree.root.right.right, "H")


Tree_ex = BinaryTree()

Tree_ex.insert_root(10)
Tree_ex.insert_left(Tree_ex.root, 5)
Tree_ex.insert_right(Tree_ex.root, 15)
Tree_ex.insert_left(Tree_ex.root.left, 3)
Tree_ex.insert_right(Tree_ex.root.left, 7)

print("=== Inorder ===")
inorder(tree.root)
print("\n=== Preorder ===")
preorder(tree.root)
print("\n=== Postorder ===")
postorder(tree.root)
print()


bst = BinarySearchTree()
    
bst.insert(23)
bst.insert(25)
bst.insert(30)
bst.insert(87)
bst.insert(91)
bst.insert(29)
bst.insert(333)
bst.insert(972)

print()
print("=== Inorder ===")
inorder(bst.root)