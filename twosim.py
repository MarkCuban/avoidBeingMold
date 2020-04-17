class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret = []
        for num in nums:
            if target-num in nums[nums.index(num)+1:]:
                ret.append(nums.index(num))
                ret.append(nums.index(target-num, nums.index(num)+1))
                break
        return ret