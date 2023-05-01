/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    const index = nums.indexOf(target);
    if (index > -1) {return index;}

    // Binary search
    let left = 0;
    if (nums[left] > target) {
        return 0;
    }    
    
    let right = nums.length - 1;
    if (nums[right] < target) {
        return (right + 1);
    }

    let half = Math.floor((right / 2));

    while (right > left) {
        if (nums[half] > target) {
            right = half;
        }
        else if (nums[half] < target) {
            left = half;
        }
        half = left + Math.floor(((right - left)/2));
        if ((right - left) <= 1) { break; }
    }

    return (half + 1);
};

var searchInsertFast = function(nums, target) {
    if (nums.includes(target)) {
        return nums.indexOf(target);
    }
    return [...nums,target].sort((a,b)=>a-b).indexOf(target);     
 };

// 2
console.log(searchInsert([1,3,5,6], 5));
// 1
console.log(searchInsert([1,3,5,6], 2));
// 4
console.log(searchInsert([1,3,5,6], 7));

// 2
console.log(searchInsertFast([1,3,5,6], 5));
// 1
console.log(searchInsertFast([1,3,5,6], 2));
// 4
console.log(searchInsertFast([1,3,5,6], 7));