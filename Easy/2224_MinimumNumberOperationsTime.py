def convertTime(self, current, correct):
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
        # If the between time is greater than or equal we may use it
        while betweenMinutes >= time:
            tmp = betweenMinutes - time
            # If tmp is greater than or equal to zero, we may consider this an operation
            # We can not change betweenMinutes if tmp becomes negative
            if tmp >= 0:
                count += 1
                betweenMinutes = tmp
    return count