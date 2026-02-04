from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))
        output = 1
        max_output = 1

        for j in range(len(nums) - 1):
            if nums[j] + 1 == nums[j + 1]:
                output += 1
            else:
                output = 1
            max_output = max(max_output, output)

        return max_output


solution = Solution()
print(solution.longestConsecutive([1,2,6,7,8]))