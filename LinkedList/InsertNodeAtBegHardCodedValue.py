#Linked List Insertion with Static Input (hard coded value) 
class Node:
    def __init__(self,data):
        self.info=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def insbeg(self,ele):
        current=Node(ele)
        if self.head is None:
            self.head=current
        else:
            current.next=self.head
            self.head=current
    
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
mylist.insbeg(10)
mylist.insbeg(20)
mylist.insbeg(30)

print("My linked list")
mylist.display()