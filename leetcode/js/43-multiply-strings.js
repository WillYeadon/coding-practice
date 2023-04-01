/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var multiply = function(num1, num2) {
    // Check if either input is zero and return '0' if true
    if (num1 === '0' || num2 === '0') {
        return '0';
    }

    // Get the lengths of the input strings
    const m = num1.length;
    const n = num2.length;

    // Initialize an array to hold the intermediate products and their positions
    const result = Array(m + n).fill(0);

    // Iterate through the digits of num1 and num2 in reverse order
    for (let i = m - 1; i >= 0; i--) {
        for (let j = n - 1; j >= 0; j--) {
            // Calculate the product of the current digit pairs
            const prod = Number(num1[i]) * Number(num2[j]);
            // Calculate the positions in the result array for the current digit pairs
            const pos1 = i + j;
            const pos2 = i + j + 1;
            // Add the product to the corresponding positions in the result array
            const sum = prod + result[pos2];
            result[pos1] += Math.floor(sum / 10);
            result[pos2] = sum % 10;
        }
    }

    // Convert the result array into a string and remove any leading zeros
    let ans = '';
    let i = 0;
    while (result[i] === 0) {
        i++;
    }
    for (; i < result.length; i++) {
        ans += result[i];
    }

    return ans;
};

// "6"
console.log(multiply("2", "3"));
// "56088"
console.log(multiply("123", "456"));
