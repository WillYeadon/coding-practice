/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var findBall = function(grid) {
    let balls = grid[0].length;
    let rows = grid.length;
    let output = Array(balls).fill(-1);

    for (ball = 0; ball < balls; ball++) {
        // Pick a starting ball
        let bounced = ball;
        let exit = true;

        for (row = 0; row < rows; row++) {
            let flag = 'hold';
            // Bounce left or right
            if (grid[row][bounced] == 1) {
                bounced += 1;
                flag = 'right'
            }
            else {
                bounced -= 1;
                flag = 'left'
            }

            // If hit wall break (-1 is default anyway)
            if ((bounced < 0) || (bounced >= balls)) {
                exit = false;
                break;
            }
            // Check for v 
            if ((grid[row][bounced] == 1 && flag == 'left') || 
                (grid[row][bounced] == -1 && flag == 'right')) {
                exit = false;
                break;
            }
        }
        if (exit) {
            output[ball] = bounced;
        }
    }

    return output;
};

/**
 * @param {number[][]} grid
 * @return {number[]}
 */
function findBallFast(grid) {
    const rows = grid.length;
    const cols = grid[0].length;
    const ans = [];

    for (let i = 0; i < cols; i++) {
        let c = i;

        for (let r = 0; r < rows; r++) {
            if (grid[r][c] === 1) {
                if (c === cols - 1 || grid[r][c + 1] === -1) {
                    c = -1;
                    break;
                }
                c++;
            } else {
                if (c === 0 || grid[r][c - 1] === 1) {
                    c = -1;
                    break;
                }
                c--;
            }
        }

        ans.push(c);
    }

    return ans;
}

// [1,-1,-1,-1,-1]
console.log(findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]));
//[-1]
console.log(findBall([[-1]]));
// [0,1,2,3,4,-1]
console.log(findBall([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]));

// [1,-1,-1,-1,-1]
console.log(findBallFast([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]));
//[-1]
console.log(findBallFast([[-1]]));
// [0,1,2,3,4,-1]
console.log(findBallFast([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]));
