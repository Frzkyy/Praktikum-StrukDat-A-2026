class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def tampilkan_antrean(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")

def sisipkan_vip(head, plat_baru, plat_target):
    platBaru = Node(plat_baru)
    currentNode = head
    while currentNode.next.data != plat_target and currentNode.next:
        currentNode = currentNode.next
    
    platBaru.next = currentNode.next
    currentNode.next = platBaru
    return head

    

vip1 = Node("BM 8127 BX")
vip2 = Node("B 9910 WX")
vip3 = Node("BD 2209 HZ")
vip4 = Node("BA 5410 PI")
vip1.next = vip2
vip2.next = vip3
vip3.next = vip4

tampilkan_antrean(vip1)
