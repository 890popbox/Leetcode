def maxArea(self, height):
    # Sliding window solution to move in pointers closer, water==area
    left, right = 0, len(height) - 1
    water = 0
    # We only have to go until this condition, use lowest height, width is simple to find here
    while left < right:
        w, h = right - left, min(height[left], height[right])
        water = max(water, w * h)
        # Move forward or back keeping track of the larger wall
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return water
