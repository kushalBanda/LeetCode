class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        s = list(s)

        for i in s:
            if i in ("(", "{", "["):
                stack.append(i)
            elif stack and ((i == ")" and stack[-1] == "(") or (i == "}" and stack[-1] == "{") or (i == "]" and stack[-1] == "[")):
                stack.pop()
            else:
                return False
        return not stack