/**
 * @param {string} s
 * @return {number}
 */
// Just an object
var convert = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000,
}

function parseTwo(s) {
    return [convert[s.charAt(0)], convert[s.charAt(1)]]
}

var romanToInt = function(s) {
    running = 0
    length = s.length
    if (length == 1) {
        return convert[s]
    }

    for (let i = 1; i < length + 1; i++) {
        sub = parseTwo(s.substring(i - 1, i + 1))

        if (!sub[1]) {
            sub[1] = 0;
        }

        if (sub[0] > sub[1]) {
            running += sub[0];
        }
        else if (sub[0] == sub[1]) {
            running += (sub[0] + sub[1]);
            i += 1;
        }
        else {
            running += (sub[1] - sub[0]);
            i += 1;
        }
    }

    return running
};

// New map, I think this is faster than just a 
// regular object
let values = new Map()

// set keys and values of map
values.set("M", 1000)
values.set("D", 500)
values.set("C", 100)
values.set("L", 50)
values.set("X", 10)
values.set("V", 5)
values.set("I", 1)

var romanToIntFast = function(s) {
    let sum = 0
    let i = 0
        
    while (i < s.length) {
        // current symbol
        let currentSymbol = s.charAt(i)
        
        // value of that symbol
        let currentValue = values.get(currentSymbol)
        
        // hold / hypothetical next value
        let nextValue = 0
        
        // If not at the end of the string update nextValue
        if (i + 1 < s.length) {
            let nextSymbol = s.charAt(i + 1)
            nextValue = values.get(nextSymbol)
        }
        
        // If special value like IV or CM 
        // add and advance two
        if (currentValue < nextValue) {
            sum += (nextValue - currentValue);
            i += 2;
        // Else just add as normal.
        } else {
            sum += currentValue;
            i += 1;
        }
    }
    
    return sum
};

console.log(romanToInt('III')); // 3
console.log(romanToInt('LVIII')); // 58 
console.log(romanToInt('MCMXCIV')); // 1994

// Lot faster than mine but does essentially the same thing?
// Maybe using map rather than a regular object?
console.log(romanToIntFast('III')); // 3
console.log(romanToIntFast('LVIII')); // 58 
console.log(romanToIntFast('MCMXCIV')); // 1994