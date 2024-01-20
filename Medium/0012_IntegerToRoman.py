def intToRoman(self, num):
    # Using a list to map values, index==0 being the ones place incrementing by 4 each step
    # 1,4,5,9 ==> 10, 40, 50, 90 ==> 100, 400, 500, 900 ==> 1000 being the final index
    roman_numerals = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    ans = []
    index = 0

    # Scan each digit of the number from the lowest tenth to largest
    # It is important that the list is reversed and not the roman numeral itself
    # 58 ==> [VIII, L] => Reverse this and return as the output
    while num > 0:
        digit = num % 10
        num /= 10

        # Two special cases
        if digit == 9:
            ans.append(roman_numerals[index + 3])
            digit -= 9
        elif digit == 4:
            ans.append(roman_numerals[index + 1])
            digit -= 4

        # 8 ==> VIII, 5 Must be added before the 3 one digits
        # 3 ==> III, These digits must be together when appended to the list
        if digit > 4:
            rmdr = roman_numerals[index + 2] + roman_numerals[index] * (digit - 5)
            ans.append(rmdr)
        elif digit:
            rmdr = roman_numerals[index] * digit
            ans.append(rmdr)

        # Move up some roman numerals to the next ones/tenths place
        index += 4

    # Reverse the list and return the answer as a string
    # 1994 ==> List is ['IV', 'XC', 'CM', 'M'] ==> MCMXCIV
    return ''.join(reversed(ans))


# This solution runs in O(N) time and space, with two passes; reversing a list of 4 items is very quick
# Solution is optimal when most digits are 1,4,5,9

'''
Optimal constant solution, O(1) time and O(N) space; A bit of setup but fast
ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
hrns = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
ths = ["", "M", "MM", "MMM"]

return ths[num / 1000] + hrns[(num % 1000) / 100] + tens[(num % 100) / 10] + ones[num % 10]
'''
