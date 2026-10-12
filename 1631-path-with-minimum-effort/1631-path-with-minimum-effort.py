class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
            rows, cols = len(heights), len(heights[0])
            effort = [[float('inf')]*cols for _ in range(rows)]
            effort[0][0] = 0
            heap = [(0, 0, 0)]
            while heap:
                e, r, c = heapq.heappop(heap)
                if (r, c) == (rows-1, cols-1): return e
                if e > effort[r][c]: continue
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<rows and 0<=nc<cols:
                        new_e = max(e, abs(heights[nr][nc]-heights[r][c]))
                        if new_e < effort[nr][nc]:
                            effort[nr][nc] = new_e
                            heapq.heappush(heap, (new_e, nr, nc))