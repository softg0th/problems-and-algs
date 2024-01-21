from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        longest = 0
        for char in range(len(strs[0])):
            if strs[0][char] == strs[-1][char]:
                longest += 1
            else:
                break
        return strs[0][:longest]


sol = Solution()
print(sol.longestCommonPrefix(["dog","racecar","car"]))