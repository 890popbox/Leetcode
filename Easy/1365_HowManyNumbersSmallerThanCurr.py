def smallerNumbersThanCurrent(nums):
    d = {}
    # Scan through the sorted numbers, using the index and number itself
    for index, number in enumerate(sorted(nums)):
        # If this number isn't in the map, add it to the map
        if number not in d:
            d[number] = index
    # Return a list using the numbers that map to a dictionary
    return [d[n] for n in nums]