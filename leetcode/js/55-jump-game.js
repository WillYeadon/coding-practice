/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    let current = nums.length - 1;  

    for (let i = current - 1; i > -1; i--) {
        if (i + nums[i] >= current) {
            current = i;
        }           
    }

    return current === 0; 
};