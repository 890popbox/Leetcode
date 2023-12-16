def findPeaks(self, mountain):
    return [i for i in range(1, len(mountain)-1) if (mountain[i-1] < mountain[i] > mountain[i+1])]
# There is no need to record the first or last item of the array, so scan through every item besides those
# There will always be an item before and after to compare to, if the current is the greatest out of both record it
