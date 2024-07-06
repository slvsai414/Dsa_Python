class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.back =None
    
class DoubllyLinkeList:
    def __init__(self):
        self.head=None
        self.tail= None
    
    def add_starting(self,data):
        new_node = Node(data)
        if self.head == None and self.tail == None:
            self.head  = new_node
            self.tail = new_node
            return new_node
        
        new_node.next = self.head
        self.head.back = new_node
        new_node.back = None
        self.head= new_node



    def add_end(self,data):
        new_node = Node(data)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            return
        
        self.tail.next = new_node
        new_node.back =  self.tail
        self.tail = new_node

    def delete_node_starting(self):
        if self.head is None and self.tail is None:
            print('Nothing to delete at the starting of Doublly LinkedList')
            return
        temp=self.head.next
        self.head.next=None
        temp.back = None
        self.head = temp

    def delete_node_ending(self):
        if self.head is None and self.tail is None:
            print('Nothing to delete at the ending of Doublly LinkedList')
            return
        temp=self.tail
        self.tail = temp.back
        self.tail.next =None
        temp.back = None





    def print_dll(self):
        if self.head is None and self.tail is None:
            print('Doubly LinkedList is Empty')
            return
        temp = self.head

        while temp is not None:
            print(temp.data,end="<-->")
            temp = temp.next
        print()






dl1=DoubllyLinkeList()

dl2= DoubllyLinkeList()

dl1.print_dll()
dl2.print_dll()



for i in range(10,21):
    dl1.add_starting(i)

dl1.print_dll()


for i in range(100,111):
    dl2.add_end(i)

dl2.print_dll()

dl1.delete_node_starting()

dl1.print_dll()


dl2.delete_node_ending()
dl2.print_dll()