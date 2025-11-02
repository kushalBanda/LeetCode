from typing import List
class Solution:
    def findDisappearNumbers(self, nums: List[int]) -> List[int]:
        setNums = set(nums)
        return [i for i in range(1, len(nums) + 1) if i not in setNums]

# Test Cases
solution = Solution()
print(solution.findDisappearNumbers([4,3,2,7,8,2,3,1]))