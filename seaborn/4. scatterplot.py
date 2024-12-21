import seaborn as sb
from matplotlib import pyplot as plt
import pandas as pd

df = sb.load_dataset('tips')
print("=====first 10 =========")
print(df.head(10))
print("=====info=========")
print(df.info())
print("=====describe=========")
print(df.describe())
print("=====scatterplot=========")
plt.figure(figsize=(8,8))
sb.scatterplot(data=df,x="total_bill",y="tip",hue="size",style="size",size="size",markers='o')
plt.show()
