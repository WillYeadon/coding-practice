/**
 * @param {number} n
 * @return {boolean}
 */
var happyHelper = function(n) {
    seen = [];
    flag = false;
    while (n != 1) {
        if (seen.includes(n)) {
            flag = true
            n = 1;
        };
        seen.push(n);
        s = String(n).split('');
        newNum = 0;
        for (let i = 0; i < s.length; i++) {
            newNum += Number(s[i])**2;
        }
        n = newNum;
    }

    return (flag ? false : true);
}

var isHappy = function(n) {
    if (n == 1) {return true} 
    if (n < 7) {return false}          
    
    return happyHelper(n);
};

console.log(isHappy(2));
console.log(isHappy(7));
console.log(isHappy(8));
console.log(isHappy(19));