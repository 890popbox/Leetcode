def myPow(self, x, n):
    # power of zero is 1, return helper to divide and conquer, eventually 1*x will be returned
    def helper(x, n):
        if x==0: return 0
        if n==0: return 1
        tmp = helper(x, n//2)
        tmp*=tmp
        if n%2==0:
            return tmp
        else:
            return tmp * x
    # use a helper function to get the positive answer, negative power is just 1/ans
    ans = helper(x, abs(n))
    if n<0:
        return 1/ans
    return ans

# Figuring out 2 to the power of 0,1,2,5 is all we need in order to solve 2^10
# goal here is to cut each sqt, rather than multiplying number by 2 ten times
# Divide ten in half until zero; 10, 5, 2, 1, 1. 2^0 == 1 and 2^1 == 2
# So 2^2 is two 2^1's or 4, and 4*4 is 2^4 so 2*4*4 = 32 or 2^5, this means 32*32==1024 or 2^10
