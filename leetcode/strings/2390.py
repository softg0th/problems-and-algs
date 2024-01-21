class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for character in s:
            if character != '*':
                stack.append(character)
            else:
                stack.pop()
        return ''.join(stack)


sol = Solution()
print(sol.removeStars('erase*****'))