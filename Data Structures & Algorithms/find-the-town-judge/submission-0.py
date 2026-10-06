class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        outgoing = {}
        incoming = {}

        for i in range(1,n+1):
            incoming[i] = 0
            outgoing[i] = 0

        print(outgoing,incoming)
        for item in trust:
            outward = item[0]
            inward =item[1]

            incoming[inward]+=1
            outgoing[outward]+=1
        

        for i in range(1,n+1):
            if incoming[i] ==n-1 and outgoing[i]==0:
                return i
        
        return -1
        
        