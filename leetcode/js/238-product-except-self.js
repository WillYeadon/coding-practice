/**
 * @param {number[]} nums
 * @return {number[]}
 */

var productExceptSelf = function(nums) {
    let answer = [...nums];
    let product = nums[0];
    let product2 = nums[0];
    let zeros = 0;
    
    if (product2 === 0) { 
        product2 = 1;
        zeros += 1;
    }

    for (let i = 1; i < nums.length; i++) {
        product *= nums[i];
        if (nums[i] === 0) {
            zeros += 1;
        }
        if ((nums[i] !== 0) && (zeros < 2)) {
            product2 *= nums[i];
        }
        if (zeros > 1) {
            product2 = 0;
        }
    }

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== 0) {
            answer[i] = product * Math.pow(nums[i], -1);
        }
        else {
            answer[i] = product2;
        }
    }

    return answer;
};