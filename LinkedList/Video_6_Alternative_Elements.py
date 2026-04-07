#Find Sum, Count, Average of a Linked List
class Node:
    def __init__(self,data):
        self.info=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def insbeg(self,ele):
        current=Node(ele)
        if self.head is None:
            self.head=current
        else:
            current.next=self.head
            self.head=current
    
    def display(self):
        if self.head is None:
            print("Empty Linked List")
            return
        else:
            current=self.head
            while current:
                print(current.info," -> ", end="")
                current=current.next
            print("None")
    
    #Approach 1 using count variable
    def displayAlternate1(self):
        if self.head is None:
            print("Empty Linked List")
            return
        else:
            count=1
            current=self.head
            while current:
                if count%2!=0:
                    print(current.info," -> ", end="")
                count+=1
                current=current.next
            print("None")
    
    #Approach 2 using flag concept (1 and -1)
    def displayAlternate2(self):
        if self.head is None:
            print("Empty Linked List")
            return
        else:
            display=1
            current=self.head
            while current:
                if display==1:
                    print(current.info," -> ", end="")
                display=display*(-1)
                current=current.next
            print("None")
    
    #Approach 3 using pointer move
    def displayAlternate3(self):
        if self.head is None:
            print("Empty Linked List")
            return
        else:
            current=self.head
            while current:
                print(current.info," -> ", end="")
                if current.next:  # Check if we can skip one node
                    current = current.next.next
                else: # We are at the last node of an odd-length list
                    current = None
            print("None")

mylist=LinkedList()
n=int(input("How many elements you want to insert"))
for i in range(n):
    ele=int(input("Enter element"))
    mylist.insbeg(ele)

print("My linked list")
mylist.display()
print("Alternative Elements using Approach I ")
mylist.displayAlternate1()
print("Alternative Elements using Approach II ")
mylist.displayAlternate2()
print("Alternative Elements using Approach III ")
mylist.displayAlternate3()