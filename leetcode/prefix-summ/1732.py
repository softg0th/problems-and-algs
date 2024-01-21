from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        current = 0

        for point in gain:
            current += point
            if current >= highest:
                highest = current
        return highest

sol = Solution()
print(sol.largestAltitude([-4,-3,-2,-1,4,3,2]))

