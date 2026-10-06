class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        hashMap=dict()
        checkMap=dict()
        for i in t:
            hashMap[i]=1+hashMap.get(i,0)
        
        l=0
        result=""
        have=0
        res,resLen =[-1,-1],float("infinity")
        need= len(hashMap)
        for r in range(len(s)):

            if s[r] in t:
                checkMap[s[r]]=1+checkMap.get(s[r],0)

                if checkMap[s[r]] == hashMap[s[r]]:
                    have+=1
            
            while have == need:
                if r-l+1<resLen:
                    res=[l,r]
                    resLen = r-l+1

                if s[l] in t:
                    checkMap[s[l]] -=1

                    if checkMap[s[l]]<hashMap[s[l]]:
                        have-=1
                l+=1
        l,r=res
        return s[l:r+1] if resLen !=float("infinity") else ""







            