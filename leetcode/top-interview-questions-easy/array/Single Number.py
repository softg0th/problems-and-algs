from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dct = {}
        for num in nums:
            dct[f'{num}'] = 0
        for num in nums:
            dct[str(num)] += 1
        for k in dct:
            if dct[k] == 1:
                return int(k)

sol = Solution()
print(sol.singleNumber([4,1,2,1,2]))