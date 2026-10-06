class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        outbound = {i:[] for i in range(1,n+1)}
        inbound = {i:[] for i in range(1,n+1)}

        for outgoing,incoming in trust:
            outbound[outgoing].append(incoming)
            inbound[incoming].append(outgoing)
        
        for x in range(1,n+1):
            if len(outbound[x])==0 and len(inbound[x])==n-1:
                return x
        return -1 