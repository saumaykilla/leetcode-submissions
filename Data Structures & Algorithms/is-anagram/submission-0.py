class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1=dict()
        string2=dict()
        for i in s:
            if i in string1:
                string1[i]+=1
            else:
                string1[i]=1
        for i in t:
            if i in string2:
                string2[i]+=1
            else:
                string2[i]=1

        return (string1==string2)