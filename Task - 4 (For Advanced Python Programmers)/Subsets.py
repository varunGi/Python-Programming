class Solution:
    def s(self,x,nums,n,r,i):
        r1=r.copy()
        if(i==n):
            r.sort()
            x.append(r)
            return
        r1.insert(i,nums[i])
        self.s(x,nums,n,r,i+1)
        self.s(x,nums,n,r1,i+1)
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        x=[]
        self.s(x,nums,n,[],0)
        return x