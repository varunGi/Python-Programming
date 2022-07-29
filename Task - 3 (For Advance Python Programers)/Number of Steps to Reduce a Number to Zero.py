class Solution:
    def numberOfSteps(self, num: int) -> int:
        c=0
        while(num!=0):
            if(num%2==0):
                c=c+1
                num=num//2
            else:
                c=c+1
                num=num-1
        return c