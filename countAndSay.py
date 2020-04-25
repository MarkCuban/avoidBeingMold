class Solution:

    def countString(self, string):
        n = 0
        tmp = 0
        ret = ''
        for ch in string:
            if tmp == 0:
                tmp = ch
            if ch == tmp:
                n += 1
            else:
                ret += str(n)
                ret += tmp
                tmp = ch
                n = 1

        ret += str(n)
        ret += tmp        

        return ret


    def countAndSay(self, n: int) -> str:
        ret = '1'
        print(ret)
        for i in range(0, n-1):
            ret = self.countString(ret)
            print(ret)

        return ret


        


sol = Solution()

n = 5
print(sol.countAndSay(n))