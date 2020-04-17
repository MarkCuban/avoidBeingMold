class Solution:
    
    def getMedian(self, nums):
        ret = 0
        if len(nums) % 2 == 0:
            ret = (nums[len(nums)//2]+nums[len(nums)//2-1])/2
        else:
            ret = nums[len(nums)//2]
        
        return ret
            
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums = nums1+nums2
        nums.sort()
        
        return self.getMedian(nums)