class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        k = len(s1)
        l = 0 
        counts1,counts2 = {},{}

        for i in range(len(s1)):
            counts1[s1[i]] = 1 + counts1.get(s1[i],0)

        for r in range(len(s2)):
            counts2[s2[r]] = 1 + counts2.get(s2[r],0)

            while (r-l+1)>k:
                counts2[s2[l]] -= 1
                if counts2[s2[l]] == 0:
                    del counts2[s2[l]]
                l+=1
        
            if counts2==counts1:
                return True
        return False

        