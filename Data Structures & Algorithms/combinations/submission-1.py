class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def backtrack(i,subset):
            if i> n:
                if len(subset) == k:
                    res.append(subset.copy())
                return
            subset.append(i)
            backtrack(i+1,subset)
            subset.pop()
            backtrack(i+1,subset)



        backtrack(1,[])
        return res