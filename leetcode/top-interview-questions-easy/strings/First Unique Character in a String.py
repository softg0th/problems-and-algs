class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = {}

        for sign in s:
            if sign not in letters.keys():
                letters[sign] = 0
            else:
                letters[sign] += 1

        for letter in range(len(s)):
            if letters[s[letter]] == 0:
                return letter
        return -1

sol = Solution()
print(sol.firstUniqChar('aabb'))
