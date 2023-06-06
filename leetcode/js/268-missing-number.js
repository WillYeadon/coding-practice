/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    const length = nums.length;
    let all = Array.from(Array(length + 1).keys());
    for (let i = 0; i <= length; i++) {
        if (!nums.includes(all[i])) {
            return all[i];
        }
    }
};

var missingNumberFast = function(nums) {
    let len = nums.length; 
    let sum = nums.reduce((a,b)=>a+b,0);
    let res = len*(len+1) / 2;
    return res - sum
};