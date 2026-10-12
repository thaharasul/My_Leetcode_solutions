class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
            from collections import Counter
            counts = Counter(nums)
            ordered = sorted(counts.items(), key=lambda x: -x[1])
            return [num for num, _ in ordered[:k]]