from typing import List


class Solution:
    def countNegatives(self, grid):
        result = 0
        for row in grid:
            row = sorted(row)
            mid = len(row) // 2
            low = 0
            high = len(row) - 1
            iterations = 0
            while row[mid] != 0 and low <= high:
                smol = 0
                if row[high] < 0 and iterations == 0:
                    smol += len(row[::high])
                    result += smol
                    break
                iterations = 1
                if 0 > row[mid]:
                    low = mid - 1
                    smol += 1
                else:
                    high = mid - 1
                mid = (low + high) // 2
                if low > high:
                    pass
                else:
                    result += smol
        return result

s = Solution()
print(s.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
