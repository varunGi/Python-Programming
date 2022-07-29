def hammingWeight(n):
        c=0
        for i in range(32):
            if(n>>i)%2==1:
                c=c+1
        return c
class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        for i in range(0,n+1):
            l.append(hammingWeight(i))
        return l