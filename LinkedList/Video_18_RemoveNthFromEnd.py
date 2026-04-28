# Study Trigger: Linked List Operations
# Program: Remove Nth Node from End (Optimized One-Pass)
# Time Complexity : O(n)    Space Complexity : O(1)
# Problem: LeetCode 19 (Remove Nth Node From End of List)
# Video Link : https://youtube.com/playlist?list=PLMsw1Zy78Kz3THKZUYuht-dLB7bwlheZ-

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

    def removeNthFromLast(self, n):
        # Create a dummy node to handle edge cases (like removing the head)
        dummy = Node(0)
        dummy.next = self.head
        
        slow = dummy
        fast = dummy
        
        # Step 1: Move fast pointer 'n + 1' steps ahead
        # This ensures 'slow' stops exactly one node BEFORE the target
        for i in range(n + 1):
            if fast is None:
                return None  # List is smaller than n
            fast = fast.next
            
        # Step 2: Move both pointers until fast hits the end
        while fast:
            slow = slow.next
            fast = fast.next
            
        # Step 3: Remove the node by skipping it
        if slow.next:
            slow.next = slow.next.next
            
        # Update head in case the original head was removed
        self.head = dummy.next
        return self.head

    def display(self):
        current = self.head
        while current:
            print(current.info, end=" -> ")
            current = current.next
        print("None")


# --- Testing the Logic ---
mylist = LinkedList()

# Creating a list: 10 -> 20 -> 30 -> 40 -> 50
mylist.insend(10)
mylist.insend(20)
mylist.insend(30)
mylist.insend(40)
mylist.insend(50)

print("Original List:")
mylist.display()

n = 2
print(f"\nRemoving {n}nd node from the end...")
mylist.removeNthFromLast(n)

print("Updated List:")
mylist.display()