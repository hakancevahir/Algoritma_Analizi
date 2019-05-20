
# coding: utf-8

# In[20]:

def maxVal(toConsider, avail):
    if toConsider == [] or avail ==0:
        result = (0, ())
    elif toConsider[0][2]>avail:  #burada .getWeight yerine 2 yazdık altta 2. değer weight değerimiz 0-names 1-vals 2-weights
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem=toConsider[0]
        withVal, withToTake = maxVal(toConsider[1:],avail - nextItem[2])
        withVal+=nextItem[1] #getValue yerine 1
        withoutVal, withoutToTake = maxVal(toConsider[1:],avail)
        if withVal > withoutVal:
            result=(withVal, withToTake + (nextItem,))
        else:
            result=(withoutVal, withoutToTake)
    return result

def getitems():
    names = ['a','b','c','d']
    vals=[6,7,8,9]
    weights=[3,3,2,5]
    
    items_a=[names[0],vals[0],weights[0]]
    items_b=[names[1],vals[1],weights[1]]
    items_c=[names[2],vals[2],weights[2]]
    items_d=[names[3],vals[3],weights[3]]
    items_c
    
    items=[items_a,items_b,items_c,items_d]
    return items

getitems()


# In[21]:

items=getitems()
maxVal(items,10)
#(24, (['d', 9, 5], ['c', 8, 2], ['b', 7, 3])) --> b , c ve d kitaplarını aldığımızda weightimizi karşılayan en yüksek value değerine sahip olmuş oluyoruz.


# In[ ]:



