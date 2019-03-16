
# coding: utf-8

# In[86]:

# matrix_1 mxn
# matrix_2 nxp
# matrix_3=matrix_1 * matrix_2   , mxp


# In[87]:

import numpy as np

def get_value_from_row_col(r_1,c_1):   # karşmaşıklığı O(n) --> r_1 ve c_1 in uzunluklarına karşılık gelmekte
    t=0
    for i in range(len(r_1)):
        t=t+r_1[i]*c_1[i]
    return t

a=[1,2,3,4]
b=[5,6,7,8]
get_value_from_row_col(a,b)


# In[88]:

b=[[1,2,3,4],[5,6,7,8],[1,2,3,4],[5,6,7,8]] # 4x4
a=[[1,2,3,4],[5,6,7,8]] # 2x4
#a*b tanımlı  ,  b*a tanımsız

def get_row_from_matrix(a,i):
    return a[i]
def get_col_from_matrix(a,j):
    col=[]
    for i in range(len(a)):   # for i in a
        col.append(a[i][j])   # col.append(i[j])
    return col

print(get_col_from_matrix(a,1))


# In[89]:

def matrix_multiply(m_1,m_2):   # O(m.n.p)  Amxn Bnxp = Cmp,  --> eğer matrix kareyse O(n^3)
    m=len(m_1) #satır sayısı
    n=len(m_2[0]) #sutun sayısı
    r=np.zeros((m,n)) #r[]
    for i in range(m):
        for j in range(n):
            a=get_row_from_matrix(m_1,i)
            b=get_col_from_matrix(m_2,j)
            c=get_value_from_row_col(a,b)
            r[i][j]=c #r[i].append(c)
    return r.tolist()


# In[90]:

d=matrix_multiply(a,b)
print(d)
d[0][1]


# In[ ]:



