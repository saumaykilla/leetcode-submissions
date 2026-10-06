class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        nums = [-stone for stone in stones]
        heapq.heapify(nums)

        while len(nums)>1:

            firstStone = heapq.heappop(nums)
            secondStone = heapq.heappop(nums)

            if abs(firstStone) - abs(secondStone) >0:
                heapq.heappush(nums,-(abs(firstStone) - abs(secondStone)))
            
        
        return abs(nums[0]) if nums else 0