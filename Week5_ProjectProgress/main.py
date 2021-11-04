import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

print(" Data Pre-Processing")

data = pd.read_csv ("/Users/samuelkawuma/Desktop/SamplesForProject/Project data.csv")
"""
total_rows = data.count()
print("*******************************************")
print(data.info())
print("*******************************************")
#print ('Total Columns in the data frame are ',total_columns)
print("*******************************************")
print ('Total Rows in the data frame are ',total_rows)
print("*******************************************")
print(data.head(5))
print("*******************************************")
print(data.tail(5))
print("*******************************************")
print('Shape: ',data.shape)
print("*******************************************")
print(data.dtypes)
print("*******************************************")
#print(data.std())
#print("*******************************************")
print(data.describe())
print("*******************************************")
print(data.isnull().sum())
print("*******************************************")
print("The Null Values are ;\n",data.isnull())
print("*******************************************")
print("The  Number Null Values are ;\n",data.isnull().sum())
print("There Appears not to be any null values in the the data frames")

duplicate =data[data.duplicated(keep = 'last')]
  
print("Duplicate Rows :",duplicate)

df1 = data.drop(['NumOfProducts','Exited'],axis = 1)
df2 = data.drop(data.columns[[0, 1, 2, 4]], axis = 1)
df3 = data.drop(data.columns[[10, 11, 12, 13]], axis = 1)
print(data)
print(df1)
print(df2)
print(df3)


data = pd.DataFrame(np.random.randn(1000, 4),  columns=["CustomerId", "Age","Gender","EstimatedSalary"])

data = data.cumsum()

plt.figure();

data.plot.bar();


#plottting age

ages = data['Age'].astype(int)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.hist(ages, bins=np.max(ages) - np.min(ages))
plt.show()
"""


#Plotting Estimared Salary

salary = data['EstimatedSalary'].astype(int)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.hist(salary, bins=np.max(ages) - np.min(salary))
plt.show()



