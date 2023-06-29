/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    let shadow = Array.from(nums);
    let length = nums.length;
    let remainder = k % length;

    for (let i = 0; i < length; i++) {
        if (i < remainder) {
            nums[i] = shadow[length - remainder + i];
        }
        else {
            nums[i] = shadow[i - remainder];
        }
    }

};