    def checkPerfectNumber(self, num):
        if num==1: return False
        sq = int(sqrt(num))
        s = 1
        for i in range(2, sq +1):
            if num%i==0:
                s+=i
                s+=num//i
        return s==num

# We only have to go up to the sq and add backwards as needed
