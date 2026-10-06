class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start=0
        end = len(numbers)-1

        while start<end:
            sumation= numbers[start]+numbers[end]
            
            if(sumation==target):
                return [start+1,end+1]
            
            elif(sumation>target):
                end-=1
            elif(sumation<target):
                start+=1
        
        return