# Study Trigger: Linked List Operations
# Program: Find Nth Node from End (Two-Pointer / Gap Logic)
# Time Complexity : O(n)    Space Complexity : O(1)
# Problem: Practice Problem (Nth Node from Last)
# Video Link : https://youtube.com/playlist?list=PLMsw1Zy78Kz3THKZUYuht-dLB7bwlheZ-&si=Kc1wS_Gz4tzL2lqw

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

    def getNthFromLast(self, n):
        # Initializing both pointers to head
        slow = self.head
        fast = self.head
        
        # Step 1: Move fast pointer 'n' steps ahead to create the gap
        for i in range(n):
            if fast is None:
                return None  # List is smaller than n
            fast = fast.next
            
        # Step 2: Move both pointers one step at a time
        # When fast reaches None, slow will be at the Nth node from end
        while fast:
            slow = slow.next
            fast = fast.next
            
        return slow  # This is our target node


# --- Testing the Logic ---
mylist = LinkedList()

# Creating a list: 10 -> 20 -> 30 -> 40 -> 50
mylist.insend(10)
mylist.insend(20)
mylist.insend(30)
mylist.insend(40)
mylist.insend(50)

n = 2
result_node = mylist.getNthFromLast(n)

if result_node:
    print(f"The {n}nd node from the end is: {result_node.info}")
else:
    print(f"The list is shorter than {n} nodes.")