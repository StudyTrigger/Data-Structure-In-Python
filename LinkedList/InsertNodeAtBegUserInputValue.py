#Linked List Insertion with Dynamic User Input
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
n=int(input("How many elements you want to insert"))
for i in range(n):
    ele=int(input("Enter element"))
    mylist.insbeg(ele)

print("My linked list")
mylist.display()