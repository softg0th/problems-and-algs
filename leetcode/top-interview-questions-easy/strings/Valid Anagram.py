class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s = sorted(s)
        t = sorted(t)

        for indx in range(len(s)):
            if s[indx] != t[indx]:
                return False
        return True


sol = Solution()
print(sol.isAnagram('ac', 'bb'))
