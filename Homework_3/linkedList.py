# Cesar Almendarez
# CSULA Spring 2023
# CS 3035-01 Programming Paradigms
# Homework 2 (Linked List ADT)
# Due - April 14 2023

class Node:
    def __init__(self, node_data):
        self.node_data = node_data
        self.next_node = None
        self.previous_node = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self): 
        return self.head is None
    
    def insertHead(self, data):
        # Create Node instance
        new_node = Node(data)

        if self.isEmpty(): 
            self.tail = new_node
        else: 
            self.head.previous_node = new_node

        new_node.next_node = self.head

        self.head = new_node
    
    def removeHead(self):
        #
        if self.isEmpty(): 
            return None

        #
        removed_node = self.head

        #
        self.head = removed_node.next_node

        #
        if self.head is None:
            self.tail = None
        else:
            self.head.previous_node = None

            return removed_node.node_data
        
    #
    def insertTail(self, data):
        #
        new_node = Node(data)

        #
        if self.isEmpty():
            self.head = new_node
        else:
            self.tail.next_node = new_node
            new_node.previous_node = self.tail
        
        #
        self.tail = new_node

    #
    def removeTail(self):
        #
        if self.isEmpty():
            return None
        
        #
        removed_node = self.tail

        #
        self.tail = removed_node.previous_node

        #
        if self.tail is None:
            self.head = None
        else:
            self.tail.next_node = None

        return removed_node.node_data
    
    def insertAtPos(self, data, pos):

        new_node = Node(data)

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

linked_list = LinkedList()
linked_list.insertHead(1)
linked_list.insertHead(2)
linked_list.insertHead(3)
linked_list.traverse()











        