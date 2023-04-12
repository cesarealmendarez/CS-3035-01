# Cesar Almendarez
# CSULA Spring 2023
# CS 3035-01 Programming Paradigms
# Lab 19 (ADT: Stack)
# April 5 2023

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]

    def size(self):
        return len(self.stack)
    
# Create Stack class instance
stack = Stack()

# Pushing 5 elements to stack
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

# Popping 2 elements from stack
stack.pop()
stack.pop()

# Print size of stack
print("Size of stack = ", stack.size())

# Test if empty stack
print("Stack is empty = ", stack.isEmpty())

# Peeking top element
print("Peeking top element of stack = ", stack.peek())

# Sample Output
# Size of stack =  3
# Stack is empty =  False
# Peeking top element of stack =  3
