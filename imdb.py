import pandas as pd
import matplotlib.pyplot as plt
print("TASK 1")
print("Loading the file...")
df=pd.read_csv("D:\Data sets (l&b)\IMDB-Movie-Data.csv")
print(df)
#-----------------------------------------------------------
print("TASK 2")
print("First 5 rows-")
pd.set_option('display.max_columns',12)
print(df.head(5))
#-----------------------------------------------------------
print("TASK 3")
print("Data types of each column-")
print(df.dtypes)
print("missing values-")
print(df.isnull().sum())
#-----------------------------------------------------------
print("TASK 4")
print("Handling missing values-")
x=round(df["Revenue (Millions)"].median(),2)
y=round(df["Metascore"].median(),2)
df['Revenue (Millions)']=df['Revenue (Millions)'].fillna(x)
df['Metascore']=df['Metascore'].fillna(y)
#-----------------------------------------------------------
print("TASK 5")
columns_to_drop = ['Metascore', 'Description']
df_essential = df.drop(columns=columns_to_drop)
print(df_essential)
#-----------------------------------------------------------
print("TASK 6")
print("Average runtime-")
avg_runtime=df["Runtime (Minutes)"].mean()
print(avg_runtime)
#-----------------------------------------------------------
print("TASK 7")
movies_count=df["Genre"].value_counts()
print(movies_count)
#-----------------------------------------------------------
print("TASK 8")
top_5=df.value_counts("Director")
print(top_5.head())
#-----------------------------------------------------------
print("TASK 9")
