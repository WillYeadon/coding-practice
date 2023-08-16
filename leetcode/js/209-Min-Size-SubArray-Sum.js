/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, nums) {
    let ans = Infinity;  
    let running = 0, count = 0, left = 0, right = 0;

    while (left < nums.length) {      
        if ((running >= target) && (count < ans)) {
            ans = count; 
        }
        if (running < target) {
            running += nums[right];
            right++;
            count++;
        }
        else {
            running -= nums[left];
            left++;
            count--;
        }
        if (left > right) {right = left;}
    }
    if (ans === Infinity) {return 0;}
    else {return ans;}
};

var minSubArrayLenShort = function(target, nums) {
    let ans = Infinity;
    let running = 0;
    let left = 0;

    for (let right = 0; right < nums.length; right++) {
        running += nums[right];
        while (running >= target) {
            ans = Math.min(ans, right - left + 1);
            running -= nums[left];
            left++;
        }
    }

    return ans === Infinity ? 0 : ans;
};
