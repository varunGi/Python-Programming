# 1 b) Shuffle the Array
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        m=n
        b=[]
        for i in range(m):
            b.append(nums[i])
            b.append(nums[i+m])
        
        return b