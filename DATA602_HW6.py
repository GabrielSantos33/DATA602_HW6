




# Q1  Load your dataset into python using the pandas library and save data into a dataframe named dfi (where i is one of your datasets, for a total of 4).
import pandas as pd
df1 = pd.read_csv("E:\\Users\\drake\\Documents\\CUNY SPS\\MASTERS\\DATA 602\\Week 7\\GroupedByActorsFinal.csv")
df2 = pd.read_csv("E:\\Users\\drake\\Documents\\CUNY SPS\\MASTERS\\DATA 602\\Week 7\\Motor_Vehicle_Collisions_Crashes.csv")
df3 = pd.read_csv("E:\\Users\\drake\\Documents\\CUNY SPS\\MASTERS\\DATA 602\\Week 7\\precautions.csv")
df4 = pd.read_csv("E:\\Users\\drake\\Documents\\CUNY SPS\\MASTERS\\DATA 602\\Week 7\\car.data.txt")



# Q2  Preview your data by calling your dataframe’s name. How many columns and rows do you see?
print(df1)
print(df2)
print(df3)
print(df4)


# Q3  Examine the shape of your data using the .shape command and the data types of your columns using .dtypes.

shape = df1.shape

print('\nDataFrame Shape :', shape)
print('\nNumber of rows :', shape[0])
print('\nNumber of columns :', shape[1])


shape2 = df2.shape

print('\nDataFrame Shape :', shape2)
print('\nNumber of rows :', shape2[0])
print('\nNumber of columns :', shape2[1])



shape3 = df3.shape

print('\nDataFrame Shape :', shape3)
print('\nNumber of rows :', shape3[0])
print('\nNumber of columns :', shape3[1])



shape4 = df4.shape

print('\nDataFrame Shape :', shape4)
print('\nNumber of rows :', shape4[0])
print('\nNumber of columns :', shape4[1])

# Q4  Use .describe() on your data. What do you notice about your data? What does this command return?


df1.describe() 
df2.describe()
df3.describe()
df4.describe()


# Answer On applying pandas describe function to a dataframe, the result is also returned as a dataframe . This dataframe will consist of a statistics summary for all the numeric features of the dataframe.


# Q5  Use the .head() and .tail() command - what does this do?

df1.head()
df1.tail()

df2.head()
df2.tail()

df3.head()
df3.tail()

df4.head()
df4.tail()