from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(x) for x in digits]
        digits = ''.join(digits)
        digits = int(digits)
        ans = digits + 1
        ans = list(str(ans))
        ans = [int(x) for x in ans]
        return ans



sol = Solution()
print(sol.plusOne([9]))