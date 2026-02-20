class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t) 
        
        for value in s:
            if value in t:
                t.remove(value)
            else:
                return False
        if len(t) == 0:
            return True 
        else:
            return False

solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))