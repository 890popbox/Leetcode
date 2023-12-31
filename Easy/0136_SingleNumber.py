def singleNumber(self, nums):
    # 10 10 01
    # 100 001 010 001 010
    number = 0
    for n in nums:
        number ^= n
    return number
# use the xor operator on all elements, this works because every number must appear twice besides one
