/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    //const halfLeng = Math.floor(nums.length, 2);
    let uniques = new Map();

    for (let i of nums) {
    if (!uniques.has(i)) {
        uniques.set(i, 1);
    } else {
        uniques.set(i, uniques.get(i) + 1);
    }
    }
    let maxCount = 0;
    let maxElement = null;

    for (let [key, count] of uniques.entries()) {
    if (count > maxCount) {
        maxCount = count;
        maxElement = key;
    }
    }
    return maxElement;
};