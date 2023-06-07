/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
function swap(s, i, j) {
    let hold = s[i];
    s[i] = s[j];
    s[j] = hold;
}

var reverseString = function(s) {
    const length = s.length;
    for (let i = 0; i < Math.floor(length / 2); i++) {
        swap(s, i, length - 1 - i);
    }
};