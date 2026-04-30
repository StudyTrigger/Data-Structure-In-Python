# Study Trigger: Linked List Operations
# Program: Check if Linked List is Palindrome
# Time Complexity : O(n)    Space Complexity : O(1)

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

    def isPalindrome(self):
        if self.head is None or self.head.next is None:
            return True
        
        # Step 1: Find middle
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse second half
        prev = None
        curr = slow
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Step 3: Compare both halves
        first = self.head
        second = prev
        
        while second:
            if first.info != second.info:
                return False
            first = first.next
            second = second.next
        
        return True


# --- Testing the Logic ---
mylist = LinkedList()

# Example 1: Palindrome → 10 -> 20 -> 30 -> 20 -> 10
mylist.insend(10)
mylist.insend(20)
mylist.insend(30)
mylist.insend(20)
mylist.insend(10)

if mylist.isPalindrome():
    print("Linked List is Palindrome")
else:
    print("Linked List is NOT Palindrome")