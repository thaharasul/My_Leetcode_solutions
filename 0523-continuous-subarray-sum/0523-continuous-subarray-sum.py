class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = {0: -1}
        prefix = 0
        for i, num in enumerate(nums):
            prefix += num
            remainder = prefix % k
            if remainder in seen:
                if i - seen[remainder] > 1:
                    return True
            else:
                seen[remainder] = i
        return False
        