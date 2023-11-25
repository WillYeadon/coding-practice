class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head:
            return
        newList = Node(head.val, head.next, head.random)
        startNew = newList
        startOld = head

        while head.next:
            newList.next = Node(head.next.val)
            head = head.next
            newList = newList.next
        head = startOld
        newList = startNew
        while head:
            random = head.random
            if random:
                subStartOld = startOld
                count = 0
                while subStartOld.next:
                    if subStartOld == random:
                        break
                    subStartOld = subStartOld.next
                    count += 1
                subStartNew = startNew   
                while count > 0:
                    subStartNew = subStartNew.next
                    count -= 1
                newList.random = subStartNew
            head = head.next
            newList = newList.next

        return startNew