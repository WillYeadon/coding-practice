function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let n1 = '';
    let n2 = '';

    while (l1) {
        n1 = l1.val + n1;
        l1 = l1.next;
    }
    while (l2) {
        n2 = l2.val + n2;
        l2 = l2.next;
    }

    const sum = BigInt(n1) + BigInt(n2);
    const digits = sum.toString().split('').map(Number);   
    const ans = new ListNode(digits.pop());
    let current = ans;

    while (digits.length > 0) {
        current.next = new ListNode(digits.pop());
        current = current.next;
    }

    return ans
};

console.log(addTwoNumbers(new ListNode(2, new ListNode(4, new ListNode(3))),
        new ListNode(5, new ListNode(6, new ListNode(4)))));
console.log(addTwoNumbers(new ListNode(0), new ListNode(0)));