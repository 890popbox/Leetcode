def maxProfit(self, prices):
    profit=0
    buy=prices[0]
    # start off assuming there is no profit and scan future sell prices comparing them with current buy price
    for sell in prices[1:]:
        # if selling on this day generates a higher profit, save that profit
        if sell-buy > profit:
            profit = sell-buy
        # otherwise if our sell price is less than the price we have been buying for
        elif sell < buy:
            buy = sell
    return profit
# this works because all profit compared to the original buy day have been accounted for
# any future profit will only improve buying at the lower price
