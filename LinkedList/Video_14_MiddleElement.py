# Study Trigger: Linked List Operations
# Program: Find Middle of a Linked List (Fast & Slow Pointer)
# Time Complexity : O(n)    Space Complexity : O(1)
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

    def find_middle(self):
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next          # Slow moves 1 step
            fast = fast.next.next     # Fast moves 2 steps
            
        return slow  # This is the middle node

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

n = int(input("How many elements you want to insert: "))
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    mylist.insend(ele)

print("\nOriginal Linked List:")
mylist.display()

# Finding the middle element
middle_node = mylist.find_middle()

if middle_node:
    print(f"\nMiddle Element is: {middle_node.info}")
else:
    print("\nThe list is empty.")
