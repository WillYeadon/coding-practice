from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linked_list(lst):
    if not lst:
        return None
    
    head = ListNode(lst[0])
    current = head
    
    for i in range(1, len(lst)):
        new_node = ListNode(lst[i])
        current.next = new_node
        current = new_node
        
    return head

def linked_list_to_list(head):
    # Initialize an empty list to store the values
    result = []

    # Traverse the linked list and append each value to the list
    current = head
    while current:
        result.append(current.val)
        current = current.next

    return result

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        vals = []

        while current:
            vals.append(current.val)
            current = current.next

        if len(vals) > 0:
            newHead = ListNode(vals[-1])
        else:
            newHead = None

        current = newHead
        for i in range(len(vals) - 1, 0, -1):
#            print(vals[i - 1])
            current.next = ListNode(vals[i - 1])
            current = current.next

        return newHead
    
x = Solution()
y = x.reverseList(list_to_linked_list([0,1,4,-2]))
z = linked_list_to_list(y)
print(z)     