# Verbose solution. Dummy points to the origional ll even if prev moves
# Utilize a dummy node to maintain a reference to the original list's head, 
# create a new sublist for in-place reversal, and then reconnect this 
# reversed sublist with the original list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # Edge case: if the list is empty or there's no need to reverse, return the head
        if not head or left == right:
            return head

        # Dummy node to handle edge cases, especially when reversing starts at the head
        dummy = ListNode(0)
        dummy.next = head

        # 'prev' will eventually point to the node just before the reversal starts
        prev = dummy

        # Move 'prev' to one node before the start of the reversal
        for _ in range(left - 1):
            prev = prev.next

        # 'current' will point to the first node to be reversed
        current = prev.next

        # Start reversing the nodes
        reverse = None
        for _ in range(right - left + 1):
            next_temp = current.next  # Store the next node
            current.next = reverse     # Reverse the link
            reverse = current          # Move 'reverse' forward
            current = next_temp        # Move 'current' forward

        # Connect the end of the reversed part to the remaining list
        prev.next.next = current

        # Connect the start of the reversed part to the initial list
        prev.next = reverse

        # Return the new head of the list
        return dummy.next

# Helper function to create a linked list from a list of values
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

# Example usage
solution = Solution()

# Example 1: Reversing from 2 to 4 in the list [1,2,3,4,5]
list1 = create_linked_list([1, 2, 3, 4, 5])
print("Original List 1:")
print_linked_list(list1)
result1 = solution.reverseBetween(list1, 2, 4)
print("Reversed List 1 (2 to 4):")
print_linked_list(result1)

# Example 2: Reversing the entire list [1,2,3,4]
list2 = create_linked_list([1, 2, 3, 4])
print("Original List 2:")
print_linked_list(list2)
result2 = solution.reverseBetween(list2, 1, 4)
print("Reversed List 2 (1 to 4):")
print_linked_list(result2)
