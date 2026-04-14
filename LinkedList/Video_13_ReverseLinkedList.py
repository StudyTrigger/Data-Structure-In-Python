# Study Trigger: Linked List Operations
# Program: Reverse a Linked List (Iterative Method)
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

    def reverse_list(self):
        prev = None
        curr = self.head
        
        while curr:
            # 1. Store (Save the next node)
            next_node = curr.next
            
            # 2. Todo (Reverse the link)
            curr.next = prev
            
            # 3. Jodo (Update previous)
            prev = curr
            
            # 4. Aage Badho (Move to the saved next node)
            curr = next_node
            
        # Update the head of the list to the last node processed
        self.head = prev

    def display(self):
        if self.head is None:
            print("Empty Linked List")
        else:
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

print("Original Linked List:")
mylist.display()

print("\nReversing the list...")
mylist.reverse_list()

print("Reversed Linked List:")
mylist.display()