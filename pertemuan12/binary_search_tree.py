class Node:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, kode, nama):
        new_node = Node(kode, nama)

        if self.root is None:
            self.root = new_node
            print(f"[INSERT] Data masuk: {kode} - {nama}")
            return

        current = self.root

        while True:
            if kode < current.kode:
                if current.left is None:
                    current.left = new_node
                    print(f"[INSERT] Data masuk: {kode} - {nama}")
                    return
                current = current.left

            else:
                if current.right is None:
                    current.right = new_node
                    print(f"[INSERT] Data masuk: {kode} - {nama}")
                    return
                current = current.right

    def search(self, kode):
        current = self.root

        while current:
            if kode == current.kode:
                return current

            elif kode < current.kode:
                current = current.left

            else:
                current = current.right

        return None

    def traversal_inorder(self, node):
        if node:
            self.traversal_inorder(node.left)
            print(f"{node.kode} - {node.nama}")
            self.traversal_inorder(node.right)

    def get_min(self):
        current = self.root

        while current.left:
            current = current.left

        return current

    def get_max(self):
        current = self.root

        while current.right:
            current = current.right

        return current

    def height(self, node):
        if node is None:
            return -1

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        if left_height > right_height:
            return left_height + 1

        return right_height + 1


tree = BST()

print('SISTEM DATA ARSIP "PUSAT INFORMASI"')
print("=" * 42)

tree.insert(55, "Algoritma")
tree.insert(25, "Pemrograman Web")
tree.insert(75, "Machine Learning")
tree.insert(15, "Logika Informatika")
tree.insert(35, "Keamanan Sistem")
tree.insert(65, "Cloud Computing")
tree.insert(90, "Analisis Data")

print("\n[INFO] Daftar Arsip (In-Order Traversal):")
tree.traversal_inorder(tree.root)

print()

cari_1 = tree.search(65)
if cari_1:
    print(f"[SEARCH] ID 65 ditemukan: {cari_1.nama}")
else:
    print("[SEARCH] ID 65 tidak ditemukan.")

cari_2 = tree.search(100)
if cari_2:
    print(f"[SEARCH] ID 100 ditemukan: {cari_2.nama}")
else:
    print("[SEARCH] ID 100 tidak ditemukan.")

minimum = tree.get_min()
maximum = tree.get_max()

print(f"\n[STATISTIK] ID Terkecil : {minimum.kode}")
print(f"[STATISTIK] ID Terbesar : {maximum.kode}")

print(f"[INFO] Height Tree : {tree.height(tree.root)}")

print("=" * 42)
print("Proses Selesai!")