## learning objectives
# from this lecture you will learn about
# 1->understand waht pandas is and why it is used
# 2-> load real world datasets (like csv files)
# 3-> perform basic data manipulation and analysis using pandas
# 4-> apply pandas concepts via a mini hands on project

# what is pandas
#-> pandas is a powerful and widely used open source data analysis and manipulation library for Python. It provides data structures and functions needed to manipulate structured data seamlessly. It is built on top of numpy and is designed to work with tabular data, such as spreadsheets or SQL tables.

## problem with numpy(problem before pandas)
#-> numpy arrays are powerful but lack labels for rows and columns, which can make data manipulation and analysis more difficult. For example, if you have a dataset with multiple columns, it can be hard to keep track of which column represents what data. Additionally, numpy does not have built-in functions for handling missing data or performing group operations, which are common tasks in data analysis.

#->hard to analyze tabular (row and column) data
#-> real world datasets often have missing values and numpy does not have built in functions to handle them
#-> lack of built in functions for group operations like grouping data by a certain column and performing operations on those groups

#-> Real world data comes in csv,Excel,SQL databases and numpy does not have built in functions to read and write these formats

###################### pandas to the rescue  ################

## two main data structures in pandas
#-> Series: a one dimensional labeled array that can hold any data type (integers, strings, floating point numbers, etc.). It is similar to a column in a spreadsheet or a SQL table. Each element in a Series has an associated label, which can be used to access and manipulate the data.

import pandas as pd
series=pd.Series([10,20,30,40],index=['a','b','c','d'])    
print(series)
print(series['b'])  # accessing element using label
 

#-> DataFrame: a two dimensional labeled data structure with columns of potentially different types. It is similar to a spreadsheet or a SQL table. Each column in a DataFrame is a Series, and the DataFrame itself has an index that labels the rows.

df=pd.DataFrame({
    'Name':['Alice','Bob','Charlie','David'],    ## column 1
    'Age':[25,30,35,40],                          ## column 2
    'City':['New York','Los Angeles','Chicago','Houston']  #column 3
})
print(df)
print("df['Name']:", df['Name'])  # accessing a column
print("df.loc[1]:", df.loc[1])   # accessing a row using label
print("df.iloc[1]:", df.iloc[1])  # accessing a row using integer position
print("df.head():", df.head())     # accessing first 5 rows of the dataframe
print("df.describe():", df.describe()) # getting summary statistics of the dataframe


#########   why pandas is used   #########
#              need                                        pandas feature
#->Handle CSV/Excel/SQL data formats        -> read_csv(),read_excel(),read_sql()
#->filter,clean and transform               ->.loc[],.iloc[],.dropna(),.fillna(),.apply(),.map()
#->group data and summarize data            -> .groupby(),.agg(),.pivot_table()
#->Integarte with visualization               works well with libraries like matplotlib,seaborn,plotly etc.


#########   ways of Creating a series #########
#-> from a list
s1=list(range(10,50,10))
series1=pd.Series(s1)
print("series1:", series1)
#-> from a numpy array
import numpy as np

s2=np.array([5,10,15,20])
series2=pd.Series(s2)
print("series2:", series2)
#-> from a dictionary
s3={'a':1,'b':2,'c':3,'d':4}
series3=pd.Series(s3)
print("series3:", series3)
#-> from a scalar value
series4=pd.Series(10,index=['a','b','c','d'])
print("series4:", series4)
# from a list with custom index
s5=list(range(1,5))
series5=pd.Series(s5,index=['w','x','y','z'])
print("series5:", series5)

#########  accessing elements in a series  #########
#-> using labels
print("series5['x']:", series5['x'])
#-> using integer position
print("series5.iloc[1]:", series5.iloc[1])
#-> using boolean indexing
print("series5[series5>2]:", series5[series5>2])
#-> using .loc[] and .iloc[]
print("series5.loc['y']:", series5.loc['y'])
print("series5.iloc[2]:", series5.iloc[2])

############## operations on series ##############
#-> arithmetic operations
s6=series5*2
print("series5*2:", s6)
s7=series5+10
print("series5+10:", s7)
s8=series5*series5
print("series5*series5:", s8)
#-> statistical operations
print("series5.mean():", series5.mean())
print("series5.median():", series5.median())
print("series5.std():", series5.std())
print("series5.sum():", series5.sum())
print("series5.min():", series5.min())
print("series5.max():", series5.max())

####### real world uses of series ########
#-> time series data
#-> stock prices, weather data, etc.
#-> representing a column in a dataframe
#-> example: creating a series for the 'Age' column in the dataframe created earlier
#Applying vectorized operations on a single value in a series


######### pandas DataFrame  #########



