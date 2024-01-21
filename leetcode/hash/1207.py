from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occ = {}

        for num in arr:
            if str(num) not in occ:
                occ[str(num)] = 1
            else:
                occ[(str(num))] += 1

        all_occs = [x for x in occ.values()]
        prev_len = len(all_occs)
        fin_len = len(set(all_occs))

        return True if prev_len == fin_len else False


sol = Solution()
print(sol.uniqueOccurrences([1, 2]))
