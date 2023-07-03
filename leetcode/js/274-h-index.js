/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    citations.sort((a, b) => a - b);
        
    let i = 0;
    let h = citations[i];

    while (i < citations.length - 1 && h < citations.slice(i + 1).length) {
        i += 1;
        h = citations[i];
    }

    return Math.min(h, citations.length - i);
};

var hIndexSuccinct = function(citations) {
    citations.sort((a,b)=> b-a)
    let h = 0;
    while (citations[h]>h) {
        h++;
    }

    return h;
};