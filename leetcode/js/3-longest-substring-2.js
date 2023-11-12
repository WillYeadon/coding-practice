/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let longest = 0;
    let current = [];
    for (let i of s) {
        if (!(current.includes(i))) {
            current.push(i);
        }
        else {
            while (current.includes(i)) {
                current.shift();
            }
            current.push(i);
        }
        longest = Math.max(longest, current.length);
    }
    return longest;
};
// 3
console.log(lengthOfLongestSubstring("abcabcbb"));