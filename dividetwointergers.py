class Solution:

    def getSub(self, div, divs):
        ret = 0
        while True:
            if div-divs >= 0:
                div = div-divs
                ret += 1
            else:
                break
        return ret, div
        

    def divide(self, dividend: int, divisor: int) -> int:
        ret = ''
        flag = False
        if (divisor < 0 and dividend > 0) or (divisor > 0 and dividend < 0):
            flag = True

        dividend = abs(dividend)
        divisor = abs(divisor)
        len_divisor = len(str(divisor))
        str_dividend = str(dividend)
        str_tmp = str_dividend[0:len_divisor]

        if int(str_tmp) < divisor:
            len_divisor += 1
            str_tmp = str_dividend[0:len_divisor]

        i = 0
        while True:
            div, mod = self.getSub(int(str_tmp), divisor)
            ret += str(div)
            if len_divisor+i < len(str_dividend):
                str_tmp = str(mod)+(str_dividend[len_divisor+i:len_divisor+i+1])
            else:
                break
            
            i += 1


        if flag:
            ret = -int(ret)
        else:
            ret = int(ret)

        return ret


sol = Solution()

dividend = 10
divisor = 3

print(sol.divide(dividend, divisor))