from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ret = 0

        i = 0
        while i < len(nums):
            if i != len(nums)-1:
                if nums[i] == nums[i+1]:
                    nums[i+1:] = nums[i+2:]
                else:
                    i += 1
            else:
                break
        
        return len(nums)

sol = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(sol.removeDuplicates(nums))