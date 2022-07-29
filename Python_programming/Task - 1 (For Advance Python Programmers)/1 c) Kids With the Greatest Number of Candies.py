
# 1 c) Kids With the Greatest Number of Candies
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]
        a=candies
        for i in range(len(a)):
            a[i]=a[i]+extraCandies
            if(max(a)==a[i]):
                result.append(True)
            else:
                result.append(False)
            a[i]=a[i]-extraCandies
            
        return result
