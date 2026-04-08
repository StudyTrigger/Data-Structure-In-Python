#Node insert at end of Linked List 
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
    
    def insend(self, ele):
        new_node = Node(ele)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            
            current.next = new_node
    
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
n=int(input("How many elements you want to insert"))
for i in range(n):
    ele=int(input("Enter element"))
    mylist.insend(ele)

print("My linked list")
mylist.display()