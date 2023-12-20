def xorOperation(self, n, start):
    output = 0
    for i in range(start,start+(2*n),2):
        output = output ^ i
    return output
# Create a val to return, instead of storing an array of nums where nums[i] = start + 2 * i
# Run a loop that deals with each of these numbers, this allows you to deal with each value in place without storing them
# Use the logical XOR operator on each number and return the output
