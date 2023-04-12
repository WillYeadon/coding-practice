Array.prototype.last = function() {
    length = this.length;
 
    if (length === 0) {return -1;}
    else {return this[length - 1];}
 };
const arr1 = [1, 2, 3];
console.log(arr1.last()); // 3
const arr2 = [];
console.log(arr2.last());