    def fizzBuzz(self, n):
        ans=[]
        for i in range(n):
            fizz = (i+1)%3==0
            buzz = (i+1)%5==0
            if fizz and buzz:
                ans.append("FizzBuzz")
            elif fizz:
                ans.append("Fizz")
            elif buzz:
                ans.append("Buzz")
            else:
                ans.append(str(i+1))
        return ans

# FizzBuzz, do the math once for each, you now only have to compare 1 and zero a few times, or it continues
