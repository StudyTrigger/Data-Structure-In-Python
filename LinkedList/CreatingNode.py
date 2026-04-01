class Node:
    def __init__(self,data):
        self.info=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def display(self):
        if self.head is None:
            print("Empty Linked List")
            return
        else:
            current=self.head
            while current:
                print(current.info," -> ", end="")
                current=current.next
            print("None")

mylist=LinkedList()
node1=Node(10)
node2=Node(20)
node3=Node(30)

mylist.head=node1
node1.next=node2
node2.next=node3

print("My linked list")
mylist.display()