# titanic dataset:Exploratory Data Analysis (EDA) and Visualization

#step 1: Load the dataset
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load the Titanic dataset
df = sns.load_dataset('titanic')
# Display the first few rows of the dataset
# print(df.info())

# <class 'pandas.DataFrame'>
# RangeIndex: 891 entries, 0 to 890
# Data columns (total 15 columns):
#  #   Column       Non-Null Count  Dtype   
# ---  ------       --------------  -----   
#  0   survived     891 non-null    int64   
#  1   pclass       891 non-null    int64   
#  2   sex          891 non-null    str     
#  3   age          714 non-null    float64 
#  4   sibsp        891 non-null    int64   
#  5   parch        891 non-null    int64   
#  6   fare         891 non-null    float64 
#  7   embarked     889 non-null    str     
#  8   class        891 non-null    category
#  9   who          891 non-null    str     
#  10  adult_male   891 non-null    bool    
#  11  deck         203 non-null    category
#  12  embark_town  889 non-null    str     
#  13  alive        891 non-null    str     
#  14  alone        891 non-null    bool    
# dtypes: bool(2), category(2), float64(2), int64(4), str(5)
# memory usage: 80.7 KB
# None

#### Basic Data cleaning and preprocessing
# drop less useful or highly missing columns
df.drop(columns=['deck', 'embark_town'], inplace=True)

# fill missing values in 'age' with the median age
df['age'].fillna(df['age'].median(), inplace=True)

# fill embarked with the mode (most common value)
df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)

#drop rows with any remaining missing values (if any)
df.dropna(inplace=True)

#confirm that there are no missing values left
print(df.isnull().sum())

## step -4:Univariate Analysis - understanding the distribution of individual features
# 1. Categorical features: 'survived', 'pclass', '  sex', 'embarked', 'class', 'who', 'adult_male', 'alive', 'alone'
# 2. Numerical features: 'age', 'sibsp', 'parch', 'fare'    
# sns.countplot(x='survived', data=df)
# plt.title('Survival Count') 
# plt.show()

# sns.histplot(df['age'], bins=20, kde=True)
# plt.title('Age Distribution')
# plt.xlabel('Age')
# plt.ylabel('Frequency')
# plt.show()

# sns.countplot(x='pclass', data=df)
# plt.title('Passenger Class Distribution')
# plt.show()

### Bivariate Analysis - understanding the relationship between two features
# sns.countplot(x='sex',hue='survived', data=df)
# plt.title('survival by gender')
# plt.show()

# pclass vs survival
sns.countplot(x='pclass',hue='survived', data=df)
plt.title('survival by passenger class')
plt.show()

## feature engineering - creating new features that might be useful for analysis or modeling

# create a new feature :is_child - whether the passenger is a child (age < 18)
df['is_child'] = df['age'] < 18
# create family_size - total number of family members aboard (sibsp + parch)
df['family_size'] = df['sibsp'] + df['parch']

df.to_csv('titanic_cleaned.csv', index=False)
