class Solution:
    def countNegatives(self, grid):
        result = 0
        #   temp = []

        for row in grid:
            if len(row) > 1:
                row = sorted(row)
                left = 0
                right = len(row)-1
            else:
                if row[0] < 0:
                    result += 1
                continue
            iterations = 0
            #   print(result)
            while left < right:
                if row[left] == row[right] and iterations == 0:
                    if row[right] < 0:
                        result += len(row)
                    break
                if row[left] < 0 and row[right] < 0 and iterations == 0:
                    result += len(row)
                    break
                iterations = 1
                #   print(left, right)
                if row[right] >= 0 and row[left] >= 0:
                    temp_row_left = left
                    temp_row_right = right
                    left += 1
                    right -= 1
                    if left == temp_row_right and right == temp_row_left:
                        break
                if row[left] < 0:
                    #   temp.append((row, row[left]))
                    result += 1
                    left += 1
                if row[right] < 0:
                    #   temp.append((row, row[right]))
                    right -= 1
                    result += 1

        return result


s = Solution()
print(s.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
