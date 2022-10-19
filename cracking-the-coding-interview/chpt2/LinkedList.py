class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList():
    def __init__(self, head = None):
        self.head = head
        
    def append(self, new_node):
        current = self.head
        
        if (self.head):
            while (current.next):
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
            
    def delete(self, del_node):
        current = self.head
        
        if (current is not None):
            if (current.data == del_node):
                self.head = current.next
                current = None
                return

        while (current is not None):
            if (current.data == del_node):
                break
            previous = current
            current = current.next
        
        if (current == None):
            return
        
        previous.next = current.next
        current = None
 
    def printElements(self):
        current = self.head
        
        if (self.head):
            print(current.data)
            while (current.next):
                current = current.next
                print(current.data)
        else:
            print("List empty?")
            
    def delDup(self):
        hash1 = {}
        current = self.head

        while (current.next):
            if current.data in hash1:
                self.delete(current.data)
            else:
                hash1[current.data] = 1

            current = current.next

        if not current.next:
            self.delete(current.data)
                    
            
        