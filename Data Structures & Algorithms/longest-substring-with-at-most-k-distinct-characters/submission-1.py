class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        freqMap = dict()
        l = 0
        resLen = 0

        for r in range(len(s)):

            freqMap[s[r]] = freqMap.get(s[r], 0) + 1
            
            while len(freqMap)>k:
                freqMap[s[l]] -= 1
                if freqMap[s[l]]==0:
                    del freqMap[s[l]]
                l+=1
            resLen = max(resLen, r - l + 1)
        return resLen


        