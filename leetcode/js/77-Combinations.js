/**
 * Function to generate all combinations C(n, k)
 * @param {number} n - The larger number in C(n, k)
 * @param {number} k - The smaller number in C(n, k)
 * @return {number[][]} - An array of arrays, each of which is a k-combination of the numbers 1, 2, ..., n
 */
var combine = function(n, k) {
    // Initialize an empty array to store the final combinations
    let ans = [];

    // Base Case 1: If k is zero, then there is only one combination: the empty set
    if (k === 0) {
        return [[]];
    }

    // Base Case 2: If n is smaller than k, then no valid combination can be formed
    if (n < k) {
        return [];
    }

    // Start iterating from 'n' down to 'k'
    for (let i = n; i >= k; i--) {
        // Recursive call to generate combinations of size 'k-1' from the numbers 1, ..., i-1
        let smallerComb = combine(i - 1, k - 1);

        // For each of the smaller combinations, add the current number 'i' 
        // This effectively builds combinations of size 'k' that include 'i'
        for (let comb of smallerComb) {
            comb.push(i);  // Add the current number to the existing smaller combination
            ans.push(comb);  // Add this new combination to the answer list
        }
    }

    // Return the final array of combinations
    return ans;
};

// Test the function
console.log(combine(4, 2));  // Should output [[2, 1], [3, 1], [3, 2], [4, 1], [4, 2], [4, 3]]
