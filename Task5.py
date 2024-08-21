"""Description:
Engineer new features and select relevant
features for model training.
Responsibility:
1.Generate meaningful features from existing
data.
2.Use techniques like PCA or feature
importance to select the most important
features.
Optimize feature sets for improved model
performance."""
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
df=pd.read_csv("C:\\Users\\ASUS\\Downloads\\heart.csv")
print(df.head(5))
#!!!!!!!!!!!!!!!!!!!!!
print(df.tail())
#!!!!!!!!!!!!!!!!!!!!!
print(df.columns.values)
#!!!!!!!!!!!!!!!!!!!!!
print(df.isna().sum())
#!!!!!!!!!!!!!!!!!!!!!
print(df.info())
#!!!!!!!!vr!!!!!!!!!!!!!
"""df.hist(bins=90, grid=False, figsize=(20, 15))
plt.show()"""
#!!!!!!!!!!!!!!!!!!!!!
print(df.describe())
""" Questions : 
1. How many people have heart disease and how many people doesn't have heart disease?
2. People of which sex has most heart disease?',
3. People of which sex has which type of chest pain most?',
4. People with which chest pain are most pron to have heart disease?"""
#answer 1 :-
print(df.target.value_counts())
#bar chart
df.target.value_counts().plot(kind='bar', color=["orchid", "salmon"])
plt.title("Heart Disease Values (VR)")
plt.xlabel("1 = Heart Disease, 0 = No Heart Disease")
plt.ylabel("Amount")
plt.show()
#pie chart
df.target.value_counts().plot(kind='pie', figsize=(8, 6), autopct='%1.1f%%', colors=["orchid", "salmon"])
plt.title("Distribution of Heart Disease (VR)")
plt.legend(["Disease", "No Disease"])
plt.show()
#!!!!!!!!!vr!!!!!!!!!!!!
print(df.sex.value_counts())
df.sex.value_counts().plot(kind='pie', figsize=(8, 6), autopct='%1.1f%%', colors=["skyblue", "lightpink"])
plt.title('Male Female Ratio(VR)')
plt.legend(['Male', 'Female'], loc="upper right")
plt.show()
#!!!!!!!!!!!!!!!!!!!!!
#answer 2:-
cross_tab = pd.crosstab(df.target, df.sex)

# Display the cross-tabulation
print(cross_tab)
sns.countplot(x='target', data=df, hue='sex')
plt.title("Heart Disease Frequency for Sex (VR)")
plt.xlabel("0 = No Heart Disease, 1 = Heart Disease")
plt.ylabel("Count")
plt.show()
#!!!!!!!!!!vr!!!!!!!!!!!
#answer 3 :-
df.cp.value_counts().plot(kind='bar', color=['salmon', 'lightskyblue', 'springgreen', 'khaki'])
plt.title('Chest Pain Type vs Count (VR)')
plt.xlabel('Chest Pain Type')
plt.ylabel('Count')
plt.show()
#3.2
pd.crosstab(df.sex, df.cp).plot(kind='bar', color=['coral', 'lightskyblue', 'plum', 'khaki'])
plt.title('Type of Chest Pain for Sex (VR)')
plt.xlabel('0 = Female, 1 = Male')
plt.ylabel('Count')
plt.show()
#!!!!!!!!!!vr!!!!!!!!!!!
#answer 4 
sns.countplot(x='cp', data=df, hue='target', palette='Set2')
plt.title('Chest Pain Type vs Heart Disease(VR)')
plt.xlabel('Chest Pain Type')
plt.ylabel('Count')
plt.show()

# Create the distribution plot with a normal distribution curve
sns.displot(x='age', data=df, bins=30, kde=True, color='blue')

plt.title('Age Distribution with Normal Distribution Curve(VR)')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()