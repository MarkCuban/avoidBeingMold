from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#        ret = []
#        for num in nums:
#            if target-num in nums[nums.index(num)+1:]:
#                ret.append(nums.index(num))
#                ret.append(nums.index(target-num, nums.index(num)+1))
#                break
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]        

#        return ret


sol = Solution()

nums = [2, 7, 11, 15]
target = 9

print(sol.twoSum(nums, target))