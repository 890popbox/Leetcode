def addStrings(self, num1, num2):
    # Get the end of each string to be used later in simple addition math
    l, l2 = len(num1) - 1, len(num2) - 1
    x, carry = 0, 0
    answer = ""

    while l >= 0 or l2 >= 0 or carry > 0:
        digit1 = int(num1[l]) if l >= 0 else 0
        digit2 = int(num2[l2]) if l2 >= 0 else 0
        x = digit1 + digit2 + carry
        carry = x // 10
        x = x % 10

        answer = str(x) + answer
        if l >= 0:
            l -= 1
        if l2 >= 0:
            l2 -= 1

    return answer
