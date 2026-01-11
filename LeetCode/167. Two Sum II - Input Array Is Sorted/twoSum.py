from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output = []
        for j, i in enumerate(numbers):
            if (target - i) in numbers[j+1:]:
                output.append(j+1)
                output.append(numbers[j+1:].index(target - i) + j + 2)
                return output   

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))