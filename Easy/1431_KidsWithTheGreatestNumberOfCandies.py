def kidsWithCandies(self, candies, extraCandies):
    greatest = max(candies)
    return [(c+extraCandies >= greatest) for c in candies]
# Store the greatest number of candies in the array, then create a list of True and False
# If that person + extraCandies is equal or greater than the current greatest, True is returned otherwise False
