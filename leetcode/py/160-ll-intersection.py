from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        left, right = [], []
        while (headA):
            left.append(headA)
            headA = headA.next
        while (headB):
            right.append(headB)
            headB = headB.next
        for i in left:
            if i in right:
                return i
        return
        