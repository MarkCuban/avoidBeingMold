from typing import List

class Solution:

    def binarySearch(self, nums, tar):
        
        if nums == None or len(nums) == 0:
            return -1

        max_n = len(nums)-1
        min_n = 0

        while min_n <= max_n:

            mid = min_n + (max_n-min_n)//2

            if nums[mid] > tar:
                max_n = mid-1
            elif nums[mid] < tar:
                min_n = mid+1
            else:
                return mid
        
        return -1

    def search(self, nums: List[int], target: int) -> int:
        if nums == None or len(nums) == 0:
            return -1

        max_n = len(nums)-1
        min_n = 0

        if nums[min_n] <= nums[max_n]:
            binary = True
        else:
            binary = False

        while min_n <= max_n:

            mid = min_n + (max_n-min_n)//2
            if binary == True:
       
                if nums[mid] > target:
                    max_n = mid-1
                elif nums[mid] < target:
                    min_n = mid+1
                else:
                    return mid
            else:
                if mid <= 0:
                    mid = 1

                left = nums[0:mid]
                right = nums[mid:]
                
                res = self.search(left, target)
                if res != -1:
                    return res
                else:
                    res = self.search(right, target)
                    if res != -1:
                        return res+mid
                    return -1
            
        return -1





sol = Solution()

nums = [23, 56, 149, 386, 1, 3, 5, 6, 7, 9, 20]
target = 386
print(sol.search(nums, target))