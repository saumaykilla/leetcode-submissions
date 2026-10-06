class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Hashmap=dict()

        for i in range(len(s1)):
            s1Hashmap[s1[i]]=1 + s1Hashmap.get(s1[i],0)
        

        l=0
        r=len(s1)-1

        while(r<len(s2)):
            s2Hashmap = dict()
            for i in s2[l:r+1]:
                s2Hashmap[i]=1+s2Hashmap.get(i,0)
            if s1Hashmap == s2Hashmap:
                return True
            l+=1
            r+=1
        return False
