import math

class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        zeros = nums.count(0)

        if zeros > 1:
            return [0] * n

        product = math.prod(x for x in nums if x != 0)

        result = []
        for x in nums:
            if zeros == 1:
                result.append(product if x == 0 else 0)
            else:
                result.append(product // x)
        return result
