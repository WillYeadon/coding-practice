/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    let numDict = {};
    
    for (let i = 0; i < nums.length; i++) {
        let num = nums[i]
        if ((num in numDict) && ((i - numDict[num]) <= k)) {
            return true;
        }
        numDict[num] = i;
    }
    return false;
};