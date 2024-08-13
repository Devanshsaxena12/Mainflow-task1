import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
df=pd.read_csv('C:\\Users\\hp\\OneDrive\\Desktop\\python\\USvideos.csv')
#print(df.head())
print("Shape of the dataset is ",df.shape)
# dropping duplicate rows
df=df.drop_duplicates()
print("After deleting Duplicate rows Shape of the dataset is ",df.shape)
#Descriptive Statistics
print(df.describe())
#Printing Information of dataset
print(df.info())
#Dropping thumbnail_link and description as they contains links
venv remove_column=['thumbnail_link', 'description']
df=df.drop(columns=remove_column)
print("After Dropping two columns ",df.shape)
df['trending_date']=df['trending_date'].apply(lambda x: datetime.strptime(x, '%y.%d.%m'))
#Formating Date
print(df.head())
df['publish_time']=pd.to_datetime(df['publish_time'])
print(df.head())