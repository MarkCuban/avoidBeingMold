from typing import List
class Solution:

    letters = {
        '1': None,
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    def getNextPoint(self, digits, seq):
        
        try:
            for i in range(0, len(digits)):
                ch = digits[len(digits)-i-1]
                letter = self.letters[ch]
                if letter != None:
                    idx = seq[len(digits)-i-1]
                    idx += 1
                    if idx >= len(letter):
                        idx = 0
                        seq[len(digits)-i-1] = idx
                    else:
                        seq[len(digits)-i-1] = idx
                        break
        except:
            pass


        return seq
        
    def letterCombinations(self, digits: str) -> List[str]:
        ret = []
        seq = {}

        for x in range(0, len(digits)):
            seq[x] = 0

        while True:
            tmp = ''
            for i in range(0, len(digits)):
                letter = self.letters[digits[i]]
                if letter is not None:
                    tmp += letter[seq[i]]
            
            if len(tmp) > 0:
                ret.append(tmp)
            seq = self.getNextPoint(digits, seq)

            finish = True
            for key in seq.keys():
                if seq[key] != 0:
                    finish = False
            if finish == True:
                break
            
        return ret



sol = Solution()

target = "22"

print(sol.letterCombinations(target))


