from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i = 0
        j = 0

        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        ans = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ans.append(nums1[i])
                i += 1
                j += 1
        return ans


sol = Solution()
print(sol.intersect([4,9,5], [9,4,9,8,4]))


'''
Расписать:
1. Сначала сортируем массивы, потому что проход будет поэтапным:

1 = [4, 5, 9]
2 = [4, 4, 8, 9, 9]

2. Сравниваем первые два поинтера:
Попадаем во второй кейс, заносим 4 в массив, сдвигаемся

3. Сравниваем 5 и 4, сдвиг вправо

4. Сравниваем 5 и 8, сдвиг влево

5. Сравниваем 9 и 8, сдвиг вправо

6. Сравниваем 9 и 9, заносим 1, брейк по длине массива

'''