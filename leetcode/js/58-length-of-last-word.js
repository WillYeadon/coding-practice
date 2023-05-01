/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    const trimmed = s.trim()
    const split = trimmed.split(/\s+/);

    return split[split.length - 1].length;
};

// 5
console.log(lengthOfLastWord("Hello World"));
// 4
console.log(lengthOfLastWord("   fly me   to   the moon  "));
// 6
console.log(lengthOfLastWord("luffy is still joyboy"));
