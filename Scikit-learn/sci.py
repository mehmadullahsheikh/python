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
X=pd.DataFrame(iris.data,columns=iris.feature_name)
y=pd.Series(iris.target)
df=X.copy()
df['target']=y
