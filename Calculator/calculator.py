#Basic calculator project
import math
def cube(n):
    """
    Return the cube of a number, an integer provided as 'n'
    """
    return n * n * n

def squareroot(n):
    """
    Returns the square root of the number n. If n < 0, 
    then return the string "NAN" (Not A Number)
    """
    if n < 0:
        return "NAN"
    else:
        return math.sqrt(n)

def negate(n):
    """ Return the negative value of the argument 'n'.
    """
    return (0 - n)

def factorial(n):
    """Return n factorial
    The factorial of anything <= 1 is 1.
    The factorial of any integer greater than 1 is the product of all
    the integers from 1 to the number itself. For example,
    4 factorial = 1 x 2 x 3 x 4 = 24.
    """
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
