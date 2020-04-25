class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:return 0

        for i in range(0, len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1
        

sol = Solution()

haystack = ''
needle = ''

print(sol.strStr(haystack, needle))