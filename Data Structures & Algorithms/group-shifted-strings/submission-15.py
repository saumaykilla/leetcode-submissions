class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strings:
            key = []
            for i in range(len(word) - 1):
                diff = (ord(word[i]) - ord(word[i+1])) % 26
                key.append(diff)

            result[tuple(key)].append(word)
        print(result)
        return list(result.values())