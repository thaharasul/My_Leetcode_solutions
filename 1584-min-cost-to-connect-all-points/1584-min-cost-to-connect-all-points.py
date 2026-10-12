class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
            n = len(points)
            visited = [False] * n
            heap = [(0, 0)]
            total = 0
            edges_used = 0
            while heap and edges_used < n:
                cost, node = heapq.heappop(heap)
                if visited[node]: continue
                visited[node] = True
                total += cost
                edges_used += 1
                for nxt in range(n):
                    if not visited[nxt]:
                        d = abs(points[node][0]-points[nxt][0]) + abs(points[node][1]-points[nxt][1])
                        heapq.heappush(heap, (d, nxt))
            return total