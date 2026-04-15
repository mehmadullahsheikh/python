######  Pandas miniproject: Titanic dataset analysis ######
import pandas as pd

######## converting text file to CSV file and reading the CSV file ########
# df = pd.read_csv("Titanic.txt")   # reads text as CSV
# df.to_csv("Titanic.csv", index=False)
# print("df.head():", df.head())  # accessing first 5 rows of the dataframe

##### problem statement:You have been hired as a data analyst by a historical research team investing the Titanic disaster. Your task is to analyze the passenger data and uncover insights about survival patterns based on factors such as age, gender, and passenger class. You will need to clean and preprocess the data, perform exploratory data analysis, and create visualizations to present your findings to the research team. Your analysis will help shed light on the factors that influenced survival during this tragic event.

## using the Titanic dataset , you will
 # 1. clean and preprocess the data
 # 2. explore and summarize key values
 # 3. identify trends in survival rates
 #4. answer specific bussiness questions using pandas

 ##### objective and tasks ###
 # 1.load and understand the dataset
 # read the csv into a pandas dataframe
 # display the first few rows of the dataframe to understand its structure and contents usinf df.head()
 #check the structure usin df.info() to identify missing values and data types
df=pd.read_csv('Titanic.csv')
print( df.head())  # accessing first 5 rows of the dataframe
print( df.info()) # checking the structure of the dataframe to identify missing values and data types

# 2.Handle missing values
# identify columns with missing values using df.isnull().sum()
# fill missing values in the 'Age' column with the median age using df.fillna({'Age': df['Age'].median()}, inplace=True)
# drop columns like cabin (too many missing values) using df.drop('Cabin', axis=1, inplace=True)

print("Missing values in each column:\n", df.isnull().sum()) # identifying columns with missing values

df.fillna({'Age': df['Age'].mean()}, inplace=True) # filling missing values in the 'Age' column with the median age

df.drop('Cabin', axis=1, inplace=True) # dropping the 'Cabin' column with too many missing values

print("Data after handling missing values:\n", df.head()) # displaying the first few rows of the dataframe after handling missing values
print("Missing values in each column after handling:\n", df.isnull().sum()) # checking for missing values after handling

 #### 3.Exploratory data analysis
 # a. what is the overall survival rate?
 # b.what is the survival rate by gender
# c.what is the survival rate by passenger class
# d. what is the average age of survivors vs non-survivors
# e. what is the servival rate of children (age < 16) vs adults (age >= 16)

# a. overall survival rate
overall_survival_rate = df['Survived'].mean() * 100
print(f"Overall Survival Rate: {overall_survival_rate:.2f}%")
# b. survival rate by gender
survival_rate_by_gender = df.groupby('Sex')['Survived'].mean() * 100
print("\nSurvival Rate by Gender:\n", survival_rate_by_gender)
# c. survival rate by passenger class  
survival_rate_by_class = df.groupby('Pclass')['Survived'].mean() * 100
print("\nSurvival Rate by Passenger Class:\n", survival_rate_by_class)
# d. average age of survivors vs non-survivors
average_age_survivors = df[df['Survived'] == 1]['Age'].mean()
average_age_non_survivors = df[df['Survived'] == 0]['Age'].mean()
print(f"\nAverage Age of Survivors: {average_age_survivors:.2f}")
print(f"Average Age of Non-Survivors: {average_age_non_survivors:.2f}")
# e. survival rate of children (age < 16) vs adults (age >= 16)
df['AgeGroup'] = df['Age'].apply(lambda x: 'Child' if x < 16 else 'Adult' if x <= 90 else 'Elderly')
survival_rate_by_age_group = df.groupby('AgeGroup')['Survived'].mean() * 100
print("\nSurvival Rate by Age Group:\n",survival_rate_by_age_group)            


###### Advanced Insights
t=df[(df['Survived'] == 1)]['Age'].min()
tt=df[(df['Survived'] == 1)]['Age'].max()
print(f"\nYoungest survivor's age: {t:.2f}")
print(f"Oldest survivor's age: {tt}")

survival_age=df[df['Survived'] == 1][['Age']].sort_values(by='Age',ascending=True)
print("\nSurvivors sorted by age:\n", survival_age)
