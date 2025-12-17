class Solution(object):
    def maximumProfit(self, prices, k):
        """
        :type prices: List[int]
        :type k: int
        :rtype: int
        """
        n = len(prices)
        x0 = prices[0]
        dp = [[0, -x0, x0] for _ in range(k + 1)]

        for i in range(1, n):
            x = prices[i]
            for t in range(k, 0, -1):
                profit, buy, sell = dp[t]
                prev_profit = dp[t - 1][0]

                dp[t][0] = max(profit, buy + x, sell - x)
                dp[t][1] = max(buy, prev_profit - x)
                dp[t][2] = max(sell, prev_profit + x)

        return dp[k][0]

        