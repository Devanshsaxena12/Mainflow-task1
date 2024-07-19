import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from scipy import stats

df=pd.read_csv("C:\\Users\\hp\\OneDrive\\Desktop\\divyanshu\\data.csv")
#for printing the types of variables 
print(type(df))

print("-------------------------------------------")

#for printing summary of the dataset
print(df.info())

print("------------------------------------------")

#for deleting duplicate rows
df=df.drop_duplicates()
print(df)
print("------------------------------------------")

#for descriptive stats 
print(df.describe())

print("-----------------------------------------")

#for checking NULL values 
print(df.isnull())

print("------------------------------------------")

#for printing the sum of null values 
print(df.isnull().sum())

print("-------------------------------------------")

#printing total null values
print(df.isnull().sum().sum())

print("-----------------------------------------")

#for filling values(pad method)
df2=df.fillna(value=0)
print(df2)

print("---------------------------------------------------")

#for forward filling 
df3=df.fillna(method='pad')
print(df3)

print("---------------------------------------------------")

#For dropping columns
if 'Observation' in df2.columns:
    df2.drop('Observation', axis=1, inplace=True)
else:
    print("Column 'Observation' does not exist in the DataFrame")

print("---------------------------------------------------")

#for detecting outliers
q1 = df2.quantile(0.25)
q3 = df2.quantile(0.75)

IQR = q3 - q1  #Interquartile Range
print(IQR)
df2_filtered = df2[~((df2 < (q1 - 1.5 * IQR)) | (df2 > (q3 + 1.5 * IQR))).any(axis=1)]
print(df2_filtered)