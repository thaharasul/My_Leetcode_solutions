class Solution:
    def partition(self, s: str) -> list[list[str]]:
        
            n = len(s)
            result = []
            for mask in range(1 << (n - 1)):
                cuts = [0] + [i + 1 for i in range(n - 1) if mask & (1 << i)] + [n]
                parts = [s[cuts[i]:cuts[i + 1]] for i in range(len(cuts) - 1)]
                if all(p == p[::-1] for p in parts):
                    result.append(parts)
            return result