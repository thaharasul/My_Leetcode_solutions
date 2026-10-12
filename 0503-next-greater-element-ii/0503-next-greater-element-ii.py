class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
            n = len(nums)
            result = [-1] * n
            for i in range(n):
                for k in range(1, n):
                    j = (i + k) % n
                    if nums[j] > nums[i]:
                        result[i] = nums[j]
                        break
            return result