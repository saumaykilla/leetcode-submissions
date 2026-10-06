class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        ans=0
        check=len(s)


        for i in t:
            if(s[ans]==i):
                ans+=1
            if ans==check:
                return True
        
        return False