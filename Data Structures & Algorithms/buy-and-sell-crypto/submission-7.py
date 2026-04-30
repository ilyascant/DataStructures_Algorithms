class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        minBuy = prices[0]

        for price in prices:
            maxProf = max(maxProf, price-minBuy)
            minBuy = min(price, minBuy)

        return maxProf