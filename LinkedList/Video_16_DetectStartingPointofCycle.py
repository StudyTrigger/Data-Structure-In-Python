# Study Trigger: Linked List Operations
# Program: Find Starting Node of Cycle (Floyd’s Cycle-Finding Algorithm)
# Time Complexity : O(n)    Space Complexity : O(1)
# LeetCode : Problem 142
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

    def find_cycle_start(self):
        slow = self.head
        fast = self.head
        
        # Step 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        else:
            return None   # No cycle
        
        # Step 2: Move one pointer to head
        slow = self.head
        
        # Step 3: Move both one step
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow   # Starting node of cycle


# --- Testing the Logic ---
mylist = LinkedList()
# Adding elements: 1 -> 2 -> 3 -> 4
mylist.insend(1)
mylist.insend(2)
mylist.insend(3)
mylist.insend(4)

# Manually creating a cycle: 4 -> 2
mylist.head.next.next.next.next = mylist.head.next

start_node = mylist.find_cycle_start()

if start_node:
    print("Cycle starts at node with value:", start_node.info)
else:
    print("No Cycle Found.")