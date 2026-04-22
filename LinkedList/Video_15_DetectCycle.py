# Study Trigger: Linked List Operations
# Program: Cycle Detection in a Linked List (Floyd’s Cycle-Finding Algorithm)
# Time Complexity : O(n)    Space Complexity : O(1)
# LeetCode : Problem 141
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

    def has_cycle(self) -> bool:
        # Both racers start at the starting line
        slow = self.head
        fast = self.head
        
        # While the Rabbit has a path to run...
        while fast and fast.next:
            slow = slow.next          # Moves 1 step
            fast = fast.next.next     # Moves 2 steps
            
            # The Magic Moment: They meet!
            if slow == fast:
                return True
        
        # If the Rabbit hits a dead end, there's no cycle
        return False

# --- Testing the Logic ---

mylist = LinkedList()
# Adding elements: 1 -> 2 -> 3 -> 4
mylist.insend(1)
mylist.insend(2)
mylist.insend(3)
mylist.insend(4)

# Manually creating a cycle for testing: 4 -> 2
mylist.head.next.next.next.next = mylist.head.next

if mylist.has_cycle():
    print("Cycle Detected!")
else:
    print("No Cycle Found.")