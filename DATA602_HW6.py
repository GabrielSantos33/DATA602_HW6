# DATA602: 
# Gabriel Santos
# 010/08/2022
# Week 7
# Assignment 6


'''
In this assignment, you will practice loading data into your python environment. It is
recommended that you use either google colab or juypter notebook, however, you may
use any environment you prefer as long as you are using the pandas library.
'''



''' Q1  Load your dataset into python using the pandas library and save data into a dataframe named dfi (where i is one of your datasets, for a total of 4).
'''
import pandas as pd
df1 = pd.read_csv("https://raw.githubusercontent.com/GabrielSantos33/DATA602_HW6/main/GroupedByActorsFinal.csv")
df2 = pd.read_csv("https://raw.githubusercontent.com/GabrielSantos33/DATA602_HW6/main/Motor_Vehicle_Collisions_Crashes.csv")
df3 = pd.read_csv("https://raw.githubusercontent.com/GabrielSantos33/DATA602_HW6/main/precautions.csv")
df4 = pd.read_csv("https://raw.githubusercontent.com/GabrielSantos33/DATA602_HW6/main/car.data.txt")


''' Q2  Preview your data by calling your dataframe’s name. How many columns and rows do you see?
'''   
print(df1) #[32 rows x 5 columns]
print(df2) #[272 rows x 29 columns]
print(df3) #[41 rows x 5 columns]
print(df4) #[1727 rows x 7 columns]


''' Q3  Examine the shape of your data using the .shape command and the data types of your columns using .dtypes.
'''
shape = df1.shape

print('\nDataFrame Shape :', shape) # DataFrame Shape : (32, 5)
print('\nNumber of rows :', shape[0]) # Number of rows : 32
print('\nNumber of columns :', shape[1])  # Number of columns : 5


shape2 = df2.shape

print('\nDataFrame Shape :', shape2) # DataFrame Shape : (272, 29)
print('\nNumber of rows :', shape2[0]) # Number of rows : 272
print('\nNumber of columns :', shape2[1]) # Number of columns : 29



shape3 = df3.shape

print('\nDataFrame Shape :', shape3) # DataFrame Shape : (41, 5)
print('\nNumber of rows :', shape3[0]) # Number of rows : 41
print('\nNumber of columns :', shape3[1]) # Number of columns : 5



shape4 = df4.shape

print('\nDataFrame Shape :', shape4) # DataFrame Shape : (1727, 7) 
print('\nNumber of rows :', shape4[0]) # Number of rows : 1727
print('\nNumber of columns :', shape4[1]) # Number of columns : 7

''' Q4  Use .describe() on your data. What do you notice about your data? What does this command return?
'''

''' The result is  as a dataframe. This dataframe will consist of a statistics summary for all the numeric features of the dataframe.
'''

df1.describe() 
#        Assets and Resources Score  ...  Systems and Enviroments Score
#count                   32.000000  ...                      32.000000
#mean                     0.172443  ...                       0.096600
#std                      0.123270  ...                       0.127711
#min                      0.000599  ...                       0.001278
#25%                      0.092344  ...                       0.014718
#50%                      0.159626  ...                       0.049609
#75%                      0.251640  ...                       0.093795
#max                      0.438447  ...                       0.536250

#[8 rows x 4 columns]

df2.describe()
#           ZIP CODE   LATITUDE  ...  VEHICLE TYPE CODE 4  VEHICLE TYPE CODE 5
#count     19.000000  29.000000  ...                  0.0                  0.0
#mean   10728.315789  39.335393  ...                  NaN                  NaN
#std      573.298744   7.565667  ...                  NaN                  NaN
#min    10001.000000   0.000000  ...                  NaN                  NaN
#25%    10170.000000  40.683098  ...                  NaN                  NaN
#50%    10467.000000  40.708770  ...                  NaN                  NaN
#75%    11219.500000  40.803980  ...                  NaN                  NaN
#max    11432.000000  40.892933  ...                  NaN                  NaN

#[8 rows x 16 columns]

df3.describe()
#              Disease              Precaution_1  ...    Precaution_3 Precaution_4
#count              41                        41  ...              40           40
#unique             41                        32  ...              30           24
#top     Drug Reaction  Consult nearest hospital  ...  consult doctor    follow up
#freq                1                         3  ...               6            6

#[4 rows x 5 columns]

df4.describe()
#       vhigh vhigh.1     2   2.1 small   low  unacc
#count   1727    1727  1727  1727  1727  1727   1727
#unique     4       4     4     3     3     3      4
#top     high    high     3     4   med   med  unacc
#freq     432     432   432   576   576   576   1209

#[4 rows x 8 columns]


'''Q5  Use the .head() and .tail() command - what does this do?
'''
'''head() returns the first n rows.
   tail() returns the last n rows.
'''

df1.head()
#  Country  ...  Systems and Enviroments Score
#0     BEL  ...                       0.004498
#1     DNK  ...                       0.536250
#2     DEU  ...                       0.001355
#3     GRC  ...                       0.065791
#4     ESP  ...                       0.013933

