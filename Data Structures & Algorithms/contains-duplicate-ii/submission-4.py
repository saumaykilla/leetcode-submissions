class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        hashMap = {}

        for i in range(0,len(nums)):
            if nums[i] in hashMap and i- hashMap[nums[i]]<=k:
                    return True
            else:
                hashMap[nums[i]]=i
        return False
        