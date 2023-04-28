/**
 * @param {character[][]} board
 * @return {boolean}
 */
var checkSet = function(can) {
    const nums = ['1','2','3','4','5',
                    '6','7','8','9','.'];
    for (let i = 0; i < can.length; i++) {
        if (!nums.includes(can[i])) {
            return false;
        }
    }

    let strippedCan  = can.filter(function(value) {
        return value !== '.';
    });

    let set = new Set(strippedCan);

    if (set.size !== strippedCan.length) {
        return false;
    }

    return true;    
}

var isValidSudoku = function(board) {
    // Check rows
    for (let row = 0; row < board.length; row++) {
        if (!checkSet(board[row])) {
            console.log(board[row]);
            console.log('rows');
            return false;
        }
    }

    // Check columns
    for (let column = 0; column < board.length; column++) {
        let candidate = [board[0][column], board[1][column], board[2][column],
                         board[3][column], board[4][column], board[5][column],
                         board[6][column], board[7][column], board[8][column]];
        
        if (!checkSet(candidate)) {
            console.log('cols');
            return false;
        }
    }

    // Check squares
    for (let x = 0; x < 7; x += 3) {
        for (let y = 0; y < 7; y += 3) {
                    let candidate = [board[x][y], board[x + 1][y], board[x + 2][y],
                         board[x][y + 1], board[x + 1][y + 1], board[x + 2][y + 1],
                         board[x][y + 2], board[x + 1][y + 2], board[x + 2][y + 2]];
        
            if (!checkSet(candidate)) {
                console.log('squares');
                return false;
            }
        }
    }

    return true;
};

// true
console.log(isValidSudoku(
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
));
// false
console.log(isValidSudoku(
    [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
));