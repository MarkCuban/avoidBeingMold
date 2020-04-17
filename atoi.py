class Solution:
    def myAtoi(self, str: str) -> int:
        
        str = str.strip()
        target = ''
        valid = False
        ret = 0
        
        for ch in str:
            if ch is '-' or ch is '+':
                if valid == True:
                    valid = False
                else:
                    valid = True
            elif (ch >= '0' and ch <= '9'):
                valid = True
            else:
                valid = False
            
            if valid:
                target += ch
            else:
                break
                
        print('target is ', target)
        if len(target) == 0:
            return 0
        else:
            neg = False
            for idx in range(0, len(target)):
#                print('idx', idx)
                if target[idx] == '-':
                    neg = True
                elif target[idx] == '+':
                    neg = False
                else:
#                    print('s', 10**(len(target)-idx-1))
                    ret += int(target[idx])* (10**(len(target)-idx-1))
                    
        if neg:
            ret = -ret
            
        if ret > 2**31-1:
            ret = 2**31-1
        elif ret < -2**31:
            ret = -2**31
            
        return ret
                