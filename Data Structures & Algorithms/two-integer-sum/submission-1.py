class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        track = dict()
        output =list()

        for i in range(0,len(nums)):
            diff = target - nums[i]

            if diff in track:
                return [track[diff],i]
            else:
                track[nums[i]]= i
            

        