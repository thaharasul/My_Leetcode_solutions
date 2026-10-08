class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        result = [x for x in nums if x != 0]
        result += [0] * (len(nums) - len(result))
        for i in range(len(nums)):
            nums[i] = result[i]