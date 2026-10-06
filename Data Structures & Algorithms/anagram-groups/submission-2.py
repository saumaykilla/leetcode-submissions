class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result =dict()

        for word in strs:
            anagram = [0]*26
            for char in word:
                anagram[ord(char)-ord('a')]+=1
            
            key = tuple(anagram)
            if key not in result:
                result[key]=[]
            result[key].append(word)
        
        return list(result.values())