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
        
        if (current.value == del_node):
            self.head = current.next
        else:
            while (current.next):
                if (current.next.value == del_node):
                    current.next = current.next.next
                    break
                else:
                    current.next = current.next
                    
    def printElements(self):
        current = self.head
        
        if (self.head):
            print(current.data)
            while (current.next):
                current = current.next
                print(current.data)
        else:
            print("List empty?")

                    
            
        