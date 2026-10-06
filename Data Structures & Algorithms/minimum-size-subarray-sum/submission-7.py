class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        cur = 0
        output = float("inf")

        for r in range(len(nums)):
            cur += nums[r]
            
            while cur >= target:
                output = min(output, r - l + 1)
                cur -= nums[l]
                l += 1

        return 0 if output == float("inf") else output
