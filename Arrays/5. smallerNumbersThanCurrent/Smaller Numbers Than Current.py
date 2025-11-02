from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums = sorted(nums)
        hashMap = {} # val, indx

        for i, num in enumerate(sortedNums):
            if num not in hashMap:
                hashMap[num] = i
        print(hashMap)

        return [hashMap[num] for num in nums]

# Test Cases
solution = Solution()
print(solution.smallerNumbersThanCurrent([8,1,2,2,3]))