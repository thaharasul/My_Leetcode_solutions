class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        or_all = 0
        for num in nums:
            or_all |= num
        return or_all * (1 << (len(nums) - 1))