# Problem: check list for dulplicates
# Solutions Time and Space: O(n): Iterate through list and create set, Space = size of set


'''
if len(set(nums)) == len(nums):
    return False
else:
    return True
'''

# Notes
# - Sets are fast, Note that empty Set cannot be created through {}, it creates dictionary, unless you include values.
# - set is implemeneted as a hash table, so lookup, insert, delete are all O(1) on average.

# Code
from typing import List
class Solution: 
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums): 
            return False
        else: 
            return True

# Test Cases
solution = Solution()
print(solution.containsDuplicate([1,2,1,3,4,5,6,7,8,9,10]))