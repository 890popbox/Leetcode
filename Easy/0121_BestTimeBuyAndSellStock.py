def maxProfit(self, prices):
    profit=0
    buy=prices[0]
    # Start off assuming there is no profit and scan future sell prices comparing them with current buy price
    for sell in prices[1:]:
        # if the sell price is greater than the buy price calculate the profit
        if sell > buy:
            profit = max(profit, sell-buy)
        # otherwise this means that day is lower than our current buy price, so update it
        else:
            buy = sell
    return profit
# this works because all profit compared to the original buy day have been accounted for
# any future profit will only improve buying at the lower price
