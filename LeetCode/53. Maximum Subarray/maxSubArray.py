from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum+num)
            max_sum = max(max_sum, current_sum)
        return max_sum

solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
# print(solution.maxSubArray([5,4,-1,7,8]))