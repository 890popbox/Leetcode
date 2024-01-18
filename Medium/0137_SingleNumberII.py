def singleNumber(self, nums):
    # 10 10 11 10
    # Keep track of if the number appeared once or twice
    ones = 0
    twos = 0

    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones

    return ones

# Quick rundown of how this works, eventually everything will fall into the two or more category
# one,two == 0,0.. update=> 2, 0
# one,two == 2,0.. update=> 0, 2
# one,two == 0,2.. update=> 3, 2
# one,two == 3,2.. update=> 3, 2
# In the last check, (3^2) & !2 ==> 1 & !2 ==> 0001 & 1101
# And will keep each area where both bits are the same, so 0011 and the ones still holds 3
