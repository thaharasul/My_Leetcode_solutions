class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique = sorted(set(nums))
        for i, v in enumerate(unique):
            nums[i] = v
        return len(unique) 