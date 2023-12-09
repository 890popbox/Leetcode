def distributeCandies(self, candies, num_people):
    # Create a list with the number of people, start each of their candies at zero
    output = [0] * num_people
    i, d = 0, 0
    # While we still have candies to give out
    while candies > 0:
        d += 1
        # If the distrib is more than the candies remaining, add the rest of them and return the output early
        if d > candies:
            output[i] += candies
            return output
        # Share the distrib of candies to the current person index, remove candy from total and increase index by one
        output[i] += d
        candies -= d
        i += 1
        # Once the index is out of bounds, put it back in bounds
        if i >= num_people:
            i -= num_people
    return output
# We could also use the modulus operator and one variable instead of two, both would be constant memory
