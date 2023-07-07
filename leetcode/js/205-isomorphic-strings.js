/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    if (s.length != t.length) { return false; }

    let x = new Map();
    let y = new Map();

    for (let i = 0; i < s.length; i++) {
        let sChar = s[i];
        let tChar = t[i];

        if ((x.has(sChar) && x.get(sChar) !== tChar) || 
            (y.has(tChar) && y.get(tChar) !== sChar)) {
            return false;
        }

        x.set(sChar, tChar);
        y.set(tChar, sChar);
    }

    return true;
};