/**
 * @param {number} numRows
 * @return {number[][]}
 */

var generate = function(numRows) {
    if (numRows === 0) { return []; }
    if (numRows === 1) { return [[1]]; }
    if (numRows === 2) { return [[1], [1, 1]]; }

    let ans = [];

    for (let i = 0; i < numRows; i++) {
        let currentRow = [1];
        let length = ans.length;
        if (length > 0) {
            let previousRow = ans[length - 1];
            for (let j = 0; j < previousRow.length - 1; j++) {
                currentRow.push(previousRow[j] + previousRow[j + 1]);
            }
            currentRow.push(1);
        }
        ans.push(currentRow);
    }
    return ans;
};

console.log(generate(5));
console.log(generate(1));