# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        if not head:
            return None
        
        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next       
        nodes.sort(key=lambda node: node.val)
        
        head = nodes[0]
        current = head
        for node in nodes[1:]:
            current.next = node
            current = current.next
        current.next = None  
        return head