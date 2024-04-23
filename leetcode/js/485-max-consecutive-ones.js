/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    let max = 0;
    let current = 0;
    for (let i of nums) {
        current += i;
        max = Math.max(max, current);
        if (i === 0) {
            current = 0;
        }
    }
    return max;
};