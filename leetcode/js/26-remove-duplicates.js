/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let i = 0;
    while (i < nums.length - 1) {
        // Just don't increment unless no splice
        // this gets past the for loop difficulties
        if (nums[i] == nums[i+1]) {
            nums.splice(i+1, 1);
        }
        else {
            i += 1;
        }
    }
    return nums.length;
};

console.log(removeDuplicates([1,1,2]));
console.log(removeDuplicates([0,0,1,1,1,2,2,3,3,4]));