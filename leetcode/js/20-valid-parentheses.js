/**
 * @param {string} s
 * @return {boolean}
 */

// Could probs have used some kind of hash map here
function checkClosed(o, c) {
    switch (o) {
        case '(':
            return (c == ')') ? true : false; 
        case '{':
            return (c == '}') ? true : false;
        case '[':
            return (c == ']') ? true : false;
        default:
            return false;
    }
}

var isValid = function(s) {  
    const closed = [')','}',']'];
    const stack = [];

    for (let i = 0; i < s.length; i++) {
        let candidate = s[i]

        if (closed.includes(candidate)) {
            if (stack.length === 0) {return false;}
            if (!checkClosed(stack.pop(), candidate)) {return false;}
        }
        else {
            stack.push(s[i])
        }
    }

    if (stack.length > 0) {return false;}

    return true;
};

// true
console.log(isValid("()"));
// true
console.log(isValid("()[]{}"));
// false
console.log(isValid("(]"));