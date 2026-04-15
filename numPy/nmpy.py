#a=[1,2,3]
#b=[2,4,7]
# result=[a[i]*b[i] for i in range(len(a))]
# print(result)

# Numpy in action
#### Array creation #######
import numpy as np
# a=np.array([1,2,3])  # 1d
# c=np.array([[1,2,3],[4,5,6]])  # 2d 

# ### broadcasting
# a=np.array([1,2,3])
# b=np.array([2,4,7])
# result=a*b
# print(result)

# # element wise multiplication/addition/subtraction
# a=a*2
# b=b+2
# c=c-2
# print(a)
# print(b)
# print(c)

# # built in functions
# print(np.sqrt(a))
# print(np.exp(a))
# print(np.log(a))

# ## reshaping and aggregation
# c=np.arange(6).reshape(3,2)
# print(c)

# ## axis=0 -> column wise and axis=1 -> row wise
# print(np.sum(c,axis=0))
# print(np.sum(c,axis=1))
# print(np.mean(c,axis=0))

# ## speed comparison of numpy and list comprehension
# import time
# import numpy as np
# #-> list comprehension
# N=1000000
# a=list(range(N))
# b=list(range(N))
# start=time.time()
# result=[a[i]*b[i] for i in range(len(a))]
# end=time.time()
# print("List comprehension time:",end-start)
# #-> numpy
# a=np.arange(N)
# b=np.arange(N)
# start=time.time()
# result=a*b
# end=time.time()
# print("Numpy time:",end-start)

# matrix multiplication using numpy and list comprehension
# N=1000
# #-> list comprehension
# a=[[i+j for j in range(N)] for i in range(N)]
# b=[[i-j for j in range(N)] for i in range(N)]
# c=[[0 for j in range(N)] for i in range(N)]
# start=time.time()
# for i in range(N):
#     for j in range(N):
#         c[i][j]=sum(a[i][k]*b[k][j] for k in range(N))
# end=time.time()
# print("List comprehension matrix multiplication time:",end-start)
# #-> numpy
# a1=np.array([[i+j for j in range(N)] for i in range(N)])
# b1=np.array([[i-j for j in range(N)] for i in range(N)])
# c1=np.zeros((N,N))
# start=time.time()
# c1=a1 @ b1  # matrix multiplication using @ operator
# end=time.time()
# print("Numpy matrix multiplication time:",end-start)

## numpy role in machine learning
#-> data manipulation and preprocessing
#-> linear algebra operations
#-> random number generation
#-> performance optimization
#-> integration with other libraries like pandas, scikit-learn, tensorflow, etc.
#-> example: data normalization using numpy
# feature engineering
#model training and evaluation


## numpy project
## you are given  the marks of 5 students in 3 subjects. You need to calculate the average marks of each student and Identify the student with the highest average marks.
marks=np.array([np.random.randint(50,100) for _ in range(15)]).reshape(5,3)
print("Marks of students:\n",marks)
average_marks=np.mean(marks,axis=1)
print("Average marks of each student:\n",average_marks)
highest_avg_index=np.argmax(average_marks)
print("Student with the highest average marks is Student",highest_avg_index+1,"with average marks of",average_marks[highest_avg_index])

all_subjects_max=np.max(marks,axis=0)
print("Maximum marks for each subject:\n",all_subjects_max)

subject_topper_index=np.argmax(marks,axis=0)
print("Topper for each subject:\n",subject_topper_index+1)



