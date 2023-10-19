def minCoin(cents):
    # Can't give change if not positive
    if cents < 1:
        return 0
    # USD currency
    coins = [25, 10, 5, 1]
    minCoins = cents
    tmpCents = cents
    num_of_coins = 0
    for coin in coins:
        num_of_coins += tmpCents // coin
        tmpCents = tmpCents % coin
        if tmpCents == 0:
            if num_of_coins < minCoins:
                minCoins = num_of_coins
            num_of_coins = 0
            tmpCents = cents
    return minCoins

print(minCoin(22))
print(minCoin(11))
print(minCoin(57))