from LinkedList import Node, LinkedList


def loopNode(list1):
    nodes = {}
    loop = False
    l1 = list1.head
    
    while l1 and not loop:
        if l1 in nodes:
            nodes[l1] += 1
        else:
            nodes[l1] = 1
        
        if nodes[l1] > 1:
            loop = True
        l1 = l1.next

    return loop

ll1 = LinkedList()

data1 = [1,2,3]
data2 = [4,5,6]

for i in data1:
    ll1.append(Node(i))

x = Node('a')
ll1.append(x)

for i in data2:
    ll1.append(Node(i))

ll1.append(x)

print(loopNode(ll1))