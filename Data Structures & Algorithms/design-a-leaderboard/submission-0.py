class Leaderboard:

    def __init__(self):
        self.leaderBoard ={}

        

    def addScore(self, playerId: int, score: int) -> None:
            self.leaderBoard[playerId] = self.leaderBoard.get(playerId,0) + score
        

    def top(self, K: int) -> int:
        heap=[]
        for ele in self.leaderBoard.values():
            heapq.heappush(heap,ele)
            if len(heap) > K:
                heapq.heappop(heap)
        res=0
        while heap:
            res +=heapq.heappop(heap)
        return res
        

    def reset(self, playerId: int) -> None:
        self.leaderBoard[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
