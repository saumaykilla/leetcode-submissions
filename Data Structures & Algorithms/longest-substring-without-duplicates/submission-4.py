class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left,right=0,0
        track=set()
        while right<len(s) :
            if s[right] not in track:
                track.add(s[right])
                longest = max(longest,right-left+1)
                right+=1
            elif left<right:
                track.remove(s[left])
                left+=1
        return longest
                
        