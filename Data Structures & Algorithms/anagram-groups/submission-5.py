class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashSet = defaultdict(list)

        for word in strs:
            track = [0]*26
            for char in word:
                track[ord(char)- ord('a')] += 1
            
            hashSet[tuple(track)].append(word)
        
        return list(hashSet.values())