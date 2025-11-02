# Problem: Check list for one missing number in range [0,n]


# Solution 1: O(N): Iterate through list and check if index is equal to value
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        for i,v in enumerate(sortedNums):
            if (i != v):
                return v - 1

            if v == len(nums) - 1:
                return v+1

# Test Cases
solution = Solution()
print(solution.missingNumber([0,1,2,3,4,5,6,7,9,10]))

# Solution 2: O(N): Iterate through list and sum (twice: once for given list and once for expected using range)
class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)
# Test Cases
solution2 = Solution2()
print(solution2.missingNumber([0,1,2,3,4,5,6,7,9,10]))





# Notes:
# - Len = O(1)
# - Range object creation = O(1)
# Sum = O(N)
# +1 in range(n) because n will be excluded otherwise
