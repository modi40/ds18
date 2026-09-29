import numpy as np
import pandas as pd

data = {
    'Emp_ID': [1, 2, 2, 3, 4, 5, 6, 7, 8],
    'Age': [25, 30, 30, np.nan, 35, 40, 28, 65, 32],
    'Dept': ['HR', 'IT', 'IT', 'Finance', 'Sales', np.nan, 'Marketing', 'IT', 'HR'],
    'Years_Experience': [2, 5, 5, 7, 10, 15, 4, 35, 6],
    'Performance_Rating': [3.5, 4.0, 4.0, 3.8, np.nan, 4.5, 3.9, 4.2, 4.0]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df = df.drop_duplicates()
print("\nAfter Removing Duplicates:")
print(df)

df['Age'] = df['Age'].fillna(df['Age'].median())
df['Dept'] = df['Dept'].fillna(df['Dept'].mode()[0])
df['Performance_Rating'] = df['Performance_Rating'].fillna(df['Performance_Rating'].mean())
print("\nAfter Handling Missing Values:")
print(df)

Q1 = df['Years_Experience'].quantile(0.25)
Q3 = df['Years_Experience'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['Years_Experience'] < lower_bound) | (df['Years_Experience'] > upper_bound)]
print("\nOutliers Detected in Years_Experience using IQR:")
print(outliers)
