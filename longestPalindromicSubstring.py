class Solution:
    
    def isPalidrome(self, s: str) -> bool:
        for i in range(0, len(s)//2):
            ch = s[i]
            ch2 = s[0-i-1]
#            print('ch, ch2', ch, ch2)
            if ch != ch2:
                return False
        return True
    
    def longestPalindrome(self, s: str) -> str:
        ret = ''
        
        start = 0
        while start < len(s):
            subs = ''
            root = 0
#            print('start is', start, len(s))
            if len(s) <= 1:
                extend_range = 1
            else:
                extend_range = min(start+1, len(s)-start-1)
#            print('extend_range is ', extend_range)
            for extend in range(0, extend_range+1):
#                print('extend is', extend)
                
                try:
                    while (s[start] == s[start+root+1]):
                        root += 1
                        if len(s) == start+root+1:
                            break

#                    print('root is', root)
                    subs = s[start-extend:start+1+extend+root]
                except:
                    subs = s[start-extend:start+1+extend]
                    
#                print('subs is ', subs)
                
                if len(ret) < len(subs) or len(ret) == 0:
                    if self.isPalidrome(subs) is False:
                        break
                    else:
                        ret = subs
            start = start+1+root
        return ret