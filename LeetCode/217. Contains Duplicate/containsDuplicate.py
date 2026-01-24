from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for num in nums:
            if num in hashMap:
                return True
            else:
                hashMap[num] = num
                print(hashMap)
        return False

solution = Solution()
print(solution.containsDuplicate([1,2,3,1]))