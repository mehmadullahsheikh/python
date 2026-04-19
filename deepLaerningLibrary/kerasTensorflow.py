## what is keras
# 1:leras is a user friendly high level API for building neural networks
# 2: you can define models in just a few lines

#### what is tensorflow
#1: tensorflow is a complete deep learning framwork that handles:
  #a:tensor operations
  #b:training loops and gradients
  #c:gpu execution
  #d:deployment (mobile ,web,cloud)
#2:keras is a convenient front-end,tensorflow is the powerflow engine behind it

#### let us build a simple binary classifier using keras

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
# 1. Generate a 2D binary classification dataset
X, y = make_classification (n_samples=500, n_features =2, n_informative=2,
n_redundant=0,
n_clusters_per_class=1, random_state=42)

# 2. Scale the features
scaler= StandardScaler ()
X_scaled= scaler.fit_transform(X)
# 3. Train-test split
X_train, X_test, y_train, y_test= train_test_split(X_scaled, y, test_size=0.2,
random_state=42)