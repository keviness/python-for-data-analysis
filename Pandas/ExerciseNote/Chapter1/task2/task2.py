# Chapter1 task2
import numpy as np
import pandas as pd

df = pd.read_csv("Kobe_data.csv")
print(df.head())

#Q1: 哪种action_type和combined_shot_type的组合是最多的？
#print("df[action_type]:\n", df["action_type"].head())
#print("df[combined_shot_type]\n", df["combined_shot_type"].head())
#print("zip(df[action_type], df[combined_shot_type])\n", zip(df["action_type"], df["combined_shot_type"]))
task1_a = zip(df["action_type"], df["combined_shot_type"])
#print("list(a)\n", list(a))
s = pd.Series(task1_a)
#print("series:", s.head())
result = s.value_counts().index[0]
print("result:", result)

#Q2: 在所有被记录的game_id中，遭遇到最多的opponent是一个支？
# 由于一场比赛会有许多次投篮，但对阵的对手只有一个，本题相当于问科比和哪个队交锋次数最多
task2_a = zip(df["game_id"], df["opponent"])
task2_s = pd.Series(task2_a)
print("task2_s: ",task2_s)
task2_result = task2_s.value_counts().index[0]
print("task2_result:", task2_result)