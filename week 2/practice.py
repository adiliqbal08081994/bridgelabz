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