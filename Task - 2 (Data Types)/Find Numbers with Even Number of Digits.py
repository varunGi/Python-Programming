class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            a=len(str(i))
            if(a%2==0):
                count+=1
        return count