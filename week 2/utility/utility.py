#linked list
class _BagListNode(object):
    def __init__(self,item):
        self.item=item
        self.next=None


class _BagIterator:
    def __init__(self,listHead):
        self._curNode=listHead

    def __iter__(self):
        return self
    def __next__(self):
        if self._curNode is not None:
            raise StopIteration
        else:
            item = self._curNode.item
            self._curNode=self._curNode.next
            return self.item



class Bag:
    #construct an empty bag
    def __init__(self):
        self._head=None
        self._size=0
    
    def __len__(self):
        return self._size

    def __contains__(self,target):
        curNode=self._head
        while curNode is not None and curNode.item!=target:
            curNode=curNode.next
        return curNode is not None

    def __append__(self,item):
        newNode=_BagListNode(item)
        newNode.next=self._head
        self._head= newNode
        self._size += 1
    def remove(self,item):
        predNode=None
        curNode = self._head
        while curNode is not None and curNode.item!=item:
            predNode=curNode
            curNode=curNode.next
        
        assert curNode is not None
        self._size -= 1
        if curNode is self._head:
            self._head=curNode.next

        else:
            predNode.next=curNode.next
        

        return curNode.item
    def __display__(self):
        curnode=self._head
        while curnode is not None:
            print(curnode.item)
            curnode=curnode.next
    def __insert__(self,value,position):
        n=position
        curnode=self._head
        
        while curnode is not None and n!=0:
            prednode=curnode
            curnode=curnode.next
            n=n-1
        ins=_BagListNode(value)
        prednode.next=ins
        ins.next=curnode
        self._size+=1
        self.head=ins
    def __add__(self,value):
        if self.__contains__(value)==False:
            self.__append__(value)
    
    def __elements__(self):
        
        curnode=self._head
        while curnode is not None:
            yield curnode.item
            curnode=curnode.next

            
    
    
    
            

    def __iter__(self):
        return _BagIterator(self._head)


# ordered linked list
class Newnode:
    def __init__(self,item):
        self.item=item
        self.next=None
class sortedlist():
    def __init__(self):
        self.head=None
        self._size=0
    def __len__(self):
        return self._size
    def __add__(self,element):
        newobject=Newnode(element)
        newobject.next=self.head
        self.head=newobject
        self._size+=1
    
    def __ins__(self,item,position):
        n=position
        newobject=Newnode(item)
        currnode=self.head
        while currnode is not None and n!=0:
            pred=currnode
            currnode=currnode.next
            n-=1
        pred.next=newobject
        newobject.next=currnode
        self._size+=1
    def __display__(self):
        curnode=self.head
        while curnode is not None:
            print(curnode.item)
            curnode=curnode.next
    def comparing(self,item):
        currnode=self.head
        n=0
        while currnode is not None and currnode.item>item:
            currnode=currnode.next
            n=n+1
        return n
    def __sortlinkedlist__(self,item):
        t=self.comparing(item)
        if t==0:
            self.__add__(item)
        else:
            self.__ins__(item,t)         



'''this is the program to build a doubly linked list'''
# this class creates an object which is capable of holding refrences of 2 objects
class newobject:
    def __init__(self,data):
        self.pre = None
        self.next = None
        self.data = data

# this class creates the doubaly linked list by holding refrence of predecessor and successor node
class DoublyLinkedList:
#creating instance of object 
    def __init__(self):
        self.start=None
        self.end=None
        self.size=0
# this function returns the length of linked list
    def length(self):
        return self.size
#this function adds the object to left side    
    def add_front(self,data):
        while self.start is None and self.end is None:
            new=newobject(data)
            self.start=new
            self.end=new
            self.size+=1
            return
        while self.start is not None:
            new=newobject(data)
            new.pre=self.end
            self.end.next=new
            self.end=new
            self.size+=1
            return
#this function adds the object to right side 
    def add_rear(self,data):
        new=newobject(data)
        new.next=self.start
        self.start.pre=new
        self.start=new
        self.size += 1
#this function inserts in position value
    def insert(self,position,value):
        firstpointer=self.start
        assert position < self.size and position > 0
        n=0
        while n<position-1:
            n=n + 1
            firstpointer = firstpointer.next
        new = newobject(value)
        secondpointer = firstpointer.next
        secondpointer.pre = new
        new.next = secondpointer
        firstpointer.next = new
        new.pre = firstpointer
        self.size += 1
#this will remove the items from left size and will return the value
    def remove_left(self):
        if self.size==1:
            temp = self.start
            self.start = None
            self.end = None
            self.size -= 1
            return temp.data
           
        curr=self.start
        curr1=curr.next
        curr1.pre=None
        curr.next=None
        self.start=curr1
        self.size -= 1
        return curr.data
#this will remove the items from right size and will return the value
    def remove_right(self):
        if self.size==1:
            temp = self.start
            self.start = None
            self.end = None
            self.size -= 1
            return temp.data
        curr=self.end
        curr1=curr.pre
        curr1.next=None
        curr.pre=None
        self.end=curr1
        self.size -= 1
        return curr.data
#this will delete the in position value and will return the value
    def removeByPosition(self,position):
        n = 0
        assert position < self.size and position >0
        curr= self.start
        while n < position :
            n += 1
            curr=curr.next
        before = curr.pre
        after  = curr.next
        before.next = after
        after.pre   = before
        curr.next = None 
        curr.pre = None
        self.size -= 1
        return curr.data       
#this will display all the values in the linked list        
    def display(self):
        curr=self.start
        while curr is not None:
            print(curr.data)
            curr=curr.next
    def search(self,data):
        n=0
        curr=self.start
        while n < self.size:
            n +=1
            if curr.data == data:
                return (data,n)
            curr = curr.next
        return 'not found'
            
            
    
    
    

