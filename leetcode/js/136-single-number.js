/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let dict = {};
    for (let i of nums) {
        console.log(i)
        if (!(i in dict)) {
            dict[i] = 1;
        }
        else {
            dict[i] += 1;
        }
    }
    for (let key in dict) {
        if (dict[key] === 1) {
            return key
        }
    }
    return 0;
};