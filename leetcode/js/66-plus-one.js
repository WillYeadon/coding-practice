/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    
    let carry = 1;

    for (let i = digits.length - 1; i >= 0; i--) {
        let sum = digits[i] + carry;
        if (sum >= 10) {
            digits[i] = sum - 10;
            carry = 1;
        } else {
            digits[i] = sum;
            carry = 0;
            break;
        }
    }
    
    if (carry === 1) {
        digits.unshift(1);
    }
    
    return digits;
};

// [1,2,4]
console.log(plusOne([1,2,3]));

// [4,3,2,2]
console.log(plusOne([4,3,2,1]));

// [1,0]
console.log(plusOne([9]));