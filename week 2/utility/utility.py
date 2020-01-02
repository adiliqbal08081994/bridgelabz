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


