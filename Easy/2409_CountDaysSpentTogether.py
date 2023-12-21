def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
    # Days in each month list == [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Create a list of how many days are between each month by using the days in the month list
    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(0, len(months) - 1):
        months[i + 1] += months[i]

    # Get the latest time someone arrived in rome, and the earliest time they left using max/min
    # String evalutes this fine using min and max
    # Function that calculates how many days are in the given day
    def calcDays(date):
        return months[int(date[:2]) - 1] + int(date[3:])

    return max(0, calcDays(min(leaveAlice, leaveBob)) - calcDays(max(arriveAlice, arriveBob)) + 1)
