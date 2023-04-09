/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let longest = 0; // Initialize the length of the longest substring
    let left = 0; // Initialize the left pointer of the sliding window
    let right = 0; // Initialize the right pointer of the sliding window
    const seen = {}; // Initialize an object to store the last index of each character in the current substring

    // Iterate through the string with the right pointer
    while (right < s.length) {
        // Check if the current character is not in the current substring
        // or its index is less than or equal to the left pointer
        console.log(left, right);
        if (!seen[s[right]] || seen[s[right]] <= left) {
            // Update the character's index in the seen object
            seen[s[right]] = right + 1;

            // Update the longest substring length if the current substring is longer
            longest = Math.max(longest, right - left + 1);

            // Move the right pointer one step forward
            right++;
        } else {
            // Move the left pointer to the position right after the last occurrence of the repeated character
            left = seen[s[right]];
        }
    }

    return longest; // Return the length of the longest substring
};

var lengthOfLongestSubstringNested = function(s) {
    let longest = 0
    let i = 0;
    let candidate = 1;
    const length = s.length - 1;
    while (i < length + 1) {
        if (s[i] != s[i+1]) {
            let j = i;
            let seen = [s[j]]
            candidate = 1;
            while((s[j] != s[j+1]) 
                   && !seen.includes(s[j+1])
                   && (j < length)) {
                seen.push(s[j+1]);
                candidate += 1;
                j += 1;
            }
        }
        if (candidate > longest) {
            longest = candidate;
        }

        i++;
    }

    return longest;
};

// 3
console.log(lengthOfLongestSubstring("abcabcbb"));
/*
// 1
console.log(lengthOfLongestSubstring("bbbbb"));
// 3
console.log(lengthOfLongestSubstring("pwwkew"));

// 3
console.log(lengthOfLongestSubstringNested("abcabcbb"));
// 1
console.log(lengthOfLongestSubstringNested("bbbbb"));
// 3
console.log(lengthOfLongestSubstringNested("pwwkew"));
*/