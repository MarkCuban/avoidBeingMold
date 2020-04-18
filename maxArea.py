from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
#        max_area = 0
#        for i in range(0, len(height)):
#            for j in range(i+1, len(height)):
#                area = min(height[i], height[j])*(j-i)
#                if max_area < area:
#                    max_area = area
        max_i = 0
        max_j = len(height)-1

        i = 0
        j = 0
        direction = True
        max_area = 0

        while max_i+i < max_j-j:

            area = min(height[max_i+i], height[max_j-j])*(max_j-j-max_i-i)

            if max_area < area:
                max_area = area

            if direction == True:
                if height[max_i+i] >= height[max_j-j]:
                    max_i = max_i+i
                    i = 0
                    j += 1
                    direction = 1-direction
                else:
                    i += 1
            else:
                if height[max_j-j] >= height[max_i+i]:
                    max_j = max_j-j
                    j = 0
                    i += 1
                    direction = 1-direction
                else:
                    j += 1

        return max_area

'''
        i = 1
        j = 1
        turn = True
        flag = False
        max_i = 0
        max_j = len(height)-1

        while max_i + i < max_j - j:

            a = max_j - max_i
            b = min(height[max_i], height[max_j])

            if turn == True:
                n = min(height[max_i+i], height[max_j]) - b
            else:
                n = min(height[max_i], height[max_j-j]) - b

            delta_s = a*n-b-n
            ret = True if delta_s > 0 else False
            if ret == True:
                flag = True
                if turn == True:
                    max_i = max_i+i
                else:
                    max_j = max_j-j
            else:
                if flag == True:
                    turn = 1-turn
                    flag = False

                if turn == True:
                    
                    i += 1
                else:
                    j += 1

        return min(height[max_i],height[max_j])*(max_j-max_i)
'''
               

#height = [2,3,4,5,18,17,6]
height = [1,8,6,2,5,4,8,3,7]

solution = Solution()

print(solution.maxArea(height))