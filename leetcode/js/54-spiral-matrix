/**
 * @param {number[][]} matrix
 * @return {number[]}
 */

var spiralOrder = function(matrix) {
    let height = matrix.length;
    let width = matrix[0].length;
    
    let output = [];
    let overall = height * width;
    
    let currentHeight = height;
    let currentWidth = width;
    
    let startRow = 0;
    let startCol = 0;

    while (output.length < overall) {
        for (let i = startCol; i < startCol + currentWidth; i++) {
            output.push(matrix[startRow][i]);
        }

        for (let i = startRow + 1; i < startRow + currentHeight; i++) {
            output.push(matrix[i][startCol + currentWidth - 1]);
        }

        if (output.length < overall) {
            for (let i = startCol + currentWidth - 2; i >= startCol; i--) {
                output.push(matrix[startRow + currentHeight - 1][i]);
            }

            for (let i = startRow + currentHeight - 2; i > startRow; i--) {
                output.push(matrix[i][startCol]);
            }
        }

        startRow += 1;
        startCol += 1;
        currentWidth -= 2;
        currentHeight -= 2;
    }

    return output;
};

console.log(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]));
console.log(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]));