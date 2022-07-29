# 1 a) Running sum of 1 d array
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a=nums[0]
        for i in range(1,len(nums)):
            nums[i]=nums[i]+a
            a=nums[i]
        return nums
