class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mini = prices[0]

        res = 0

        for i in range(1, len(prices)):
            mini = min(mini, prices[i])

            res = max(res, prices[i] - mini)
        return res

           