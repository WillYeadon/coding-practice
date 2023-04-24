/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let negative = false;

    if (x < 0) {
        negative = true;
        x = -x;
    }

    ans = 0;
    digits = x.toString().split('').map(Number);

    // Remove leading/trailing zeros.

    while (digits[digits.length - 1] === 0) {
        digits.pop();
    }

    var reversed = [];
    while (digits.length > 0) {
        reversed.push(digits.pop());
    }

    ans = reversed.reduce((acc, val) => acc * 10 + val, 0);

    if (negative) {
        ans = -ans;
    }

    if ((ans < -2147483648) || (ans > 2147483647)) {
        return 0;
    }

    return ans;
};

// 321
console.log(reverse(123));
// -321
console.log(reverse(-123));
// 21
console.log(reverse(120));