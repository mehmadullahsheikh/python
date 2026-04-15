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
