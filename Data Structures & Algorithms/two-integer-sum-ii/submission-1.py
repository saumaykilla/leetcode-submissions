class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        checkMap = dict()

        for i in range(0,len(numbers)):
            diff = target - numbers[i]

            if diff in checkMap:
                return [checkMap[diff]+1,i+1]

            checkMap[numbers[i]]=i