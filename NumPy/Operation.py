import numpy as np

a = np.array([1,2,3,4])
print(a+1)   #vectroization
print(a**2)

b = np.ones(4) + 1 #bydefault -> float
print(b)
print(a-b)
print(a*b)

c = np.diag([1,2,3,4])
print(c*c)
#or 
print(c.dot(c))

a = np.array([1,2,3,4])
b = np.array([1,4,2,4])
print(a==b)  #compare element
print(a>b)

c = np.array([1,2,3,4])
print(np.array_equal(a,b))  #check array wise
print(np.array_equal(a,c))  #check array wise

a = np.array([1,1,0,0],dtype=bool)
b = np.array([1,0,1,0],dtype=bool)
print(np.logical_or(a,b))
print(np.logical_and(a,b))
print(np.logical_not(a,b))
print(np.logical_xor(a,b))

#TRANSCEBDENTAL FUNCTION

print(np.sin(a))
print(np.cos(a))
print(np.log(a))
print(np.exp(a))  #e^x for each element
 
a = np.arange(4)
# print(a+np.array([2,3]))

x = np.array([2,4,3,2])
print(np.sum(x))

x = np.array([[1,1],[2,2]])
print(x)

print(x.sum(axis=0)) #colums sum
print(x.sum(axis=1)) #row sum

print(x.min())
print(x.max())
print(x.argmin())  #index of mini element
print(x.argmax())  #index of max element

print(np.all([True,True,False]))  #check all value true
print(np.any([True,True,False]))  #check any value true

a= np.zeros((50,50))
print(np.any(a != 0))
print(np.all(a==a))

a = np.array([1,2,3,2])
b = np.array([2,2,3,2])
c = np.array([6,4,4,5])
print(((a<=b)&(b<=c)).all())

x = np.array([1,2,3,1])
y = np.array([[1,2,3],[5,6,1]])
print(x.mean())
print(np.median(x))
print(np.median(y,axis=-1))  #last axis
print(x.std())
# 1.calulate mean 2.c= no-mean 3. square of (c) then total 4.population variance

#load data into numpy array obj
data = np.loadtxt('populations.txt')
print(data)