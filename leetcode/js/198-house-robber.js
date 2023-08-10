/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    // Handle the case where there are no houses
    if (nums.length === 0) return 0;
    // Handle the case where there's only one house
    if (nums.length === 1) return nums[0];
    
    // Initialize a dynamic programming array 'dp' to store the maximum amounts that can be robbed up to each house
    let dp = new Array(nums.length);
    // The maximum amount robbed from the first house is simply the value of that house
    dp[0] = nums[0];
    // The maximum amount robbed from the first two houses is the greater of the values of those two houses
    dp[1] = Math.max(nums[0], nums[1]);
    
    // Iterate through the rest of the houses, starting from the third
    for (let i = 2; i < nums.length; i++) {
        // For each house, we have two choices:
        // 1. Rob the current house, in which case we add its value to the maximum amount robbed up to two houses before it (since we can't rob adjacent houses)
        // 2. Skip the current house, in which case the maximum amount robbed so far is the same as the maximum amount robbed up to the previous house
        // We take the maximum of these two choices and store it in 'dp'
        dp[i] = Math.max(dp[i-1], dp[i-2] + nums[i]);
    }
    
    // The last element in 'dp' now contains the maximum amount that can be robbed from all the houses without violating the constraint of not robbing adjacent houses
    return dp[nums.length - 1];
};
