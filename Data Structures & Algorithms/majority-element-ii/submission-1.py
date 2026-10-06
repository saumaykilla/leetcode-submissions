class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res=set()

        hashMap ={}

        for i in nums:
            hashMap[i] = hashMap.get(i,0) + 1

            if hashMap[i] > len(nums)//3 and i not in res:
                res.add(i)

        return list(res)
