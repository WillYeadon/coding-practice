/**
 * @param {number[]} ratings
 * @return {number}
 */
var candy = function(ratings) {
    // The number of children
    let n = ratings.length;

    // Initialize an array to hold the number of candies for each child.
    // Each child gets at least one candy, so we fill the array with 1s.
    let candies = new Array(n).fill(1);

    // Make a forward pass through the ratings.
    // For each child, if their rating is higher than their left neighbor's rating,
    // they should get one more candy than their left neighbor.
    for (let i = 1; i < n; i++) {
        if (ratings[i] > ratings[i - 1]) {
            candies[i] = candies[i - 1] + 1;
        }
    }

    // Make a backward pass through the ratings.
    // For each child, if their rating is higher than their right neighbor's rating,
    // they should get at least as many candies as their right neighbor plus one.
    // However, they might already have been assigned more candies during the forward pass.
    // In that case, they should keep their higher number of candies.
    // So, we use Math.max to ensure that candies[i] is the larger of its current value and candies[i + 1] + 1.
    for (let i = n - 2; i >= 0; i--) {
        if (ratings[i] > ratings[i + 1]) {
            candies[i] = Math.max(candies[i], candies[i + 1] + 1);
        }
    }

    // Return the total number of candies.
    // We use the reduce method to sum up the values in the candies array.
    return candies.reduce((a, b) => a + b, 0);
};
