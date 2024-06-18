import pandas as pd

# Load the dataset
df = pd.read_csv("C://Users//23016//OneDrive//Documents//Python//data.csv")

# Display the first few rows of the dataset
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Drop rows with any missing values
df.dropna(inplace=True)

# Alternatively, you can fill missing values with mean or median
# df.fillna(df.mean(), inplace=True)

# Example of creating BMI (if height and weight columns existed)
# df['BMI'] = df['Weight'] / (df['Height']/100)**2

# Categorize 'Duration' into bins
bins = [0, 30, 60, 90, 120, float('inf')]
labels = ['Very Short', 'Short', 'Moderate', 'Long', 'Very Long']
df['Duration_Category'] = pd.cut(df['Duration'], bins=bins, labels=labels)

# Interaction between 'Pulse' and 'Maxpulse'
df['Pulse_Maxpulse_Ratio'] = df['Pulse'] / df['Maxpulse']

# Squaring 'Pulse' feature
df['Pulse_Squared'] = df['Pulse'] ** 2

# Example if there was a datetime column
# df['Date'] = pd.to_datetime(df['Date'])
# df['Year'] = df['Date'].dt.year
# df['Month'] = df['Date'].dt.month
# df['Day'] = df['Date'].dt.day
# df['DayOfWeek'] = df['Date'].dt.dayofweek

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv("C://Users//23016//OneDrive//Documents//Python//data.csv")
print("First few rows of the dataset:")
print(df.head())

# Display missing values
print("\nMissing values in each column:")
print(df.isna().sum())

# Handle missing values by filling with median
df.fillna(df.median(), inplace=True)

# Check data types
print("\nData types of the columns:")
print(df.dtypes)

# Select numeric columns
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns

# Apply StandardScaler
scaler = StandardScaler()
df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

print("\nFirst few rows after scaling:")
print(df.head())

# Feature Engineering
df['HRR'] = df['Maxpulse'] - df['Pulse']
df['Duration_per_Pulse'] = df['Duration'] / df['Pulse']
df['Calories_Burn_Rate'] = df['Calories'] / df['Duration']

print("\nFirst few rows after feature engineering:")
print(df.head())

# Define the target variable and features
X = df.drop('Calories', axis=1)
y = df['Calories']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\nTraining set size:", X_train.shape)
print("Testing set size:", X_test.shape)
