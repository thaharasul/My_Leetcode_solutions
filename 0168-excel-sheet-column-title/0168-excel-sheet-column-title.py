class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
            result = []
            while columnNumber > 0:
                columnNumber, rem = divmod(columnNumber - 1, 26)
                result.append(chr(65 + rem))
            return ''.join(reversed(result))