
# coding: utf-8

# In[6]:

import ctypes
from pympler import asizeof

class DynamicArray:
    def getsize(self):
        import sys
        return sys.getsizeof(self._A)
    
    def ToString(self):
        for i in self._A:
            print(i, " ")
            
    def getLength(self):
        return len(self._A)
    
    def __init__(self):
        self._n=0
        self._capacity=1
        self._A=self._make_array(self._capacity)
        
    def __len__(self):
        return self._n
    
    def __getitem__(self,k):
        if not 0 <= k <self._n:
            raise IndexError('invalid index')
        return self._A[k]
    
    def append(self,obj):
        if self._n == self._capacity: #kapasite yeterli degilse, kapasiteyi 2'ye katla.
            self._resize(2*self._capacity)
        self._A[self._n]=obj
        self._n+=1
        
    def _resize(self, c): # nonpublic utitity
        print("su an worst-case durumunda , liste dolu, başka yerden n*2 lik yer alınıp taşıma yapılacak")
        B = self._make_array(c) # new (bigger) array
        for k in range(self._n): # for each existing value
            B[k] = self._A[k]
        self._A=B # use the bigger array
        self._capacity = c
        
    def _make_array(self, c): # nonpublic utitity
        return(c*ctypes.py_object)()


# In[8]:

c=DynamicArray()
for i in range(33):
    c.append(" add an item"+str(i))
    print(str(i)+" eklendi , dizi boyutu : "+str(c.getLength()))  #c.__len__()  de olur


# In[ ]:



