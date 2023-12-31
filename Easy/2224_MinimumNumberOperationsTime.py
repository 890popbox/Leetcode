def convertTime(current, correct):
    # Get the current and correct time in minutes
    currMinutes = (int(current[0:2]) * 60) + int(current[3:5])
    corrMinutes = (int(correct[0:2]) * 60) + int(correct[3:5])
    # Get the distance between those two times
    betweenMinutes = corrMinutes - currMinutes
    # Store a count variable and times greatest to count how many operations may be preformed
    count = 0
    times = [60, 15, 5, 1]
    # Go through each time and use it as an operation
    for time in times:
        # The amount of valid operations that can be preformed with this time given
        operations = betweenMinutes // time
        # If it is above zero, it is one or more valid operations, adjust the distance and increase count
        if operations > 0:
            betweenMinutes -= (time * operations)
            count += operations
        # Once the distance between them are gone, exit early if possible
        if betweenMinutes == 0:
            return count
    return count