from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for r in range(len(matrix)):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        r
            



sol = Solution()
sol.rotate([[1,2,3],[4,5,6],[7,8,9]])
#   [[7,4,1],[8,5,2],[9,6,3]]