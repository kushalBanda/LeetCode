from typing import List

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        if len(s) > len(t):
            return False
        elif len(s) == len(t):
            return s == t
        for i in s:
            if i in t:
                t = t[t.index(i)+1:]
            else:
                return False
        return True

solution = Solution()

print(solution.isSubsequence("aaaaaa", "bbaaaa"))