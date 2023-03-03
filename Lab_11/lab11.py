'''
    File lab11.py
    Authored By: Cesar E Almendarez
    Written On: February 27 2023
'''

# Return the element at the given index of a string
def findElement(string, index):
    return string[index]

# Return a string from the concatenation of string1 and string2
def concatStrings(string1, string2):
    return string1 + string2

# Return the first half of a string
def divideString(string):
    return string[:len(string) // 2]


inputString1 = "This is a test string"
inputString2 = "...it tests your functions"
inputString3 = "functions"

print(findElement(inputString1, 0))
print(concatStrings(inputString1, inputString2))
print(divideString(inputString3))