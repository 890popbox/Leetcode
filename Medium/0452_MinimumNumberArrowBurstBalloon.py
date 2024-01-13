def findMinArrowShots(self, points):
    # sort by the ranges end, because the dart we throw will hit targets until the next start>end
    points.sort(key=lambda x: x[1])
    arrows = 0
    end = float('-inf')
    for p in points:
        # update end with the new intervals end when start>end
        if p[0] > end:
            arrows += 1
            end = p[1]
    return arrows
