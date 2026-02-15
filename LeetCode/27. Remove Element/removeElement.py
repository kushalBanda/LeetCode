from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_nums = []
        for i in nums:
            if i != val: 
                new_nums.append(i)
        nums[:] = new_nums
        return len(nums)
