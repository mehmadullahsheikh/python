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

# import pandas as pd
# series=pd.Series([10,20,30,40],index=['a','b','c','d'])    
# print(series)
# print(series['b'])  # accessing element using label
 

# #-> DataFrame: a two dimensional labeled data structure with columns of potentially different types. It is similar to a spreadsheet or a SQL table. Each column in a DataFrame is a Series, and the DataFrame itself has an index that labels the rows.

# df=pd.DataFrame({
#     'Name':['Alice','Bob','Charlie','David'],    ## column 1
#     'Age':[25,30,35,40],                          ## column 2
#     'City':['New York','Los Angeles','Chicago','Houston']  #column 3
# })
# print(df)
# print("df['Name']:", df['Name'])  # accessing a column
# print("df.loc[1]:", df.loc[1])   # accessing a row using label
# print("df.iloc[1]:", df.iloc[1])  # accessing a row using integer position
# print("df.head():", df.head())     # accessing first 5 rows of the dataframe
# print("df.describe():", df.describe()) # getting summary statistics of the dataframe


# #########   why pandas is used   #########
# #              need                                        pandas feature
# #->Handle CSV/Excel/SQL data formats        -> read_csv(),read_excel(),read_sql()
# #->filter,clean and transform               ->.loc[],.iloc[],.dropna(),.fillna(),.apply(),.map()
# #->group data and summarize data            -> .groupby(),.agg(),.pivot_table()
# #->Integarte with visualization               works well with libraries like matplotlib,seaborn,plotly etc.


# #########   ways of Creating a series #########
# #-> from a list
# s1=list(range(10,50,10))
# series1=pd.Series(s1)
# print("series1:", series1)
# #-> from a numpy array
# import numpy as np

# s2=np.array([5,10,15,20])
# series2=pd.Series(s2)
# print("series2:", series2)
# #-> from a dictionary
# s3={'a':1,'b':2,'c':3,'d':4}
# series3=pd.Series(s3)
# print("series3:", series3)
# #-> from a scalar value
# series4=pd.Series(10,index=['a','b','c','d'])
# print("series4:", series4)
# # from a list with custom index
# s5=list(range(1,5))
# series5=pd.Series(s5,index=['w','x','y','z'])
# print("series5:", series5)

# #########  accessing elements in a series  #########
# #-> using labels
# print("series5['x']:", series5['x'])
# #-> using integer position
# print("series5.iloc[1]:", series5.iloc[1])
# #-> using boolean indexing
# print("series5[series5>2]:", series5[series5>2])
# #-> using .loc[] and .iloc[]
# print("series5.loc['y']:", series5.loc['y'])
# print("series5.iloc[2]:", series5.iloc[2])

# ############## operations on series ##############
# #-> arithmetic operations
# s6=series5*2
# print("series5*2:", s6)
# s7=series5+10
# print("series5+10:", s7)
# s8=series5*series5
# print("series5*series5:", s8)
# #-> statistical operations
# print("series5.mean():", series5.mean())
# print("series5.median():", series5.median())
# print("series5.std():", series5.std())
# print("series5.sum():", series5.sum())
# print("series5.min():", series5.min())
# print("series5.max():", series5.max())

# ####### real world uses of series ########
# #-> time series data
# #-> stock prices, weather data, etc.
# #-> representing a column in a dataframe
# #-> example: creating a series for the 'Age' column in the dataframe created earlier
# #Applying vectorized operations on a single value in a series


# ######### pandas DataFrame  #########
# # each column in a DataFrame is a Series and the DataFrame itself has an index that labels the rows. A DataFrame can be thought of as a collection of Series that share the same index.

# # creating a DataFrame from a dictionary
# data={
#     'Name':['Alice','Bob','Charlie','David'],
#     'Age':[25,30,35,40],
#     'City':['New York','Los Angeles','Chicago','Houston']
# }
# df1=pd.DataFrame(data)
# print("df1:", df1)

