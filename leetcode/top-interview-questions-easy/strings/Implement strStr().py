class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0

        haystackLen = len(haystack)
        needleLen = len(needle)

        if haystackLen < needleLen:
            return -1

        buf = []
        for i in range(0, len(haystack), needleLen):
            buf.append(haystack[i:i+needleLen])
            if i+needleLen+needleLen > haystackLen:
                break

        prev = 0
        for j in range(len(buf)):
            if buf[j] == needle:
                return j + prev * (needleLen - 1)
            prev += 1
        return -1

sol = Solution()
print(sol.strStr("mississippi", "issi"))