# Study Trigger: Linked List Operations
# Program: Delete a node from a specific index/position
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
        if self.head is None: self.head = new_node
        else:
            current = self.head
            while current.next: current = current.next
            current.next = new_node

    def delpos(self, pos):
        if self.head is None:
            print("List is empty")
            return
        
        if pos == 0:
            self.head = self.head.next
            return

        current = self.head
        for i in range(pos - 1):
            if current is None or current.next is None:
                break
            current = current.next

        if current is None or current.next is None:
            print("Position out of range")
        else:
            current.next = current.next.next

    def display(self):
        current = self.head
        while current:
            print(current.info, " -> ", end="")
            current = current.next
        print("None")

mylist=LinkedList()
#to create a list first
n=int(input("How many elements you want to insert"))
for i in range(n):
    ele=int(input("Enter element"))
    mylist.insend(ele)

print("My linked list")
mylist.display()

pos=int(input("Enter position : "))
mylist.delpos(pos) 
print("After deleting node at index", pos,":")
mylist.display()