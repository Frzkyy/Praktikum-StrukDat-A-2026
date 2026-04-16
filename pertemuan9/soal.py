class Node:
    def __init__(self, judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang
        self.prev = None
        self.next = None

# ===================
#       Bagian A
# ===================

print("=" * 30)
print("           Bagian A")
print("=" * 30)

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_tail(self, judul, pengarang):
        new_node = Node(judul, pengarang)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def prepend(self, judul, pengarang):
        new_node = Node(judul, pengarang)

        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head

        self.head = new_node

    def delete_by_judul(self, judul):
        current = self.head

        while current:
            if current.judul == judul:
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                else:
                    current.prev.next = current.next

                    if current.next:
                        current.next.prev = current.prev
                return

            current = current.next

    def print_forward(self):
        current = self.head
        while current:
            print("judul:", current.judul, "|", "karya:", current.pengarang, end=" <-> ")
            current = current.next
        print("None")

    def print_backward(self):
        current = self.head

        # Pergi ke node terakhir
        while current and current.next:
            current = current.next

        # Tampilkan mundur
        while current:
            print("judul:", current.judul, "|", "karya:", current.pengarang, end=" <-> ")
            current = current.prev
        print("None")

buku = DoublyLinkedList()
buku.insert_tail("Laskar Pelangi", "Tere Liye kah?")
buku.insert_tail("Bumi Manusia", "Mungkin Tere Liye")
buku.insert_tail("Sang Pemimpi", "Bisa jadi Tere Liye")
print()
print("Ini Forward")
buku.print_forward()
print()
print("Ini Backward")
buku.print_backward()
print()
buku.delete_by_judul("Laskar Pelangi")
print()
print("Ini Menghapus Laskar Pelangi")
buku.print_backward()

# ===================
#       Bagian B
# ===================

print("=" * 30)
print("           Bagian B")
print("=" * 30)


class NodeB:
    def __init__(self, nama):
        self.nama = nama
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_tail(self, nama):
        new_node = NodeB(nama)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head


    def delete_head(self):
        nama = self.head.nama
        if self.head is None:
            return

        current = self.head
        prev = None

        while True:
            if current.nama == nama:
                
                if current == self.head and current.next == self.head:
                    self.head = None
                    
                elif current == self.head:
                    last = self.head
                    
                    while last.next != self.head:
                        last = last.next
                        
                    self.head = self.head.next
                    
                    last.next = self.head
                    
                else:
                    
                    prev.next = current.next

                return

            prev = current
            current = current.next

            if current == self.head:
                break

    def print_antrian(self):
        if self.head is None:
            print("Linked list kosong")
            return

        current = self.head

        while True:
            print(current.nama, end=" -> ")
            current = current.next

            if current == self.head:
                break

        print(f"(kembali ke {current.nama})")



antrian = CircularLinkedList()

antrian.insert_tail("Andi")
antrian.insert_tail("Budi")
antrian.insert_tail("Caca")
antrian.insert_tail("Dontol")

print("Tampilkan Antrian")
antrian.print_antrian()
print()
print("Tambahkan Edo")
antrian.insert_tail("Edo")
print()
print("Tampilkan Antrian")
antrian.print_antrian()
antrian.delete_head()
print()
print("Tampilkan Antrian")
antrian.print_antrian()