class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
            remaining = set(range(numCourses))
            prereqs = {c: set() for c in range(numCourses)}
            for a, b in prerequisites:
                prereqs[a].add(b)
            changed = True
            while changed and remaining:
                changed = False
                for c in list(remaining):
                    if prereqs[c] & remaining == set():
                        remaining.remove(c)
                        changed = True
            return len(remaining) == 0