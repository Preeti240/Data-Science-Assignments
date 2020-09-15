# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 23:07:59 2020

@author: Suyog
"""


import pandas as pd
import numpy as np

a = pd.read_csv(r"C:\Users\HP\Downloads\TY C (2020-09-09).csv",skiprows=[0])#input file
b = pd.read_csv(r"C:\Users\HP\master.csv")#output file


#Dataframe for dividing input csv
data = {'Name': [],
	't1': [],
	'duration': [],
	't2': []}
df_1 = pd.DataFrame(data)

#Column name as a date
df = a.iloc[:,:]
s = df.columns
s = ','.join(str(x) for x in s)
col_name = s.split(" ")[0].split("\t")[1] 

#To divide input file into multiple columnns
for i in range(df.shape[0]):
    s = df.iloc[i].values
    s = ','.join(str(x) for x in s)
    s = s.replace("\t?\t"," ")
    l = s.split(" ")
    nm = ','.join(str(x) for x in l[:2]).replace(","," ")
    nm = nm.title()
    row = {'Name':nm, 't1':l[2], 'duration':l[3], 't2':l[4]}
    df_1 = df_1.append(row,ignore_index=True)

#Alternate method for attendance column
'''df1 = b.iloc[:,:]

l2 = []
for i in range(df1.shape[0]):
    s = df1.iloc[i].values[1]
    j = 0
    while j<df_1.shape[0]:
        if df_1.iloc[j].values[0] == s:
            l2.append(1)
            break
        j = j+1
    if j==df_1.shape[0]:
        l2.append(0)

df1['Attendance'] = l2'''

#Method for attendance
df1 = b.iloc[:,:]
l2 = df1.Name.isin(df_1.Name).astype(int) #Attendance column as a list

#Appending attendance column with date as a column name 
csv_input = pd.read_csv('C:\\Users\\HP\\master.csv')
csv_input[col_name] = l2
csv_input.to_csv('C:\\Users\\HP\\master.csv', index=False)

