/**
 * @param {number} n
 * @return {number}
 */

function helper(n, memo) {
    if (n === 0) {
        return 0;
    }
    else if (n === 1) {
        return 1;
    }
    else if (n === 2) {
        return 2;
    }
    else if (memo.has(n)) {
        return memo.get(n);
    }
    else{
        memo.set(n, helper(n - 1, memo) + helper(n - 2, memo));
        return memo.get(n);
    }
}

var climbStairs = function(n) {
    let memo = new Map()

    return helper(n, memo);
};