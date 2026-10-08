class Solution:
    def frequencySort(self, s: str) -> str:
            count = Counter(s)
            chars = sorted(count.keys(), key=lambda c: -count[c])
            return "".join(c * count[c] for c in chars)