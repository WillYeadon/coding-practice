/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
    let solutions = [];
    let sorted = nums.sort(function(a, b){return a - b});
    const length = sorted.length;

    for (let i = 0; i < length - 3; i++) {
        // Skip over duplicates for i
        if (i > 0 && sorted[i] === sorted[i - 1]) {
            continue;
        }
        
        for (let j = i + 1; j < length - 2; j++) {
            // Skip over duplicates for j
            if (j > i + 1 && sorted[j] === sorted[j - 1]) {
                continue;
            }
            
            let candidate = sorted[i] + sorted[j];
            let left = j + 1;
            let right = length - 1;

            while (left < right) {
                let sum = sorted[left] + sorted[right];
                if (sum === target - candidate) {
                    solutions.push([sorted[i], sorted[j], sorted[left], sorted[right]]);
                    // Skip over duplicates of the left pointer
                    while (left < right && sorted[left] === sorted[left + 1]) {
                        left++;
                    }
                    // Skip over duplicates of the right pointer
                    while (left < right && sorted[right] === sorted[right - 1]) {
                        right--;
                    }
                    left++;
                    right--;
                } else if (sum < target - candidate) {
                    left++;
                } else {
                    right--;
                }
            }
        }
    }

    return solutions;
};


// [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
console.log(fourSum([1,0,-1,0,-2,2], 0));

// [[2,2,2,2]]
console.log(fourSum([2,2,2,2,2], 8));