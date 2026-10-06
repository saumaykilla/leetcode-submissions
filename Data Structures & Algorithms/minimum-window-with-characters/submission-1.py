class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count= dict()
        window = dict()
        for char in t:
            count[char]= count.get(char,0) + 1

        have,need = 0,len(count)
        res,resLen = [-1,-1], float("inf")
        left = 0

        for right in range(len(s)):

            cur = s[right]
            window[cur]= 1 + window.get(cur,0)

            if cur in count and window[cur] == count[cur]:
                have+=1

            while have==need:
                if (right-left+1) < resLen:
                    res=[left,right]
                    resLen = right - left + 1
                
                window[s[left]] -= 1

                if s[left] in count and window[s[left]] < count[s[left]]:
                    have-=1
                left+=1

        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""
                


        