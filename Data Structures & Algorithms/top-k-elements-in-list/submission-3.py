class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = dict()
        output = [[] for i in range(len(nums) + 1)]
        result=[]
        for i in nums:
            frequencyMap[i] = frequencyMap.get(i,0) + 1

        for num,count in frequencyMap.items():
            output[count].append(num)

        for i in range(len(output)-1,0,-1):
            if len(output[i])>0:
                for val in output[i]:
                    result.append(val)
                    if len(result)==k:
                        return result
        