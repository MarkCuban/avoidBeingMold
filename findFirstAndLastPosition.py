from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == None or len(nums) == 0:
            return [-1, -1]

        max_n = len(nums)-1
        min_n = 0
        ret = -1

        while min_n <= max_n:

            mid = min_n + (max_n-min_n)//2

            if nums[mid] > target:
                max_n = mid-1
            elif nums[mid] < target:
                min_n = mid+1
            else:
                ret = mid
                break

        range_ret = []
        if ret != -1:
            while ret >= 0 and nums[ret] == target:
                ret -= 1
            range_ret.append(ret+1)
            while mid < len(nums) and nums[mid] == target:
                mid += 1
            range_ret.append(mid-1)
            return range_ret

        return [-1, -1]
sol = Solution()

nums = [5, 7, 7, 8, 8, 10, 12, 12, 12, 12]

target = 12

print(sol.searchRange(nums, target))