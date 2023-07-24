/**
 * @param {number[]} height
 * @return {number}
 */

// Function to calculate how much rainwater is trapped
var trap = function(height) {
    // Initialize total rainwater trapped to 0
    let rain = 0;

    // Initialize two pointers, left and right, to the start and end of the array
    let left = 0, right = height.length - 1;

    // Initialize maximum height of bars from left and right to 0
    let maxLeft = 0, maxRight = 0;
    
    // While there are bars between the two pointers
    while (left < right) {
        // If the bar on the left is smaller or equal to the bar on the right
        if (height[left] <= height[right]) {
            // If the current bar is taller than maxLeft, update maxLeft
            if (height[left] >= maxLeft) {
                maxLeft = height[left];
            } else {
                // If the current bar is shorter than maxLeft, it can hold rainwater
                // The amount of rainwater it can hold is the difference between maxLeft and its height
                rain += maxLeft - height[left];
            }
            // Move the left pointer to the right
            left++;
        } else {
            // If the bar on the right is smaller than the bar on the left
            // If the current bar is taller than maxRight, update maxRight
            if (height[right] >= maxRight) {
                maxRight = height[right];
            } else {
                // If the current bar is shorter than maxRight, it can hold rainwater
                // The amount of rainwater it can hold is the difference between maxRight and its height
                rain += maxRight - height[right];
            }
            // Move the right pointer to the left
            right--;
        }
    }
    // Return the total amount of rainwater trapped
    return rain;
};
