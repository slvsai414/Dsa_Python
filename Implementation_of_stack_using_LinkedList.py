class Node:
    def __init__(self,data):
        self.data=  data
        self.next = None

class Stack:
    def __init__(self):
        print('Oject is created.')
        self.top=None


    def push_into_stack(self,data):
        print(data,"is pushed")
        new_ele=Node(data)
        if self.top == None:
            self.top=new_ele
            return
        new_ele.next=self.top
        self.top=new_ele
        


    def pop_from_stack(self):

        if self.top is None:
            print('Nothing to pop form stack.')
            return 
        print(self.top.data,'is deleted form stack')
        temp=self.top.next
        self.top.next=None
        self.top =temp


    def print_Stack(self):
        if self.top is None:
            print('Stack is empty.')
            return
        temp=self.top
        while temp is not None:
            print(temp.data, end='-->')
            temp=temp.next
        print()


#Creation of the object
s1=Stack()
s2=Stack()

#print of the Stacks
s1.print_Stack()

#pop from the stack
s1.pop_from_stack()


#push into stack for the object1
for i in range(1,11):
    s1.push_into_stack(i)
#print object of s1
s1.print_Stack()



#push into stack for object2
for j in range(100,111):
    s2.push_into_stack(j)
# print objects at the s2
s2.print_Stack()

#pop from stack s1 object
s1.pop_from_stack()
s1.print_Stack


#pop from the stack s2 object
s2.pop_from_stack
s2.print_Stack