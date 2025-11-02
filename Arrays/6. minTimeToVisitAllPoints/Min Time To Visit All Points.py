# Proble: From a list of points, calculate the min distance between first and last point (x1, y1)
# Solution: If the next node is 10x and -5y away, it's going to take exactly 10 steps, because you can only move 1x at a time and difference between in y is 
# made up by diagonal moves during the process of overcoming the difference in x. Time: O(N), Space: O(1)

from typing import List
class Solution: 
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        x1, y1 = points.pop()
        print(x1, y1)

        while points: 
            x2, y2 = points.pop()
            time += max(abs(x2 - x1), abs(y2 - y1))
            x1, y1 = x2, y2

        return time

# Test Cases
solution = Solution()
print(solution.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))