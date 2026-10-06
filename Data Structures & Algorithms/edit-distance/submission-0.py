class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1),len(word2)
        memo = {}
        def solve(i,j):
            if i == m:
                return n - j
            if j == n:
                return m-i

            if (i,j) in memo:
                return memo[(i,j)]

            if word1[i] == word2[j]:
                return solve(i+1,j+1)

            #insert j character at i
            insert = 1+ solve(i,j+1)
            # delete kth character
            delete = 1 + solve(i+1,j)
            # replace kth character
            replace = 1 + solve(i+1,j+1)

            memo[(i,j)] = min(insert,delete,replace)
            return memo[(i,j)]


        return solve(0,0)
        