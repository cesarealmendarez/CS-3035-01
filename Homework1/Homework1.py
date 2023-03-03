'''
    Assignment: Homework 1
    File: Homework1.py
    Authored By: Cesar E Almendarez
    Written On: February 15 2023
'''

# add accepts three values and returns x + y + z
def add(x, y, z):
    return x + y + z

# subtract accepts three values and returns z - y - x
def subtract(x, y, z):
    return z - y - x

# divide accepts two values and returns x / y
def divide(x, y):
    return x / y

# multiply accepts two values and returns x * y
def multiply(x, y):
    return x * y

# intialize x, y, z with int values
x = 5
y = 20
z = 16

# print x, y, z values
print("x =", x)
print("y =", y)
print("z =", z)

print("div(mult(add(x, y, z), x), mult(sub(x, y, z), y))")

# print expression evaluation
print(divide(multiply(add(x, y, z), x), multiply(subtract(x, y, z), y)))

'''
    Sample Run:
        x = 5
        y = 20
        z = 16
        div(mult(add(x, y, z), x), mult(sub(x, y, z), y))
        -1.1388888888888888

'''
