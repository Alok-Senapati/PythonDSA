class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def add(self, data):
        new_node = Node(data)
        if(self.size == 0):
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        
    def search(self, data):
        temp = self.head
        while temp is not None:
            if(temp.data == data):
                return temp
            temp = temp.next
        return None
    
    def insert(self, data, data_before):
        before_node = self.search(data_before)
        if(before_node):
            new_node = Node(data)
            new_node.next = before_node.next
            before_node.next = new_node
            self.size += 1
        
    def __str__(self):
        output = ""
        temp = self.head
        while(temp is not None):
            output += str(temp.data) + " >> "
            temp = temp.next
        output += 'None'
        return output
    
ll = LinkedList()
print(ll)
ll.add(5)
print(ll)
ll.add(2)
ll.add(4)
ll.add(1)
ll.add(3)
print(ll)
ll.insert(10,2)
print(ll)
print(ll.size)