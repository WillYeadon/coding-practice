/**
 * @param {number[][]} points
 * @return {number}
 */

function returnArea(p1, p2, p3) {
    // it actually doesn't matter what order p1, 2, 3 are in as
    // area uneffected by rotation
    // Use Heron's formula

    const a = Math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2);
    const b = Math.sqrt((p1[0] - p3[0])**2 + (p1[1] - p3[1])**2);
    const c = Math.sqrt((p2[0] - p3[0])**2 + (p2[1] - p3[1])**2);
    const s = 0.5 * (a + b + c);

    return Math.sqrt(s*(s - a)*(s - b)*(s - c));
}

var largestTriangleArea = function(points) {
    let maxArea = 0;
    let candidate = 0;

    for (let i = 0; i < points.length - 2; i++) {
        for (let j = i; j < points.length - 1; j++) {
            for (let k = j; k < points.length; k++) {
                candidate = returnArea(points[i], points[j], points[k]);
                if (candidate > maxArea) {
                    maxArea = candidate;
                }
            }
        }
    }

    return maxArea;
};

var largestTriangleAreaNested = function(points) {
    let summed = points.map(sublist => sublist.reduce((a, b) => a + b));
    const maxIndex = summed.indexOf(Math.max(...summed));
    const minIndex = summed.indexOf(Math.min(...summed));

    const p1 = points[maxIndex];
    const p2 = points[minIndex];
    let maxArea = 0;
    let candidate = 0;

    for (let i = 0; i < points.length; i++) {
        if ((i === maxIndex) || (i === minIndex)) {
            continue;
        }
        else {
            candidate = returnArea(p1, p2, points[i]);
            if (candidate > maxArea) {
                maxArea = candidate;
            }
        }
    } 

    return maxArea;
};

// 2.00000
console.log(largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]));
// 0.50000
console.log(largestTriangleArea([[1,0],[0,0],[0,1]]));