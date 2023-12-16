def accountBalanceAfterPurchase(self, purchaseAmount):
        x = (purchaseAmount+5)//10
        return 100 - x*10
# A number rounds up by the tenth if the ones place is 5 or greater, let's just add 5 to begin with
# That number multipled by 10 is the purchaseAmount rounded up excluding the remainder
