class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        n = len(s)
        seen = set()
        repeated = set()
        for i in range(n - 9):
            sub = s[i:i + 10]
            if sub in seen:
                repeated.add(sub)
            seen.add(sub)
        return list(repeated)