from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        while k != 0:
            current = nums.pop()
            nums.insert(0, current)
            k -= 1
        return


sol = Solution()
print(sol.rotate([-1,-100,3,99], 2))