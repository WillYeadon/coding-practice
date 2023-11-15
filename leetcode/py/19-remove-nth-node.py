from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end = head
        nodes = [end]
        while end.next:
            end = end.next
            nodes.append(end)

        nodes.pop(len(nodes) - n)
        if not nodes:
            return None
        start = nodes.pop(0)
        ans = start
        while nodes:
            start.next = nodes.pop(0)
            start = start.next
        start.next = None
        
        return ans
        