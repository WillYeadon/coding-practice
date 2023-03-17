/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    longest = '';
    firstElement = strs[0];
    candidate = '';
    candidates = strs.length;

    for (let j = 0; j < firstElement.length; j++) {
        count = 0;
        for (let i = 0; i < candidates; i++ ) {
            if (i == 0) {
                candidate = strs[i][j];
                count += 1;
            }
            else {
                if (strs[i][j] == candidate) {
                    count += 1;
                }
            }
        }

        if (count == candidates) {
            longest += candidate;
        }
        else {
            break;
        }
    }

    return longest
};

console.log(longestCommonPrefix(['car', 'cir']))
console.log(longestCommonPrefix(["flower","flow","flight"]))
console.log(longestCommonPrefix(['']))