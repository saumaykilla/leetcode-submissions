class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        ordIdx = {c:i for i,c in enumerate(order)}

        for i in range(len(words)-1):
            wrd1,wrd2 = words[i], words[i+1]

            for j in range(len(wrd1)):
                if j==len(wrd2):
                    return False
                
                if wrd1[j] != wrd2[j]:
                    if ordIdx[wrd1[j]] > ordIdx[wrd2[j]]:
                        return False
                    break
        return True