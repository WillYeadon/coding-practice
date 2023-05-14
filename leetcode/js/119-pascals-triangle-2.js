var getRow = function(rowIndex) {
    let ans = [];

    for (let i = 0; i < rowIndex + 1; i++) {
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
    return ans[ans.length - 1];
};

console.log(getRow(5));
console.log(getRow(1));