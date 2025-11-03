from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        maxItem = max(candies)
        for i in candies:
            if i + extraCandies >= maxItem:
                output.append(True)
            else:
                output.append(False)
        return output

# Test Cases
solutions = Solution()
print(solutions.kidsWithCandies([2,3,5,1,3], 3))