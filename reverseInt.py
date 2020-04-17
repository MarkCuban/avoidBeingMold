class Solution:
    def reverse(self, x: int) -> int:
        
        if x > pow(2, 31)-1 or x < -pow(2, 31):
            return 0
        
        if x >= 0:
            ret = int(str(x)[::-1])
        else:
            ret = int(str(-x)[::-1])
            ret = -ret
            
        if ret > pow(2, 31)-1 or ret < -pow(2, 31):
            return 0
        
        return ret