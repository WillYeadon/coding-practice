/**
 * @param {number[]} height
 * @return {number}
 */
var checkArea = function(x1, x2, y1, y2) {
    return (x2 - x1) * Math.min(y2, y1);
}

/*
So the brute for is O(n^2). However there is also this O(n) 
option which utilizes how when starting at the edge, the only
way to increase area is for there to be a larger height on
one of the edges of the box. Given the area is determined by the
width * smallest height you move in the smallest pointer 
(out of left and right) in the hopes of increaseing the smallest
height by greater than 1 (the loss of width).
*/

var maxArea = function(height) {
    let left = 0;
    let right = height.length - 1;

    let currentMax = checkArea(left, right, height[left], height[right]);
    let candidate = currentMax;

    while (left < right) {
        candidate = checkArea(left, right, height[left], height[right]);
        currentMax = Math.max(currentMax, candidate);
    
        if (height[left] < height[right]) {
            left += 1;
        }
        else {
            right -= 1;
        }
    }

    return currentMax;
};

var maxAreaNested = function(height) {
    let currentMax = 0;
    let candidate = 0;

    for (let start = 0; start < height.length - 1; start++) {
        for (let end = start + 1; end < height.length; end++) {
            //console.log(start, end, height[start], height[end])
            candidate = checkArea(start, end, 
                                    height[start], height[end]);
            if (candidate > currentMax) {currentMax = candidate;}
        }
    }

    return currentMax;
};

// 49
console.log(maxArea([1,8,6,2,5,4,8,3,7]));
// 1
console.log(maxArea([1,1])); 