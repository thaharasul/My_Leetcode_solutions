class Solution:
    def expArdCen(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            odd = self.expArdCen(s, i, i)
            even = self.expArdCen(s, i, i + 1)
            current_longest = odd if len(odd) > len(even) else even
            if len(current_longest) > len(longest):
                longest = current_longest
        return longest