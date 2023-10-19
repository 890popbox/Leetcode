# Function to give minimum amount of coins
def minCoin(cents, coins):
    # Change list, and init
    change = [float('inf') for x in range(cents + 1)]
    change[0] = 0
    coins.sort()  # Make sure the coins are in ascending order
    # Go through each coin in ascending order O(N * C)
    # N is coins that give change, C will be the cents
    for coin in coins:
        for amount in range(0, len(change)):
            # If the coin we are on is less than the amount, update it
            if coin <= amount:
                change[amount] = min(change[amount], 1+change[amount-coin])
    return change[cents] if change[cents] != float('inf') else -1

# USD currency coins
USCOINS = [25, 10, 5, 1]
# Test the algorithm
print(minCoin(22, USCOINS))
print(minCoin(11, USCOINS))
print(minCoin(57, USCOINS))
