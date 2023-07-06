/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
function mapVals(s) {
    let x = new Map();

    for (let i of s) {
        if (x.has(i)) {
            x.set(i, x.get(i) + 1);
        } else {
            x.set(i, 1);
        }
    }

    return x;
}

var canConstruct = function(ransomNote, magazine) {
    let mapR = mapVals(ransomNote);
    let mapM = mapVals(magazine);

    for (let [key, value] of mapR) {
        if (!mapM.has(key) || mapM.get(key) < value) {
            return false;
        }
    }
    
    return true;
}