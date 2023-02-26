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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        current = head
        shifts = length // 2
        
        while shifts > 0:
            current = current.next
            shifts -= 1

        return current
    
x = Solution()
y = x.middleNode(list_to_linked_list([1,2,3,4,5,6]))
z = linked_list_to_list(y)
print(z) 