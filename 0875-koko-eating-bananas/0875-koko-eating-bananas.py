import math
 
class Solution(object):
    def minEatingSpeed(self, piles, h):
        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            hours = sum(math.ceil(p / mid) for p in piles)
            if hours <= h:
                high = mid
            else:
                low = mid + 1
        return low