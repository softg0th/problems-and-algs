from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        anc = 0
        for priceIndx in range(len(prices)-1):
            if prices[priceIndx] < prices[priceIndx+1]:
                anc += prices[priceIndx+1]-prices[priceIndx]
        return anc


sol = Solution()
print(sol.maxProfit([7,6,4,3,1]))