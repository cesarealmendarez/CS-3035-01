
# Cesar Almendarez
# CSULA Spring 2023
# CS 3035-01 Programming Paradigms
# Lab 21(Exception Handling)
# April 13 2023

import math

class RightTriangle:
    def __init__(self, side_1, side_2, hypotenuse = None):

        # Raise error for invalid side input and invalid triplet
        try:

            side_1 = float(side_1)
            side_2 = float(side_2)

            if hypotenuse is None:
                hypotenuse = math.sqrt(side_1 ** 2 + side_2 ** 2)

            else:
                hypotenuse = float(hypotenuse)
            
            if side_1 <= 0 or side_2 <= 0 or hypotenuse <= 0:
                raise ValueError("Error - sides have to be positive!")
            
            elif abs(side_1 ** 2 + side_2 ** 2 - hypotenuse ** 2) > 0.0001:
                raise ValueError("Error - not a valid Pythagorean triplet!")
            
            else:
                self.side_1 = side_1
                self.side_2 = side_2
                self.hypotenuse = hypotenuse
                
        except (TypeError, ValueError):
            raise ValueError("Error - sides must be able to be casted as a float!")
    
    def __eq__(self, other_right_triangle):
        # Check if triangle 1 and triangle 2 are the same
        if not isinstance(other_right_triangle, RightTriangle):
            return False
        
        # are NOT a valid Pythagorean triple
        if abs(self.hypotenuse - other_right_triangle.hypotenuse) > 0.0001:
            return False
        
        # are a valid Pythagorean triple
        if (abs(self.side_1 - other_right_triangle.side_1) < 0.0001 and abs(self.side_2 - other_right_triangle.side_2) < 0.0001) or (abs(self.side_1 - other_right_triangle.side_2) < 0.0001 and abs(self.side_2 - other_right_triangle.side_1) < 0.0001):
            return True
        
        return False
    
    def __str__(self):
        return "Right Triangle with side a = {}, side b = {}, and hypotenuseotenuse = {}!".format(self.side_1, self.side_2, self.hypotenuse)


# Client Code

# Declare Triangle 1
triangle_1 = None

# While Triangle 1 is not intialized keep prompting for its attibutes
while triangle_1 is None:
    try:
        side_1 = float(input("Enter a nonnegative value for side a: "))

        side_2 = float(input("Enter a nonnegative value for side b: "))

        triangle_1 = RightTriangle(side_1, side_2)

    # Catch nonnegative value input
    except ValueError as e:
        print(e)

# Declare Triangle 2
triangle_2 = None

# While Triangle 2 is not intialized keep prompting for its attibutes
while triangle_2 is None:
    try:
        side_1 = float(input("Enter a nonnegative value for side a: "))

        side_2 = float(input("Enter a nonnegative value for side b: "))

        hypotenuse = float(input("Enter a nonnegative value for hypotenuse: "))

        triangle_2 = RightTriangle(side_1, side_2, hypotenuse)

    # Catch nonnegative value input
    except ValueError as e:
        print(e)

print("Triangle 1 is equal to itself - {}!".format(triangle_1 == triangle_1))

print("Triangle 1 is equal to Triangle 2 - {}!".format(triangle_1 == triangle_2))

# Example Output
# Enter a nonnegative value for side a: 3.0
# Enter a nonnegative value for side b: 4.0
# Enter a nonnegative value for side a: 3.0
# Enter a nonnegative value for side b: 4.0
# Enter a nonnegative value for hypotenuse: 5.0
# Triangle 1 is equal to itself - True!
# Triangle 1 is equal to Triangle 2 - True!
