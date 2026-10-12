class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
       
        from itertools import combinations
        return [list(c) for c in combinations(range(1, n + 1), k)]