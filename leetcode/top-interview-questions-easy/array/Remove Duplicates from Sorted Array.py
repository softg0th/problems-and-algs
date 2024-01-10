from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                continue
            nums[count] = nums[i]
            count += 1
        nums = nums[:count]
        return count


sol = Solution()
print(sol.removeDuplicates([1,1]))
