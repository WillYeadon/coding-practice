from LinkedList import Node, LinkedList

def sumList(list1, list2):
    l1_total = 0
    l2_total = 0
    tens = [10**i for i in range(10)]
    
    i = 0
    current = list1.head
    while (current):
        l1_total += current.data * tens[i]
        i += 1
        current = current.next

    i = 0
    current = list2.head
    while (current):
        l2_total += current.data * tens[i]
        i += 1
        current = current.next
    
    return l1_total + l2_total

ll1 = LinkedList()
ll2 = LinkedList()

data1 = [7,1,6]
data2 = [5,9,2]

for i in data1:
    ll1.append(Node(i))

for j in data2:
    ll2.append(Node(j))

ll1.printElements()
ll2.printElements()

print(sumList(ll1, ll2))