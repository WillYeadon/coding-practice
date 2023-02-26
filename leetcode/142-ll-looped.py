from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashMap = {}
        current = head

        while current:
            if current not in hashMap:
                hashMap[current] = True
            else:
                return current

            current = current.next
        
        return None