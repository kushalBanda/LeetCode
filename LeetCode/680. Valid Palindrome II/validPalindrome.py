class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s: str) -> bool:
            return s == s[::-1]
        
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return isPalindrome(s[left + 1:right + 1]) or isPalindrome(s[left:right])
            left += 1
            right -= 1
        return True

solution = Solution()