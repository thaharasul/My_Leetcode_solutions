class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(start, current):
            result.append(current[:])          # save current state

            for i in range(start, len(nums)):
                current.append(nums[i])         # add
                backtrack(i + 1, current)        # recurse
                current.pop()                    # remove

        backtrack(0, [])
        return result