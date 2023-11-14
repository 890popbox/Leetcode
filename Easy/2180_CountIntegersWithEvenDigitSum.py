def countEven(num):
    count = 0
    for i in range(2, num + 1):
        # Count the sum of the number for example, (2 + 3 + 5)
        if sum([int(digit) for digit in str(i)]) % 2 == 0:
            count += 1
    return count
