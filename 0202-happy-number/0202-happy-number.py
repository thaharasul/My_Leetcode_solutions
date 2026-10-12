class Solution:
    def isHappy(self, n: int) -> bool:
            def next_val(x):
                return sum(int(d)**2 for d in str(x))
            slow, fast = n, next_val(n)
            while fast != 1 and slow != fast:
                slow = next_val(slow)
                fast = next_val(next_val(fast))
            return fast == 1