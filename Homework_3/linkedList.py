# Cesar Almendarez
# CSULA Spring 2023
# CS 3035-01 Programming Paradigms
# Homework 2 (Linked List ADT)
# Due - April 14 2023

class Node:
    def __init__(self, node_data):
        self.node_data = node_data
        self.previous_node = None
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.tail = None
        self.head = None

    def isEmpty(self): 
        return self.head is None
    
    def insertHead(self, data):
        # Initialize Node instance
        new_node = Node(data)

        # If LinkedList is empty set tail and head to new node
        if self.isEmpty(): 
            self.tail = new_node
        else: 
            self.head.previous_node = new_node

        new_node.next_node = self.head

        self.head = new_node
    
    def removeHead(self):
        if self.isEmpty(): 
            return None

        # Get removed node instance
        removed_node = self.head

        # Set new head to node next to removed node instance
        self.head = removed_node.next_node

        if self.head is None:
            self.tail = None
        else:
            self.head.previous_node = None

            return removed_node.node_data
    
    def insertTail(self, data):
        # Initialize new node instance
        new_node = Node(data)

        # Update head and tail of Linked List
        if self.isEmpty():
            self.head = new_node
        else:
            self.tail.next_node = new_node
            new_node.previous_node = self.tail
    
        self.tail = new_node

    def removeTail(self):
        if self.isEmpty():
            return None
        
        removed_node = self.tail

        self.tail = removed_node.previous_node

        if self.tail is None:
            self.head = None
        else:
            self.tail.next_node = None

        return removed_node.node_data
    
    def insertAtPos(self, data, pos):

        # Intialize new node instance 
        new_node = Node(data)

        # If position is 1 then insert node as new head
        if pos == 1:
            self.insertHead(data)
        else:
            current_node = self.head

            i = 1

            while i < (pos - 1) and current_node is not None:
                current_node = current_node.next_node
                i += 1
            
            if current_node is None:
                self.insertTail(data)
            else:
                new_node.previous_node = current_node
                new_node.next_node = current_node.next_node

                current_node.next_node = new_node
                new_node.next_node.previous_node = new_node

    def traverse(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.node_data)
            current_node = current_node.next_node

# Pre-defined test cases for all Linked List ADT functions
linkedList = LinkedList()

# Should be True
print(linkedList.isEmpty())  

linkedList.insertHead(2)
linkedList.insertHead(4)
linkedList.insertHead(8)
linkedList.insertHead(16)

linkedList.insertTail(32)
linkedList.insertTail(64)

# Remove 16
print(linkedList.removeHead())  

# Remove 64
print(linkedList.removeTail())  

linkedList.insertAtPos(128, 3)

# 8 4 128 2 32
linkedList.traverse()  

# Output
# True
# 16
# 64
# 8
# 4
# 128
# 2
# 32









        