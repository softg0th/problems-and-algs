class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        first = len(word1)
        second = len(word2)
        merge = []
        while i < first or j < second:
            if i >= first:
                merge.append(word2[j])
                j += 1
            elif j >= second:
                merge.append(word1[i])
                i += 1
            else:
                merge.append(word1[i])
                merge.append(word2[j])
                i += 1
                j += 1
        return ''.join(merge)


sol = Solution()
print(sol.mergeAlternately('abcd', 'pq'))


