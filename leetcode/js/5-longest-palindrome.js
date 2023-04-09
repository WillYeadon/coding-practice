/**
 * @param {string} s
 * @return {string}
 */

var checkPalindrome = function(s) {
    let left = 0
    let right = s.length - 1
    
    while (left < right) {
        if (s[left] != s[right]) {
            return false
        }
        left += 1;
        right -= 1;
    }

    return true;
}

var longestPalindrome = function(s) {
    if (checkPalindrome(s)) {
        return s;
    }
    
    let longest = s[0];
    
    for (let left = 0; left < s.length; left++) {
        for (let right = left + 1; right < s.length; right++) {
            let candidate = s.slice(left, right + 1);
            if (checkPalindrome(candidate)) {
                if (candidate.length > longest.length) {
                    longest = candidate;
                }
            }

        }
    }

    return longest;
};

var longestPalindromeCentreExpand = function (string) {
    let longestPal = '';

    var getLongestPalindrome = function (leftPosition, rightPosition) {
        // While there is space to expand, and the expanded strings match
        while (
            leftPosition >= 0 &&
            rightPosition < string.length &&
            string[leftPosition] === string[rightPosition]
        ) {
            // Expand in each direction.
            leftPosition--;
            rightPosition++;
        }

        // Store the longest palindrom (if it's the longest one found so far)
        if (rightPosition - leftPosition > longestPal.length) {
            longestPal = string.slice(leftPosition + 1, rightPosition);
        }
    };

    // Loop through the letters
    for (let i = 0; i < string.length; i++) {
        // Find the longest odd palendrome
        getLongestPalindrome(i, i + 1);

        // Find the longest even palendrome
        getLongestPalindrome(i, i);

        // Check if a longer palindrome cannot be found
        if ((string.length - i) * 2 < longestPal.length) {
            // Break out to avoid unnecessary computation
            break;
        }
    }

    return longestPal;
};

// O(n^3)
// "bab", "aba" also valid
console.log(longestPalindrome("babad"));
// "bb"
console.log(longestPalindrome("cbbd"));

// O(n^2)
console.log(longestPalindromeCentreExpand("babad"));
console.log(longestPalindromeCentreExpand("cbbd"));
