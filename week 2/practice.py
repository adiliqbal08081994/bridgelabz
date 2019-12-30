import ctypes

 class _ArrayIterator():
        def __init__(self,theArray):
            self._arrayref=theArray
            self.curndx=0
        def __iter__(self):
            return self
        def __next__(self):
            if self._curndx<len(self._arrayref):
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