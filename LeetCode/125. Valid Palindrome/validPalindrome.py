from typing import List
class Solution: 
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        s_final = [i for i in s_lower if i.isalnum()]
        return s_final == s_final[::-1]


solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("race a car"))