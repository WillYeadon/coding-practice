from LinkedList import Node, LinkedList

def palinHelp(data):
    
    for i,j in zip(range(0,len(data)//2, 1),\
                   range(len(data)-1,len(data)//2 -1, -1)):
        if data[i] != data[j]:
            return False
    return True  

words = ['hannah','racecar','palindrome']

for word in words:
    ll = LinkedList()
    
    for i in word:
        ll.append(Node(i))
    
    ll.printElements()
    print(palinHelp(ll.listIfy()))
