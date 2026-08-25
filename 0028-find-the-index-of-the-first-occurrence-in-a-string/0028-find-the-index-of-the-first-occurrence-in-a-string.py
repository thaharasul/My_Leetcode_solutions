class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            c = 0
            while c < m and haystack[i + c] == needle[c]:
                c += 1
            if c == m:
                return i
        return -1