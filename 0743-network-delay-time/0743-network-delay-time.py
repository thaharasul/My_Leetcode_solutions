class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
            dist = {i: float('inf') for i in range(1, n + 1)}
            dist[k] = 0
            for _ in range(n - 1):
                for u, v, w in times:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
            result = max(dist.values())
            return result if result < float('inf') else -1