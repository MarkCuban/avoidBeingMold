class Solution:

    peidui = {
        '(' : ')',
        '[' : ']',
        '{' : '}',
    }

    stack = []
    stack_pointer = -1

    def push(self, ch):
        self.stack.append(ch)
        self.stack_pointer += 1
        return self.stack[self.stack_pointer]

    def pop(self):
        ch = self.stack[self.stack_pointer]
        self.stack.pop(self.stack_pointer)
        self.stack_pointer -= 1

        if self.stack_pointer < 0:
            return 0
        else:
            return self.stack[self.stack_pointer]

    def isEmpty(self):
        return True if len(self.stack) == 0 else False

    def isValid(self, s: str) -> bool:
        
        self.stack.clear()
        ele_stack_top = 0
        weichuli = []
        for ch in s:
#           print(dir(dict))
            if self.peidui.__contains__(ch):
                ele_stack_top = self.push(ch)
            else:
                if ele_stack_top != 0:
                    tmp = self.peidui[ele_stack_top]
                else:
                    tmp = 0

                if ch == tmp:
                    ele_stack_top = self.pop()
                else:
                    weichuli.append(ch)
        
        
        return True if self.isEmpty() and len(weichuli) == 0 else False    
        

sol = Solution()

string = '[((]))'

print(sol.isValid(string))



