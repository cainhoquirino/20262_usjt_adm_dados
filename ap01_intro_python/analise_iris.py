import pandas as abc
df = abc.read_csv("Iris.csv")
# print(df.shape)
# print(df.head())
# print(df["Species"].value_counts())
# print(df.groupby("Species")["PetalLengthCm"].mean().round(3))