# Study Trigger: Linked List Operations
# Program: Insert a node at a specific index/position
# --------------------------------------------------
class Node:
    def __init__(self, data):
        self.info = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insend(self, ele):
        new_node = Node(ele)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            
            current.next = new_node

    def inspos(self, ele, pos):
        new_node = Node(ele)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        for i in range(pos - 1):
            if current is None:
                break
            current = current.next

        if current is None:
            print("Position out of bounds")
        else:
            new_node.next = current.next
            current.next = new_node

    def display(self):
        if self.head is None:
            print("Empty Linked List")
        else:
            current = self.head
            while current:
                print(current.info, " -> ", end="")
                current = current.next
            print("None")

mylist = LinkedList()

#to create a list first
n=int(input("How many elements you want to insert"))
for i in range(n):
    ele=int(input("Enter element"))
    mylist.insend(ele)

print("My linked list")
mylist.display()

#Now add element at specific position
#Approach 1 : Passing hard code values
mylist.inspos(10, 0) # Insert 10 at pos 0
#Approach 2 : Passing user input values
ele=int(input("Enter element to be inserted "))
pos=int(input("Enter position "))
mylist.inspos(ele,pos) # Insert 15 at pos 1
print("List after specific insertions:")
mylist.display()