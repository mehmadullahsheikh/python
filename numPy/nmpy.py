#a=[1,2,3]
#b=[2,4,7]
# result=[a[i]*b[i] for i in range(len(a))]
# print(result)

# Numpy in action
#### Array creation #######
import numpy as np
# a=np.array([1,2,3])  # 1d
c=np.array([[1,2,3],[4,5,6]])  # 2d 

### broadcasting
a=np.array([1,2,3])
b=np.array([2,4,7])
result=a*b
print(result)

# element wise multiplication/addition/subtraction
a=a*2
b=b+2
c=c-2
print(a)
print(b)
print(c)

# built in functions
print(np.sqrt(a))
print(np.exp(a))
print(np.log(a))

## reshaping and aggregation
c=np.arange(6).reshape(3,2)
print(c)

## axis=0 -> column wise and axis=1 -> row wise
print(np.sum(c,axis=0))
print(np.sum(c,axis=1))
print(np.mean(c,axis=0))


