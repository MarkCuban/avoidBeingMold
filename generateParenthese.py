from typing import List

class Solution:

    stack = []
    sp = -1
    num = 0

    def push(self, ele):
        self.num += 1
        self.sp += 1
        self.stack.append(ele)
        return ele

    def pop(self):
        
        self.stack.pop(self.sp)
        self.sp -= 1
        if self.sp > 0:
            return self.stack[self.sp]
        else:
            return None

    def isProper(self, string, n):
        method = ['1', '0']
        ret = True

        self.stack = []
        self.sp = -1
        self.num = 0
        for ch in string:
            if ch is method[0]:
                self.push(ch)
            else:
                if self.sp >= 0:
                    self.pop()
                else:
                    ret = False
                    break
        
        if ret == True and self.sp == -1 and self.num == n:
            pass
        else:
            ret = False

        return ret
    
    def generateParenthesis(self, n: int) -> List[str]:
        
        ret = []
        i = 0
        
        for i in range(0x01 << n*2-1, (0x01<<n*2)):

            if i & 0x01 | 0x00 == 0x01:
                continue

            tmp = '{:b}'.format(i)
            if self.isProper(tmp, n):
                tmp = tmp.replace('1', '(')
                tmp = tmp.replace('0', ')')
                ret.append(tmp)
        return ret


sol = Solution()
n = 3
print(sol.generateParenthesis(n))