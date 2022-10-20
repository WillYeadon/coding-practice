from LinkedList import Node, LinkedList

ll = LinkedList()

#data = [1,2,3,4,5,6,7,8,9]
data = [9,8,7,6,5,4,3,2,1]
for i in data:
    ll.append(Node(i))

#ll.printElements()

print(ll.kthToLast(4))
#ll.delete(5)

#ll.printElements()