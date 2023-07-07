/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // Use a hashmap!!!
    let hashMap = new Map();
    let ans = [];
    
    nums.forEach((item, index) => {
        if (hashMap.has(target - item)) {
            ans = [hashMap.get(target - item), index];
        }
        // elsewise set the map value to the index
        // for the key of item
        hashMap.set(item, index);
    })

    return ans;
};