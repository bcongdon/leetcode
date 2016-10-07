class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        c_min, c_max = (2**32), -(2**32)
        profit = 0
        for idx, curr in enumerate(prices):
            if curr < c_min:
                c_min, c_max = curr, curr
            elif curr > c_max:
                c_max = curr
            profit = max(profit, c_max - c_min)
        return profit
