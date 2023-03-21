/**
 * Definition for singly-linked list.
**/
function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

a = new ListNode(1, new ListNode(2, new ListNode(2, new ListNode(1))));
b = new ListNode(1, new ListNode(2));
c = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(2, new ListNode(1)))));

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    let current = head;
    let length = 0;

    while (current != null) {
        length += 1;
        current = current.next;
    }

    half = Math.floor(length / 2);
    odd = false
    if (length % 2 === 1) {
        odd = true
    }

    ans1 = []
    ans2 = []

    let secondCurrent = head;
    secondLength = 0;
    while (secondCurrent != null) {
        if (secondLength < half) {
            ans1.push(secondCurrent.val);
        }
        else {
            ans2.push(secondCurrent.val);
        }

        secondLength += 1;
        secondCurrent = secondCurrent.next;
    }

    if (odd) {
        ans2.shift()
    }

    while (ans1.length > 0) {
        if (ans1.pop() != ans2.shift()) {
            return false
        }
    }

    return true;
};

var isPalindromeSlowFast = function(head) {
    if (!head || !head.next) {
        return true;
    }
    
    let slow = head;
    let fast = head;
    
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }
    
    let prev = null;
    let curr = slow;
    
    while (curr) {
        let nextNode = curr.next;
        curr.next = prev;
        prev = curr;
        curr = nextNode;
    }
    
    let firstHalf = head;
    let secondHalf = prev;
    
    while (secondHalf) {
        if (firstHalf.val !== secondHalf.val) {
            return false;
        }
        firstHalf = firstHalf.next;
        secondHalf = secondHalf.next;
    }
    
    return true;
};

console.log(isPalindrome(a));
console.log(isPalindrome(b));
console.log(isPalindrome(c));

console.log(isPalindromeSlowFast(a));
console.log(isPalindromeSlowFast(b));
console.log(isPalindromeSlowFast(c));