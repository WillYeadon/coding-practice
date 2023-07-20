class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def getNum(self, l):
        ans = []
        while (l):
            ans.append(str(l.val))
            l = l.next
        return int(''.join(ans)[::-1])

    def addTwoNumbers(self, l1, l2):
        ans = list(str(self.getNum(l1) + self.getNum(l2)))
        head = ListNode(val = int(ans.pop()))
        node = head
        while (len(ans) > 0):
            node.next = ListNode(val = int(ans.pop()))
            node = node.next
        return head