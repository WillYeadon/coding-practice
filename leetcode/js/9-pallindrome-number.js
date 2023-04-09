/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if (x == 0) {return true;}
    if (x <= 0) {return false;}
    
    // This creates a lot of unnecessary overhead
    // Can just use x.toString()
    const digits = [...x.toString()].map(Number);
    const full = digits.length;
    const half = Math.floor(full / 2);

    for (let i = 0; i < half; i++) {
        if (digits[i] != digits[full - 1 - i]) {
            return false;
        }
    }

    return true
};

console.log(isPalindrome(121));
console.log(isPalindrome(-121));
console.log(isPalindrome(10));