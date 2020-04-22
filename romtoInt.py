class Solution:

    def romanToInt(self, s: str) -> int:
        symbols = {
            'I':(1, None),
            'V':(5, 'I'),
            'X':(10, 'I'),
            'L':(50, 'X'),
            'C':(100, 'X'),
            'D':(500, 'C'),
            'M':(1000, 'C'),
        }    

        ret = 0
        canzhao = None

        for i in range(0, len(s)):
            ch = s[len(s)-i-1]
            if canzhao is not None:
                if ch == canzhao:
                    ret -= symbols[canzhao][0]
                    canzhao = None
                else:
                    ret += symbols[ch][0]
                    canzhao = symbols[ch][1]
            else:
                ret += symbols[ch][0]
                canzhao = symbols[ch][1]

        return ret

s = "MCMXCVI"

sol = Solution()

print(sol.romanToInt(s))