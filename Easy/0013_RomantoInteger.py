def romanToInt(s):
    # Dictionary mapping (roman numeral : value)
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    temp = 0
    # Add each roman numeral to the number, If the roman numeral that follows next is greater than the one we are on
    # subtract that by the bigger one.
    # For example, MCMXCIV. 1000 + (1000-100) + (100-10) + (5-1)
    for i in range(0, len(s) - 1):
        if roman_numerals[s[i]] < roman_numerals[s[i + 1]]:
            temp -= roman_numerals[s[i]]
        else:
            temp += roman_numerals[s[i]]
    # We also need a bounds check, we could do this each time in the loop or return the addition here.
    return temp + roman_numerals[s[-1]]
