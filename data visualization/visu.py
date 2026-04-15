# Data visualization
# EDA (Exploratory Data Analysis) is a crucial step in understanding the dataset and uncovering insights.
# It involves summarizing the main characteristics of the data, often using visual methods. 


######## matplotlib- foundation of data visualization in Python
# # Matplotlib is like the "C language" of visualization -
# fundamental but powerful. Most modern libraries (like
# Seaborn and Pandas plotting) are built on it.


#### lineplot 
# import matplotlib.pyplot as plt

# epochs = [1, 2, 3, 4, 5]
# train_loss = [0.8, 0.6, 0.4, 0.3, 0.2]
# val_loss = [0.9, 0.7, 0.5, 0.4, 0.3]

# plt.plot(epochs, train_loss, label='Train Loss', marker='o')
# plt.plot(epochs, val_loss, label='Validation Loss', marker='s')
# plt.xlabel('Epoch')
# plt.ylabel('Loss')
# plt.title('Training and Validation Loss')
# plt.legend()  # Add a legend to differentiate between the two lines
# plt.grid()  # Add a grid for better readability
# plt.show()

###### Bar chart-class distribution
# import matplotlib.pyplot as plt

# classes = ['Class 1', 'Class 2', 'Class 3']
# survival_rates = [62, 47, 24]  # Example survival rates for each class

# plt.bar(classes, survival_rates, color=['blue', 'orange', 'green'])
# plt.xlabel('Passenger Class')
# plt.ylabel('Survival Rate (%)')
# plt.title('Survival Rate by Passenger Class')
# plt.ylim(0, 100)  # Set y-axis limits to 0-100%
# plt.grid(axis='y')  # Add horizontal grid lines for better readability
# plt.show()


###### Histogram - feature distribution(column distribution)
## histograms are used to visualize the distribution of a single numerical variable. They show how the data is distributed across different bins or intervals.
# bins are the intervals into which the data is grouped, and the height of each bar represents the frequency of data points within that interval.

import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset("iris")

# plt.hist(df['sepal_length'], bins=10, color='skyblue', edgecolor='black')
# plt.xlabel('Age')
# plt.ylabel('Frequency')
# plt.title('Distribution of Age')
# plt.grid(axis='y')  # Add horizontal grid lines for better readability
# plt.show()

##### scatter plot - feature relationship between two numerical variables
# scatter plots are used to visualize the relationship between two numerical variables. Each point on the plot represents an observation in the dataset, with its position determined by the values of the two variables.
# scatter plots can help identify correlations, trends, and potential outliers in the data.

plt.scatter(df['sepal_length'], df['sepal_width'],c=df['species'].map({'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}), alpha=0.7)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Scatter Plot of Sepal Length vs Sepal Width')
plt.grid()
plt.show()
