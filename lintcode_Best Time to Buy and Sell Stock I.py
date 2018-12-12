class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit(self, prices):
        # write your code here
        gain = 0
        for i in range (0, len(prices)-1):
            a = prices[i+1]-prices[i]
            if (a > 0):
                gain = gain + a

        return gain