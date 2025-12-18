class Solution(object):
    def maxProfit(self, prices, strategy, k):
        """
        :type prices: List[int]
        :type strategy: List[int]
        :type k: int
        :rtype: int
        """
        n = len(prices)
        a = [strategy[i]*prices[i] for i in range(n)]
        b = sum(a)
        
        # Prefix sum for prices
        p_prices = [0]
        for x in prices:
            p_prices.append(p_prices[-1] + x)
        
        # Prefix sum for strategy*prices
        p = [0]
        for x in a:
            p.append(p[-1] + x)
        
        g = 0
        for i in range(n - k + 1):
            d = -(p[i+k] - p[i]) + (p_prices[i+k] - p_prices[i+k//2])
            if d > g:
                g = d
        
        return b + g