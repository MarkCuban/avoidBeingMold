from typing import List

class Solution:

    def len_range(self, strs):
        for string in strs:
            yield len(string)


    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ''
        try:
            str_short = min(strs, key=lambda x:len(x))
            
            for i in range(0, len(str_short)):
                if i == 0:
                    str_sh = str_short[0:]
                else:
                    str_sh = str_short[0:-i]
            
                fail = False
                for str_other in strs:
#                    print(str_other.startswith(str_sh))
                    if str_other.startswith(str_sh) == False:
                        fail = True
                        break

                if fail == False:
                    ret = str_sh
                    break
        except:
            pass
        return ret

sol = Solution()

strs = ['flower', 'flow', 'flight']

print(sol.longestCommonPrefix(strs))