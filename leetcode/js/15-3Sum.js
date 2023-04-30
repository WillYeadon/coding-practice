/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    let ordered = nums.sort((a, b) => a - b);
    let triplets = [];
    const length = ordered.length;

    for (let i = 0; i < length; i++) {
        if (i > 0 && ordered[i] === ordered[i - 1]) {
            // Skip over duplicates of the current element
            continue;
        }
        let left = i + 1;
        let right = length - 1;
        let candidate = ordered[i];
        while (left < right) {
            let sum = ordered[left] + ordered[right];
            if (sum === -candidate) {
                triplets.push([candidate, ordered[left], ordered[right]]);
                // Skip over duplicates of the left pointer
                while (left < right && ordered[left] === ordered[left + 1]) {
                    left++;
                }
                // Skip over duplicates of the right pointer
                while (left < right && ordered[right] === ordered[right - 1]) {
                    right--;
                }
                left++;
                right--;
            } else if (sum < -candidate) {
                left++;
            } else {
                right--;
            }
        }
    }

    return triplets;
};

// [[-1,-1,2],[-1,0,1]]
console.log(threeSum([-1,0,1,2,-1,-4]));
// []
console.log(threeSum([0,1,1]));
// [[0,0,0]]
console.log(threeSum([0,0,0]));