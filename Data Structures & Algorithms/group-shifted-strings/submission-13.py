class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strings:
            key = []
            for i in range(len(word) - 1):
                diff = (ord(word[i+1]) - ord(word[i]) + 26) % 26
                key.append(diff)

            result[tuple(key)].append(word)

        return list(result.values())