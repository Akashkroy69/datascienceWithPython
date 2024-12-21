import seaborn as sb
from matplotlib import pyplot as plt
import pandas as pd


# df = sb.load_dataset(f'USA_Housing.csv')
df = pd.read_csv("USA_Housing.csv")
# -----head
print("------head(10)------")
print(df.head(10))
print("------info------")
print(df.info())
print("------describe------")
print(df.describe())
print("------coloumns------")
print(df.columns)
print("------pair plot------")
print(sb.pairplot(df))
sb.pairplot(df)
print("------heatmap------")
sb.heatmap(df.corr(),annot=True)

