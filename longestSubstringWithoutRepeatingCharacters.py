class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret = 0
        
        for start in range(0, len(s)):

            subs = s[start]
            for end in range(start+1, len(s)):
                if s[end] not in subs:
                    subs += s[end]
                else:
                    break
            if ret < len(subs):
                ret = len(subs)
                
        return ret
            