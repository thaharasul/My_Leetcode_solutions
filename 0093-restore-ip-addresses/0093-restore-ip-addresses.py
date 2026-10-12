class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
            n = len(s)
            result = []
            for i in range(1, min(4, n)):
                for j in range(i + 1, min(i + 4, n)):
                    for k in range(j + 1, min(j + 4, n)):
                        parts = [s[:i], s[i:j], s[j:k], s[k:]]
                        if all(0 < len(p) <= 3 and (p == '0' or p[0] != '0') and int(p) <= 255 for p in parts):
                            result.append('.'.join(parts))
            return result