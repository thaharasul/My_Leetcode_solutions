class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime = bytearray(b'\x01') * n
        is_prime[0] = is_prime[1] = 0

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                is_prime[i * i:n:i] = b'\x00' * (((n - 1 - i * i) // i) + 1)

        return sum(is_prime)