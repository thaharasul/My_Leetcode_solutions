class Solution:
    def isValid(self, s: str) -> bool:
            prev_len = -1
            while len(s) != prev_len:
                prev_len = len(s)
                s = s.replace('()', '').replace('[]', '').replace('{}', '')
            return s == ''