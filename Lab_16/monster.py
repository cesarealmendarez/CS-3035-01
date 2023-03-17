'''
    Cesar Almendarez
    CSULA Spring 2023
    CS 3035-01 Programming Paradigms
    Lab 16 (Dunder Methods) 
    March 16 2023
'''

class Monster:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def attack(self, location):
        return self.name + " attacks " + location

    # Override str method
    def __str__(self):
        return self.name + "'s size is " + str(self.size)

    # Override equity method
    def __eq__(self, other):
        return (self.name == other.name) and (self.size == other.size)
        
    # Override add method
    def __add__(self, other):
        return self.name + other.name
    
Kraken = Monster("Kraken", 100)
Yeti = Monster("Yeti", 75)

print(Kraken.attack("Norway"))
print(Yeti.attack("Himalayas"))

print(str(Kraken))
print(str(Yeti))

print(Kraken == Yeti)

print(Kraken + Yeti)

'''
Sample Output:

Kraken attacks Norway
Yeti attacks Himalayas
Kraken's size is 100
Yeti's size is 75
False
KrakenYeti

'''




    
