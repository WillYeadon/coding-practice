/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    const end = needle.length;
    for (let i = 0; i < haystack.length; i++) {
        if (haystack.slice(i,i+end) == needle) {
            return i;
        }
    }
    return -1;
};

// 1 2 3
console.log(strStr('abcdefgh', 'bc'));
console.log(strStr('Hello', 'll'));
console.log(strStr('oneTwooneTwo', 'Two'));