# # creating a DataFrame from a list of dictionaries
# data2=[
#     {'Name':'Alice','Age':25,'City':'New York'},
#     {'Name':'Bob','Age':30,'City':'Los Angeles'},
#     {'Name':'Charlie','Age':35,'City':'Chicago'},
#     {'Name':'David','Age':40,'City':'Houston'}
# ]
# df2=pd.DataFrame(data2)
# print("df2:", df2)
# # creating a DataFrame from a list of lists
# data3=[
#     ['Alice',25,'New York'],
#     ['Bob',30,'Los Angeles'],
#     ['Charlie',35,'Chicago'],
#     ['David',40,'Houston']
# ]
# df3=pd.DataFrame(data3,columns=['Name','Age','City'])
# print("df3:", df3)
# # creating a DataFrame from a numpy array
# data4=np.array([
#     ['Alice',25,'New York'],
#     ['Bob',30,'Los Angeles'],
#     ['Charlie',35,'Chicago'],
#     ['David',40,'Houston']
# ])
# df4=pd.DataFrame(data4,columns=['Name','Age','City'])
# print("df4:", df4)
# # creating a DataFrame from a Series
# s9=pd.Series(['Alice','Bob','Charlie','David'])
# s10=pd.Series([25,30,35,40])
# s11=pd.Series(['New York','Los Angeles','Chicago','Houston'])
# df5=pd.DataFrame({'Name':s9,'Age':s10,'City':s11})
# print("df5:", df5)


# ### accessing elements in a DataFrame
# #-> using column names
# print("df1['Name']:", df1['Name'])
# #-> using .loc[] and .iloc[]
# print("df1.loc[0]:", df1.loc[0])  # accessing first
# print("df1.iloc[0]:", df1.iloc[0])  # accessing first row using integer position
# print("df1.loc[0,'Name']:", df1.loc[0,'Name'])
# print("df1.iloc[0,0]:", df1.iloc[0,0])  # accessing first row and first column using integer position
# #-> using boolean indexing
# print("df1[df1['Age']>30]:", df1[df1['Age']>30])  # accessing rows where Age is greater than 30
# #-> using .at[] and .iat[]
# print("df1.at[0,'Name']:", df1.at[0,'Name'])  # accessing first row and 'Name' column using label
# print("df1.iat[0,0]:", df1.iat[0,0])  # accessing first row and first column using integer position 

# # diff loc and iloc
# #-> .loc[] is used for label-based indexing, which means you can access rows and columns using their labels. For example, df.loc[0] will access the row with the label 0, and df.loc[0,'Name'] will access the 'Name' column of the row with label 0.

# #-> .iloc[] is used for integer-based indexing, which means you can access rows and columns using their integer positions. For example, df.iloc[0] will access the first row of the DataFrame, and df.iloc[0,0] will access the first row and first column of the DataFrame.

# # Benefit                                       Description
# # Label-based indexing (.loc)                 Allows you to access rows and columns using their labels, which can be more intuitive and easier to read.
# # flexible selection                         slice by row/column labels and positions
# #easy data loading                           read from CSV, Excel, SQL databases and more
# # handling missing data                       built-in functions to handle missing data (e.g., dropna(), fillna())
# # group operations                            built-in functions for group operations (e.g., groupby(), agg(), pivot_table())
# #transformation pipelines                   Filtering,sorting,merging,reshaping data and more
# # ML ready                                 used  as input/output in  scikit-learn ,XGBoost etc  


# ###########  DataFrame basic operations ############
# # reading data from a CSV file
import pandas as pd
# df=pd.read_csv('Housing.csv')
# print("df.head():", df.head())  # accessing first 5 rows of the dataframe
# print("df.describe():", df.describe()) # getting summary statistics of the dataframe

