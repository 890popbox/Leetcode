def missingNumber(self, nums: list[int]) -> int:
    ls = [0] * (len(nums)+1)
    for n in nums:
        ls[n]+=1
    for index, number, in enumerate(ls):
        if number==0:
            return index
    return 0

# Create a frequency list where the index represents the number, mark if we have seen it
# Scan that list and return the first index we have not seen
# Another intuitive method is to subtract what the sum of n numbers should be by the actual sum