from LinkedList import Node, LinkedList

ll = LinkedList()

data = [9,8,7,6,5,4,3,2,1]
for i in data:
    ll.append(Node(i))

#ll.printElements()

new = ll.partition(5)

new.printElements()