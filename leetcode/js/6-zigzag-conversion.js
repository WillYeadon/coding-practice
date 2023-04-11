/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    if (numRows === 1) return s; // special case

    let rows = [];
    for (let i = 0; i < numRows; i++) {
       rows.push([]);
    }

    let currentRow = 0;
    let direction = -1;
    
    for (let i = 0; i < s.length; i++) {
        rows[currentRow].push(s[i]);
    if (currentRow === 0 || currentRow === numRows - 1) {
        direction = -direction;
    }
        currentRow += direction;
    }

    let result = '';
    for (let i = 0; i < numRows; i++) {
        result += rows[i].join('');
    }

    return result;
};

// "PAHNAPLSIIGYIR"
console.log(convert("PAYPALISHIRING", 3));
// "PINALSIGYAHRPI"
console.log(convert("PAYPALISHIRING", 4));
// "S" // special case
console.log(convert("S", 1));