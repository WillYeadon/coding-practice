/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    let count = 0;
    for (let a of args) {
        count += 1;
    }
    return count;
};

argumentsLength(1, 2, 3); // 3
