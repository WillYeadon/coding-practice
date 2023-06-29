/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let profit = 0;
    let candidate = 0;
    
    for (let i = 1; i < prices.length; i++) {
        candidate = prices[i] - prices[i - 1];
        if (candidate > 0) {
            profit += candidate;
        }
    }

    return profit;
};