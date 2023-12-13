def fillCups(self, amount):
    # return max(max(amount), (sum(amount) + 1) // 2), One liner using math
    seconds, total = 0, sum(amount)
    # A==largest, B==second_largest
    while total > 0:
        a, b = 0, 1
        # Replace with the biggest one
        if amount[2] > amount[a]:
            a = 2
        elif amount[2] > amount[b]:
            b = 2
        # Remove from one or more cups
        amount[a] -= 1
        amount[b] -= 1
        if amount[a] < 0 or amount[b] < 0:
            total -= 1
        else:
            total -= 2
        seconds += 1
    return seconds
