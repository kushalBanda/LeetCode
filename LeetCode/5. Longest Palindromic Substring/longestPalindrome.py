class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s: str) -> bool:
            if s == s[::-1]:
                return True
            return False
        
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return isPalindrome(s[left + 1:right + 1]) or isPalindrome(s[left:right])
            left += 1
            right -= 1
        return True
        return isPalindrome(s)  