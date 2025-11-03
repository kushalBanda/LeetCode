class Solution:
    def gcdOfStrings(self, str1, str2):
        # Helper to find GCD of two numbers manually
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        if str1 + str2 != str2 + str1:
            return ""

        length = gcd(len(str1), len(str2))
        return str1[:length]



# Test Cases
solutions = Solution()
print(solutions.gcdOfStrings("ABCABC", "ABC"))
# print(solutions.gcdOfStrings("ABABAB", "ABAB"))
# print(solutions.gcdOfStrings("LEET", "CODE"))