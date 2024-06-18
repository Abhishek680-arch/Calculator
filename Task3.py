import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset from the CSV file
df = pd.read_csv("C://Users//23016//OneDrive//Documents//Python//data.csv")

# Display the first few rows of the dataset to understand its structure
print("First few rows of the dataset:")
print(df.head())

# Display the column names
print("\nColumn names in the dataset:")
print(df.columns)

# Set the style of the visualization
sns.set(style="whitegrid")

# Handle missing values by dropping rows with any missing values
df.dropna(inplace=True)

# Scatter Plot for Duration vs Calories
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Duration', y='Calories')
plt.title('Duration vs Calories')
plt.show()

# Histogram for Calories
plt.figure(figsize=(10, 6))
sns.histplot(df['Calories'], kde=True, bins=30)
plt.title('Distribution of Calories')
plt.xlabel('Calories')
plt.show()

# Pairplot to show relationships between all numeric features
plt.figure(figsize=(10, 8))
sns.pairplot(df)
plt.suptitle('Pairplot of Dataset', y=1.02)
plt.show()

# Boxplot to show the distribution of all numeric features
plt.figure(figsize=(14, 8))
sns.boxplot(data=df, orient='h')
plt.title('Boxplot of Features')
plt.show()

# Violin plot to show the distribution and density of the numeric features
plt.figure(figsize=(14, 8))
sns.violinplot(x='variable', y='value', data=pd.melt(df))
plt.title('Violin Plot of Features')
plt.show()

# Heatmap to show the correlation between numeric features
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap of Features')
plt.show()
