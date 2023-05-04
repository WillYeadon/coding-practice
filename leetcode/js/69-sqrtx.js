/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    if (x === 0) {return 0;}
    if (x < 4) {return 1;}

    let starting = 0;
    let candidate = (starting) * (starting);

    while (candidate <= x) {
        if (candidate <= x) {
            starting += 1;
            candidate = (starting) * (starting);
        }
    } 

    return starting - 1;
};

// 2
console.log(mySqrt(4));
// 2
console.log(mySqrt(8));