'''this is class that creates stack datastructure by using doubaly linked list'''
class Stack(DoublyLinkedList):
    def add(self,data):
        self.add_front(data)
    def pop(self):
        return self.remove_right()
    def Print(self):
        self.display()
    
        
'''this is a class that creates que data structure by using doubaly linked list'''
class Que(DoublyLinkedList):
    def enque(self,data):
        self.add_front(data)
    def dequeue(self):
        return self.remove_left()
    def Print(self):
        self.display()
'''this is a class that creates deque data structure by using doubly linked list'''

    
    



#que
class Que:
    def __init__(self):
        self.qlist=[]
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.qlist)
    def enque(self,item):
        self.qlist.append(item)
            
            
    def deque(self):
        assert not self.isEmpty()
        return self.qlist.pop(0)


#stacks data structure
class _StackNode:
    def __init__(self,item,link):
        self.item=item
        self.next=link
class Stack:
    def __init__(self):
        self._top=None
        self._size=0
    def isEmpty(self):
        return self._top is None
    def __len__(self):
        return self._size
    def peek(self):
        assert not self.isEmpty()
        return self._top.item
    def pop(self):
        assert not self.isEmpty()
        node=self._top
        self._top=self._top.next
        self._size-=1
        return node.item
    def push(self,item):
        self._top=_StackNode(item,self._top)
        self._size+=1
        

    
class Node:
    def __init__(self, data):  # data is initialized
        self.data = data
        self.next = None


# linked list class is made
class LinkedList:
    """
    linked list class is made with different attributes
    """

    def __init__(self):  # this in initialization
        self.head = None
        self.size=0

    def Add_To_Start(self, data):  # here data is added to start of the list
        """
        :param data: data is input what we can add to the list
        :return: linked list
        """
        new = Node(data)
        new.next = self.head
        self.head = new
        self.size+=1

    def Add(self, data):  # data is added to the linked list
        """
        :param data: data is input what we can add to the list
        :return: linked list
        """
        new = Node(data)
        curr = self.head
        if curr is None:  # if list is empty then we will add data to the start
            self.Add_To_Start(data)
        else:
            while curr.next is not None:  # while loop is used for the curr to curr.next
                curr = curr.next
            curr.next = new
            self.size+=1
    def Print(self):  # print is used for printing out the data in the linked list
        """
        :return:  prints out the data in linked list
        """
        curr = self.head
        while curr is not None:  # while loop is used printing data
            print(curr.data, end=" ")
            curr = curr.next

    def Remove(self, data):  # remove function is used for removing the data from the linked list
        """
        :param data: particular data is removed after user input
        :return: data is returned
        """
        global prev, newlink
        curr = self.head
        if curr.data == data:  # if data at the head then head wil be replaced with next node
            self.Delete_To_Start()
        elif curr is None:  # if head is none then below print statement
            print("no list found")
        else:
            newlink = None
            prev = None
            while curr.next is not None:  # while loop is used for checking next node and then replacing
                if curr.data == data:
                    newlink = curr.next
                    break
                else:
                    prev = curr
                    curr = curr.next
            prev.next = newlink  # new address is saved and replaced with prev address
        self.size-=1

    def Delete_To_Start(self):
        """
        :return:  will delete head nodes data
        """
        curr=self.head
        self.head = self.head.next  # delete function is used to replace data with the net node
        self.size-=1
        return self.head.data

    def Delete_At_End(self):
        """
        :return:  will delete last nodes data
        """
        curr = self.head
        if curr is None:  # if list is empty the below statement is printed
            print("list is empty")
        else:
            prev = None
            while curr.next is not None:  # while loop is used for the replacing the address of the node
                prev = curr
               
                curr = curr.next
            prev.next = None
            
        self.size-=1
        return curr.data

    def Add_At_Position(self, position, data):
        """
        :param position: position at which data user wants to delete
        :param data: data user wants to delete
        :return: data will be deleted
        """
        new = Node(data)
        curr = self.head
        if curr is None:  # if list is empty then below statement wll be printed
            self.Add_To_Start(data)
        else:
            for position in range(position - 1):  # for loop is used to check the address and replace the data
                curr = curr.next
            prev = curr.next
            curr.next = new
            new.next = prev
        self.size-=1

    def Delete_At_Position(self, position):
        """
        :param position: will delete the data at the position
        :return: de linked data
        """
        curr = self.head
        if curr is None:  # if list is empty then below statement will printed
            print("list is empty")
        else:
            for position in range(position - 1):  # for loop is used for checking the address and deleting the data
                curr = curr.next
            prev = curr.next.next
            curr.next = prev
        self.size-=1

    def Search(self, data):
        """
        :param data: will take input from the user and check if data exist in the linked list
        :return: will return true or false
        """
        curr = self.head
        if curr is None:  # if list is empty then delete
            print("list is empty")
        else:
            while curr.next is not None:  # while loop is used for finding address
                if curr.next.data == data:
                    return True
                curr = curr.next
    def __len__(self):
        return self.size
    def __isempty__(self):
        return self.size==0
    def extract(self):  # print is used for printing out the data in the linked list
        """
        :return:  prints out the data in linked list
        """
        curr = self.head
        while curr is not None:  # while loop is used printing data
            yield(curr.data)
            curr = curr.next

                
class Deque(LinkedList):
    
    def addFrontItem(self,data):
        self.Add_To_Start(data)
    def addLastItem(self,data):
        self.Add(data)
    def __show__():
        return self.Print()