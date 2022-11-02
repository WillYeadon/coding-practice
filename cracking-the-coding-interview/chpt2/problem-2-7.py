from LinkedList import Node, LinkedList

def intersection(list1, list2):        
    l1, l2 = list1.head, list2.head  
    while l1 != l2:
        l1 = l1.next if l1 else list2.head
        l2 = l2.next if l2 else list1.head
        
    return l1

ll1 = LinkedList()
ll2 = LinkedList()

#
data1 = [7,1,6,1]
data2 = [5,9,2]

for i in data1:
    ll1.append(Node(i))

for j in data2:
    ll2.append(Node(j))

x = Node('a')

ll1.append(x)
ll2.append(x)

for i in data1:
    ll1.append(Node(i))

for j in data2:
    ll2.append(Node(j))

ll1.printElements()
ll2.printElements()

print(intersection(ll1, ll2))