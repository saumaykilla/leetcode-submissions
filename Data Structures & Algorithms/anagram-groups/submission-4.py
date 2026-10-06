class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for i in strs:
            hashset = [0]*26
            for char in i:
                hashset[ord(char)-ord('a')]+=1
            
            output[tuple(hashset)].append(i)
        
        return list(output.values())
        