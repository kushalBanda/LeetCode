# Solution 1: O(N^2)

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedNums = sorted(nums)

        for i, v in enumerate(sortedNums):
            if v + sortedNums[i+1] == target:
                return [i, i+1]

# Test Cases
solution = Solution()
print(solution.twoSum([2,7,11,15], 9))

# Solution 2: O(N)
class Solution2:
    def twoSum(self, nums: List[int], target: int):
        hashMap = {} #val, indx
        for indx, val in enumerate(nums):
            diff = target - val
            
            if diff in hashMap:
                return [hashMap[diff], indx]
            hashMap[val] = indx

# Test Cases
solution2 = Solution2()
print(solution2.twoSum([2,7,11,15], 9))