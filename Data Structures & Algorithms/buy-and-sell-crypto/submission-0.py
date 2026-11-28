class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxes = [0]*(n+1)
        for i in range(n, 0, -1):
            maxes[i-1] = max(prices[i-1], maxes[i])
        return max(0, max([maxes[i] - prices[i] for i in range(n)]))