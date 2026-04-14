# Study Trigger: Linked List Operations
# Program: Delete the first node (Head) of the Linked List
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
            while current.next:
                current = current.next
            current.next = new_node

    def delfirst(self):
        if self.head is None:
            print("List is empty, nothing to delete")
        else:
            self.head = self.head.next

    def display(self):
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

mylist.delfirst()
print("After deleting first node:")
mylist.display()