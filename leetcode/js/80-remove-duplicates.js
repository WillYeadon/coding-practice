/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    const length = nums.length;
    if (length < 3) { return; }

    let start = nums[0];
    let count = 0;

    for (let i = 1; i < length; i++) {
        if (nums[i] === start) {
            count += 1;
            if (count > 1) {
                nums[i] = '_';
            }
        }
        else {
            start = nums[i];
            count = 0; 
        }
    }

    for (let j = nums.length - 1; j >= 0; j--) {
        if (nums[j] == '_') {
            nums.splice(j, 1);
        }
    }
};