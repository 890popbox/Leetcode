def isPalindrome(x):
    # A negative is not a palindrome
    if x < 0:
        return False
    # We will have to reverse the number mathematically
    number = x
    rev = 0
    while number > 0:
        rev *= 10
        rev += number % 10
        number //= 10
    return x == rev
# Apparently you can also do this by only reversing half of the number.
