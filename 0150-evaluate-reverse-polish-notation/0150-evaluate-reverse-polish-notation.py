class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
            tokens = tokens[:]
            ops = {'+', '-', '*', '/'}
            while len(tokens) > 1:
                for i, t in enumerate(tokens):
                    if t in ops:
                        a, b = int(tokens[i - 2]), int(tokens[i - 1])
                        if t == '+': res = a + b
                        elif t == '-': res = a - b
                        elif t == '*': res = a * b
                        else: res = int(a / b)
                        tokens[i - 2:i + 1] = [str(res)]
                        break
            return int(tokens[0])