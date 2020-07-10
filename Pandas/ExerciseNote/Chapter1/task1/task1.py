'''
title: pandas task1
author: keviness
data: 2020.7.9
'''
import pandas as pd
import numpy as np

df = pd.read_csv("Game_of_Thrones_Script.csv")
#print(df[["Season", "Episode"]])
#Q1: 在所有的数据中，一共出现了多少人物？
print("Q1".center(30, "*"))
print(df["Name"].nunique())

#Q2: 以单元格计数（即简单把一个单元格视作一句），谁说了最多的话？
#print(df["Sentence"].count())
print("Q2".center(30, "*"))
print(df["Name"].value_counts())
print(df["Name"].value_counts().index[0])

#Q3: 以单词计数，谁说了最多的单词？
s = df["Sentence"]
d = s.apply(lambda x: len(x))
print("Q3".center(30, "*"))
print(d.idxmax())
print(df.loc[d, "Name"])
#print(df["Sentence"].apply(lambda x: len(x)).idxmax())