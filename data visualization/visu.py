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
# df=sns.load_dataset("iris")

# plt.hist(df['sepal_length'], bins=10, color='skyblue', edgecolor='black')
# plt.xlabel('Age')
# plt.ylabel('Frequency')
# plt.title('Distribution of Age')
# plt.grid(axis='y')  # Add horizontal grid lines for better readability
# plt.show()

##### scatter plot - feature relationship between two numerical variables
# scatter plots are used to visualize the relationship between two numerical variables. Each point on the plot represents an observation in the dataset, with its position determined by the values of the two variables.
# scatter plots can help identify correlations, trends, and potential outliers in the data.

# plt.scatter(df['sepal_length'], df['sepal_width'],c=df['species'].map({'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}), alpha=0.7)
# plt.xlabel('Sepal Length')
# plt.ylabel('Sepal Width')
# plt.title('Scatter Plot of Sepal Length vs Sepal Width')
# plt.grid()
# plt.show()

# seaboarn is a powerful data visualization library built on top of Matplotlib. It provides a high-level interface for creating informative and attractive statistical graphics. Seaborn simplifies the process of creating complex visualizations and offers a variety of built-in themes and color palettes to enhance the aesthetics of your plots. It also integrates well with pandas DataFrames, making it easier to visualize data directly from your datasets.

# df=sns.load_dataset("titanic")

# sns.countplot(x='survived', data=df)
# plt.title('Survival Count')
# plt.xlabel('Survived')
# plt.ylabel('Count')
# plt.show()

# boxplot - feature distribution and outliers
# box plots are used to visualize the distribution of a numerical variable and identify potential outliers. They display the median, quartiles, and potential outliers in the data. The box represents the interquartile range (IQR), which contains the middle 50% of the data, while the whiskers extend to the minimum and maximum values within 1.5 times the IQR. Points outside this range are considered outliers.

# sns.boxplot(x='survived', y='age', data=df)
# plt.title('Box Plot of Age by Survival Status')
# plt.xlabel('Survived')
# plt.ylabel('Age')
# plt.show()

# violin plot - feature distribution and outliers
# violin plots are similar to box plots but also show the kernel density estimation of the data, providing a more detailed view of the distribution. They can help identify the shape of the distribution and potential multimodality in the data.

# sns.violinplot(x='pclass', y='fare', hue='survived', data=df)
# plt.title('Violin Plot of Age by Passenger Class and Survival Status')
# plt.xlabel('Passenger Class')
# plt.ylabel('Age')
# plt.legend(title='Survived', loc='upper right')
# plt.show()

# heatmap - feature correlation
# heatmaps are used to visualize the correlation between numerical variables in a dataset. They display a matrix of values where the color intensity represents the strength of the correlation. Heatmaps can help identify which features are strongly correlated with each other, which can be useful for feature selection and understanding relationships in the data.

# corr = df.corr(numeric_only=True)
# sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
# plt.title('Correlation Heatmap')
# plt.show()

## pairplot - feature relationship between multiple numerical variables
# pair plots are used to visualize the relationships between multiple numerical variables in a dataset. They create a grid of scatter plots for each pair of variables, along with histograms or density plots on the diagonal to show the distribution of each variable. Pair plots can help identify correlations, trends, and potential outliers across multiple features.
# sns.pairplot(df[[ 'age', 'fare' ,'survived','pclass']].dropna(), hue='survived')
# plt.suptitle('Pair Plot of Age, Fare, Survival Status, and Passenger Class', y=1.02)
# plt.show()

#plotly is an interactive graphing library that allows you to create dynamic and visually appealing plots. It provides a wide range of chart types, including line plots, scatter plots, bar charts, and more. Plotly's interactive features enable users to zoom, pan, and hover over data points for additional information, making it a powerful tool for exploratory data analysis and presentation.

#heatmap correlation using plotly
# import plotly.express as px
# fig=px.scatter(df,x='age',y='fare',color='survived',size='pclass',hover_data=['sex','embarked'],title='Scatter Plot of Age vs Fare Colored by Survival Status and Sized by Passenger Class')
# fig.show()


########### 2D scatter plot using plotly
# import plotly.express as px
# df=px.data.iris()
# fig=px.scatter(df,x='sepal_length',y='sepal_width',color='species',size='petal_length')
# fig.show()

###  3d scatter plot using plotly
import plotly.express as px
df=px.data.iris()
fig=px.scatter_3d(df,x='sepal_length',y='sepal_width',z='petal_length',color='species',size='petal_width',symbol='species',opacity=0.8,title='3D Scatter Plot of Iris Dataset')
fig.show()

