"""
    File: Lab5.py
    Authored By: Cesar E Almendarez
    Written On: February 7 2023

    This program will ask the user to enter an integer using the input() method.
    Their integer will then be casted as an int and stored in the variable userInt
    userInt will then be passed as a parameter into evenOdd()
    If userInt % 2 results in a remainder of 0, then userInt is even
    Else if userInt % 2 results in a remainder other than 0, then userInt is odd
"""

def evenOdd(userInt):
    if userInt % 2 == 0:
        print("%d is even" % userInt)
    else:
        print("%d is odd" % userInt)


userInt = int(input("Please enter an integer: "))

evenOdd(userInt = userInt)

"""
    Sample Runs: 

    Please enter an integer: 1023
    1023 is odd

    Please enter an integer: -1982
    -1982 is even
"""