#[5 rows x 5 columns]

df1.tail()
#           Country  ...  Systems and Enviroments Score
#27             ROU  ...                       0.336826
#28  SouthernEurope  ...                       0.095160
#29   WesternEurope  ...                       0.027118
#30  NorthernEurope  ...                       0.186249
#31   EasternEurope  ...                       0.084366

#[5 rows x 5 columns]


df2.head()
#  CRASH DATE CRASH TIME  ... VEHICLE TYPE CODE 4  VEHICLE TYPE CODE 5
#0   3/3/2020       0:00  ...                 NaN                  NaN
#1  3/13/2019      10:15  ...                 NaN                  NaN
#2   4/2/2015       1:15  ...                 NaN                  NaN
#3   4/2/2015      22:30  ...                 NaN                  NaN
#4   3/3/2020      11:20  ...                 NaN                  NaN

#[5 rows x 29 columns]

df2.tail()
#    CRASH DATE CRASH TIME  ... VEHICLE TYPE CODE 4  VEHICLE TYPE CODE 5
#267        NaN        NaN  ...                 NaN                  NaN
#268        NaN        NaN  ...                 NaN                  NaN
#269        NaN        NaN  ...                 NaN                  NaN
#270        NaN        NaN  ...                 NaN                  NaN
#271        NaN        NaN  ...                 NaN                  NaN

#[5 rows x 29 columns]


df3.head()
#          Disease  ...                 Precaution_4
#0   Drug Reaction  ...                    follow up
#1         Malaria  ...           keep mosquitos out
#2         Allergy  ...  use ice to compress itching
#3  Hypothyroidism  ...             get proper sleep
#4       Psoriasis  ...                   salt baths

#[5 rows x 5 columns]


df3.tail()
#            Disease  ...           Precaution_4
#36     Heart attack  ...                    NaN
#37        Pneumonia  ...              follow up
#38        Arthritis  ...                massage
#39  Gastroenteritis  ...  ease back into eating
#40     Tuberculosis  ...                   rest

#[5 rows x 5 columns]


df4.head()
#   vhigh vhigh.1  2 2.1  small   low  unacc
#0  vhigh   vhigh  2   2  small   med  unacc
#1  vhigh   vhigh  2   2  small  high  unacc
#2  vhigh   vhigh  2   2    med   low  unacc
#3  vhigh   vhigh  2   2    med   med  unacc
#4  vhigh   vhigh  2   2    med  high  unacc


df4.tail()
#     vhigh vhigh.1      2   2.1 small   low  unacc
#1722   low     low  5more  more   med   med   good
#1723   low     low  5more  more   med  high  vgood
#1724   low     low  5more  more   big   low  unacc
#1725   low     low  5more  more   big   med   good
#1726   low     low  5more  more   big  high  vgood

'''Extra Credit (3 pts)
1.Choose one of your datasets and remove the header information. (Can delete
the row in excel, etc..)
2.Import the data into your environment using pandas. Display the .head() of your
data showing no header information.
3.Using pandas, update the dataset to include the header information. Display the
updated data using .head().

'''
shape2 = df2.shape
print(shape2)
print(df2) #Before
#    CRASH DATE CRASH TIME  ... VEHICLE TYPE CODE 4  VEHICLE TYPE CODE 5
#0     3/3/2020       0:00  ...                 NaN                  NaN
#1    3/13/2019      10:15  ...                 NaN                  NaN
#2     4/2/2015       1:15  ...                 NaN                  NaN
#3     4/2/2015      22:30  ...                 NaN                  NaN
#4     3/3/2020      11:20  ...                 NaN                  NaN

df2.columns = range(df2.shape[1]) 


print(df2)
#0     3/3/2020   0:00   BROOKLYN  11208.0  ...                NaN  NaN NaN NaN
#1    3/13/2019  10:15  MANHATTAN  10004.0  ...                NaN  NaN NaN NaN
#2     4/2/2015   1:15        NaN      NaN  ...  PASSENGER VEHICLE  NaN NaN NaN
#3     4/2/2015  22:30        NaN      NaN  ...  PASSENGER VEHICLE  NaN NaN NaN
#4     3/3/2020  11:20  MANHATTAN  10036.0  ...          Box Truck  NaN NaN NaN

print(df2.columns)
#RangeIndex(start=0, stop=29, step=1)
print(df2.head()) #After

#          0      1          2        3   ...                 25   26  27  28
#0   3/3/2020   0:00   BROOKLYN  11208.0  ...                NaN  NaN NaN NaN
#1  3/13/2019  10:15  MANHATTAN  10004.0  ...                NaN  NaN NaN NaN
#2   4/2/2015   1:15        NaN      NaN  ...  PASSENGER VEHICLE  NaN NaN NaN
#3   4/2/2015  22:30        NaN      NaN  ...  PASSENGER VEHICLE  NaN NaN NaN
#4   3/3/2020  11:20  MANHATTAN  10036.0  ...          Box Truck  NaN NaN NaN