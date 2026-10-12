class Solution:
    def canJump(self, nums: list[int]) -> bool:
            farthest = 0
            for i, num in enumerate(nums):
                if i > farthest:
                    return False
                farthest = max(farthest, i + num)
            return True