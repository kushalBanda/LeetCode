class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = [] 
        for p in path.split("/"):
            if p == "..":
                if stack:
                    stack.pop()
            elif p and p != ".":
                stack.append(p)
        return "/" + "/".join(stack)
            


solution = Solution()
# print(solution.simplifyPath("/home//"))
print(solution.simplifyPath("/home/user/Documents/../Pictures"))