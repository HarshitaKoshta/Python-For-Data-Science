import numpy as np

a = np.arange(10)
print(a)

a = np.zeros((3,3))
print(a)

a = np.arange(10,50,5)
print(a)
print(a.shape)
print(a.dtype)
print(a.size)

a = np.random.rand(4,4)

print("Array", a)
print("Mean:", np.mean(a))
print("Sum:", np.sum(a))

a = np.array([2,45,2,54,2,3,66,56])
# a[a>50] = 50
# print(a)

print(a[len(a)-2:len(a)])

a = np.eye(5)
print(a)

print(a.flatten())

arr = np.arange(1,13)
arr=arr.reshape(3,4)
print(arr.shape)

a = np.eye(4,3)
print(a)

a = np.array([24,5,66,3,4,5,35])
a[a>10] = 20
print(a)

a = np.random.rand(2,3)
b = np.random.rand(2,3)

print(a*b)

a= np.array([2,4,23,1,3])
print(a.sort)

a = np.arange(1,30)
a[a%3==0] = -1
print(a)

arr = np.array([[1,2],[3,4],[5,6]])
print(arr.flatten())


arr = np.array([10, 20, 30, 40, 50])
normalized = (arr - arr.min()) / (arr.max() - arr.min())
print(normalized)

