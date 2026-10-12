class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
            n = len(nums)
            result = set()
            for mask in range(1 << n):
                subset = tuple(sorted(nums[i] for i in range(n) if mask & (1 << i)))
                result.add(subset)
            return [list(t) for t in result]