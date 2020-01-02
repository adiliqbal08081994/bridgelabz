#data structure practice


#Array implimentation
import ctypes
class _ArrayIterator():
        def __init__(self,theArray):
            self._arrayref=theArray
            self.curndx=0
        def __iter__(self):
            return self
        def __next__(self):
            if self.curndx<len(self._arrayref):
                entry=self._arrayref[self.curndx]
                self.curndx += 1
                return entry
            else:
                raise StopIteration

class Array:
    def __init__(self,size):
        self._size=size
        PyArrayType=ctypes.py_object * size
        self.elements=PyArrayType()
        self.clear(None)
    def __len__(self):
        return self._size
    
    def __getitem__(self,index):
        assert index>=0 and index<=len(self)
        return self.elements[index]
    
    def __setitem__(self,index,value):
        assert index>=0 and index<=len(self)
        self.elements[index]=value
    def clear(self,value):
        for i in range(len(self)):
            self.elements[i]=value
    
    def __iter__(self):
        return _ArrayIterator(self.elements)

#2D Array implimentation

class Array2D:
    def __init__(self,numRows,numCols):
        self._TheRows=Array(numRows)

    for i in range(numRows):
        self._TheRows[i]=Array(numCols)
    def numRows(self):
        return len(self._TheRows)
    def numCols(self):
        return len(self._TheRows[0])
    def clear(self,value):
        for row in range(self.numRows()):
            row.clear(value)

    def __getitem__(self,ndxTuple):
        assert len(ndxTuple)==2
        row=ndxTuple[0]
        col=ndxTuple[1]
        assert row>0 and row<self.numRows()and col>0 and col<self.numCols()
        the1Darray=self._TheRows[row]
        return the1Darray[col]

    def __setitems__(self,ndxTuple,Value):
        assert len(ndxTuple)==2
        row=ndxTuple[0]
        col=ndxTuple[1]
        assert row>0 and row<self.numRows()and col>0 and col<self.numCols()
        the1Darray=self._TheRows[row]
        the1Darray[col]=Value


# matrix implimentation

class Matrix:
    def __init__(self,numRows,numCols):
        self._theGrid=Array2D(numRows,numCols)
        self._theGrid.(clear)
    
    def numRows(self):
        return self._theGrid.numRows()
    def numCols(self):
        return self._theGrid.numCols
    
    def __getitems__(self,ndxTuple):
        return self._theGrid[ndxTuple[0],ndxTuple[1]]
    
    def __setitems__(self,ndxTuple,Value):
        self._theGrid[ndxTuple[0],ndxTuple[1]]=Value
    

    def _transpose(self):
        pass



# set implimentation
class Set:
    def __init__(self):
        self._theElemens=list()
    def __len__(self):
        return len(self._theElemens)
    def __contains__(self,elements):
        return elements in self._theElemens
    

    def __add__(self,elements):
        if elements not in self._theElemens:
            self._theElemens.append(elements)

    def __remove__(self,element):
        assert element in self._theElemens
        self._theElemens.remove(element)
    

    def __eq__(self,setB):
        if len(self)!=len(setB):
            return False
        else:
            return self.isSubsetOf(setB)
    def isSubsetOf(self,setB):
        for elements in self:
            if elements not in setB:
                return False
            
            return True
    

    def union(self,setB):
        newset=Set()
        newset._theElemens.extend(self._theElemens)
        return newset

#creat a map function
class _MapEntry :
    def __init__( self, key, value ):
        self.key = key
        self.value = value
# Implementation of Map ADT using a single list.
class Map :
    # Creates an empty map instance.
    def __init__( self ):
        self._entryList = list()
    # Returns the number of entries in the map.
    def __len__( self ):
        return len( self._entryList )
    # Determines if the map contains the given key.
    def __contains__( self, key ):
        ndx = self._findPosition( key )
        return ndx is not None
    # Adds a new entry to the map if the key does exist. Otherwise, the
    # new value replaces the current value associated with the key.
    def add( self, key, value ):
        ndx = self._findPosition( key )
        if ndx is not None : # if the key was found
            self._entryList[ndx].value = value
            return False
        else : # otherwise add a new entry
            entry = _MapEntry( key, value )
            self._entryList.append( entry )
            return True
        
    # Returns the value associated with the key.
    def valueOf( self, key ):
        ndx = self._findPosition( key )
        assert ndx is not None, "Invalid map key."
        return self._entryList[ndx].value
    # Removes the entry associated with the key.
    def remove( self, key ):
        ndx = self._findPosition( key )
        assert ndx is not None, "Invalid map key."
        self._entryList.pop( ndx )
    # Returns an iterator for traversing the keys in the map.
    def __iter__( self ):
        return _MapIterator( self._entryList )
    # Helper method used to find the index position of a category. If the
    # key is not found, None is returned.
    def _findPosition( self, key ):
    # Iterate through each entry in the list.
        for i in range( len(self) ) :
    # Is the key stored in the ith entry?
            if self._entryList[i].key == key :
                return i
    # When not found, return None.
        return None
    # Storage class for holding the key/value pairs.


#implimentation of a linked list


class Bag:
    #construct an empty bag
    def __init__(self):
        self._head=None
        self._size=0
    
    def __len__(self):
        return self._size

    def __contains__(self,target):
        curNode=self.head
        while curNode is not None and curNode.item!=target:
            curNode=curNode.next
        return curNode is not None

    def add(self,items):
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
        if curNode is _head:
            self._head=curNode.next

        else:
            predNode.next=curNode.next
        

        return curNode.item

    def __iter__(self):
        return _BagIterator(self._head)


class _BagListNode(object):
    def __init__(self,item):
        self.item=item
        self.next=None


class _BagIterator:
    def __init__(self,listHead):
        self._curNode=listHead

    def __iter__(self):
        return self
    def next(self):
        if self._curNode is not None:
            raise StopIteration
        else:
            item = self._curNode.item
            self._curNode=self._curNode.next
            return item




