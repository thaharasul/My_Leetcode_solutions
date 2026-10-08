class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
            lo, hi = 1, max(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                total = sum(-(-num // mid) for num in nums)
                if total <= threshold:
                    hi = mid
                else:
                    lo = mid + 1
            return lo