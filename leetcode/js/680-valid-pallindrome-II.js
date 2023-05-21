/**
 * @param {string} s
 * @return {boolean}
 */
function isPalindrome(s, start, end) {
    while (start < end) {
        if (s[start] !== s[end]) {
            return false;
        }
        start++;
        end--;
    }
    return true;
}

var validPalindrome = function(s) {
    let start = 0;
    let end = s.length - 1;

    while (start < end) {
        if (s[start] !== s[end]) {
            // Try skipping either the left or right character
            return (
                isPalindrome(s, start + 1, end) || isPalindrome(s, start, end - 1)
            );
        }
        start++;
        end--;
    }

    return true; // The string is a valid palindrome
};

// true
console.log(validPalindrome("aba"));
// true
console.log(validPalindrome("abca"));
// false
console.log(validPalindrome("abc"));
