class Solution:
    def myAtoi(self, s: str) -> int:
        acceptable = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', ' ', '+'}
        stack = []

        for indx in range(len(s)):
            if s[indx] not in acceptable:
                break
            if s[indx] in acceptable:
                if stack and stack[-1] == '-' and s[indx] == '+' or stack and stack[-1] == '+' and s[indx] == '-':
                    print(s[indx])
                    break
                if not stack and s[indx] == ' ':
                    continue
                if stack and s[indx] in (' ', '+', '-'):
                    break

                else:
                    stack.append(s[indx])

        if stack:
            if len(stack) == 1 and stack[-1] in ('+', '-'):
                stack.pop()
                return 0
            ans = int(''.join(stack))
            if ans >= 2147483647:
                return 2147483647
            elif ans <= -2147483648:
                return -2147483648
            return ans
        return 0


sol = Solution()
print(sol.myAtoi("00000-42a1234"))
