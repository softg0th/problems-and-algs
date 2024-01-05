from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        return True

sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))