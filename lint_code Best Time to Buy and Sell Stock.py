class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit(self, prices):
        # write your code here
        if (len(prices) <= 1):
            return 0

        res = 0
        mn = 10000000
        for i in range(0, len(prices)):
            mn = min(mn, prices[i])
            res = max(res, prices[i] - mn)

        return res

