from typing import List

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        ret = []
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                ret.append([h[n], i])  

        return ret

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(0, len(nums)):
            target = -nums[i]
            nums_tar = nums[:i]+nums[i+1:]

            ret = self.twoSum(nums_tar, target)
            if ret is not None:
                for tars in ret:
                    tmp = [nums[i], nums_tar[tars[0]], nums_tar[tars[1]]]
                    tmp.sort()
                    if tmp not in ans:
                        ans.append(tmp)
    
        return ans



sol = Solution()

#nums = [-12,4,12,-4,3,2,-3,14,-14,3,-12,-7,2,14,-11,3,-6,6,4,-2,-7,8,8,10,1,3,10,-9,8,5,11,3,-6,0,6,12,-13,-11,12,10,-1,-15,-12,-14,6,-15,-3,-14,6,8,-9,6,1,7,1,10,-5,-4,-14,-12,-14,4,-2,-5,-11,-10,-7,14,-6,12,1,8,4,5,1,-13,-3,5,10,10,-1,-13,1,-15,9,-13,2,11,-2,3,6,-9,14,-11,1,11,-6,1,10,3,-10,-4,-12,9,8,-3,12,12,-13,7,7,1,1,-7,-6,-13,-13,11,13,-8]
#nums = [-1, 0, 1, 2, -1, -4]
nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]

print(sol.threeSum(nums))