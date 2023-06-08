/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    let ans = "";
    let length = Math.max(word1.length, word2.length);
    
    for (let i = 0; i < length; i++) {
        if (word1.length > 0) {
            ans += word1.charAt(0);
            word1 = word1.slice(1);
        }
        if (word2.length > 0) {
            ans += word2.charAt(0);
            word2 = word2.slice(1);
        }
    } 

    return ans;
};