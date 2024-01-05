class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if str(x)[0] == '-':
            neg = True
        if x >= 2147483647 or x <= -2147483648:
            return 0
        ans = 0
        x = abs(x)
        while x > 0:
            temp = x % 10
            ans = ans * 10 + temp
            x = x // 10
        if neg:
            ans = 0-ans
        if ans >= 2147483647 or ans <= -2147483648:
            return 0
        return ans


sol = Solution()
print(sol.reverse(-2143847412))