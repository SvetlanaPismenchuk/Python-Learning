#Euler Palindrom Problem

def is_palindrome(n: int) -> bool: 
    '''
    Checks whether an integer is a palindrome.

    A palindrome is a value that reads the same forward and backward.
    The integer n is converted into a string s so it can be reversed easily.

    Returns True if s equals its reverse, and False otherwise.
    '''
    s = str(n) 
    return s == s[::-1]  


def best_palindrome(low: int = 100, high: int = 999) -> tuple[int, int, int]:
    '''
    Finds the largest palindrome product made from multiplying two integers
    in the range [low, high].

    The function checks products a*b and keeps track of the best (largest)
    palindrome found so far using three storage variables:
      - best_palindrome: the largest palindrome product found
      - best_a: the first factor that produced best_palindrome
      - best_b: the second factor that produced best_palindrome

    Returns a tuple containing (best_palindrome, best_a, best_b).
    '''

    best_palindrome = 0
    best_a = 0
    best_b = 0

    for a in range(high, low -1, -1):
        if a * a < best_palindrome: #if the same number squared is a larger palindrome than an a * b number
            break

        for b in range(a, low -1, -1):
            product = a * b

            if product < best_palindrome:
             break
         
            if is_palindrome(product):
                best_palindrome = product
                best_a = a
                best_b = b
    return best_palindrome, best_a, best_b


def largest_palindrome_product():
    '''
    Runs the palindrome search and prints the final result.

    This function calls best_palindrome() and stores the returned values
    in x, y, and z:
      - x is the largest palindrome product
      - y and z are the two factors that multiply to give x

    It then prints the palindrome and the matching factors in a readable format.
    '''
    
    x, y, z = best_palindrome()
    
    print(f"Largest palindrome product: {x}")
    print(f"Factors: {y} x {z} = {x}")
    

largest_palindrome_product()
