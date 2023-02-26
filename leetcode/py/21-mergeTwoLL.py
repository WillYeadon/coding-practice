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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        ans = ListNode(0)

        head1 = list1
        head2 = list2

        currentA = head1
        currentB = head2
        currentC = ans

        while (currentA is not None) or (currentB is not None):
            if currentA is None:
                if currentB is not None:
                    currentC.next = currentB 
                    currentC = currentC.next    
                    currentB = currentB.next
            elif currentB is None:
                if currentA is not None:
                    currentC.next = currentA 
                    currentC = currentC.next    
                    currentA = currentA.next
            else:
                if currentA.val < currentB.val:
                    currentC.next = currentA 
                    currentC = currentC.next
                    if currentA: 
                        currentA = currentA.next
                else:
                    currentC.next = currentB 
                    currentC = currentC.next
                    if currentB: 
                        currentB = currentB.next

        ans = ans.next
        return ans
    
x = Solution()
y = x.mergeTwoLists(list_to_linked_list([1,2,4]), 
                      list_to_linked_list([1,3,4]))
z = linked_list_to_list(y)
print(z)