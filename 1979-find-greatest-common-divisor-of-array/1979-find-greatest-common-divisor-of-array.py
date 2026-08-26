class Solution:
    def findGCD(self, nums: List[int]) -> int:
       mx, mn = max(nums), min(nums)
       for i in range(mn, 0, -1):
        if mx % i == 0 and mn % i == 0:
            return i       