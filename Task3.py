import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from IPython.display import display
df=pd.read_csv("C:\\Users\\hp\\OneDrive\\Desktop\\divyanshu\\householdtask3.csv")
#________1___________ 
#display(df.head(10))
#_________2___________
#scatter plot with year against own
plt.scatter(df['year'],df['own'])
#adding title to the plot
plt.title("Scatter plot")
#Setting the x and y lables
plt.xlabel('year')
plt.ylabel('own')
plt.show()
#________3________
# Creating Histogram
plt.hist(df['income'])
plt.title('Histogram')
plt.show()
#______4________
#Line chart with year against own
plt.plot(df['year'])
plt.plot(df['own'])
#adding title to the plot 
plt.title('Line Chart')
#Setting the x and y labels
plt.xlabel('year')
plt.xlabel('owm')
#Showing result
plt.show()
#_______5__________
#Bar chart
plt.bar(df['year'],df['own'])
#adding title to the plot
plt.title("Bar chart")
#Setting the x and y lables
plt.xlabel('year')
plt.ylabel('own')
plt.show()
