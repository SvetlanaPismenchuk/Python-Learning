#Euler Palindrom Problem

def is_palindrome(n: int) -> bool: #expects input to be an integer #type hint
    s = str(n) #converts integer to string
    return s == s[::-1]  # since integer is string, we can reverse it and only return the integer if it is read the same way backwards

def best_palindrome(min: int = 100, max: int = 999) -> tuple[int, int, int]: #sets parameters of min and max value, and sets hint type to return 3 integers

best_palindrome = 0
best_a = 0
best_b = 0

    for a in range(max, min -1, -1):
        if a * a < best_palindrome: #if the same number squared is a larger palindrome than an a * b number
            break

        for b in range(a, min -1, -1):
            product = a * b

            if product < best_palindrome:
             break
             if is_palindrome(product):
            best_palindrome = product
            best_a = a
            best_b = b
    return best_palindrome, best_a, best_b

palindrome, a, b = largest_palindrome_product()
print(f"Largest palindrome product: {palindrome}")
print(f"Factors: {a} x {b} = {palindrome}")

