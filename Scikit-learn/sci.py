## introduction to scikit-learn
# scikit-learn is a powerful and widely used machine learning library in Python. It provides a simple and efficient tools for data mining and data analysis, built on top of NumPy, SciPy, and matplotlib. Scikit-learn offers a wide range of algorithms for classification, regression, clustering, dimensionality reduction, model selection, and preprocessing. It is designed to be easy to use and integrate with other Python libraries, making it a popular choice for both beginners and experienced machine learning practitioners. With its extensive documentation and active community, scikit-learn is an essential tool for anyone working in the field of machine learning.

# by the end of this section
# 1: understand the ML pipeline using scikit-learn
#2: learn KNN and decision tree algorithms and how to implement them using scikit-learn
#3:perform data preprocessing and feature engineering using scikit-learn's tools
#4: implement an end to end classification project using scikit-learn, including data cleaning, feature engineering, model training, and evaluation.

##################  what is machine learning ##########
# machine learning is a subset of artificial intelligence that focuses on developing algorithms and models that allow computers to learn from and make predictions or decisions based on data. It involves training a model on a dataset, allowing it to identify patterns and relationships within the data, and then using that model to make predictions or classifications on new, unseen data. Machine learning can be categorized into three main types: supervised learning, unsupervised learning, and reinforcement learning. It has applications in various fields such as finance, healthcare, marketing, and more, enabling businesses and organizations to gain insights and make informed decisions based on data analysis.

### Types of machine learning
# 1. Supervised Learning: In supervised learning, the model is trained on a labeled
# dataset, where the input data is paired with the corresponding output labels. The goal is to learn a mapping from inputs to outputs, allowing the model to make predictions on new, unseen data. Examples of supervised learning algorithms include linear regression, logistic regression, support vector machines, and neural networks.
# 2. Unsupervised Learning: In unsupervised learning, the model is trained on an unlabeled dataset, where the input data does not have corresponding output labels. The goal is to find patterns, relationships, or structures within the data. Examples of unsupervised learning algorithms include clustering algorithms (e.g., K-means, hierarchical clustering) and dimensionality reduction techniques (e.g., principal component analysis).
# 3. Reinforcement Learning: In reinforcement learning, an agent learns to make decisions by interacting with an environment. The agent receives feedback in the form of rewards or penalties based on its actions, and the goal is to learn a policy that maximizes cumulative rewards over time. Reinforcement learning is commonly used in areas such as robotics, game playing, and autonomous systems.

######## Ml workflow ###
#1: Data collection: Gathering and collecting relevant data for the problem at hand.
#2: Data preprocessing: Cleaning and preparing the data for analysis, including handling missing values, encoding categorical variables, and scaling features.
#3: Feature engineering: Creating new features or transforming existing features to improve the performance of the model.
#3:train/test split: Splitting the dataset into training and testing sets to evaluate the model's performance on unseen data.
#4: Model selection: Choosing an appropriate machine learning algorithm based on the problem type and data characteristics.
#5: Model training: Fitting the selected model to the training data to learn the underlying patterns and relationships.
#6: Model evaluation: Assessing the performance of the trained model using appropriate evaluation metrics (e.g., accuracy, precision, recall, F1-score) on the testing set.
#7: Hyperparameter tuning: Optimizing the model's hyperparameters to improve its performance.
#8: Model deployment: Deploying the trained model into a production environment for real-world use.



### scikit-learn provides consistent api for
# 1:models(fits,predict)
#2 : prepocessing
# 3:evaluation
#4:pipelines

######################################  start ###########################

# loading data with scikit-learn

from sklearn.datasets import load_iris
iris=load_iris()

import pandas as pd
X=pd.DataFrame(iris.data,columns=iris.feature_names)
y=pd.Series(iris.target)
df=X.copy()
df['target']=y
# print(df.head())

## visualizing dataset structure
## class distribution
import seaborn as sns
import matplotlib.pyplot as plt
# sns.countplot(x=iris.target)
# plt.title("class distribution in iris")
# plt.xlabel("Target class")
# plt.ylabel("Count")
# plt.show()

## pairwise feature relations
# sns.pairplot(df,hue='target',corner=True)
# plt.suptitle("Pairplot of Iris Features",y=1.02)
# plt.show()

### correlation map
# sns.heatmap(df.corr(),annot=True,cmap="coolwarm")
# plt.title("Feature Correlation Haetmap")
# plt.show()

####### Data preprocessing
# why preprocess
# ml models expert numeric data 
# features should be scaled for models KNN,SVM

#### split the data
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)


## scale the features
from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

import numpy as np
import matplotlib.pyplot as plt

fig,ax=plt.subplots(1,2,figsize=(14,5))
ax[0].hist(X.iloc[:,0],bins=20,color='skyblue')
ax[0].set_title("Before")

ax[1].hist(X_train[:,0],bins=20,color='orange')
ax[1].set_title("after")
plt.show()

######## Ml models in scikit-learn #################

########## k-nearest neighbours
#   think of  it like this
# you moved into a new neighborhood and you dont know which cricket team you should join so you look around at the 5 people closest to you
# if 3 of them play for team a and 2 for team b you join team a
# why? because most of your nnneighbor are  in team a

# simple example 
# you want to find out if a fruit is a apple or an orange
# you check the 5 closest fruits in your dataset based on size and color
# if 4 of them are apples and i is an orange-> the   n ew fruit is probably an apple

########## knn implememtation #####
from sklearn.neighbors import KNeighborsClassifier

knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,y_train)
y_pred_knn=knn.predict(X_test)

######### decision trees ########
# simple example : should you go outside
#you are trying to decide whether to go outside or stay home
#you ask yourself a few yes/no questions in order 
# 1.is it raining 
    # a: yes->stay home
    # b: move to the next question
# 2.do you have work to do
#   # a:yes ->stay home
#   # b:no ->go outside
# this is exactly the decision into smaller questions . each questions  is a node. each answer leads to another branch.at the end you get a final decision    

######## desicion treee
from sklearn.tree import DecisionTreeClassifier

tree=DecisionTreeClassifier(max_depth=3,random_state=42)
tree.fit(X_train,y_train)
y_pred_tree=tree.predict(X_test)

###### visualizing model evaluation
###### confusion matrix heatmap(for both models)
from sklearn.metrics import confusion_matrix,classification_report
def plot_confusion(y_true,y_pred,title):
    cm=confusion_matrix(y_true,y_pred)
    sns.heatmap(cm,annot=True,fmt='d',cmap="Blues")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title(title)
    plt.show()

plot_confusion(y_test,y_pred_knn,"KNN CONFUSION MATRIX")
plot_confusion(y_test,y_pred_tree,"DECISION TREE CONFUSION MATRIX")   

print("KNN Report:\n",classification_report(y_test,y_pred_knn))
print("Tree Report:\n",classification_report(y_test,y_pred_tree))
