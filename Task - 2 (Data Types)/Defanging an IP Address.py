class Solution:
    def defangIPaddr(self, address: str) -> str:
        s=''
        for i in address:
            if(i=='.'):
                s=s+'['
                s=s+i
                s=s+']'
            else:
                s=s+i
        return s