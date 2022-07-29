class Solution:
    def numTeams(self, rating: List[int]) -> int:
        u_dps = [0 for _ in range(len(rating))]
        l_dps = [0 for _ in range(len(rating))]
        
        count = 0
        for i in range(len(rating)):
            for j in range(i):
                if rating[j] < rating[i]:
                    count += u_dps[j]
                    u_dps[i] += 1
                else:
                    count += l_dps[j]
                    l_dps[i] += 1
                    
        return count