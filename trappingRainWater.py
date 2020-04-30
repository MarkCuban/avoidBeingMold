from typing import List

class Solution:

    def calculateWater(self, stack, sp):
        water = 0

        if stack[0] <= stack[sp]:
            bar = stack[0]

            for i in stack[1:-1]:
                water += bar-i
            bottom = 0
        else:
            bar = stack[sp]

            for i in stack[1:-1]:
                if bar > i:
                    water += bar-i
                    stack[stack.index(i)] = bar

            bottom = bar

        return water, bottom

    def trap(self, height: List[int]) -> int:
        st = []
        sp = -1
        i = 0
        water = 0
        bottom = 0
        while i < len(height):
            if sp >= 0:
                if height[i] <= st[sp]:
                    st.append(height[i])
                    sp += 1    
                    bottom = height[i]                 
                    i += 1
                else:
                    st.append(height[i])
                    sp += 1 
                    tmp, bottom = self.calculateWater(st, sp)
                    water += tmp

                    if bottom == 0:
                        st = []
                        sp = -1
                    else:
                        i += 1

            else:
                if height[i] > 0:
                    st.append(height[i])
                    sp += 1
                
                i += 1

        return water


sol = Solution()

bars = [4, 0, 3, 2, 5, 8 ,7, 0, 2, 5]
print(sol.trap(bars))