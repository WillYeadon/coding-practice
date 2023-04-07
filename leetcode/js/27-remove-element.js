/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let i = 0;

    while (i < nums.length) {
        while (nums[i] === val) {
            nums.splice(i, 1);
        }
        i += 1;
    }
    return nums.length;
};

console.log(removeElement([3,2,2,3], 3));
console.log(removeElement([0,1,2,2,3,0,4,2], 2));