from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_nums = []
        for i in nums:
            if i not in new_nums:
                new_nums.append(i)
        nums[:] = new_nums
        return len(nums)