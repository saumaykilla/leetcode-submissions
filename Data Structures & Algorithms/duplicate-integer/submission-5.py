class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        track = set()

        for a in nums:
            if a in track:
                return True
            track.add(a)
        
        return False