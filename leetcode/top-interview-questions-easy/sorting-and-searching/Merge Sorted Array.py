from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = 0, 0

        while i > len(nums1) and j > len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] < nums2[j]:
                nums1.insert(i, nums2[j])
                i += 1
                j += 1