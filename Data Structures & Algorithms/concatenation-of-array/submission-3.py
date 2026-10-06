class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        outputArrayLen = len(nums)*2

        output = [0]*outputArrayLen

        for i in range(len(nums)):
            output[i]= output[i+len(nums)] = nums[i]
        
        return output
        