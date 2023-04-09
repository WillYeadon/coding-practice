/**
 * @param {string} s
 * @return {string}
 */
var checkPalindrome = function(s) {
    let left = 0
    let right = s.length - 1
    
    while (left < right) {
        console.log(s[left], s[right]);
        if (s[left] != s[right]) {
            return false
        }
        left += 1;
        right -= 1;
    }

    return true;
}

var longestPalindrome = function(s) {
    
};

// "bab", "aba" also valid
console.log(longestPalindrome("babad"));
// "bb"
console.log(longestPalindrome("cbbd"));
