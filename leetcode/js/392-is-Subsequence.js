/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    const sLength = s.length;
    const tLength = t.length;
    
    if (sLength === 0) return true;
    if (tLength === 0 || tLength < sLength) return false;
    
    let c = 0;
    
    for (let i of t) {
        if (i === s[c]) {
            c += 1;
            if (c === sLength) {
                return true;
            } 
        }
    }

    return false; 
};