class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""

        for word in strs:
            wordLength = len(word)
            res+=str(wordLength)+"#"+word
        
        return res

    def decode(self, s: str) -> List[str]:
        i=0
        words =[]
        while i<len(s):
            if int(s[i]) >=0 and int(s[i])<=9:
                count=""
                while s[i]!="#":
                    count+=s[i]
                    i+=1
                words.append(s[i+1:i+int(count)+1])
                i=i+int(count)+1
        
        return words