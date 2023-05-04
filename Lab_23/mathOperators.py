'''
    Cesar Almendarez
    CSULA Spring 2023
    CS 3035-01 Programming Paradigms
    Lab 23 (Functions as First Class Citizens in Python) 
    April 25 2023
'''

from decimal import *

def complexNumberAdder(a, b):
    # return added complex values
    return a + b

def complexPartialAdder(a, b):
    # return added real values
    return a.real + b.real

def precisionMultiplier(a, b, precisionValue):
    #set precision value via context
    getcontext().prec = precisionValue

    # return multiplies values of a and b with provided precision value
    return Decimal(str(a)) * Decimal(str(b))

def scientificCalculator(mathFunction, funcationOne, functionTwo, *args):
    return mathFunction(funcationOne, functionTwo, *args)
    
print(scientificCalculator(complexNumberAdder, 10 + 7j, 8 - 1j))
print(scientificCalculator(complexPartialAdder, 10 + 7j, 8 - 1j)) 
print(scientificCalculator(precisionMultiplier, 7.1, 4.2, 9)) 

# Sample Output
(18+6j)
18.0
29.82