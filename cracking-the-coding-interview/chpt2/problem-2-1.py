from LinkedList import Node, LinkedList

ll = LinkedList()

data = [1,2,3,4,1,2,3,4,5,5,5]
for i in data:
    ll.append(Node(i))

#ll.printElements()

ll.delDup()
#ll.delete(5)

ll.printElements()