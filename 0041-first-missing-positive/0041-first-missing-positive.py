class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
            nums = sorted(set(n for n in nums if n > 0))
            smallest = 1
            for num in nums:
                if num == smallest:
                    smallest += 1
                elif num > smallest:
                    break
            return smallest