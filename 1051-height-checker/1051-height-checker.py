class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        def quick_sort(nums):
            if len(nums) <= 1:
                return nums
            pivot = nums[-1]
            left = [x for x in nums[:-1] if x <= pivot]
            right = [x for x in nums[:-1] if x > pivot]
            return quick_sort(left) + [pivot] + quick_sort(right)
        a= quick_sort(heights)
        c=0
        for n in range(len(a)):
            if a[n]!=heights[n]:
                c+=1
        return c

        