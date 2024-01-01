def coinChange(self, coins, amount):
    # If the amount is zero, we don't need any coins
    if amount == 0:
        return 0
    # Count how many coins we need to make the amount, returning once we found it at the lowest possible value
    stack = [0]
    level = 0
    visited = [False] * (amount + 1)
    visited[0] = True
    # This continue will finish once all possible positions have been visited and we have not returned change
    while stack:
        # level == how much coins we can return that make up amount
        level += 1
        change = stack
        stack = []
        # change will hold numbers from the stack that are numbers we can make up with existing coins
        for v in change:
            for coin in coins:
                newval = v + coin
                if newval == amount:
                    return level
                elif newval > amount:
                    continue
                # if we already visited this amount do not waste time appending it to the stack
                elif not visited[newval]:
                    visited[newval] = True
                    stack.append(newval)
    return -1
