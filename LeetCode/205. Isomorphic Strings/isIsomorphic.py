class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)

        s_to_t = {}
        t_to_s = {}

        for idx, i in enumerate(s):
            if i not in s_to_t:
                if t[idx] in t_to_s:
                    return False
                s_to_t[i] = t[idx]
                t_to_s[t[idx]] = i
            else:
                if s_to_t[i] != t[idx]:
                    return False

        return True
    
solution = Solution()
print(solution.isIsomorphic("bbbaaaba", "aaabbbba"))