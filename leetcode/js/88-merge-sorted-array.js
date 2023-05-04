/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */

function createArrayOfZeros(n) {
    return new Array(n).fill(0);
}

var merge = function(nums1, m, nums2, n) {
    const total = m + n;
    let hold = createArrayOfZeros(m + n);
    let one = 0;
    let two = 0;

    for (let i = 0; i < total; i++) {
        if ((one < m) && (two < n)) {
            if (nums1[one] <= nums2[two]) {
                hold[i] = nums1[one];
                one += 1;
            }
            else {
                hold[i] = nums2[two];
                two += 1;
            }
        }
        else {
            if ((m - one) < (n - two)) {
                hold[i] = nums2[two];
                two += 1;
            }
            else {
                hold[i] = nums1[one];
                one += 1;                
            }
        }
    }

    for (let i = 0; i < total; i++) {
        nums1[i] = hold[i];
    }
};

let nums1 = new Array(1,2,3,0,0,0);
merge(nums1, 3, [2,5,6], 3);
// [1,2,2,3,5,6]
console.log(nums1);