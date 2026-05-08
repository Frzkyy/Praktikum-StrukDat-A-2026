class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_manual(self):
        self.root = Node("P")

        self.root.left = Node("Q")
        self.root.right = Node("R")

        self.root.left.left = Node("S")
        self.root.left.right = Node("T")

        self.root.right.left = Node("U")

    def traverse_preorder(self, node, result):
        if node:
            result.append(node.data)
            self.traverse_preorder(node.left, result)
            self.traverse_preorder(node.right, result)

    def traverse_inorder(self, node, result):
        if node:
            self.traverse_inorder(node.left, result)
            result.append(node.data)
            self.traverse_inorder(node.right, result)

    def traverse_postorder(self, node, result):
        if node:
            self.traverse_postorder(node.left, result)
            self.traverse_postorder(node.right, result)
            result.append(node.data)

    def get_leaf_nodes(self, node, result):
        if node:
            if node.left is None and node.right is None:
                result.append(node.data)

            self.get_leaf_nodes(node.left, result)
            self.get_leaf_nodes(node.right, result)


tree = BinaryTree()

print('SISTEM PEMANTAUAN JALUR "KILAT EXPRESS"')
print("=" * 45)

print("[INFO] Membuat struktur jalur...")
tree.insert_manual()
print("[INFO] Struktur selesai dibuat.\n")

preorder = []
inorder = []
postorder = []
leaf_nodes = []

tree.traverse_preorder(tree.root, preorder)
tree.traverse_inorder(tree.root, inorder)
tree.traverse_postorder(tree.root, postorder)
tree.get_leaf_nodes(tree.root, leaf_nodes)

print("HASIL PENELUSURAN:")
print("1. Pre-Order  :", " - ".join(preorder))
print("2. In-Order   :", " - ".join(inorder))
print("3. Post-Order :", " - ".join(postorder))

print("\n[DATA] Jalur Akhir (Leaf Nodes):", ", ".join(leaf_nodes))

print("=" * 45)
print("Pemeriksaan Selesai!")