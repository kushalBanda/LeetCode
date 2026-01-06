from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return s.reverse()

solution = Solution()
print(solution.reverseString(["h","e","l","l","o"]))