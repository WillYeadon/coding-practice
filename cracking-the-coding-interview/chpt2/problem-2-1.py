from LinkedList import Node, LinkedList

def newMethod():
    print("New method")

ll = LinkedList()
setattr(ll, "newMethod", newMethod)

data = [1,2,3,4,1,2,3,4,5]
for i in data:
    ll.append(Node(i))

ll.printElements()
ll.newMethod()