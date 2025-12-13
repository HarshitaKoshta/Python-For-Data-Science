import numpy as np


a = np.array([0,1,2,3,4])
# print(a)

# print(np.arange(10))


# l = range(1000)
# print(%timeit (i**2 for i in l))        


# print(a.ndim)    #print dimension
# print(a.shape)   #shape
# print(len(a))


# b = np.array([[0,1,2,3],[21,4,4,5]])   #2d array
# print(b)

# print(b.ndim)    #print dimension
# print(b.shape)   #shape
# print(len(b))    #return the size of first dimension

# c = np.array([[[1,2],[3,4]],[[4,34],[43,4]]])
# print(c)
# print(c.ndim)
# print(c.shape)
# print(len(c))

# a = np.arange(10)
# print(a)

# b = np.arange(1,10,2)   #start, end (exclusive), step
# print(b)

# a = np.linspace(0,1,7)  #start, end ,divide in equal no. of parts 
# print(a)

# a = np.ones((3,3))
# print(a)

# b = np.zeros((4,3))
# print(b)

# c= np.eye(3)   #identity
# print(c)

# d= np.eye(3,2)    #rows,col
# print(d)

# a = np.diag([1,2,3,4]) #const a dig array
# print(a)
# print(np.diag(a))  #exact diagonal

# a = np.random.rand(4)   #return thr sample from the 
# print(a)

# a = np.random.rand(5)
# print(a)

a = np.random.randn(4)   
print(a)


a = np.arange(10)
print(a.dtype)

a = np.arange(10, dtype='float64')
print(a)

a = np.zeros((3,3))
print(a)
print(a.dtype)

d = np.array([1+2j,2+4j])  #complex datatype
print(d.dtype)

b = np.array([True,False,True,False])
print(b.dtype)

s = np.array(['Ram','Robert','Rahim'])
print(s.dtype)   #unicode string ,6 maximum  word  size

a = np.arange(10)
print(a[3])

a= np.diag([1,2,3])  #multi dimensional array
print(a[2,2])

a[0,2] = 5
print(a)

a = np.arange(1,10,2)
print(a)


a  = np.arange(10)
a[5:] = 10
print(a)

b = np.arange(5)
a[5:] = b[::-1]  #assign
print(a)

a = np.arange(10)
print(a)
b = a[::2]
print(b)

print(np.shares_memory(a,b))

b[0] = 10
print(a)

a=np.arange(10)
c = a[::2].copy()
print(c)
print(np.shares_memory(a,c))

c[3] = 7
print(a)

a = np.random.randint(0,20,15)
print(a)

mask = (a%2==0)  #true false
print(mask)

extract_from_a = a[mask]
print(extract_from_a)

a[mask] = -1
print(a)

a= np.arange(0,100,10)
print(a)
print(a[[2,4,2,3,2]])   #print value of index

a[[3,4,5,6]] = 1   #assign values
print(a)



