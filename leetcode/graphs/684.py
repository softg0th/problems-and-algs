from typing import List


class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u: 
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        print(u, v)
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        all_elements_set = set()
        edges_len = len(edges)

        for i in edges:
            all_elements_set.add(i[0])
            all_elements_set.add(i[1])

        ds = DisjointSet(len(all_elements_set))

        for i in edges:
            ds.union(i[0], i[1])

        for i in edges:
            current_component_count = 0
            for j in edges:
                if j != i:
                    if ds.find(i[0]) == ds.find(j[0]) == True:
                        current_component_count += 1
                        if current_component_count > 1:
                            return i


sol = Solution()
print(sol.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))