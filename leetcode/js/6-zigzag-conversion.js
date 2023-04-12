/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    if (numRows === 1) return s; // special case

    // Initialize an array of numRows arrays, to hold the characters
    // in the zigzag pattern
    let rows = [];
    for (let i = 0; i < numRows; i++) {
       rows.push([]);
    }

    // Keep track of which row in the zigzag pattern to add 
    // the current character to, and whether we're currently
    // moving up or down the zigzag
    let currentRow = 0;
    let direction = -1;
    
    // Iterate over the characters in the input string s, 
    // adding each character to the
    // appropriate row in the zigzag pattern
    for (let i = 0; i < s.length; i++) {
        // This is just looping through the string
        // console.log(s[i]);
        // However where this is pushed to will depend on the
        // current row
        rows[currentRow].push(s[i]);
    
        // If we're at the top or bottom row of the zigzag pattern,
        // switch direction
        // This is how the rows are navigated
        if (currentRow === 0 || currentRow === numRows - 1) {
          direction = -direction;
        }
        
        // Move to the next row in the appropriate direction
        // Move on in the stated direction
        currentRow += direction;
      }
    
      // Concatenate the characters in each row of the zigzag 
      // pattern to form the final output string
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