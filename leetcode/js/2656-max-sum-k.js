/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maximizeSum = function(nums, k) {
    let max = Math.max(...nums);
    let score = 0;
    for (let i = 0; i < k; i++) {
        score += (max + i);
    }
    return score;
};