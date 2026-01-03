class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        return str(x) == str(x)[::-1]


solution = Solution()
print(solution.isPalindrome(121))
