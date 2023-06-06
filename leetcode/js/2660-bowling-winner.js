/**
 * @param {number[]} player1
 * @param {number[]} player2
 * @return {number}
 */

function scorePlayer(scores) {
    let score = 0;
    let count = 0;
    for (let i = 0; i < scores.length; i++) {
        if (count > 0) {
            score += 2 * scores[i];
            count -= 1;
        }
        else {
            score += scores[i];
        }
        
        if (scores[i] === 10) {
            count = 2;
        }

    }
    
    return score;
}

var isWinner = function(player1, player2) {
    const p1 = scorePlayer(player1);
    const p2 = scorePlayer(player2);
    console.log(p1,p2);
    if (p1 > p2) {
        return 1;
    }
    else if (p1 < p2) {
        return 2;
    }
    return 0;
};