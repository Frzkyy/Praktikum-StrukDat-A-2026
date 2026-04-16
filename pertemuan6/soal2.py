class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")

def tambahKendaraan(head, plat):
    newNode = Node(plat)
    currentNode = head
    while currentNode:
        if currentNode.next == None:
            break
        currentNode = currentNode.next
    currentNode.next = newNode
    
def hapusKendaraan(head, plat):
    if head == plat:
        return head.next
    
    currentNode = head
    while currentNode.next and currentNode.next.data != plat:
        currentNode = currentNode.next

    if currentNode.next is None:
        return head

    currentNode.next = currentNode.next.next

    return head

    


mobil1 = Node("BM 8127 BX")
mobil2 = Node("B 9910 WX")
mobil3 = Node("BD 2209 HZ")
mobil4 = Node("BA 5410 PI")
mobil1.next = mobil2
mobil2.next = mobil3
mobil3.next = mobil4

traverseAndPrint(mobil1)

tambahKendaraan(mobil1, "KT 7881 PIP")

traverseAndPrint(mobil1)

hapusKendaraan(mobil1, "B 9910 WX")

traverseAndPrint(mobil1)