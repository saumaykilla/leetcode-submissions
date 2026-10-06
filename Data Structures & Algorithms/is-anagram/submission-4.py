class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = defaultdict(int)
        hashT = defaultdict(int)

        for i in s:
            hashS[i]+=1

        for i in t:
            hashT[i]+=1

        return hashS == hashT