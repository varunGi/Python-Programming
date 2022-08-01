class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        c=x^y
        count=0
        for i in range(32):
            if(c>>i)%2!=0:
                count+=1
        return count