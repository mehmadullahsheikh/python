a=[1,2,3]
b=[2,4,7]
result=[a[i]*b[i] for i in range(len(a))]
print(result)

# Numpy in action
#### Array creation #######
import numpy as np
a=np.array([1,2,3])  # 1d
b=np.array([[1,2,3],[4,5,6]])  # 2d