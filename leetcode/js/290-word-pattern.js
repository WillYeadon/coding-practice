/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function(pattern, s) {
    let p = pattern.split('');
    let t = s.split(' ');

    if (p.length != t.length) { return false; }
    
    let x = new Map();
    let y = new Map();

    for (let i = 0; i < p.length; i++) {
        let pChar = p[i];
        let tChar = t[i];

        if ((x.has(pChar) && x.get(pChar) !== tChar) || 
           (y.has(tChar) && y.get(tChar) !== pChar)) {
            return false;
        }

        x.set(pChar, tChar);
        y.set(tChar, pChar);
    }

    return true;
};