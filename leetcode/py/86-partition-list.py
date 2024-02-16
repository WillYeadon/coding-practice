class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def returnNewLL(self, values):
        start = values.pop(0)
        runner = start
        while len(values) > 0:
            runner.next = values.pop(0)
            runner = runner.next
        return start


    def partition(self, head, x):
        if not head:
            return
        start = head
        lefts = []
        rights = []
        while start:
            if start.val < x:
                lefts.append(ListNode(start.val))
            else:
                rights.append(ListNode(start.val))
            start = start.next
        if len(lefts) < 1:
            return self.returnNewLL(rights)
        if len(rights) < 1:
            return self.returnNewLL(lefts)
        leftLL = self.returnNewLL(lefts)
        rightLL = self.returnNewLL(rights)
        ans = leftLL
        while leftLL.next:
            leftLL = leftLL.next
        leftLL.next = rightLL
        return ans 