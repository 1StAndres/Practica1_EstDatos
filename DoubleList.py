from DoubleNode import DoubleNode
class DoubleList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def size(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    
    def first(self):
        return self._head
    
    def last(self):
        return self._tail
    
    def addFirst(self, e):
        n = DoubleNode(e)
        if self.isEmpty():
            self._head = n
            self._tail = n

        else:
            n.setNext(self._head)
            self._head.setPrev(n)
            self._head = n

        self._size += 1    

    def addLast(self, e):
            n = DoubleNode(e)
            if self.isEmpty():
                self._head = n
                self._tail = n

            else:
                self._tail.setNext(n)
                n.setPrev(self._tail)
                self._tail = n
            self._size +=1
    
    def removeFirst(self):
        if not self.isEmpty():
            temp = self._head
            self._head = temp.getNext() 
            temp.setNext(None)
            self._size -= 1
            return temp.getData()
        
        else:
            return None
    
    def removeLast(self):
        if not self.isEmpty():
            temp = self._tail
            self._tail = temp.getPrev() 
            temp.setNext(None)
            self._size -= 1
            return temp.getData()
        
        else:
            return None
        
    def remove(self, n): 
        if n == self._head:
            self.removeFirst()
        if n == self._tail:
            self.removeLast()

        if not self.isEmpty():
            temp = n
            prevtemp = n.getPrev()
            tempnext = n.getNext()
            prevtemp.setNext(tempnext)
            tempnext.setPrev(prevtemp)
            n.setNext(None)
            n.setPrev(None)
            self._size -= 1
            return temp.getData()
        else:
            return None
    
    def addAfter(self, n, e):
        
        if not self.isEmpty():
            if n == self._tail:
                self.addLast(e)
            else:
                new = DoubleNode(e)
                tempnext = n.getNext()
                n.setNext(new)
                tempnext.setPrev(new)
                new.setPrev(n)
                new.setNext(tempnext)
                self._size += 1
        else:
            self.addFirst()

    def addBefore(self, n, e):
        
        if not self.isEmpty():
            if n == self._head:
                self.addFirst(e)
            else:
                new = DoubleNode(e)
                prevtemp = n.getPrev()
                n.setPrev(new)
                prevtemp.setNext(new)
                new.setPrev(prevtemp)
                new.setNext(n)
                self._size += 1
        else:
            self.addFirst()

    def __iter__(self):
        self._current = self._head
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration
        data = self._current.getData()
        self._current = self._current.getNext()
        return data
