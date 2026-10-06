class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        idx = 0

        while idx<len(strs[0]):
            char = strs[0][idx]
            for i in range(1,len(strs)):
                if idx>=len(strs[i]) or strs[i][idx] !=char:
                    return res
            res+=char
            idx+=1

        return res 
        