#####  exploring the dataset
# #-> checking for missing values
# print("df.isnull().sum():", df.isnull().sum())
# #-> checking data types of columns
# print("df.dtypes:", df.dtypes)
# #-> checking unique values in a column
# print(df.info())


######  Accessing columns #####
#-> accessing a single column
# print("df['Price']:", df['price'].head())
# #-> accessing multiple columns
# print("df[['Price','Area']]:", df[['price','area']].head())
# #-> accessing columns using .loc[]
# print("df.loc[:,['Price','Area']]:", df.loc[:,['price','area']].head())


### accessing rows
#-> accessing a single row using .loc[]
# print("df.loc[0]:", df.loc[0])  # accessing first row using label
# #-> accessing a single row using .iloc[]
# print("df.iloc[0]:", df.iloc[0])  # accessing first row using integer position
# #-> accessing multiple rows using .loc[]
# print("df.loc[0:2]:", df.loc[0:2])  # accessing first 3 rows using label
# #-> accessing multiple rows using .iloc[]

# print("df.iloc[0:3]:", df.iloc[0:3])  # accessing first 3 rows using integer position

###  conditional filtering
#-> filtering rows where price is greater than 50000
# print("df[df['price']>50000]:", df[df['price']>50000].head())
# #-> filtering rows where area is greater than 2000
# print("df[df['area']>2000]:", df[df['area']>2000].head())
# #-> filtering rows where price is greater than 50000 and area is greater than 2000
# print("df[(df['price']>50000) & (df['area']>2000)]:", df[(df['price']>50000) & (df['area']>2000)].head())

## column operations
#-> creating a new column 'price_per_sqft' by dividing price by area
# df['price_per_sqft']=df['price']/df['area']
# print("df.head():", df.head())

df=pd.read_csv('Diabetes Missing Data.csv')
# print("df.head():", df.head())

#checking for missing values and filling them with mean value of the column
# print(df.isnull().sum())
df.fillna({'Glucose': df['Glucose'].mean()},inplace=True)
# print(df.isnull().sum())

# ### remove rows with missing values
# df.dropna(axis=1,inplace=True)  # drop columns with missing values
# df.dropna(inplace=True)   

# print(df.head())


###### Aggregation and grouping
#-> grouping data by 'Outcome' column and calculating mean of 'Glucose' column for each group
# grouped=df.groupby('Age').mean()
# print(grouped)

# grouped=df.groupby('Age')['Glucose'].mean()
# print(grouped)

# g2=df.groupby('Age')['Glucose'].agg(['mean','min','max'])
# print(g2)

#############  sorting data
#-> sorting data by 'Glucose' column in ascending order
# sorted_df=df.sort_values(by='Glucose')
# print("sorted_df.head():", sorted_df.head())
# #-> sorting data by 'Glucose' column in descending order
# sorted_df_desc=df.sort_values(by='Glucose',ascending=False)
# print("sorted_df_desc.head():", sorted_df_desc.head())


#########  Merging and joining dataframes
#-> creating two dataframes to merge
# df1=pd.DataFrame({
#     'ID':[1,2,3,4],
#     'Name':['Alice','Bob','Charlie','David']
# })
# df2=pd.DataFrame({
#     'ID':[3,4,5,6],
#     'Age':[25,30,35,40]
# })
# #-> merging dataframes on 'ID' column using inner join
# merged_df=pd.merge(df1,df2,on='ID',how='left')
# print("merged_df:", merged_df)


###  concatenating dataframes
#-> creating two dataframes to concatenate
df3=pd.DataFrame({
    'ID':[1,2,3,4],
    'Name':['Alice','Bob','Charlie','David']
})
df4=pd.DataFrame({
    'ID':[5,6,7,8],
    'Name':['Eve','Frank','Grace','Heidi']
})
#-> concatenating dataframes vertically
concatenated_df=pd.concat([df3,df4],ignore_index=True)
print("concatenated_df:", concatenated_df)