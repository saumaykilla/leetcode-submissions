class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res =""

        for index in range(len(strs[0])):
            c = strs[0][index]

            for j in range(1,len(strs)):

                if index>=len(strs[j]) or strs[j][index] !=c:
                    return res
            
            res+=c
        return res