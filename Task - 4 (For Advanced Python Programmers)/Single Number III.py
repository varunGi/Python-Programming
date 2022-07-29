class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a=[]
        for i in nums:
            if(nums.count(i)==1):
                a.append(i)
            if(len(a)==2):
                break
        return a
                