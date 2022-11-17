from LinkedList import Node, LinkedList

# Finds intersections, here intersections are where
# two LL contain the same node.

def intersection(list1, list2):
    # get starting nodes-        
    l1, l2 = list1.head, list2.head
    # the length here is irrelevant as once
    # they intersect every node must then match
    # 
    # check not same node
    while l1 != l2:
        # if l1 not none then increment l1
        # want to loop around at end onto other list
        l1 = l1.next if l1 else list2.head
        # if l2 not none then increment l2
        # want to loop around at end onto other list
        l2 = l2.next if l2 else list1.head
        # Here have length 9 and 5 so will intersect
        # at 14. E.g. p1 goes 0 -> 5 (1) whilst p2
        # goes 0 -> 5 (2). p1 now goes 5 -> 9 (1) 
        # whilst p2 goes 0 -> 4 (1). p1 then goes
        # 0 -> 5 (2) whilst p2 goes 4 -> 9 (1) hence
        # they intersect
        #
        # (Go through this on paper if revising)

        
    return l1

ll1 = LinkedList()
ll2 = LinkedList()

# length 6
data1 = [7,1,6,1,3,4]
# length 2
data2 = [5,9]

# different lengths no zip
for i in data1:
    ll1.append(Node(i))

for j in data2:
    ll2.append(Node(j))

x = Node('a')

# length 7
ll1.append(x)
# length 3
ll2.append(x)

for i in data2:
    ll1.append(Node(i))
    # Note this appends them both as
    # same ll now!! No need for
    # ll2.append(Node(i))

# length 9
ll1.printElements()
# length 5
ll2.printElements()

print(intersection(ll1, ll2))