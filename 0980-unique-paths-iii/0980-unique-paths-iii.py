class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
            rows, cols = len(grid), len(grid[0])
            empty = 0
            start = end = None
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 0:
                        empty += 1
                    elif grid[r][c] == 1:
                        start = (r, c)
                    elif grid[r][c] == 2:
                        end = (r, c)

            def dfs(r, c, remaining, visited):
                if (r, c) == end:
                    return 1 if remaining == 0 else 0
                total = 0
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited
                            and grid[nr][nc] != -1):
                        visited.add((nr, nc))
                        total += dfs(nr, nc, remaining - 1, visited)
                        visited.remove((nr, nc))
                return total

            return dfs(start[0], start[1], empty + 1, {start})