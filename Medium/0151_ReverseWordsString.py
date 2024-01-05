def reverseWords(self, s):
    return ' '.join(reversed(s.split()))

# split puts all words in an array in linear time
# reverse also in linear time reverses the array by going from start until middle like a palindrome
# join creates a string from the list given, strings are not mutable so appending to one recreates the string
# recreating the string results in quadratic solution and is not optimal
# each of these steps can be written without builtin functions
