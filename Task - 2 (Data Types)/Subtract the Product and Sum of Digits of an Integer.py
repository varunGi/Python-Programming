class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=0
        m=1
        l=[]
        while(n>0):
            l.append(n%10)
            n=n//10
        for i in l:
            s=s+i
            m=m*i
        return m-s