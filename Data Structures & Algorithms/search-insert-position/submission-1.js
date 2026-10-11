class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    searchInsert(nums, target) {
        let start = 0
        let end = nums.length
        let res = nums.length
        while(start <= end){
            let mid = Math.floor((start + end) / 2)
            if(nums[mid] === target){
                return mid
            }
            if(target < nums[mid]){
                end = mid - 1
                res = mid
            }
            else{
                start = mid + 1
            }
        }
        return res
    }
}
