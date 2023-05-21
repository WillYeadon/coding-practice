/**
 * @param {string} s
 * @return {boolean}
 */
function palled(input) {
    let arr = input.split('');
    let x = '';
    let y = '';

    while (arr.length > 1) {
        x = arr.pop();
        y = arr.shift();
        if (x != y) {return false;}
    }

    return true;
}
// you didn't even read the question!!!!!
var isPalindrome = function(s) {
    const alphanumericOnly = s.replace(/[^a-zA-Z0-9]/g, "");
    return palled(alphanumericOnly.toLowerCase());
};
// true
console.log("A man, a plan, a canal: Panama");
// false
console.log("race a car");
// true
console.log(" ");