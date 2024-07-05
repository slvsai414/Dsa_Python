class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        print("object as been created")
        self.head=None
        self.tail=None

    def add_begin(self,data):
        print(data,'Is adding at the Begining LinkedList')
        new_node=Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            return
        
        new_node.next= self.head
        self.head = new_node

    def add_end(self,data):
        print(data,'Is added at the end of LinkedList')
        new_node=Node(data)
        if self.tail is None and self.head is None:
            self.tail = self.head = new_node
            return 
        self.tail.next = new_node
        self.tail = new_node


    def print_linkedList(self):
        if self.head is None:
            print('LinkedList is Empty')
            return
        temp = self.head
        while temp is not None:
            print(temp.data,end='-->')
            temp=temp.next
        print()


ll1=LinkedList()
ll2=LinkedList()

ll1.print_linkedList()
ll2.print_linkedList()

for i in range(1,11):
    ll1.add_begin(i)
ll1.print_linkedList()

for j in range(100,111):
    ll2.add_end(j)
ll2.print_linkedList()
