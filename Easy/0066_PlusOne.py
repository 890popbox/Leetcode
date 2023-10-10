def plusOne(digits):
    # Let's check each digit backwards, so the end of array to start
    for i in range(len(digits) - 1, -1, -1):
        # If the digit is a 9, change it to zero and this carries the one over
        if digits[i] == 9:
            digits[i] = 0
        # This digit is not equal to 9, therefore we add a one and return the array
        else:
            digits[i] += 1
            return digits
    # If we went through all of that without returning the array everything was a 9
    # Therefore we must add 1 to the front of digits
    return [1] + digits
